from tkinter import *
from math import *
root = Tk()

ent = Entry(width=100)
btn = Button(text="Посчитать", height=3, width=30, bg='aqua', font='arial 26')
lab = Label(bg='black', fg='white', height=3, width=30, font='arial 26')


def strToSortlist(event): #Нарушение PEP8 Непонятное имя функции strToSortlist не используется snake_case
s = ent.get()  #Нарушение PEP8 отсутствие отступов 
    s = s.replace(' ', '')
    s = s.replace(',', '.')
    s0 = s
    s = s.replace('^', '**')
    try:
        ans = str(eval(s)) # Критическая уязвимость безопасности (Высокий риск) Использование eval() позволяет выполнить любой код
        lab['text'] = s0 + '=' + ans
        if len(lab['text']) > 31:
            lab['text'] = ans
    except:
        lab['text'] = 'НЕКОРРЕКТНОЕ ВЫРАЖЕНИЕ!' #Некорректная обработка ошибок ловится все исключения без разбора нет информации о конкретной ошибке, пользователю неясно, в чем проблема


btn.bind('<Button-1>', strToSortlist)
ent.bind('<Return>', strToSortlist)
ent.grid(row=1, column=0)
btn.grid(row=2, column=0)
lab.grid(row=3, column=0) #Проблемы с интерфейсом элементы не адаптируются к размеру окна фиксированные размеры виджетов нет отступов между элементами

root.mainloop() #Нет механизма закрытия приложения
