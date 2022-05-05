# This is a sample Python script.
from tkinter import *
from tkinter import messagebox
from random import *
from numpy import *
import keyboard

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



def igrok(karta1,karta2,bank,nomer,mb):
    winigr=Tk()
    winigr.geometry('200x200')
    winigr.title("игрок №",nomer)
    karta11=Label(winigr,text=karta1)
    karta11.grid(column=1,row=1)
    karta22 = Label(winigr, text=karta2)
    karta22.grid(column=1, row=2)
    ostavke=Label(winigr,text="введите сумму ставки")
    ostavke.grid(column=1,row=3)
    stavka=StringVar()
    stavka.set(mb)
    vvod=Entry(winigr, width=7,borderwidth=1,textvariable=stavka)
    vvod.grid(column=1,row=4)
    knopka=Button(winigr, command=winigr.quit)


    winigr.mainloop()

def perev(karta):
    karti = [
        ["2 крести", "3 крести", "4 крести", "5 крести", " 6 крести", "7 крести", "8 крести", "9 крести", "10 крести","валет крести", "дама крести", "король крести", "туз крести"],
        ["2 буби", "3 буби", "4 буби", "5 буби", " 6 буби", "7 буби", "8 буби", "9 буби", "10 буби", "валет буби","дама буби", "король буби", "туз буби"],
        ["2 черви", "3 черви", "4 черви", "5 черви", " 6 черви", "7 черви", "8 черви", "9 черви", "10 черви","валет черви", "дама черви", "король черви", "туз черви"],
        ["2 пики", "3 пики", "4 пики", "5 пики", " 6 пики", "7 пики", "8 пики", "9 пики", "10 пики", "валет пики","дама пики", "король пики", "туз пики"]]
    a=0
    b=0
    print(a,b)
    while karta!=karti[a][b]:
        b+=1
        if b==12:
            if karta!=karti[a][b]:
                a+=1
                b=0
            else:
                karta=karti[a][b]
    return (a,b)
def kombi(karta1,karta2,karta3,karta4,karta5,karta6,karta7):
    y1,x1=perev(karta1)
    y2,x2 = perev(karta2)
    y3,x3 = perev(karta3)
    y4,x4 = perev(karta4)
    y5,x5 = perev(karta5)
    y6,x6 = perev(karta6)
    y7,x7 = perev(karta7)
    print(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6, x7, y7)

    karta=array([(x1,y1),(x2,y2),(x3,y3),(x4,y4),(x5,y5),(x6,y6),(x7,y7)])

    x=[x1,x2,x3,x4,x5,x6,x7]
    y=[y1,y2,y3,y4,y5,y6,y7]
    karti=[[x1,y1],[x2,y2],[x3,y3],[x4,y4],[x5,y5],[x6,y6],[x7,y7]]
    karti=sorted(karti, key=lambda x:x[0])
    komb=0
    n=0
    print(karti)
    if karti[6][0]==12:
        for i in range(1,6):
            if (karti[i][0]==8 or karti[i][0]==9 or karti[i][0]==10 or karti[i][0]==11 or karti[i][0]==12) and karti[i][1]==karti[i-1][1]:
                n+=1


        if n==4:
            komb=10
        print(n, "10")
        n=0

    elif komb!=10:
        for i in range(1,6):
            if karti[i][0]-karti[i-1][0]==1 and karti[i][1]==karti[i-1][1]:
                n+=1

        if n==4:
            komb=9
        print(n,"9")
        n=0

    elif komb!=9:
        for i in range(1,6):
            if x.count(karti[0][i])==4:
                komb=8
        print(n,"8")
        n=0

    elif komb!=8:
        for i in range(1,6):
            while karti[i][0]==karti[i-1][0] :
                n+=1
                a=karti[i][0]
        if n==1 or n==2:
            while karti[i][0]==karti[i-1][0] and karti[i][0]!=a:
                n+=1
            if n==3:
                komb=7
        print(n,"7")
        n=0

    elif komb!=7:
        for i in range(0,6):
            if y.count(karti[i][1])==5:
                komb=6

    elif komb!=6:
        print("gg")
        for i in range(1,6):
            if karti[i][0]-karti[i-1][0]==1:
                n+=1

        if n==4:
            komb=5
        print(n,"6")
        n=0

    elif komb!=5:
        for i in range(1,6):
            if x.count(karti[i][0])==3:
                komb=4

    elif komb!=4:
        for i in range(0,6):
            if x.count(karti[i][0])==2:
                a=karti[i][0]
                for n in range(i,6):
                    if x.count(karti[n+1][0])==2 and karti[n+1][0]!=a:
                        komb=3

    elif komb!=3:
        for i in range(0,6):
            if x.count(karti[i][0]) == 2:
                komb=2

    else:
        komb=1
    star=max(karti[0][0],karti[1][0])

    return komb,star


