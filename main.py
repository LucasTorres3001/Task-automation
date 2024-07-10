import pyautogui as pg
import pandas as pd


table_name = 'produtos.csv'

table = pd.read_csv(table_name)

pg.PAUSE = 2


pg.hotkey(['win','s'])
pg.write(message='Chrome')
pg.press(keys='enter')

pg.hotkey('ctrl', 't')
pg.write(message='https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pg.press(keys='enter')
pg.press(keys='tab')

pg.PAUSE = 0.6

pg.write(message='goku.agiota@outlook.com')
pg.press(keys='tab')
pg.write(message='abcdefg')
pg.press(keys='enter')

pg.PAUSE = 0.2

for line in table.index:
   code = str(table.loc[line, 'codigo'])
   pg.press(keys='tab')
   pg.write(message=code)

   brand = str(table.loc[line, 'marca'])
   pg.press(keys='tab')
   pg.write(message=brand)

   type_ = str(table.loc[line, 'tipo'])
   pg.press(keys='tab')
   pg.write(message=type_)

   category = str(table.loc[line, 'categoria'])
   pg.press(keys='tab')
   pg.write(message=category)

   unit_price = str(table.loc[line, 'preco_unitario'])
   pg.press(keys='tab')
   pg.write(message=unit_price)

   cost = str(table.loc[line, 'custo'])
   pg.press(keys='tab')
   pg.write(message=cost)

   pg.press(keys='tab')
   obs = str(table.loc[line, 'obs'])
   if obs != 'NaN':
      pg.write(message=obs)
      
   pg.press(keys='enter')
   pg.click(x=258, y=553)
