from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import telebot
import time
import Infos
import datetime as dt
import logging
 
logging.basicConfig(level= logging.INFO, filename="logs.log")

driver = webdriver.Chrome()

driver.get('https://www.playpix.com/pb/live-casino/home/-1/All?openGames=40003094-real&gameNames=Roulette%20A')
time.sleep(5)
    

janela = driver.window_handles[0]

#Variaveis do Telegram##########################################################################
TOKEN = '6918654241:AAEGSqhjnbwVyuYUJDUjasjl4tJZAkU9RMM'

chat_id = '-1001937645179'

bot = telebot.TeleBot(token=TOKEN)

bot.send_message(chat_id=chat_id, text='🤖 ROBÔ ROLETA A ANALISANDO...')
#bot.send_message(chat_id=chat_id, text='Link para Cadastro: https://m.playpix.com/#/?action=register&reference_code=ccUaid0NfG7Z4SOZ')
#bot.send_message(chat_id=chat_id, text='Link para Jogar: https://www.playpix.com/pb/live-casino/home/-1/All?openGames=40003094-real&gameNames=Roulette%20A')

#AGURDANDO OS DADOS APARECEREM###################################################################################################
   # close_button = driver.find_element_by_xpath('')
    #close_button.click()
    #time.sleep(2)

if driver.find_element(By.XPATH, '/html/body/div[1]/div[6]/div/div/div/div/div/div[2]/form/div[1]').size != 0:
    time.sleep(1)

    username=driver.find_element(By.XPATH, '/html/body/div[1]/div[6]/div/div/div/div/div/div[2]/form/div[1]/div[3]/div/label/input')
    password=driver.find_element(By.XPATH, '/html/body/div[1]/div[6]/div/div/div/div/div/div[2]/form/div[1]/div[4]/div/label/input')  

    username.send_keys(Infos.username) 
    password.send_keys(Infos.password)
    time.sleep(1)

    log_in_button = driver.find_element(By.XPATH, '/html/body/div[1]/div[6]/div/div/div/div/div/div[2]/form/div[1]/div[6]/div/button')
    log_in_button.click()
    time.sleep(1)


#iframe1 = driver.find_element(By.XPATH, '/html/body/noscript[1]/text()')

#driver.switch_to.frame(iframe1)

while len(driver.find_elements(By.XPATH, '/html/body/div[1]/div[3]/div[1]/div[1]/div/iframe')) == 0:
    time.sleep(2)                        
    
iframe2 = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[1]/div[1]/div/iframe')                                          
driver.switch_to.frame(iframe2)

while len(driver.find_elements(By.XPATH, '/html/body/div[2]/div/div[1]/div/iframe')) == 0:
    time.sleep(2)                          
    
iframe3 = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/iframe') 
driver.switch_to.frame(iframe3)

while len(driver.find_elements(By.XPATH, '/html/body/div[2]/div/div[1]/div[8]/div[3]/div/div[1]')) == 0:
    time.sleep(2)
    
#Variaveis Gerais################################################################################

resultado = None 

check_resultado = None 

coluna = None

duzia = None 

reds = None

cor = None

blacks = None

rodadas = 0

#Variaveis de Estrategia##################################################################################

entrada_co = True 
green_co = False 
gale1_co = False 
gale2_co = False 
red_co = False 

entrada_du = True 
green_du = False 
gale1_du = False 
gale2_du = False 
red_du = False

entrada_vermelho = True
green_vermelho = False
gale1_vermelho = False 
gale2_vermelho = False 
red_vermelho = False

entrada_black = True
green_black = False
gale1_black = False 
gale2_black = False 
red_black = False

entrada_par = True
green_par = False
gale1_par = False
gale2_par = False
red_par = False

entrada_impar = True
green_impar = False
gale1_impar = False
gale2_impar = False
red_impar = False

red = 0
green = 0
zero = 0
totalgreen = 0
totalred = 0
banca = 200
agora = dt.datetime.now()

#########################################################################################

def conlunas(i):
    
    global coluna
    
    coluna = []
    
    for x in i:
        
        if int(x) in [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]:
            coluna.append('CO3')
            
        elif int(x) in [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]:
            coluna.append('CO2')
            
        elif int(x) in [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34]:
            coluna.append('CO1')
            
        elif int(x) == 0:
            coluna.append('ZERO_CO')
    
    print(f'COLUNAS: {coluna}')
    return coluna 

########################################################################################

def duzias(i):
    
    global duzia 
    
    duzia = []
    
    for x in i:
    
        if int(x) in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
            duzia.append('D1')
            
        elif int(x) in [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]:
            duzia.append('D2')
            
        elif int(x) in [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]:
            duzia.append('D3')
            
            
        elif int(x) == 0:
            duzia.append('ZERO_DU')
            
    print(f'DUZIAS: {duzia}')
        
    return duzia

########################################################################################