def koloda():
    karti= [["2 крести","3 крести","4 крести","5 крести"," 6 крести","7 крести","8 крести","9 крести","10 крести","валет крести","дама крести","король крести","туз крести"],
            ["2 буби","3 буби","4 буби","5 буби"," 6 буби","7 буби","8 буби","9 буби","10 буби","валет буби","дама буби","король буби","туз буби"],
            ["2 черви","3 черви","4 черви","5 черви"," 6 черви","7 черви","8 черви","9 черви","10 черви","валет черви","дама черви","король черви","туз черви"],
            ["2 пики","3 пики","4 пики","5 пики"," 6 пики","7 пики","8 пики","9 пики","10 пики","валет пики","дама пики","король пики","туз пики"]]

    vidankart=[]
    kolvokart=1
    b = randint(0, 12)
    a = randint(0, 3)
    vidankart.append(karti[a][b])
    while kolvokart<13:
        prov = 0
        b = randint(0, 12)
        a = randint(0, 3)
        n=0

        for i in range(0,kolvokart):
            if vidankart[n]!=karti[a][b]:
                prov+=1
                n+=1
            else:
                print("==")
                b = randint(0, 12)
                a = randint(0, 3)
                n+=1

        if prov==kolvokart:
            vidankart.append(karti[a][b])
            kolvokart += 1
            print("+1")
    print(vidankart)
    return (vidankart[0],vidankart[1],vidankart[2],vidankart[3],vidankart[4],vidankart[5],vidankart[6],vidankart[7],vidankart[8],vidankart[9],vidankart[10],vidankart[11],vidankart[12],)
def huynya():
    messagebox.showinfo("долбоёб", "Вводи числа блять")

def huynya2():
    messagebox.showinfo("долбоёб", "Вводи имена покороче")

def provvvod(bank1,bank2,bank3,bank4,name1,name2,name3,name4):

    bankp1 = bank1.isdigit()
    bankp2 = bank2.isdigit()
    bankp3 = bank3.isdigit()
    bankp4 = bank4.isdigit()
    namep1=len(name1)
    namep2=len(name2)
    namep3=len(name3)
    namep4=len(name4)
    prov=0
    i=0
    if bankp1==True:
        if bankp2==True:
            if bankp3==True:
                if bankp4==True:
                    prov=1
                else:
                    huynya()
            else:
                huynya()
        else:
            huynya()
    else:
        huynya()

    if namep1<9:
        if namep2<9:
            if namep3<9:
                if namep4<9:
                    if prov==1:
                        i=1
                else:
                    huynya2()
            else:
                huynya2()
        else:
            huynya2()
    else:
        huynya2()
    return i


def stol(bank1,bank2,bank3,bank4,name1,name2,name3,name4):

    bank=StringVar()
    bank.set("0")
    nomerrazd = StringVar()
    nomerrazd.set("0")
    nomerigr = StringVar()
    nomerigr.set("0")
    winstol=Tk()
    winstol.geometry('600x400')
    winstol.title("покер. игровой стол")
    winstolverh=Label(winstol, text="банк  =")
    winstolverh.grid(column=5,row=0)
    winstolverh2 = Label(winstol, text=bank.get())
    winstolverh2.grid(column=6, row=0)
    winstolbok = Label(winstol, text="номер раздачи")
    winstolbok.grid(column=10, row=0)
    winstolbok = Label(winstol, text=nomerrazd.get())
    winstolbok.grid(column=11, row=0)
    winstolbok2 = Label(winstol, text="номер игры")
    winstolbok2.grid(column=10, row=1)
    winstolbok2 = Label(winstol, text=nomerigr.get())
    winstolbok2.grid(column=11, row=1)
    karta1,karta2,karta3,karta4,karta5,karta11,karta12,karta21,karta22,karta31,karta32,karta41,karta42=koloda()
    print(karta2)
    print(kombi("дама буби","дама черви","дама крести","валет черви", "дама пики", "король черви", "туз черви"))
    winstol.mainloop()


