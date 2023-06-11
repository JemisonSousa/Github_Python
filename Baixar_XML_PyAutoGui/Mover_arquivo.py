import pyautogui as pg
import time

# pg.alert("O código vai começar, não mexa mais a partir daqui")
pg.PAUSE = 0.5
pg.press("winleft")
pg.write("chrome")
pg.press("enter")
time.sleep(1)
pg.write("https://drive.google.com/drive/my-drive")
pg.press("enter")

pg.hotkey("winleft", "d")
pg.moveTo(1308, 35)
pg.mouseDown()
pg.moveTo(757, 696)
pg.hotkey("alt", "tab")
pg.mouseUp()
pg.alert("Operaçção concluída com sucesso, volte a utilizar o PC")






# print(pg.position())