def cores(i):
    
    global reds
    global blacks
    global cor
    
    reds = []
    blacks = []
    cor = []
    
    for x in i:
    
        if int(x) in [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]:
            reds.append('VERMELHO')
            cor.append('VERMELHO')
    
        if int(x) in [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]:
            blacks.append('PRETO')
            cor.append('PRETO')

        elif int(x) == 0:
            cor.append('ZERO')
            
    print(f'CORES: {cor}')    
        
    return reds, blacks

########################################################################################

def par_impar(i):

    global pares
    global impares
    global ambos

    pares = []
    impares = []
    ambos = []

    for x in i:
        
        if int(x) in [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36]:
            pares.append('PAR')
            ambos.append('PAR')

        if int(x) in [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35]:
            impares.append('IMPAR')
            ambos.append('IMPAR')

        elif int(x) == 0:
            ambos.append('ZERO')

    print(f'TIPOS: {ambos}')
    return pares, impares

########################################################################################

def estrategia_coluna(co):
    
    global entrada_co   
    global entrada_du
    global entrada_vermelho
    global entrada_black
    global entrada_par
    global entrada_impar
    global green_co
    global gale1_co
    global gale2_co
    global red_co
    global red
    global green
    global zero

#COLUNA 1######################################################################################

    if co[0:2] == ['CO1', 'CO1'] and entrada_co == True:
        
        bot.send_message(chat_id=chat_id, text='ENTRADA COLUNAS 2 e 3')
        
        entrada_co = False 
        entrada_du = False
        entrada_vermelho = False
        entrada_black = False 
        entrada_par = False
        entrada_impar = False
        green_co = True
        gale1_co = True
        
        return 
        
        
        
    elif co[0:3] == ['CO2', 'CO1', 'CO1'] and green_co == True:
        
        bot.send_message(chat_id=chat_id, text='GREEN')
        
        entrada_co = True 
        entrada_du = True
        entrada_vermelho = True
        entrada_black = True
        entrada_par = True
        entrada_impar = True
        green_co = False 
        gale1_co = False 
        gale2_co = False 
        red_co = False
        green += 1
        time.sleep(130) 
        
        return
        
        
    elif co[0:3] == ['CO3', 'CO1', 'CO1'] and green_co == True:
        
        bot.send_message(chat_id=chat_id, text='GREEN')
        
        entrada_co = True 
        entrada_du = True
        entrada_vermelho = True
        entrada_black = True
        entrada_par = True
        entrada_impar = True
        green_co = False 
        gale1_co = False 
        gale2_co = False 
        red_co = False 
        green += 1 
        time.sleep(130)
        
        return
    
    
         
    elif co[0:3] == ['ZERO_CO', 'CO1', 'CO1'] and green_co == True:
        
        bot.send_message(chat_id=chat_id, text='GREEN NO ZERO')
        
        entrada_co = True 
        entrada_du = True
        entrada_vermelho = True
        entrada_black = True 
        entrada_par = True
        entrada_impar = True
        green_co = False 
        gale1_co = False 
        gale2_co = False 
        red_co = False
        zero += 1 
        time.sleep(130)
        
        return
        
        
        
    elif co[0:3] == ['CO1', 'CO1', 'CO1'] and gale1_co == True:
        
        bot.send_message(chat_id=chat_id, text='GALE 1')
        
        
        gale1_co = False 
        gale2_co = True
        
        return 
    
    elif co[0:3] == ['CO1', 'CO1', 'CO1'] and gale2_co == True:
        
        bot.send_message(chat_id=chat_id, text='GALE 2')
        
        
        gale2_co = False 
        red_co = True
        
        return 
    
    elif co[0:3] == ['CO1', 'CO1', 'CO1'] and red_co == True:
        
        bot.send_message(chat_id=chat_id, text='RED')
        
        
        red_co = False 
        green_co = False 
        entrada_co = True 
        entrada_du = True
        entrada_vermelho = True
        entrada_black = True
        entrada_par = True
        entrada_impar = True
        red += 1
        time.sleep(600)

        
        return 
   
