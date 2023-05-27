import socket
import keyboard
import logging
import numpy as np
import joblib
import time

from brainflow.board_shim import BoardShim, BrainFlowInputParams, BoardIds
from brainflow.data_filter import DataFilter

from scipy.signal import filtfilt, firwin, freqz
import concurrent.futures

# Conexão com raspberry pi


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("raspberrypi",5000))

 # Aquisição brainflow

board_id = BoardIds.CYTON_DAISY_BOARD.value

BoardShim.enable_dev_board_logger()
logging.basicConfig(level=logging.DEBUG) # Ativa as mensagens log do brainflow para fazer debug
params = BrainFlowInputParams()
params.serial_port = 'COM4' # Porta COM do BT dongle no PC
channel_labels = ['C3','CP3','P3','PO3','P7','PO7','Fz','Cz','CPz','Pz','C4','CP4','P4','PO4','P8','PO8']

'''
This line creates a new socket object s using the socket.socket() function. The AF_INET parameter 
specifies the address family, which in this case is IPv4, indicating that the socket will use IP 
addresses. The SOCK_STREAM parameter indicates that this socket will use the TCP (Transmission Control 
Protocol) protocol for reliable, stream-oriented communication.
'''

def main():

    # Modelo

    model = joblib.load('C:/Users/migue/OneDrive/Ambiente de Trabalho/EEG stuff/Motor Imagery/MotorImagery-BCI/Model/MI_BCI_model.pkl')
    W = np.load('C:/Users/migue/OneDrive/Ambiente de Trabalho/EEG stuff/Motor Imagery/MotorImagery-BCI/Model/Matrix_W.npy', allow_pickle=True)
    feat_idx = np.load('C:/Users/migue/OneDrive/Ambiente de Trabalho/EEG stuff/Motor Imagery/MotorImagery-BCI/Model/FeatVec_idx.npy', allow_pickle=True)
    feat_bands = np.load('C:/Users/migue/OneDrive/Ambiente de Trabalho/EEG stuff/Motor Imagery/MotorImagery-BCI/Model/band_idx.npy', allow_pickle=True)
    n_comp = 4

    print()

    # Classes

    classes = {"rest/block": 1, 
            "left_fist/block": 2,
            "right_fist/block": 3, 
            "both_fists/block": 4,
            "both_feet/block": 5}

    # Banco de frequências

    fs = 125 # Hz
    nyquist = fs/2

    min_freq = 4
    max_freq = 40

    n_bands = int((max_freq - min_freq)/2)

    bands = []
    f1 = 4
    f2 = 8

    for i in range(1,n_bands):
        bands.append([f1,f2])
        f1+=2
        f2+=2

    feat_bandss = [band for count,band in enumerate(bands) if feat_bands[count] == True]

    numtaps = 501 # Ordem
    noise_freq = 25.213

    BoardShim.enable_dev_board_logger()
    logging.basicConfig(level=logging.DEBUG) # Ativa as mensagens log do brainflow para fazer debug

    try:  
        print("\nBoard description: \n")
        print(BoardShim.get_board_descr(board_id))
        board = BoardShim(board_id, params) # Inicialização da board
        board.prepare_session()

        board.start_stream(4500) # O parâmetro corresponde ao tamanho do Buffer. O valor é o default do brainflow
        
        eeg_channels = BoardShim.get_eeg_channels(board_id) # O brainflow adquire dados de várias coisas correspondentes a cada coluna de dados mas apenas 8/16 delas correspondem aos dados do EEG
        sampling_rate = BoardShim.get_sampling_rate(board_id)
        eeg_channels = eeg_channels[0:len(channel_labels)]

        print(eeg_channels)

        #data = np.zeros((sampling_rate, len(eeg_channels)))
        sec = 4

        interval = 5  # Time interval in seconds
        start = time.time()
    
        while(True):

            current_time = time.time()
            elapsed_time = current_time - start

            data = board.get_current_board_data(sampling_rate * sec)
        
            # Variável com os dados da placa. 
            # O parâmetro define a quantidade de amostras a retirar do buffer. Neste caso retira as amostras de 4s 
            if int(elapsed_time) >= 5 and round(elapsed_time, 1) % interval == 0:
                
                bf_proc = time.time()
            
                pred = pred_class(data[eeg_channels].T, feat_bandss, len(feat_bands), feat_idx, len(eeg_channels), W, n_comp, classes, model, numtaps, noise_freq, nyquist)
    
                c = np.sum(pred, axis = 1)
                c = np.argmax(c)

                message = str(c)
                s.send(message.encode("utf-8"))

                proc_time = time.time() - bf_proc
                print('Processing time: ', proc_time)
                print('Label :', c+1)

            if keyboard.is_pressed('esc'): # Clicar no esc para parar o stream.
                stopStream(board)

    except BaseException:
        print("--------------------------------------------------------------------------------------------------------------------------")
        logging.warning('Exception', exc_info=True)
        print("--------------------------------------------------------------------------------------------------------------------------")

    finally:
        stopStream(board)
            
