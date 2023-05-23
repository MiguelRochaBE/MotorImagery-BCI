import socket
import keyboard
import logging
import numpy as np
import joblib

from brainflow.board_shim import BoardShim, BrainFlowInputParams, BoardIds
from brainflow.data_filter import DataFilter

# Model

model = joblib.load('Model/MI_BCI_model.pkl')
W = np.load('Model/Matrix_W.npy', allow_pickle=True)
FeatVec_idx = np.load('Model/FeatVec_idx.npy', allow_pickle=True)
band_idx = np.load('Model/band_idx.npy', allow_pickle=True)

# Frequency bank 

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

bands = [band for band, idx in zip(bands, band_idx) if idx]
'''The zip() function returns a zip object,which is an iterator of tuples where the first item 
in each passed iterator ispaired together, and then the second item in each passed iterator are 
pairedtogether etc.'''

# Data acquisition EEG

board_id = BoardIds.CYTON_DAISY_BOARD.value

BoardShim.enable_dev_board_logger()
logging.basicConfig(level=logging.DEBUG) # Ativa as mensagens log do brainflow para fazer debug
params = BrainFlowInputParams()
params.serial_port = 'COM7' # Porta COM do BT dongle no PC
channel_labels = ['C3','CP3','P3','PO3','P7','PO7','Fz','Cz','CPz','Pz','C4','CP4','P4','PO4','P8','PO8']

'''
This line creates a new socket object s using the socket.socket() function. The AF_INET parameter 
specifies the address family, which in this case is IPv4, indicating that the socket will use IP 
addresses. The SOCK_STREAM parameter indicates that this socket will use the TCP (Transmission Control 
Protocol) protocol for reliable, stream-oriented communication.
'''

def main():
    BoardShim.enable_dev_board_logger()
    logging.basicConfig(level=logging.DEBUG) # Ativa as mensagens log do brainflow para fazer debug

    try:  
        print("\nBoard description: \n")
        print(BoardShim.get_board_descr(board_id))
        board = BoardShim(board_id, params) # Inicialização da board
        board.prepare_session()

        board.start_stream(450000) # O parâmetro corresponde ao tamanho do Buffer. O valor é o default do brainflow
        
        eeg_channels = BoardShim.get_eeg_channels(board_id) # O brainflow adquire dados de várias coisas correspondentes a cada coluna de dados mas apenas 8/16 delas correspondem aos dados do EEG
        sampling_rate = BoardShim.get_sampling_rate(board_id)
        eeg_channels = eeg_channels[0:len(channel_labels)]

        data = np.zeros((sampling_rate, len(eeg_channels)))

        while(True):
            # Variável com os dados da placa. 
            # O parâmetro define a quantidade de amostras a retirar do buffer. Neste caso retira as amostras de 1s 
            data = board.get_board_data(sampling_rate*16)

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


if __name__ == '__main__':
    main() 


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("raspberrypi",5000))

while True:
    message = input("Enter your message: ")
    s.send(message.encode("utf-8"))



# CSP functions

def spatially_filter_EEG(W, EEG, n_comp):

    Z = []
    
    W = np.delete(W, np.s_[n_comp:-n_comp:], 0)

    for trial in range(len(EEG)):
      Z.append( W @ np.squeeze(EEG[trial].T) )
    

    return Z

def feat_vector(Z):
    
    feat = []
    
    for i in range(len(Z)):
        var = np.var(Z[i], ddof=1, axis=1)
        varsum = np.sum(var)
        
        feat.append(np.log10(var/varsum))
        
    return feat