from tkinter import*
class Keeper:
   def __init__(self,canvas,team):
      self.canvas=canvas
      self.team=team
      self.x=0
      self.y=0

      if team==True:
         self.e_image=PhotoImage(file="gif/t_player5.gif")
         self.image=canvas.create_image(-25,400,image=self.e_image\
                                        ,anchor='nw')
      else:
         self.e_image=PhotoImage(file="gif/f_player5.gif")
         self.image=canvas.create_image(1450,400,image=self.e_image\
                                        ,anchor='nw')

   def draw(self):
      self.canvas.move(self.image,self.x,self.y)

      

      

      
      
      