#COLUNA 2######################################################################################


    elif co[0:2] == ['CO2', 'CO2'] and entrada_co == True:
        
        bot.send_message(chat_id=chat_id, text='ENTRADA COLUNAS 1 e 3')
        
        
        entrada_co = False 
        entrada_du = False
        entrada_vermelho = False
        entrada_black = False 
        entrada_par = False
        entrada_impar = False 
        green_co = True
        gale1_co = True
        
        return 
        
        
        
    elif co[0:3] == ['CO1','CO2', 'CO2'] and green_co == True:
        bot.send_message(chat_id=chat_id, text='GREEN')
        
        entrada_co = True 
        entrada_du = True
        entrada_vermelho = True
        entrada_black = True
        entrada_par = True
        entrada_impar = True
        green_co = False 
        gale1_co = False 
        gale2_co = False 
        red_co = False 
        green += 1
        time.sleep(130)
        
        return
        
        
    elif co[0:3] == ['CO3','CO2', 'CO2'] and green_co == True:
        
        bot.send_message(chat_id=chat_id, text='GREEN')
        
        entrada_co = True 
        entrada_du = True
        entrada_vermelho = True
        entrada_black = True
        entrada_par = True
        entrada_impar = True
        green_co = False 
        gale1_co = False 
        gale2_co = False 
        red_co = False 
        green += 1
        time.sleep(130)
        
        return
    
    elif co[0:3] == ['ZERO_CO', 'CO2', 'CO2'] and green_co == True:
        
        bot.send_message(chat_id=chat_id, text='GREEN NO ZERO')
        
        entrada_co = True 
        entrada_du = True
        entrada_vermelho = True
        entrada_black = True
        entrada_par = True
        entrada_impar = True
        green_co = False 
        gale1_co = False 
        gale2_co = False 
        red_co = False 
        zero += 1
        time.sleep(130)
        
        return
        
        
    elif co[0:3] == ['CO2','CO2', 'CO2'] and gale1_co == True:
        
        bot.send_message(chat_id=chat_id, text='GALE 1')
        
        
        gale1_co = False 
        gale2_co = True
        
        return 
    
    elif co[0:3] == ['CO2','CO2', 'CO2'] and gale2_co == True:
        
        bot.send_message(chat_id=chat_id, text='GALE 2')
        
        
        gale2_co = False 
        red_co = True
        
        return 
    
    elif co[0:3] == ['CO2','CO2', 'CO2'] and red_co == True:
        
        bot.send_message(chat_id=chat_id, text='RED')        
        
        red_co = False 
        green_co = False 
        entrada_co = True 
        entrada_du = True
        entrada_vermelho = True
        entrada_black = True
        entrada_par = True
        entrada_impar = True
        red += 1
        time.sleep(600)

        
        return 
    
#COLUNA 3################################################################################

    elif co[0:2] == ['CO3', 'CO3'] and entrada_co == True:
        
        bot.send_message(chat_id=chat_id, text='ENTRADA COLUNAS 1 e 2')
        
        entrada_co = False 
        entrada_du = False
        entrada_vermelho = False
        entrada_black = False 
        entrada_par = False
        entrada_impar = False
        green_co = True
        gale1_co = True
        
        return 
        
        
        
    elif co[0:3] == ['CO1','CO3', 'CO3'] and green_co == True:
        
        bot.send_message(chat_id=chat_id, text='GREEN')
        
        entrada_co = True 
        entrada_du = True
        entrada_vermelho = True
        entrada_black = True
        entrada_par = True
        entrada_impar = True
        green_co = False 
        gale1_co = False 
        gale2_co = False 
        red_co = False
        green +=1 
        time.sleep(130)
        
        return
        
        
    elif co[0:3] == ['CO2','CO3', 'CO3'] and green_co == True:
        
        bot.send_message(chat_id=chat_id, text='GREEN')
        
        entrada_co = True 
        entrada_du = True
        entrada_vermelho = True
        entrada_black = True
        entrada_par = True
        entrada_impar = True
        green_co = False 
        gale1_co = False 
        gale2_co = False 
        red_co = False 
        green += 1
        time.sleep(130)
        
        return
    
    elif co[0:3] == ['ZERO_CO', 'CO3', 'CO3'] and green_co == True:
        
        bot.send_message(chat_id=chat_id, text='GREEN NO ZERO')
        
        entrada_co = True 
        entrada_du = True
        entrada_vermelho = True
        entrada_black = True
        entrada_par = True
        entrada_impar = True
        green_co = False 
        gale1_co = False 
        gale2_co = False 
        red_co = False 
        zero += 1
        time.sleep(130)
        
        return
        
        
    elif co[0:3] == ['CO3','CO3', 'CO3'] and gale1_co == True:
        
        bot.send_message(chat_id=chat_id, text='GALE 1')
        
        
        gale1_co = False 
        gale2_co = True
        
        return 
    
    elif co[0:3] == ['CO3','CO3', 'CO3'] and gale2_co == True:
        
        bot.send_message(chat_id=chat_id, text='GALE 2')
        
        
        gale2_co = False 
        red_co = True
        
        return 
    
    elif co[0:3] == ['CO3','CO3', 'CO3'] and red_co == True:
        
        bot.send_message(chat_id=chat_id, text='RED')        
        
        red_co = False 
        green_co = False 
        entrada_co = True 
        entrada_du = True
        entrada_vermelho = True
        entrada_black = True
        entrada_par = True
        entrada_impar = True
        red += 1
        time.sleep(600)

        return
    

def estrategia_duzia(du):
    
    global entrada_du
    global entrada_co
    global entrada_vermelho
    global entrada_black
    global entrada_par
    global entrada_impar
    global green_du
    global gale1_du
    global gale2_du
    global red_du
    global red
    global green
    global zero
    
