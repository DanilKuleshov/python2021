from tkinter import *
import random

root = Tk()
root.title('Виселица')
canvas = Canvas(root, width=600, height=600)
canvas.pack(fill=BOTH)

def but():
    y = 0
    while y < 600:
        x = 0
        while x < 600:
            canvas.create_rectangle(x, y, x + 30, y + 30, fill="Gainsboro", outline="black")

            x = x + 30
        y = y + 30


faq = '''
Суть игры
Суть этой игры в отгадывании слова по буквам
за определённое количество ходов.

Бот задумывает какое-нибудь слово. Пишет его 
первую и последнюю буквы, а вместо недостающих 
букв ставит черточки. Задача игрока - отгадать 
загаданное слово. Он называет любую букву. 
Если эта буква в слове есть - ведущий вписывает 
её своё на место. Если нет, то данная буква будет 
подсвечена красным цветом, затем начинают рисовать 
"виселицу". За эти несколько попыток игрок должен 
угадать слово. Если не получилось - проиграл.
'''
canvas.create_text(310, 240, text=faq, fill="DimGray", font=("Monospace", "15"))
slova = ['виселица', 'смартфон', 'маргарин', 'мегагерц', 'страница', 'креветка', 'микрофон', 'автопарк']

def arr():
    but()
    word = random.choice(slova)

    wo = word[1:-1]
    wor = []
    for i in wo:
        wor.append(i)
    a0 = canvas.create_text(282, 40, text=word[0], fill="purple", font=("Monospace", "18"))
    a1 = canvas.create_text(315, 40, text='_', fill="purple", font=("Monospace", "18"))
    a2 = canvas.create_text(347, 40, text='_', fill="purple", font=("Monospace", "18"))
    a3 = canvas.create_text(380, 40, text='_', fill="purple", font=("Monospace", "18"))
    a4 = canvas.create_text(412, 40, text='_', fill="purple", font=("Monospace", "18"))
    a5 = canvas.create_text(444, 40, text='_', fill="purple", font=("Monospace", "18"))
    a6 = canvas.create_text(477, 40, text='_', fill="purple", font=("Monospace", "18"))
    a6 = canvas.create_text(510, 40, text=word[-1], fill="purple", font=("Monospace", "18"))
    list1 = [1, 2, 3, 4, 5, 6]
    alfabet = u'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    canvas.create_line(10, 10, 200, 10, width=4)
    canvas.create_line(10, 10, 10, 400, width=4)
    canvas.create_line(50, 10, 10, 100, width=4)
    er = []
    win = []

    def a(v):
        ind_alf = alfabet.index(v)
        key = alfabet[ind_alf]

        if v in wor:

            ind = wor.index(v)
            b2 = list1[ind]
            wor[ind] = '1'

            def kord():
                if b2 == 1:
                    x1, y1 = 315, 40
                if b2 == 2:
                    x1, y1 = 347, 40
                if b2 == 3:
                    x1, y1 = 380, 40
                if b2 == 4:
                    x1, y1 = 412, 40
                if b2 == 5:
                    x1, y1 = 444, 40
                if b2 == 6:
                    x1, y1 = 477, 40
                return x1, y1

            x1, y1 = kord()
            win.append(v)
            a2 = canvas.create_text(x1, y1, text=wo[ind], fill="purple", font=("Monospace", "18"))
            btn[key]["bg"] = "green"
            if not v in wor:
                btn[key]['state'] = 'disabled'
            if v in wor:
                win.append(v)
                ind2 = wor.index(v)
                b2 = list1[ind2]
                x1, y1 = kord()
                canvas.create_text(x1, y1, text=wo[ind2], fill="purple", font=("Monospace", "18"))
            if len(win) == 6:
                canvas.create_text(310, 400, text="You win!", fill="LimeGreen", font=("Monospace", "30"))
                canvas.create_text(310, 460, text="If you want to play again, pleas enter Restart", fill="LimeGreen", font=("Monospace", "15"))
                for i in alfabet:
                    btn[i]['state'] = 'disabled'
        else:
            er.append(v)
            btn[key]["bg"] = "red"
            btn[key]['state'] = 'disabled'

            if len(er) == 1:
                golova()
            elif len(er) == 2:
                telo()
            elif len(er) == 3:
                rukaL()
            elif len(er) == 4:
                rukaP()
            elif len(er) == 5:
                nogaL()
            elif len(er) == 6:
                nogaP()
                end()
            root.update()

    btn = {}

    def gen(u, x, y):

        btn[u] = Button(root, text=u, width=3, height=1, command=lambda: a(u))
        btn[u].place(x=str(x), y=str(y))

    x = 265
    y = 110
    for i in alfabet[0:7]:
        gen(i, x, y)
        x = x + 33
    x = 265
    y = 137
    for i in alfabet[7:14]:
        gen(i, x, y)
        x = x + 33
    x = 265
    y = 164
    for i in alfabet[14:21]:
        gen(i, x, y)
        x = x + 33
    x = 265
    y = 191
    for i in alfabet[21:28]:
        gen(i, x, y)
        x = x + 33
    x = 298
    y = 218
    for i in alfabet[28:33]:
        gen(i, x, y)
        x = x + 33
    canvas.create_rectangle(240, 90, 510, 270, fill="LightGray", outline="black")

    def golova():

        canvas.create_oval(79, 59, 120, 80, width=4, fill="Gainsboro")

        root.update()

    def telo():

        canvas.create_line(100, 80, 100, 200, width=4)

        root.update()

    def rukaP():

        canvas.create_line(100, 80, 145, 100, width=4)

        root.update()

    def rukaL():

        canvas.create_line(100, 80, 45, 100, width=4)

        root.update()

    def nogaL():

        canvas.create_line(100, 200, 45, 300, width=4)

        root.update()

    def nogaP():

        canvas.create_line(100, 200, 145, 300, width=4)

        root.update()

    def end():
        canvas.create_text(310, 400, text="The end", fill="red", font=("Monospace", "30"))
        canvas.create_text(310, 460, text="If you want to play again, pleas enter the Restart", fill="red", font=("Monospace", "15"))
        canvas.create_line(100, 10, 100, 60, width=4)
        for i in alfabet:
            btn[i]['state'] = 'disabled'


def changeText():
    btn01['text'] = 'Restart'

def together():
    changeText()
    arr()

btn01 = Button(root, text='Start', width=40, height=1, command=lambda: together())
btn01.place(x=165, y=542)
btn01["bg"] = "Gray"
root.mainloop()
