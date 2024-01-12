import pyautogui
import time

#https://dlp.hashtagtreinamentos.com/python/intensivao/login
pyautogui.PAUSE = 1

# 1 - Abrir o navegador
pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")

# 2 - Entrar o sistema da empresa
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

# 3 - Fazer login
pyautogui.click(x=473, y=355)
pyautogui.write("pedroherique.pepper@gmail.com")
pyautogui.press("tab")
pyautogui.write("pedrin123")
pyautogui.press("tab")
pyautogui.press("enter")

# 4 - Importando base de dados
import pandas

tabela = pandas.read_csv("produtos.csv")
print(tabela)
for linha in tabela.index:
    pyautogui.PAUSE =  0.5
    pyautogui.click(x=434, y=242)
    #Codigo
    pyautogui.write(tabela.loc[linha, "codigo"])
    pyautogui.press("tab")
    #Marca
    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")
    #Tipo
    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")
    #Categoria
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    #Preco_Unitario
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    #Custo
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    #Obs
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(obs)
        #Envio de dados
    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(5000)