#DUZIA 1######################################################################################
    
    if du[0:2] == ['D1', 'D1'] and entrada_du == True:
        
        bot.send_message(chat_id=chat_id, text='ENTRADA DUZIAS 2 e 3')
        
        entrada_du = False 
        entrada_co = False
        entrada_vermelho = False
        entrada_black = False
        entrada_par = False
        entrada_impar = False
        green_du = True
        gale1_du = True
        
        return 
        
        
        
    elif du[0:3] == ['D2', 'D1', 'D1'] and green_du == True:
        bot.send_message(chat_id=chat_id, text='GREEN')
        
        entrada_du = True 
        entrada_co = True
        entrada_vermelho = True
        entrada_black = True
        entrada_par = True
        entrada_impar = True
        green_du = False 
        gale1_du = False 
        gale2_du = False 
        red_du = False
        green += 1
        time.sleep(130) 
        
        return
        
        
    elif du[0:3] == ['D3', 'D1', 'D1'] and green_du == True:
        bot.send_message(chat_id=chat_id, text='GREEN')
        
        entrada_du = True 
        entrada_co = True
        entrada_vermelho = True
        entrada_black = True
        entrada_par = True
        entrada_impar = True
        green_du = False 
        gale1_du = False 
        gale2_du = False 
        red_du = False 
        green += 1
        time.sleep(130)
        
        return
        
    elif du[0:3] == ['ZERO_DU', 'D1', 'D1'] and green_du == True:
        
        bot.send_message(chat_id=chat_id, text='GREEN NO ZERO')
        
        entrada_du = True 
        entrada_co = True
        entrada_vermelho = True
        entrada_black = True
        entrada_par = True
        entrada_impar = True
        green_du = False 
        gale1_du = False 
        gale2_du = False 
        red_du = False 
        zero += 1
        time.sleep(130)
        
        return
        
        
    elif du[0:3] == ['D1', 'D1', 'D1'] and gale1_du == True:
        
        bot.send_message(chat_id=chat_id, text='GALE 1')
        
        
        gale1_du = False 
        gale2_du = True
        
        return 
    
    elif du[0:3] == ['D1', 'D1', 'D1'] and gale2_du == True:
        
        bot.send_message(chat_id=chat_id, text='GALE 2')
        
        
        gale2_du = False 
        red_du = True
        
        return 
    
    elif du[0:3] == ['D1', 'D1', 'D1'] and red_du == True:
        
        bot.send_message(chat_id=chat_id, text='RED')
        
        
        red_du = False 
        green_du = False 
        entrada_du = True 
        entrada_co = True
        entrada_vermelho = True
        entrada_black = True
        entrada_par = True
        entrada_impar = True
        red += 1
        time.sleep(600)
        
        return 
    
#DUZIA 2######################################################################################
    
    elif du[0:2] == ['D2', 'D2'] and entrada_du == True:
        
        bot.send_message(chat_id=chat_id, text='ENTRADA DUZIAS 1 e 3')
        
        entrada_du = False 
        entrada_co = False
        entrada_vermelho = False
        entrada_black = False
        entrada_par = False
        entrada_impar = False
        green_du = True
        gale1_du = True
        
        return 
        
        
        
    elif du[0:3] == ['D1', 'D2', 'D2'] and green_du == True:
        
        bot.send_message(chat_id=chat_id, text='GREEN')
        
        entrada_du = True 
        entrada_co = True
        entrada_vermelho = True
        entrada_black = True
        entrada_par = True
        entrada_impar = True
        green_du = False 
        gale1_du = False 
        gale2_du = False 
        red_du = False 
        green += 1
        time.sleep(130) 
        
        return
        
        
    elif du[0:3] == ['D3', 'D2', 'D2'] and green_du == True:
        
        bot.send_message(chat_id=chat_id, text='GREEN')
        
        entrada_du = True 
        entrada_co = True
        entrada_vermelho = True
        entrada_black = True
        entrada_par = True
        entrada_impar = True
        green_du = False 
        gale1_du = False 
        gale2_du = False 
        red_du = False 
        green += 1
        time.sleep(130) 
        
        return
    
    elif du[0:3] == ['ZERO_DU', 'D2', 'D2'] and green_du == True:
        bot.send_message(chat_id=chat_id, text='GREEN NO ZERO')
        
        entrada_du = True 
        entrada_co = True
        entrada_vermelho = True
        entrada_black = True
        entrada_par = True
        entrada_impar = True
        green_du = False 
        gale1_du = False 
        gale2_du = False 
        red_du = False 
        zero += 1
        time.sleep(130) 
        
        return
        
        
    elif du[0:3] == ['D2', 'D2', 'D2'] and gale1_du == True:
        
        bot.send_message(chat_id=chat_id, text='GALE 1')
        
        
        gale1_du = False 
        gale2_du = True
        
        return 
    
    elif du[0:3] == ['D2', 'D2', 'D2'] and gale2_du == True:
        
        bot.send_message(chat_id=chat_id, text='GALE 2')
        
        
        gale2_du = False 
        red_du = True
        
        return 
    
    elif du[0:3] == ['D2', 'D2', 'D2'] and red_du == True:
        
        bot.send_message(chat_id=chat_id, text='RED')       
        
        red_du = False 
        green_du = False 
        entrada_du = True 
        entrada_co = True
        entrada_vermelho = True
        entrada_black = True
        entrada_par = True
        entrada_impar = True
        red += 1
        time.sleep(600) 
        
        return 
   
