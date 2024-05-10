import pyautogui;
import time;
import pandas;

#? Waits for 0.5s after every command bellow this line
pyautogui.PAUSE = 0.5;

#? On Windows -> Open windows explorer -> find brower -> open browser
# pyautogui.press("win")
# pyautogui.write("chrome")
# pyautogui.press("enter")

#? On Linux -> Click on chrome icon on navbar and open new window
pyautogui.click(x=922, y=1045, button='right')
pyautogui.click(x=922, y=849)


#? Go page where we will dump the csv
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

#? Waits for page to load
time.sleep(3)

#? Look for login input -> fill login form -> login
pyautogui.click(x=946, y=440)
pyautogui.write("email@email.com.br")
pyautogui.press("tab")
pyautogui.write("kdasjdiaojsd2w123123")
pyautogui.press("tab")
pyautogui.press("enter")

#? Waits for page to load
time.sleep(5)

#? Acess csv data
table = pandas.read_csv("PowerUp/products.csv")

#? Fill dump form with csv data by accessing every input in a loop based on every line of the csv document (each input received a column)
#? First element of a form can be selected by tab or by clicking at the position of the first input
for line in table.index :
  pyautogui.click(x=933, y=329) 
  pyautogui.write(str(table.loc[line, "codigo"]))
  pyautogui.press("tab")
  
  pyautogui.write(str(table.loc[line, "marca"]))
  pyautogui.press("tab")
  
  pyautogui.write(str(table.loc[line, "tipo"]))
  pyautogui.press("tab")
  
  pyautogui.write(str(table.loc[line, "categoria"]))
  pyautogui.press("tab")
  
  pyautogui.write(str(table.loc[line, "preco_unitario"]))
  pyautogui.press("tab")
  
  pyautogui.write(str(table.loc[line, "custo"]))
  pyautogui.press("tab")
  
  obs = str(table.loc[line, "obs"])
  if obs != "nan":
    pyautogui.write(obs)
  pyautogui.press("tab")
  
  pyautogui.press("enter")
  pyautogui.scroll(999)
  