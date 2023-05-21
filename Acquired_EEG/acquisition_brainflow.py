# Documentação do Brainflow: https://brainflow.readthedocs.io/en/stable/UserAPI.html

'''
Este scrip é executado a partir do terminal de forma a definir os elétrodos onde se quer adquirir o EEG

Para correr o script é preciso primeiro definir o diretório onde ele está:
- cd path

De seguida:
- python acquisition_brainflow.py --subject 1 --age 25 --gender Male

'''

# Setup importante da cyton/cyton+daisy: https://docs.openbci.com/Troubleshooting/FTDI_Fix_Windows/

import keyboard
import logging
import numpy as np
import argparse
import pandas as pd
import matplotlib.pyplot as plt
import csv

from brainflow.board_shim import BoardShim, BrainFlowInputParams, BoardIds
from brainflow.data_filter import DataFilter

board_id = BoardIds.CYTON_DAISY_BOARD.value

BoardShim.enable_dev_board_logger()
logging.basicConfig(level=logging.DEBUG) # Ativa as mensagens log do brainflow para fazer debug
params = BrainFlowInputParams()
params.serial_port = 'COM7' # Porta COM do BT dongle no PC
channel_labels = ['C3','CP3','P3','PO3','P7','PO7','Fz','Cz','CPz','Pz','C4','CP4','P4','PO4','P8','PO8']

def main():
    BoardShim.enable_dev_board_logger()
    logging.basicConfig(level=logging.DEBUG) # Ativa as mensagens log do brainflow para fazer debug

    parser = argparse.ArgumentParser() # Permite definir os parâmetros através da consola sem ser necessário ter o editor aberto
    parser.add_argument('--subject', type=int, # Este é o único parâmetro necessário colocar para testar (SYNTHETIC_BOARD)
                        help='Subjects code number',
                        required=True, default='')
    parser.add_argument('--age', type=int,
                        help='Subjects Age',
                        required=True, default='')
    parser.add_argument('--gender', type=str, help='Subjects gender', required=True, default='')
    args = parser.parse_args()
    
    try:  
        print("\nBoard description: \n")
        print(BoardShim.get_board_descr(board_id))
        board = BoardShim(board_id, params) # Inicialização da board
        board.prepare_session()
        board.config_board('/2') # Ativar leitura analógica (Fotoresisência no pino D12). Cyton board ASCII commands: https://docs.openbci.com/Cyton/CytonSDK/
        board.start_stream(450000) # O parâmetro corresponde ao tamanho do Buffer. O valor é o default do brainflow
        
        eeg_channels = BoardShim.get_eeg_channels(board_id) # O brainflow adquire dados de várias coisas correspondentes a cada coluna de dados mas apenas 8/16 delas correspondem aos dados do EEG
        sampling_rate = BoardShim.get_sampling_rate(board_id)
        eeg_channels = eeg_channels[0:len(channel_labels)]
        
        data = np.zeros((sampling_rate, len(eeg_channels)))
        ldr = np.zeros((sampling_rate,1))

        file_name = 'S' + str(args.subject) + '_' + str(args.age) + '_' + args.gender + '.csv'

        while(True):
            # Variável com os dados da placa. 
            # O parâmetro define a quantidade de amostras a retirar do buffer. Neste caso retira as amostras de 1s 
            data = board.get_board_data(sampling_rate) 
            ldr = data[24] # Pino analógico D12.    

            if np.size(ldr) > 0:
                write_data = DataFilter.write_file(np.concatenate([data[eeg_channels],np.array([ldr])]), file_name, 'a')


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