#DUZIA 3######################################################################################
    
    elif du[0:2] == ['D3', 'D3'] and entrada_du == True:
        
        bot.send_message(chat_id=chat_id, text='ENTRADA DUZIAS 1 e 2')
        
        entrada_du = False 
        entrada_co = False 
        entrada_vermelho = False
        entrada_black = False
        entrada_par = False
        entrada_impar = False
        green_du = True
        gale1_du = True
        
        return 
        
        
        
    elif du[0:3] == ['D1', 'D3', 'D3'] and green_du == True:
        
        bot.send_message(chat_id=chat_id, text='GREEN')
        
        entrada_du = True 
        entrada_co = True
        entrada_vermelho = True
        entrada_black = True
        entrada_par = True
        entrada_impar = True
        green_du = False 
        gale1_du = False 
        gale2_du = False 
        red_du = False 
        green += 1
        time.sleep(130) 
        
        return
        
        
    elif du[0:3] == ['D2', 'D3', 'D3'] and green_du == True:
        
        bot.send_message(chat_id=chat_id, text='GREEN')
        
        entrada_du = True 
        entrada_co = True
        entrada_vermelho = True
        entrada_black = True
        entrada_par = True
        entrada_impar = True
        green_du = False 
        gale1_du = False 
        gale2_du = False 
        red_du = False
        green += 1 
        time.sleep(130) 
        
        return
        
    elif du[0:3] == ['ZERO_DU', 'D3', 'D3'] and green_du == True:
        
        bot.send_message(chat_id=chat_id, text='GREEN NO ZERO')
        
        entrada_du = True 
        entrada_co = True
        entrada_vermelho = True
        entrada_black = True
        entrada_par = True
        entrada_impar = True
        green_du = False 
        gale1_du = False 
        gale2_du = False 
        red_du = False 
        zero += 1
        time.sleep(130) 
        
        return
        
    elif du[0:3] == ['D3', 'D3', 'D3'] and gale1_du == True:
        
        bot.send_message(chat_id=chat_id, text='GALE 1')
        
        
        gale1_du = False 
        gale2_du = True
        
        return 
    
    elif du[0:3] == ['D3', 'D3', 'D3'] and gale2_du == True:
        
        bot.send_message(chat_id=chat_id, text='GALE 2')
        
        
        gale2_du = False 
        red_du = True
        
        return 
    
    elif du[0:3] == ['D3', 'D3', 'D3'] and red_du == True:
        
        bot.send_message(chat_id=chat_id, text='RED')       
        
        red_du = False 
        green_du = False 
        entrada_du = True 
        entrada_co = True
        entrada_vermelho = True
        entrada_black = True
        entrada_par = True
        entrada_impar = True
        red += 1
        time.sleep(600) 
        
        return


def estrategia_vermelho(vermelho):
    
    global entrada_du
    global entrada_co
    global entrada_vermelho
    global entrada_black
    global entrada_par
    global entrada_impar
    global green_vermelho
    global gale1_vermelho
    global gale2_vermelho
    global red_vermelho
    global red
    global green
    global zero
    
    
    if vermelho[0:3] == ['VERMELHO', 'VERMELHO', 'VERMELHO'] and entrada_vermelho == True:
        
        bot.send_message(chat_id=chat_id, text='ENTRADA PRETO')
        
        entrada_du = False 
        entrada_co = False
        entrada_vermelho = False
        entrada_black = False
        entrada_par = False
        entrada_impar = False
        green_vermelho = True
        gale1_vermelho = True
        
        return 
             
    elif vermelho[0:3] == ['PRETO', 'VERMELHO', 'VERMELHO'] and green_vermelho == True:
        bot.send_message(chat_id=chat_id, text='GREEN')
        
        entrada_du = True 
        entrada_co = True
        entrada_vermelho = True
        entrada_black = True
        entrada_par = True
        entrada_impar = True
        green_vermelho = False 
        gale1_vermelho = False 
        gale2_vermelho = False 
        red_vermelho = False
        green += 1
        time.sleep(130)  
        
        return

    elif vermelho[0:3] == ['ZERO','VERMELHO', 'VERMELHO'] and green_vermelho == True:
        bot.send_message(chat_id=chat_id, text='GREEN')

        entrada_co = True 
        entrada_du = True
        entrada_vermelho = True
        entrada_black = True
        entrada_par = True
        entrada_impar = True
        green_vermelho = False 
        gale1_vermelho = False 
        gale2_vermelho = False 
        red_vermelho = False 
        zero += 1
        time.sleep(130) 
        
        return       

    elif vermelho[0:3] == ['VERMELHO', 'VERMELHO', 'VERMELHO'] and gale1_vermelho == True:
        
        bot.send_message(chat_id=chat_id, text='GALE 1')
        
        
        gale1_vermelho = False 
        gale2_vermelho = True
        
        return 
    
    elif vermelho[0:3] == ['VERMELHO', 'VERMELHO', 'VERMELHO'] and gale2_vermelho == True:
        
        bot.send_message(chat_id=chat_id, text='GALE 2')
        
        
        gale2_vermelho = False 
        red_vermelho = True
        
        return 
    
    elif vermelho[0:3] == ['VERMELHO', 'VERMELHO', 'VERMELHO'] and red_vermelho == True:
        
        bot.send_message(chat_id=chat_id, text='RED')
        
        
        red_vermelho = False 
        green_vermelho = False 
        entrada_du = True 
        entrada_co = True
        entrada_vermelho = True
        entrada_black = True
        entrada_par = True
        entrada_impar = True
        red += 1
        time.sleep(600) 
        
        return 


