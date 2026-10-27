import pyautogui
import time

# ---> É usado para fazer comentários dentro do Python. 

# Comando pyautogui 
#pyautogui.click --> Clicar em algum lugar 
#pyautogui.press --> Apertar 1 tecla 
#pyautogui.write --> Escrever um texto 
#pyautogui.hotkey --> Apertar uma combinação de teclas (atalhos)
 
# Passo a passo do projeto

pyautogui.PAUSE = 0.5 # --> Faz todos os comandos esperar 

#Passo 1: Entrar no sistema da empresa - https://dlp.hashtagtreinamentos.com/python/intensivao/login 
#Entrar no Google Chrome

#Para fazer isso de forma autonôma utiluza o comando | --> pyautogui |
# Então para ele clicar uma tecla de forma automática vamos usar --> pyautogui.press 

pyautogui.press("win")
pyautogui.write("opera") 
pyautogui.press("enter")

#Entrando no site da empresa
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

#Comando para esperar depois do enter
#esperar 3 segundos
time.sleep(3) # --> Faz esperar somente aqui 

#Passo 2: fazer o login no sistema
#Para peencher o e-mail
pyautogui.click(x=-680, y=407) 
pyautogui.write("teste.user@gmail.com")

#Para preencher a senha
pyautogui.press("tab")
pyautogui.write("Teste12345*@")

#Botão para logar
pyautogui.press("tab")
pyautogui.press("enter")

#eperar 3 segundos 
time.sleep(3)

#Passo 3: Improtando a base de dados 
import pandas # --> | pandas | arquivo para exportação de uma base de dados 

tabela = pandas.read_csv("produtos.csv") # --> Criando a uma váriavel, chamando de tabela

print(tabela)

#Passo 4: Cadastrando um produto

for linha in tabela.index: #Para cada linha da minha tabela, tudo que está dentro do laço for é o que você quer que ele excute denovo 
    pyautogui.click(x=-698, y=292)
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)

    pyautogui.press("tab") #Comando para pular para o próximo campo
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca)

    pyautogui.press("tab") #Comando para pular para o próximo campo
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)

    pyautogui.press("tab") #Comando para pular para o próximo campo
    categoria = str (tabela.loc[linha, "categoria"]) 
    pyautogui.write(categoria)

    pyautogui.press("tab") #Comando para pular para o próximo campo
    preco_unitario = str (tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)

    pyautogui.press("tab") #Comando para pular para o próximo campo
    custo = str (tabela.loc[linha, "custo"])
    pyautogui.write(custo)

    pyautogui.press("tab") #Comando para pular para o próximo campo
    obs = str (tabela.loc[linha, "obs"])
    
    if obs != "nan":
        pyautogui.write(obs)    


    pyautogui.press("tab") #Passa para o botão de enviar
    pyautogui.press("enter") 

    pyautogui.scroll(10000) # --> Comando para rolar a tela para baixo ou para cima | número positivo dentro dos parênteses sobe e número negativo desce 

#Passo 5: Repetir o procedimento para todos produtos 

#nan --> Isso no Python significa Not a Number - ( Não a número) 