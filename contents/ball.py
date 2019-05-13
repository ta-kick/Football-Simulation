from tkinter import*
class Ball:
   def __init__(self,canvas,color):
      self.canvas=canvas
      self.color=color
      self.id=canvas.create_oval(10,10,25,25,fill=color)
      self.canvas.move(self.id,340,240)
      self.x=0
      self.y=0
      self.canvas_height=self.canvas.winfo_height()
      self.canvas_width=self.canvas.winfo_width()

   def draw(self):
      self.canvas.move(self.id,self.x,self.y)
      pos=self.canvas.coords(self.id)
      if pos[1]<=0:
         self.y=6
      if pos[3]>=self.canvas_height:
         self.y=-6
      if pos[0]<=0:
         self.x=6
      if pos[2]>=self.canvas_width:
         self.x=-6
