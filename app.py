##Projeto python01
import pyautogui
from time import sleep
##PASSOS
#Clicar e digitar NOME
pyautogui.click(698,379,duration = 2)#usuario
pyautogui.write("petros")#Escrever
#CLICAR e DIGITAR SENHA
pyautogui.click(707,407, duration =2)
pyautogui.write("123")
#CLICAR EM ENTRAR
pyautogui.click(592,441, duration = 2 )
#EXTRAIR PRODUTO
with open ("produtos.txt", "r") as arquivos:
    for linha in arquivos: 
        produto = linha.split(",")[0]
        quantidade = linha.split(",")[1]
        preco = linha.split(",")[2]
        # CLICAR e DIGITAR PRODUTO
        pyautogui.click(408,363, duration= 2)
        pyautogui.write(produto)
        #CLICAR e DIgitar QUANTIDADE
        pyautogui.click(393,392, duration = 2)
        pyautogui.write(quantidade)
        #CLICAR E DIGITAR PREÇO
        pyautogui.click(406,423, duration = 2)
        pyautogui.write(preco)
        #CLICAR EM REGISTRAR
        pyautogui.click(311,580, duration = 1)
sleep = (1)