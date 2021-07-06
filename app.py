"""
List of exercises for training
"""
import toga
from toga.style import Pack
from toga.style.pack import CENTER, COLUMN, ROW

import threading
import json

#import pandas as pd
import os


def read_exercises():

    #ds = pd.read_excel(os.path.join('data/Exercises.xlsx'))
    #ds.fillna('', inplace=True)
    with open('data/Exercises.json') as f:
        data = json.load(f)

    print(data)
    return data


class MyTraining(toga.App):

    ds = read_exercises()

    l_title = toga.Label('', style=Pack(alignment='center', font_size=20, font_weight='bold'))   # non funziona lo style ... ma nemmeno negli esempi scaricati ...
    l_val = toga.Label('')
    l_descr = toga.Label('')
    b_timer = toga.Button('0')


    index_ex = 0

    def startup(self):

        main_box = toga.Box(style=Pack(direction=COLUMN))
        self.l_title.text = self.ds[0]['Title']
        self.l_val.text = self.elaborate_l_val(0)
        self.l_descr.text = self.ds[0]['Description']

        button = toga.Button('Next', on_press=self.my_callback)
        main_box.add(self.l_title)
        main_box.add(self.l_val)
        main_box.add(toga.Divider())
        main_box.add(self.l_descr)
        main_box.add(button)
        main_box.add(toga.Divider())
        main_box.add(self.b_timer)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

[self.index_ex]

    def my_callback(self,button):
        # handle event
        if self.index_ex < len(self.ds)-1:
            self.index_ex = self.index_ex + 1
            self.l_title.text = self.ds[self.index_ex]['Title']
            self.l_descr.text = self.ds[self.index_ex]['Description']
            self.l_val.text = self.elaborate_l_val(self.index_ex)
        else:
            self.l_title.text = "FINE"
            self.l_descr.text = ''
            self.l_val.text = ''

    def elaborate_l_val(self,ind):
        if self.ds[ind]['Type'] == 'Count':
            return "{} x {}\n{}'' rest between rep".format(self.ds[ind]['Repetition'],self.ds[ind]['Number'],self.ds[ind]['Rest between rep'])
        elif self.ds[ind]['Type'] == 'Time':
            return "{} rep {}\'' each\n{}'' rest between rep".format(self.ds[ind]['Repetition'],self.ds[ind]['Number'],self.ds[ind]['Rest between rep'])
        else:
            return "UNKOWN"

    def get_time(self):
        seconds = 0
        while not self.event.is_set():
            seconds += 1
            self.clock = str(datetime.timedelta(seconds=seconds))
            self.status.set_text(self.clock)
            time.sleep(1)

def main():

    return MyTraining()