def predprovvod(bank1,bank2,bank3,bank4,name1,name2,name3,name4):
    a=provvvod(bank1,bank2,bank3,bank4,name1,name2,name3,name4)
    if a==1:
        stol(bank1,bank2,bank3,bank4,name1,name2,name3,name4)

def vvoddannih():
    prov=0
    winvvod=Tk()
    winvvod.geometry('600x200')
    winvvod.title("покер. начальное меню")
    winvvodverh=Label(winvvod,text="Введите данные об игроках")
    winvvodverh.grid(column=1,row=0)
    vvodname1=Label(winvvod, text="| имя 1 игрока |")
    vvodname1.grid(column=2,row=1)
    vvodname2 = Label(winvvod, text="| имя 2 игрока |")
    vvodname2.grid(column=3,row=1)
    vvodname3 = Label(winvvod, text="| имя 3 игрока |")
    vvodname3.grid(column=4,row=1)
    vvodname4 = Label(winvvod, text="| имя 4 игрока |")
    vvodname4.grid(column=5,row=1)

    name1=StringVar()
    name1.set("имя 1")
    vvodname11=Entry(winvvod, relief=RAISED, width=15,borderwidth=2,textvariable=name1)
    vvodname11.grid(column=2,row=2)

    name2 = StringVar()
    name2.set("имя 2")
    vvodname22 = Entry(winvvod, relief=RAISED, width=15, borderwidth=2, textvariable=name2)
    vvodname22.grid(column=3, row=2)

    name3 = StringVar()
    name3.set("имя 3")
    vvodname33 = Entry(winvvod, relief=RAISED, width=15, borderwidth=2, textvariable=name3)
    vvodname33.grid(column=4, row=2)

    name4 = StringVar()
    name4.set("имя 4")
    vvodname44 = Entry(winvvod, relief=RAISED, width=15, borderwidth=2, textvariable=name4)
    vvodname44.grid(column=5, row=2)

    vvodbank1 = Label(winvvod, text="| банк 1 игрока |")
    vvodbank1.grid(column=2, row=3)
    vvodbank2 = Label(winvvod, text="| банк 2 игрока |")
    vvodbank2.grid(column=3, row=3)
    vvodbank3 = Label(winvvod, text="| банк 3 игрока |")
    vvodbank3.grid(column=4, row=3)
    vvodbank4 = Label(winvvod, text="| банк 4 игрока |")
    vvodbank4.grid(column=5, row=3)

    bank1 = StringVar()
    bank1.set("1")
    vvodbank11 = Entry(winvvod, relief=RAISED, width=15, borderwidth=2, textvariable=bank1)
    vvodbank11.grid(column=2, row=4)

    bank2 = StringVar()
    bank2.set("2")
    vvodbank22 = Entry(winvvod, relief=RAISED, width=15, borderwidth=2, textvariable=bank2)
    vvodbank22.grid(column=3, row=4)

    bank3 = StringVar()
    bank3.set("3")
    vvodbank33 = Entry(winvvod, relief=RAISED, width=15, borderwidth=2, textvariable=bank3)
    vvodbank33.grid(column=4, row=4)

    bank4 = StringVar()
    bank4.set("рп 4")
    vvodbank44 = Entry(winvvod, relief=RAISED, width=15, borderwidth=2, textvariable=bank4)
    vvodbank44.grid(column=5, row=4)

    sohr = Button(winvvod, text="сохранить", command=predprovvod(bank1.get(), bank2.get(), bank3.get(), bank4.get(), name1.get(), name2.get(),name3.get(), name4.get()))
    sohr.grid(column=3, row=6)
    print("proverka =", prov)
    prov= provvvod(bank1.get(), bank2.get(), bank3.get(), bank4.get(), name1.get(), name2.get(),name3.get(), name4.get())
    soohr=StringVar()
    soohr.set(" ")

    if prov==1:
        print("proverka =", prov)
        soohr.set("данные добавлены")
    sohrtext=Label(winvvod, text=soohr.get())
    sohrtext.grid(column=1,row=1)
    zakr=Button(winvvod,text="закрыть",command=lambda:winvvod.destroy())
    zakr.grid(column=4,row=6)

    winvvod.mainloop()









# Press the green button in the gutter to run the script.
vvoddannih()
