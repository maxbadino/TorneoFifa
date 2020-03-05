from tkinter import *

root= Tk()
root.geometry("420x550")

####################################################################


#######################################################################

Partido1 = StringVar()
Partido2 = StringVar()
Partido3 = StringVar()
Partido4 = StringVar()
Partido5 = StringVar()
Partido6 = StringVar()

sel1=IntVar()
sel2=IntVar()
sel3=IntVar()
sel4=IntVar()
sel5=IntVar()
sel6=IntVar()
sel7=IntVar()
sel8=IntVar()
sel9=IntVar()
sel10=IntVar()
sel11=IntVar()
sel12=IntVar()
sel13=IntVar()

imagen=PhotoImage(file="fifa21.gif")
fondo1=Label (root,image=imagen).place(x=110,y=20)

etiqueta = Label(text = "Torneo Los Pibes")
etiqueta.place(x=80,y=120)
etiqueta.config(font=("Helvetica",25))

etiqueta = Label(text = "-->Seleccionar Jugadores:")
etiqueta.place(x=110,y=165)
etiqueta.config(font=("Helvetica",12))

chek1=Checkbutton(root,text="Matias Coletti",variable=sel1, onvalue=1, offvalue=0).place(x=20,y=190)
chek2=Checkbutton(root,text="Leandro Coletti",variable=sel2, onvalue=1, offvalue=0).place(x=145,y=190)
chek3=Checkbutton(root,text="Luciano Coletti",variable=sel3, onvalue=1, offvalue=0).place(x=270,y=190)
chek4=Checkbutton(root,text="Max Badino",variable=sel4, onvalue=1, offvalue=0).place(x=20,y=210)
chek5=Checkbutton(root,text="Demian Badino",variable=sel5, onvalue=1, offvalue=0).place(x=145,y=210)
chek6=Checkbutton(root,text="Leandro Brorglia",variable=sel6, onvalue=1, offvalue=0).place(x=270,y=210)
chek7=Checkbutton(root,text="Javier Hashem",variable=sel7, onvalue=1, offvalue=0).place(x=20,y=230)
chek8=Checkbutton(root,text="Ezequiel Polito",variable=sel8, onvalue=1, offvalue=0).place(x=145,y=230)
chek9=Checkbutton(root,text="Sebastian Insua",variable=sel9, onvalue=1, offvalue=0).place(x=270,y=230)
chek10=Checkbutton(root,text="Maxi Bravo",variable=sel10, onvalue=1, offvalue=0).place(x=20,y=250)
chek11=Checkbutton(root,text="Mariano Erdocia",variable=sel11, onvalue=1, offvalue=0).place(x=145,y=250)
chek12=Checkbutton(root,text="Gaston Curbelo",variable=sel12, onvalue=1, offvalue=0).place(x=270,y=250)
#chek13=Checkbutton(root,text="Cristian Wells",variable=sel13, onvalue=1, offvalue=0).place(x=20,y=190)

Button(root, text="MEZCLAR JUGADORES").place(x=130,y=285)

Label(root, text="Partido 1").place(x=60,y=320)
Entry(root, justify="center", textvariable=Partido1).place(x=20,y=340)

Label(root, text="Partido 2").place(x=60,y=370)
Entry(root, justify="center", textvariable=Partido2).place(x=20,y=390)

Label(root, text="Partido 3").place(x=60,y=420)
Entry(root, justify="center", textvariable=Partido3).place(x=20,y=440)

Label(root, text="Partido 4").place(x=300,y=320)
Entry(root, justify="center", textvariable=Partido4).place(x=250,y=340)

Label(root, text="Partido 5").place(x=300,y=370)
Entry(root, justify="center", textvariable=Partido5).place(x=250,y=390)

Label(root, text="Partido 6").place(x=300,y=420)
Entry(root, justify="center", textvariable=Partido6).place(x=250,y=440)

Button(root, text="A DORMIR!").place(x=160,y=480)

root.mainloop()