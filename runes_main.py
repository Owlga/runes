import sys
import sqlite3
from random import sample, randint

from PyQt5.QtWidgets import QApplication, QMainWindow, QInputDialog, QTableWidgetItem
from PyQt5.QtGui import QPixmap
from PIL import Image

from runes import Ui_MainWindow
from runes1 import MainOne
from runes3 import MainThree
from runes5 import MainFive
from runes_help import MainHelp
from runes_pro import MainPro
from runes_history import MainHistory

RUNES = ['fehu', 'uruz', 'thurisaz', 'ansuz', 'raido', 'cano', 'gebo', 'vunjo', 'hagalaz',
         'nautiz', 'isa', 'jera', 'eivaz', 'pertho', 'algiz', 'sowlu', 'teivaz', 'berkana',
         'evaz', 'mannaz', 'laguz', 'inguz', 'othala', 'dagaz', 'odin']

CON = sqlite3.connect('runes.db')
TOTAL = 0


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn5.clicked.connect(self.make5)
        self.btn3.clicked.connect(self.make3)
        self.btn1.clicked.connect(self.make1)
        self.btn5_new.clicked.connect(self.make5_new)
        self.btn_help.clicked.connect(self.help)
        self.btnr.clicked.connect(self.pro)
        self.history.clicked.connect(self.get_history)
        cur = CON.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS runes (id INTEGER PRIMARY KEY, 
        name TEXT, position INTEGER);''')
        CON.commit()
        cur.execute('''DELETE from runes''')
        CON.commit()

    def make5(self):
        self.second = MakeFive()
        self.second.show()

    def make3(self):
        self.second = MakeThree()
        self.second.show()

    def make1(self):
        self.second = MakeOne()
        self.second.show()

    def make5_new(self):
        self.second = MakeFiveNew()
        self.second.show()

    def help(self):
        self.second = MakeHelp()
        self.second.show()

    def pro(self):
        num, ok_pressed = QInputDialog.getInt(self, "сколько?",
                                                   "выберите число", 3, 1, 25, 1)
        if ok_pressed:
            self.second = MakePro(num)
            self.second.show()

    def get_history(self):
        cur = CON.cursor()
        result = cur.execute("""SELECT * FROM runes""").fetchall()
        self.second = MakeHistory(result)
        self.second.show()


class MakeFive(QMainWindow, MainFive):
    def __init__(self):
        global TOTAL
        super().__init__()
        self.setupUi(self)
        total = [(el, randint(0, 1)) for el in sample(RUNES, 5)]

        filename = total[0][0] + '.png'
        if total[0][1] == 1:
            im = Image.open(filename)
            im2 = im.rotate(180)
            im2.save('ex.png')
            filename = 'ex.png'
        self.pixmap = QPixmap(filename)
        self.label_2.setPixmap(self.pixmap)

        filename = total[1][0] + '.png'
        if total[1][1] == 1:
            im = Image.open(filename)
            im2 = im.rotate(180)
            im2.save('ex.png')
            filename = 'ex.png'
        self.pixmap = QPixmap(filename)
        self.label_3.setPixmap(self.pixmap)

        filename = total[2][0] + '.png'
        if total[2][1] == 1:
            im = Image.open(filename)
            im2 = im.rotate(180)
            im2.save('ex.png')
            filename = 'ex.png'
        self.pixmap = QPixmap(filename)
        self.label.setPixmap(self.pixmap)

        filename = total[3][0] + '.png'
        if total[3][1] == 1:
            im = Image.open(filename)
            im2 = im.rotate(180)
            im2.save('ex.png')
            filename = 'ex.png'
        self.pixmap = QPixmap(filename)
        self.label_4.setPixmap(self.pixmap)

        filename = total[4][0] + '.png'
        if total[4][1] == 1:
            im = Image.open(filename)
            im2 = im.rotate(180)
            im2.save('ex.png')
            filename = 'ex.png'
        self.pixmap = QPixmap(filename)
        self.label_6.setPixmap(self.pixmap)

        with open('meanings.txt', encoding='utf-8') as file:
            lines = file.readlines()
            for el in total:
                mean = ((lines[RUNES.index(el[0])].split(';'))[el[1]]).rstrip('\n')
                if lines[RUNES.index(el[0])].split(';')[0] == \
                        lines[RUNES.index(el[0])].split(';')[1].rstrip('\n'):
                    self.txt.appendPlainText(f'ваша руна {el[0]} не имеет перевернутого значения, она означает {mean}')
                else:
                    self.txt.appendPlainText(f'ваша руна {el[0]} в положении {el[1]} означает {mean}')
                cur = CON.cursor()
                TOTAL = TOTAL + 1
                cur.execute(f'''INSERT INTO runes (ID, name, position) VALUES ('{TOTAL}', '{el[0]}', {el[1]})''')
                CON.commit()


class MakeThree(QMainWindow, MainThree):
    def __init__(self):
        global TOTAL
        super().__init__()
        self.setupUi(self)
        total = [(el, randint(0, 1)) for el in sample(RUNES, 3)]

        filename = total[0][0] + '.png'
        if total[0][1] == 1:
            im = Image.open(filename)
            im2 = im.rotate(180)
            im2.save('ex.png')
            filename = 'ex.png'
        self.pixmap = QPixmap(filename)
        self.label.setPixmap(self.pixmap)

        filename = total[1][0] + '.png'
        if total[1][1] == 1:
            im = Image.open(filename)
            im2 = im.rotate(180)
            im2.save('ex.png')
            filename = 'ex.png'
        self.pixmap = QPixmap(filename)
        self.label_3.setPixmap(self.pixmap)

        filename = total[2][0] + '.png'
        if total[2][1] == 1:
            im = Image.open(filename)
            im2 = im.rotate(180)
            im2.save('ex.png')
            filename = 'ex.png'
        self.pixmap = QPixmap(filename)
        self.label_2.setPixmap(self.pixmap)

        keys = ('вся ситуация', 'что надо делать', 'что будет если это сделать')
        with open('meanings.txt', encoding='utf-8') as file:
            lines = file.readlines()
            for i, el in enumerate(total):
                mean = ((lines[RUNES.index(el[0])].split(';'))[el[1]]).rstrip('\n')
                self.txt.appendPlainText(f'{keys[i]}: {mean}')
                cur = CON.cursor()
                TOTAL = TOTAL + 1
                cur.execute(f'''INSERT INTO runes (ID, name, position) VALUES ('{TOTAL}', '{el[0]}', {el[1]})''')
                CON.commit()


class MakeOne(QMainWindow, MainOne):
    def __init__(self):
        super().__init__()
        global TOTAL
        self.setupUi(self)
        total = [(RUNES[randint(0, 24)], randint(0, 1))]

        filename = total[0][0] + '.png'
        if total[0][1] == 1:
            im = Image.open(filename)
            im2 = im.rotate(180)
            im2.save('ex.png')
            filename = 'ex.png'
        self.pixmap = QPixmap(filename)
        self.label.setPixmap(self.pixmap)

        with open('meanings.txt', encoding='utf-8') as file:
            lines = file.readlines()
            for el in total:
                mean = ((lines[RUNES.index(el[0])].split(';'))[el[1]]).rstrip('\n')
                if lines[RUNES.index(el[0])].split(';')[0] == \
                        lines[RUNES.index(el[0])].split(';')[1].rstrip('\n'):
                    self.txt.appendPlainText(f'ваша руна {el[0]} не имеет перевернутого значения, она означает {mean}')
                else:
                    self.txt.appendPlainText(f'ваша руна {el[0]} в положении {el[1]} означает {mean}')
                cur = CON.cursor()
                TOTAL = TOTAL + 1
                cur.execute(f'''INSERT INTO runes (ID, name, position) VALUES ('{TOTAL}', '{el[0]}', {el[1]})''')
                CON.commit()


class MakeFiveNew(QMainWindow, MainFive):
    def __init__(self):
        super().__init__()
        global TOTAL
        self.setupUi(self)
        keys = ('вам предстоит', 'это принесёт', 'но будет', 'а потом будет', 'общий итог')
        total = [(el, randint(0, 1)) for el in sample(RUNES, 5)]

        filename = total[0][0] + '.png'
        if total[0][1] == 1:
            im = Image.open(filename)
            im2 = im.rotate(180)
            im2.save('ex.png')
            filename = 'ex.png'
        self.pixmap = QPixmap(filename)
        self.label_2.setPixmap(self.pixmap)

        filename = total[1][0] + '.png'
        if total[1][1] == 1:
            im = Image.open(filename)
            im2 = im.rotate(180)
            im2.save('ex.png')
            filename = 'ex.png'
        self.pixmap = QPixmap(filename)
        self.label_3.setPixmap(self.pixmap)

        filename = total[2][0] + '.png'
        if total[2][1] == 1:
            im = Image.open(filename)
            im2 = im.rotate(180)
            im2.save('ex.png')
            filename = 'ex.png'
        self.pixmap = QPixmap(filename)
        self.label.setPixmap(self.pixmap)

        filename = total[3][0] + '.png'
        if total[3][1] == 1:
            im = Image.open(filename)
            im2 = im.rotate(180)
            im2.save('ex.png')
            filename = 'ex.png'
        self.pixmap = QPixmap(filename)
        self.label_4.setPixmap(self.pixmap)

        filename = total[4][0] + '.png'
        if total[4][1] == 1:
            im = Image.open(filename)
            im2 = im.rotate(180)
            im2.save('ex.png')
            filename = 'ex.png'
        self.pixmap = QPixmap(filename)
        self.label_6.setPixmap(self.pixmap)

        with open('meanings.txt', encoding='utf-8') as file:
            lines = file.readlines()
            for i, el in enumerate(total):
                mean = ((lines[RUNES.index(el[0])].split(';'))[el[1]]).rstrip('\n')
                self.txt.appendPlainText(f'{keys[i]}: {mean}')
                cur = CON.cursor()
                TOTAL = TOTAL + 1
                cur.execute(f'''INSERT INTO runes (ID, name, position) VALUES ('{TOTAL}', '{el[0]}', {el[1]})''')
                CON.commit()


class MakeHelp(QMainWindow, MainHelp):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        for el in RUNES:
            self.cmb.addItem(el)
        self.btn.clicked.connect(self.information)

    def information(self):
        total = self.cmb.currentText()
        self.txt.clear()
        with open('meanings.txt', encoding='utf-8') as file:
            lines = file.readlines()
            el = total
            mean1 = ((lines[RUNES.index(el)].split(';'))[0]).rstrip('\n')
            mean2 = ((lines[RUNES.index(el)].split(';'))[1]).rstrip('\n')
            if mean1 == mean2:
                self.txt.appendPlainText(f'руна {el} не имеет перевернутого значения, она означает {mean1}')
            else:
                self.txt.appendPlainText(f'руна {el} в положении 0 означает {mean1}, в положении 1 означает {mean2}')
            self.pixmap = QPixmap(total + '.png')
            self.lbl2.setPixmap(self.pixmap)


class MakePro(QMainWindow, MainPro):
    def __init__(self, num):
        super().__init__()
        global TOTAL
        self.setupUi(self)
        btns = [self.label, self.label_2, self.label_3, self.label_4, self.label_5,
                self.label_6, self.label_7, self.label_8, self.label_9, self.label_10,
                self.label_11, self.label_12,self.label_13, self.label_14, self.label_15,
                self.label_16, self.label_17, self.label_18, self.label_19, self.label_20,
                self.label_21, self.label_22, self.label_23, self.label_24, self.label_25]
        self.txt.clear()
        total = [(el, randint(0, 1)) for el in sample(RUNES, num)]

        with open('meanings.txt', encoding='utf-8') as file:
            lines = file.readlines()
            for i, el in enumerate(total):
                mean = ((lines[RUNES.index(el[0])].split(';'))[el[1]]).rstrip('\n')
                if lines[RUNES.index(el[0])].split(';')[0] == \
                        lines[RUNES.index(el[0])].split(';')[1].rstrip('\n'):
                    self.txt.appendPlainText(
                        f'ваша руна {el[0]} не имеет перевернутого значения, она означает {mean}')
                else:
                    self.txt.appendPlainText(f'ваша руна {el[0]} в положении {el[1]} означает {mean}')
                cur = CON.cursor()
                TOTAL = TOTAL + 1
                cur.execute(f'''INSERT INTO runes (ID, name, position) VALUES ('{TOTAL}', '{el[0]}', {el[1]})''')
                CON.commit()

                filename = el[0] + '.png'
                if el[1] == 1:
                    im = Image.open(filename)
                    im2 = im.rotate(180)
                    im2.save('ex.png')
                    filename = 'ex.png'
                self.pixmap = QPixmap(filename)
                btns[i].setPixmap(self.pixmap)

        for el in btns:
            if el.text() == 'TextLabel':
                el.setText('')


class MakeHistory(QMainWindow, MainHistory):
    def __init__(self, result):
        super().__init__()
        self.setupUi(self)
        self.tbl.setRowCount(len(result))
        for i, el in enumerate(result):
            for j, ell in enumerate(el):
                self.tbl.setItem(i, j, QTableWidgetItem(str(ell)))


'''if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
'''
app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec())