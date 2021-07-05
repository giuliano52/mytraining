"""
List of exercises for training
"""
import toga
from toga.style import Pack
from toga.style.pack import CENTER, COLUMN, ROW, Pack


import pandas as pd
import os


def read_exercises():
    ds = pd.read_excel('data/Exercises.xlsx')
    ds.fillna('', inplace=True)
    return ds


class MyTraining(toga.App):

    l_title = toga.Label('', style=Pack(alignment='center', font_size=20, font_weight='bold'))   # non funziona lo style ... ma nemmeno negli esempi scaricati ...
    l_val = toga.Label('')
    l_descr = toga.Label('')
    ds = read_exercises()
    index_ex = 0

    def startup(self):

        main_box = toga.Box(style=Pack(direction=COLUMN))
        self.l_title.text = self.ds['Title'][0]
        self.l_val.text = self.elaborate_l_val(0)
        self.l_descr.text = self.ds['Description'][0]

        button = toga.Button('Next', on_press=self.my_callback)
        main_box.add(self.l_title)
        main_box.add(self.l_val)
        main_box.add(toga.Divider())
        main_box.add(self.l_descr)
        main_box.add(button)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()


    def my_callback(self,button):
        # handle event
        if self.index_ex < len(self.ds)-1:
            self.index_ex = self.index_ex + 1
            self.l_title.text = self.ds['Title'][self.index_ex]
            self.l_descr.text = self.ds['Description'][self.index_ex]
            self.l_val.text = self.elaborate_l_val(self.index_ex)
        else:
            self.l_title.text = "FINE"
            self.l_descr.text = ''
            self.l_val.text = ''

    def elaborate_l_val(self,ind):
        if self.ds['Type'][ind] == 'Count':
            return "{} x {}".format(self.ds['Repetition'][ind],self.ds['Number'][ind])
        elif self.ds['Type'][ind] == 'Time':
            return "{} rep {}'' each ".format(self.ds['Repetition'][ind],self.ds['Number'][ind])
        else:
            return "UNKOWN"

def main():
    return MyTraining()
