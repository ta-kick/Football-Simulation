from tkinter import *
from contents.soccer_simulate import *
from contents.keeper import *

tk=Tk()
tk.title("Game")
tk.resizable(0,0)
tk.wm_attributes("-topmost",1)

canvas=Canvas(tk,width=1500,height=900,bd=0,highlightthickness=0)
canvas.pack()
tk.update()
bg=PhotoImage(file="gif/background.gif")
canvas.create_image(0,0,image=bg,anchor='nw')
canvas.create_line(750,0,750,900)
canvas.create_oval(650,350,850,550)
canvas.create_rectangle(0,350,25,550)
canvas.create_rectangle(1475,350,1500,550)
ball=Ball(canvas,'black')

players=[ [] ]

for i in range(2):
   players[0].append(Player(canvas,True,i,ball))
j=[]
for i in range(2):
   j.append(Player(canvas,False,i,ball))
players.append(j)

k=[]
k.append(Keeper(canvas,True))
k.append(Keeper(canvas,False))
text=Text()

while True:
   ball.draw()
   for i in range(2):
      k[i].draw()
   for i in range(2):
      for j in range(2):
         players[i][j].draw()
   tk.update_idletasks()
   tk.update()
   time.sleep(0.03)