def estrategia_preto(preto):
    
    global entrada_du
    global entrada_co
    global entrada_vermelho
    global entrada_black
    global entrada_par
    global entrada_impar
    global green_black
    global gale1_black
    global gale2_black
    global red_black
    global red
    global green
    global zero

    if preto[0:3] == ['PRETO', 'PRETO', 'PRETO'] and entrada_black == True:
        
        bot.send_message(chat_id=chat_id, text='ENTRADA VERMELHO')
        
        entrada_du = False 
        entrada_co = False
        entrada_vermelho = False
        entrada_black = False
        entrada_par = False
        entrada_impar = False
        green_black = True
        gale1_black = True
        
        return 
             
    elif preto[0:3] == ['VERMELHO', 'PRETO', 'PRETO'] and green_black == True:
        bot.send_message(chat_id=chat_id, text='GREEN')
        
        entrada_du = True 
        entrada_co = True
        entrada_vermelho = True
        entrada_black = True
        entrada_par = True
        entrada_impar = True
        green_black = False 
        gale1_black = False 
        gale2_black = False 
        red_black = False
        green += 1
        time.sleep(130) 
        
        return

    elif preto[0:3] == ['ZERO','VERMELHO', 'VERMELHO'] and green_black == True:
        bot.send_message(chat_id=chat_id, text='GREEN')

        entrada_co = True 
        entrada_du = True
        entrada_vermelho = True
        entrada_black = True
        entrada_par = True
        entrada_impar = True
        green_black = False 
        gale1_black = False 
        gale2_black = False 
        red_black = False 
        zero += 1
        time.sleep(130) 
        
        return
           
    elif preto[0:3] == ['PRETO', 'PRETO', 'PRETO'] and gale1_black == True:
        
        bot.send_message(chat_id=chat_id, text='GALE 1')
        
        
        gale1_black = False 
        gale2_black = True
        
        return 
    
    elif preto[0:3] == ['PRETO', 'PRETO', 'PRETO'] and gale2_black == True:
        
        bot.send_message(chat_id=chat_id, text='GALE 2')
        
        
        gale2_black = False 
        red_black = True
        
        return 
    
    elif preto[0:3] == ['PRETO', 'PRETO', 'PRETO'] and red_black == True:
        
        bot.send_message(chat_id=chat_id, text='RED')
        
        
        red_black = False 
        green_black = False 
        entrada_du = True 
        entrada_co = True
        entrada_vermelho = True
        entrada_black = True
        entrada_par = True
        entrada_impar = True
        red += 1
        time.sleep(600) 
        
        return 


