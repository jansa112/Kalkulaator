#Kodutöö nr 5
#15.04.2021
#Jaanus Paasoja ITT20
# Kalkulaator
from tkinter import *
avaldis = ""
def press(num):
    global avaldis
    avaldis = avaldis + str(num)
    muutujad.set(avaldis)
def equalpress():   
    try:
        global avaldis
        kokku = str(eval(avaldis))
        muutujad.set(kokku)
        avaldis = ""
    except: 
        muutujad.set(" Viga ")
        avaldis = ""
def clear():
    global avaldis
    avaldis = ""
    muutujad.set("")
#Aken
if __name__ == "__main__":
    aken = Tk()
    aken.configure(background="#32AB1C")
    aken.title("Kalkulaator")
    aken.geometry("340x250")
    aken.resizable(0,0)
#Sisestus
    muutujad = StringVar()
    sisestus = Entry(aken, textvariable=muutujad).grid(columnspan=4, ipadx=70)
#Nupud
    nupp1 = Button(aken, text="1", fg="#B6F522", bg="#482C8D", command=lambda: press(1), height=1, width=7).grid(row=2, column=0)
    nupp2 = Button(aken, text="2", fg="#B6F522", bg="#482C8D", command=lambda: press(2), height=1, width=7).grid(row=2, column=1)
    nupp3 = Button(aken, text="3", fg="#B6F522", bg="#482C8D", command=lambda: press(3), height=1, width=7).grid(row=2, column=2)
    nupp4 = Button(aken, text="4", fg="#B6F522", bg="#482C8D", command=lambda: press(4), height=1, width=7).grid(row=3, column=0)
    nupp5 = Button(aken, text="5", fg="#B6F522", bg="#482C8D", command=lambda: press(5), height=1, width=7).grid(row=3, column=1)
    nupp6 = Button(aken, text="6", fg="#B6F522", bg="#482C8D", command=lambda: press(6), height=1, width=7).grid(row=3, column=2)
    nupp7 = Button(aken, text="7", fg="#B6F522", bg="#482C8D", command=lambda: press(7), height=1, width=7).grid(row=4, column=0)
    nupp8 = Button(aken, text="8", fg="#B6F522", bg="#482C8D", command=lambda: press(8), height=1, width=7).grid(row=4, column=1)
    nupp9 = Button(aken, text="9", fg="#B6F522", bg="#482C8D", command=lambda: press(9), height=1, width=7).grid(row=4, column=2)
    nupp0 = Button(aken, text="0", fg="#B6F522", bg="#482C8D", command=lambda: press(0), height=1, width=7).grid(row=5, column=0)
    pluss = Button(aken, text="+", fg="#B6F522", bg="#482C8D",command=lambda: press("+"), height=1, width=7).grid(row=2, column=3)
    miinus = Button(aken, text="-", fg="#B6F522", bg="#482C8D", command=lambda: press("-"), height=1, width=7).grid(row=3, column=3)
    korruta = Button(aken, text="*", fg="#B6F522", bg="#482C8D", command=lambda: press("*"), height=1, width=7).grid(row=4, column=3)
    jaga = Button(aken, text="/", fg="#B6F522", bg="#482C8D", command=lambda: press("/"), height=1, width=7).grid(row=5, column=3)
    võrdub = Button(aken, text="=", fg="#B6F522", bg="#482C8D", command=equalpress, height=1, width=7).grid(row=5, column=2)
    koma = Button(aken, text=".", fg="#B6F522", bg="#482C8D", command=lambda: press("."), height=1, width=7).grid(row=5, column=1)
    kustuta= Button(aken, text="Kustu", fg="#B6F522", bg="#482C8D", command=clear, height=1, width=7).grid(row=6, column=0)
    ruut = Button(aken, text="Aste", fg="#B6F522", bg="#482C8D", command=lambda: press("**"), height=1, width=7).grid(row=6, column=1)
    aken.mainloop()