def stopStream(board): # Termina a sessão corretamente
    logging.info('End')
    if board.is_prepared():
        logging.info('Releasing session')
        board.release_session()  


''' --------------------- Funções --------------------- '''

# Funções CSP 

# CSP modificado para classificação em tempo real (1 trial)

def spatially_filter_EEG_rt(W, EEG, n_comp):

    W = np.delete(W, np.s_[n_comp:-n_comp:], 0)

    Z = W @ EEG.T
    
    return Z

def feat_vector_rt(Z):

    var = np.var(Z, ddof=1, axis=1)
    varsum = np.sum(var)
        
    feat = np.log10(var/varsum)
        
    return feat

# Processamento

def zero_pad_signal(signal, pad_amount):
    padded_signal = np.pad(signal, ((pad_amount, pad_amount), (0, 0)), mode='constant')
    return padded_signal

def eeg_processing(args):

    # Filtragem do banco de frequências

    data, band, n_bands, n_ch, W, n_comp, classes, numtaps, noise_freq, nyquist = args
    
    n_samples, _ = np.shape(data)
    filt_eeg = np.zeros((n_bands, n_samples, n_ch))
    
    #print(f"Filtragem na banda de frequências: {band[0]} - {band[1]} Hz")

    lowcut = band[0]   
    highcut = band[1]

    if band[0] == 22 or band[0] == 24:
        filt = firwin(numtaps, [lowcut/nyquist, (noise_freq-0.7)/nyquist, (noise_freq+0.7)/nyquist, highcut/nyquist], pass_zero=False)
        #print(f"Retirar componente dos {noise_freq:.2f} Hz",)
    else:
        filt = firwin(numtaps, [lowcut/nyquist, highcut/nyquist], pass_zero=False)

    # Zero Pad

    filt_len = len(filt) * 3
    data_len = len(data)

    pad_amount = round((filt_len - data_len)/2) + 1 

    data = zero_pad_signal(data, pad_amount)
  
    filt_eeg = filtfilt(filt, 1, data, axis = 0)

    filt_eeg = filt_eeg[pad_amount:data_len + pad_amount, :]

    # CSP por classe

    test_feat_vect = np.zeros((len(classes),n_comp*2))

    for _, c_id in classes.items():
            
        Z_aux_test = spatially_filter_EEG_rt(W[c_id-1,:,:], filt_eeg, n_comp)
        test_feat_vect[c_id-1,:] = (feat_vector_rt(Z_aux_test)) 


    return test_feat_vect

def conc_feat_vect(featVec, feat_bands, feat_idx, classes):

    perClass_fV = np.zeros((len(classes),np.sum(feat_idx)))

    for _, c_id in classes.items():
        for band in range(1,len(feat_bands)):
            if band == 1:
                aux1_test = np.hstack((featVec[band-1][c_id-1], featVec[band][c_id-1])) #[:,0:n_comp]
            else:
                aux1_test = np.hstack((aux1_test,featVec[band][c_id-1])) #[:,0:n_comp]
            
        aux1_test = [aux1_test[i] for i in feat_idx if i ==1]
        
        perClass_fV[c_id-1,:] = aux1_test

    return perClass_fV

def pred_class(data, bands, n_bands, feat_idx, n_ch, W, n_comp, classes, model, numtaps, noise_freq, nyquist):
    results = []
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=None) as executor:
        futures = []
        for count, band in enumerate(bands):
            args = (data, band, n_bands, n_ch, W[count], n_comp, classes, numtaps, noise_freq, nyquist)
            future = executor.submit(eeg_processing, args)
            futures.append(future)

        for future in futures:
            
            try:
                result = future.result()
                results.append(result)
                
            except Exception as e:
              
                print(f"Exception in processing band: {e}")

        c = np.zeros((len(classes),len(classes)))
      
        try:
            perClass_fV = conc_feat_vect(results, bands, feat_idx, classes)

            for _,c_id in classes.items():
                c[c_id-1,0:len(classes)] = model.predict_proba(perClass_fV[c_id-1].reshape(1,-1))
            
            pred = c

        except Exception as e:
            pred = c
            print(f"Exception in classifying {e}")

    return pred


def find_max_index(matrix):
    max_value = float('-inf')
    max_row = -1
    max_col = -1

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] > max_value:
                max_value = matrix[row][col]
                max_row = row
                max_col = col

    return max_row, max_col

''' --------------------- Funções --------------------- '''

if __name__ == '__main__':

    main() 