def estrategia_par(tipo):

    global entrada_du
    global entrada_co
    global entrada_vermelho
    global entrada_black
    global entrada_par
    global entrada_impar
    global green_par
    global gale1_par
    global gale2_par
    global red_par
    global red
    global green
    global zero

    if tipo[0:3] == ['PAR', 'PAR', 'PAR'] and entrada_par == True:
        
        bot.send_message(chat_id=chat_id, text='ENTRADA IMPAR')
        
        entrada_du = False 
        entrada_co = False
        entrada_vermelho = False
        entrada_black = False
        entrada_par = False
        entrada_impar = False
        green_par = True
        gale1_par = True
        
        return 
             
    elif tipo[0:3] == ['IMPAR', 'PAR', 'PAR'] and green_par == True:
        bot.send_message(chat_id=chat_id, text='GREEN')
        
        entrada_du = True 
        entrada_co = True
        entrada_vermelho = True
        entrada_black = True
        entrada_par = True
        entrada_impar = True
        green_par = False 
        gale1_par = False 
        gale2_par = False 
        red_par = False
        green += 1
        time.sleep(130) 
        
        return

    elif tipo[0:3] == ['ZERO','PAR', 'PAR'] and green_par == True:
        bot.send_message(chat_id=chat_id, text='GREEN NO ZERO')

        entrada_co = True 
        entrada_du = True
        entrada_vermelho = True
        entrada_black = True
        entrada_par = True
        entrada_impar = True
        green_par = False 
        gale1_par = False 
        gale2_par = False 
        red_par = False 
        zero += 1
        time.sleep(130) 
        
        return
           
    elif tipo[0:3] == ['PAR', 'PAR', 'PAR'] and gale1_par == True:
        
        bot.send_message(chat_id=chat_id, text='GALE 1')
        
        
        gale1_par = False 
        gale2_par = True
        
        return 
    
    elif tipo[0:3] == ['PAR', 'PAR', 'PAR'] and gale2_par == True:
        
        bot.send_message(chat_id=chat_id, text='GALE 2')
        
        
        gale2_par = False 
        red_par = True
        
        return 
    
    elif tipo[0:3] == ['PAR', 'PAR', 'PAR'] and red_par == True:
        
        bot.send_message(chat_id=chat_id, text='RED')
        
        
        red_par = False 
        green_par = False 
        entrada_du = True 
        entrada_co = True
        entrada_vermelho = True
        entrada_black = True
        entrada_par = True
        entrada_impar = True
        red += 1
        time.sleep(600) 
        
        return 


def estrategia_impar(tipo):

    global entrada_du
    global entrada_co
    global entrada_vermelho
    global entrada_black
    global entrada_par
    global entrada_impar
    global green_impar
    global gale1_impar
    global gale2_impar
    global red_impar
    global red
    global green
    global zero

    if tipo[0:3] == ['IMPAR', 'IMPAR', 'IMPAR'] and entrada_impar == True:
        
        bot.send_message(chat_id=chat_id, text='ENTRADA PAR')
        
        entrada_du = False 
        entrada_co = False
        entrada_vermelho = False
        entrada_black = False
        entrada_par = False
        entrada_impar = False
        green_impar = True
        gale1_impar = True
        
        return 
             
    elif tipo[0:3] == ['PAR', 'IMPAR', 'IMPAR'] and green_impar == True:
        bot.send_message(chat_id=chat_id, text='GREEN')
        
        entrada_du = True 
        entrada_co = True
        entrada_vermelho = True
        entrada_black = True
        entrada_par = True
        entrada_impar = True
        green_impar = False 
        gale1_impar = False 
        gale2_impar = False 
        red_impar = False
        green += 1
        time.sleep(130)  
        
        return

    elif tipo[0:3] == ['ZERO','IMPAR', 'IMPAR'] and green_impar == True:
        bot.send_message(chat_id=chat_id, text='GREEN NO ZERO')

        entrada_co = True 
        entrada_du = True
        entrada_vermelho = True
        entrada_black = True
        entrada_par = True
        entrada_impar = True
        green_impar = False 
        gale1_impar = False 
        gale2_impar = False 
        red_impar = False 
        zero += 1
        time.sleep(130) 
        
        return
           
    elif tipo[0:3] == ['IMPAR', 'IMPAR', 'IMPAR'] and gale1_impar == True:
        
        bot.send_message(chat_id=chat_id, text='GALE 1')
        
        
        gale1_impar = False 
        gale2_impar = True
        
        return 
    
    elif tipo[0:3] == ['IMPAR', 'IMPAR', 'IMPAR'] and gale2_impar == True:
        
        bot.send_message(chat_id=chat_id, text='GALE 2')
        
        
        gale2_impar = False 
        red_impar = True
        
        return 
    
    elif tipo[0:3] == ['IMPAR', 'IMPAR', 'IMPAR'] and red_par == True:
        
        bot.send_message(chat_id=chat_id, text='RED')
        
        
        red_par = False 
        green_impar = False 
        entrada_du = True 
        entrada_co = True
        entrada_vermelho = True
        entrada_black = True
        entrada_par = True
        entrada_impar = True
        red += 1
        time.sleep(600) 
        
        return 


########################################################################################

