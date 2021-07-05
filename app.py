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
    return ds


class MyTraining(toga.App):

    main_label = toga.Label('')
    ds = read_exercises()
    index_ex = 0

    def startup(self):




        main_box = toga.Box(style=Pack(direction=COLUMN))
        self.main_label.text = self.ds['Text'][self.index_ex]

        button = toga.Button('Click me', on_press=self.my_callback)
        main_box.add(self.main_label)
        main_box.add(button)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()


    def my_callback(self,button):
        # handle event
        #    print(self.ds)
        # self.label.value = (self.ds['Text'][1])
        print('ciao')
        self.index_ex = self.index_ex + 1
        self.main_label.text = self.ds['Text'][self.index_ex]









def main():
    return MyTraining()
