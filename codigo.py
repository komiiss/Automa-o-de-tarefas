
import pyautogui
import time
pyautogui.PAUSE = 2.7 # tempo de espera entre cada comando do pyautogui


link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
# passo 1: entar no sistema da empresa
#abrir o navegador
pyautogui.press('win')  
pyautogui.write('chrome')
pyautogui.press('enter')

pyautogui.write(link)
pyautogui.press('enter')
time.sleep(5) #pausa para o site carregar

# passo 2: fazer login no sistema

#clicar no campo de email
pyautogui.click(x=952, y=515)
pyautogui.write("testando@gmail.com")
#clicar no campo de senha
pyautogui.click(x=996, y=638)
pyautogui.write("automatacaoteste123")
# logar
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(2) #pausa para o sistema carregar

# passo 3: abrir a base de dados
import pandas

tabela = pandas.read_csv("Produtos.csv")
print(tabela)

# passo 4: cadastrar 1 produto
pyautogui.click(x=968, y=368) #clicar no campo do código
pyautogui.write("MOLO000251")
pyautogui.press("tab") # passar para o próximo campo

# marca
pyautogui.write("Logitech")
pyautogui.press("tab")

# tipo de produto
pyautogui.write("Mouse")
pyautogui.press("tab")

# categoria
pyautogui.write("1")
pyautogui.press("tab")

# preço unitário
pyautogui.write("25.95")
pyautogui.press("tab")

# custo
pyautogui.write("6.5")
pyautogui.press("tab")  

# observações
pyautogui.write("obs")
pyautogui.press("tab")
pyautogui.press("enter")  # salvar o produto



# passo 5: repetir o passo o passo 4 até acabar a lista de produtos
for linha in tabela.index:
    pyautogui.click(x=968, y=368) #clicar no campo do código
    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    pyautogui.press("tab") # passar para o próximo campo

    # marca
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")

    # tipo de produto
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")

    # categoria
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")

    # preço unitário
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    # custo
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")  

    # observações
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(str(obs))
        pyautogui.press("tab")
        pyautogui.press("enter")  # salvar o produto