def resolvendo_problema():
    
    
    driver.switch_to.window(janela)

    while len(driver.find_elements(By.XPATH, '/html/body/div[1]/div[3]/div[1]/div[1]/div/iframe')) == 0:
        time.sleep(2)                         
        
    iframe1 = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[1]/div[1]/div/iframe')
                                             
    driver.switch_to.frame(iframe1)
       
    try:
            
        iframe2 = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/iframe')
        
        if iframe2.is_displayed():
            driver.switch_to.frame(iframe2)    
    
    except NoSuchElementException:
        pass           
    
    try: 
    
        botao = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/button[2]')
        if botao.is_displayed():
            botao.click()
    
    except NoSuchElementException:
        pass

  #  try:

       # if driver.find_elements(By.XPATH, '/html/body/div[1]/div[3]/div/div[3]/div/div') != 0:
           # driver.get('https://www.playpix.com/pb/live-casino/home/-1/All?openGames=40003094-real&gameNames=Roulette%20A')

  #  except NoSuchElementException:
      #  pass
       
   # try:

       # if driver.current_url != "https://www.playpix.com/pb/live-casino/home/-1/All?openGames=40003094-real&gameNames=Roulette%20A":
            #driver.get('https://www.playpix.com/pb/live-casino/home/-1/All?openGames=40003094-real&gameNames=Roulette%20A')
           # time.sleep(3)
           # if driver.find_element(By.XPATH, '/html/body/div[1]/div[6]/div/div/div/div/div/div[2]/form/div[1]').size != 0:
             #   time.sleep(1)

              #  username=driver.find_element(By.XPATH, '/html/body/div[1]/div[6]/div/div/div/div/div/div[2]/form/div[1]/div[3]/div/label/input')
                #password=driver.find_element(By.XPATH, '/html/body/div[1]/div[6]/div/div/div/div/div/div[2]/form/div[1]/div[4]/div/label/input')  

              #  username.send_keys(Infos.username) 
              #  password.send_keys(Infos.password)
               # time.sleep(1)

              #  log_in_button = driver.find_element(By.XPATH, '/html/body/div[1]/div[6]/div/div/div/div/div/div[2]/form/div[1]/div[6]/div/button')
              #  log_in_button.click()
              #  time.sleep(1)
    
  #  except NoSuchElementException:
      #  pass

    try:
        afk = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]').is_displayed()

        if afk:
            driver.refresh()
            #fazer dar refresh na página pra testar
            #print('Resolvendo o Poblema de Inatividade na Roleta!')       
            time.sleep(2)
            driver.get('https://www.playpix.com/pb/live-casino/home/-1/All?openGames=40003094-real&gameNames=Roulette%20A')
            time.sleep(3)
            if driver.find_element(By.XPATH, '/html/body/div[1]/div[6]/div/div/div/div/div/div[2]/form/div[1]').size != 0:
                time.sleep(1)

                username=driver.find_element(By.XPATH, '/html/body/div[1]/div[6]/div/div/div/div/div/div[2]/form/div[1]/div[3]/div/label/input')
                password=driver.find_element(By.XPATH, '/html/body/div[1]/div[6]/div/div/div/div/div/div[2]/form/div[1]/div[4]/div/label/input')  

                username.send_keys(Infos.username) 
                password.send_keys(Infos.password)
                time.sleep(1)

                log_in_button = driver.find_element(By.XPATH, '/html/body/div[1]/div[6]/div/div/div/div/div/div[2]/form/div[1]/div[6]/div/button')
                log_in_button.click()
                time.sleep(1)

    except NoSuchElementException:
        pass

########################################################################################   
    #preciso tratar a tela de inatividade com botão verde 
    
def extracao():
    
    global resultado 
    
    resultado = []
    
    driver.switch_to.window(janela)



    while len(driver.find_elements(By.XPATH, '/html/body/div[1]/div[3]/div[1]/div[1]/div/iframe')) == 0:
       time.sleep(2)                         
        
    iframe1 = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[1]/div[1]/div/iframe')
                                             
    driver.switch_to.frame(iframe1)

    while len(driver.find_elements(By.XPATH, '/html/body/div[2]/div/div/div/iframe')) == 0:
        time.sleep(2)
        
    iframe2 = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/iframe') 
                                             

    driver.switch_to.frame(iframe2)

    while len(driver.find_elements(By.XPATH, '/html/body/div/div/div[1]/div[9]/div[1]/div')) == 0:
         time.sleep(2)

    time.sleep(5)

    resultado = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div[8]/div[3]/div/div[1]').text.split()

        
    return resultado 


while True:
    
    try:
        
        resolvendo_problema()
        
        extracao()
        
        if resultado != check_resultado:
            check_resultado = resultado
            
            conlunas(resultado)
            
            duzias(resultado)

            cores(resultado)     
                    
            par_impar(resultado)

            print(resultado)

            rodadas+=1 
            
            if rodadas >= 2:        
                estrategia_coluna(coluna)
                estrategia_duzia(duzia)
                estrategia_preto(cor)
                estrategia_vermelho(cor)
                estrategia_par(ambos)
                estrategia_impar(ambos)

            if rodadas%20 == 0:

                print(f'Greens: {green} | {(green*100)/(green+red+zero)}%')
                print(f'Reds: {red} | {(red*100)/(green+red+zero)}%')
                banca = (100 + (green * 2.5) + (zero * 35)) - (red * 78)
                fim = dt.datetime.now()
                logging.info(f'Banca: {banca}, {agora}, {fim}')

    except:

        extracao()