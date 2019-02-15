from tkinter import *

fenetre = Tk()
#side=TOP     :  haut
#side=LEFT    :  gauche
#side=BOTTOM  :  bas
#side=RIGHT   :  droite
frame0 = Frame(fenetre,
               borderwidth=5)
frame0.pack(side=TOP,
            padx=50,
            pady=50)

labelFrame0 = Label(frame0,
                    text="Je suis le texte du frame0 (Mis en TOP de la fenetre)").pack()

frame1 = Frame(fenetre,
               borderwidth=5,
               bg="limegreen")

frame1.pack(side=LEFT,
            padx=30,
            pady=30)

labelFrame1 = Label(frame1,
                    text="Je suis le texte du label appartenant au Frame1 (Mis en LEFT de la fenetre)").pack()
frame2 = LabelFrame(fenetre,
                    borderwidth=5,
                    text="je suis le frame2 de type LabelFrame",
                    bg="orange")

frame2.pack(side=RIGHT,
            padx=30,
            pady=30)

labelFrame2 = Label(frame2,
                    text="Je suis le texte du label appartenant au frame2 (Mis en RIGHT de la fenetre)").pack()

frame3 = Frame(frame2,
               bg="white")

frame3.pack(side=LEFT,
            padx=30,
            pady=30)

labelFrame3 = Label(frame3,
                    text="Texte du Frame3 (Mis en LEFT du frame2)")

labelFrame3.pack(padx=10,
                 pady=10)

frame4 = Frame(frame2,
               bg="yellow")

frame4.pack(side=RIGHT,
            padx=30,
            pady=30)

labelFrame4 = Label(frame4,
                    text="Texte du frame4 (Mis en RIGHT du frame2)")

labelFrame4.pack(padx=10,
                 pady=10)

frame5 = Frame(frame4,
               bg="cyan")

frame5.pack(side=BOTTOM,
            padx=15,
            pady=15)

labelFrame5 = Label(frame5,
                    text="Texte du frame5 (Mis en BOTTOM du frame4)")

labelFrame5.pack(padx=20,
                 pady=5)

frame6 = Frame(frame4,
               bg="brown")

frame6.pack(side=BOTTOM,
            padx=30,
            pady=30)

photo = PhotoImage(file="./media/image/oslo_petit.png")
canvas = Canvas(frame6,
                width=100,
                height=133)
canvas.create_image(0,0,anchor=NW, image=photo)
canvas.pack()