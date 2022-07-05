import requests 
import os
import time
from datetime import datetime


def VerificaStatus():
    lista_servere = open('Servere.txt', 'r') 


    while True: 
        
            dataTimeObj = datetime.now()
            timpObj = dataTimeObj.time()
            timpStr = timpObj.strftime("%H:%M:%S")
            linie = lista_servere.readline()

            if not linie:
                break

            r = requests.get('{}'.format(linie.strip())) 
            
            
            if r.status_code == 200: 
                print('[' + timpStr + '] ' + '{} -->'.format(linie.strip()) + 'Este Activ')
            elif r.status_code > 200:
                print('[' + timpStr + '] ' + '{} -->'.format(linie.strip()) + 'Este Inactiv')
            elif r.status_code < 200:
                print('[' + timpStr + '] ' + '{} -->'.format(linie.strip()) + 'Este Inactiv')


    lista_servere.close() 

while True:
    print('Verificare status server(Activ/Inactiv): ')
    VerificaStatus() 
    
    time.sleep(60) 
    os.system('cls')
