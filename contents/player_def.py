from tkinter import *
import time
from contents.keeper import *
class Player_def:
   def __init__(self,canvas,team,num,ball):
      self.canvas=canvas
      self.ball=ball
      self.num=num
      self.team=team
      self.canvas_height=self.canvas.winfo_height()
      self.canvas_width=self.canvas.winfo_width()
      self.c=0
      self.c2=0
      self.c_turn=0
      self.offence=1
      self.b_hold=0
      self.movestart=False
      self.current_image=0
      self.next_image=0
      self.current_image1=2
      self.next_image1=2
     
      self.last_time=time.time()

      self.images_t=[
         PhotoImage(file="gif/t_player1.gif"),
         PhotoImage(file="gif/t_player2.gif"),
         PhotoImage(file="gif/t_player3.gif"),
         PhotoImage(file="gif/t_player4.gif")
      ]
      self.images_f=[
         PhotoImage(file="gif/f_player1.gif"),
         PhotoImage(file="gif/f_player2.gif"),
         PhotoImage(file="gif/f_player3.gif"),
         PhotoImage(file="gif/f_player4.gif")
      ]
      
      if team==True:
         #color='blue'
         each_image=self.images_t[0]
         x=300
         if num==self.b_hold:
            self.x=0
            self.y=0
         else:
            self.x=0
            self.y=0
            self.movestart=True
      else:
         each_image=self.images_f[0]
         x=1130
         self_y=[6,-6]
         self.y=self_y[num]
         #color='red'
         self.x=0
      starts_y=[200,600]
      self.image=canvas.create_image(x,starts_y[num],\
                                     image=each_image,anchor='nw')
      pos_p=self.coords()
      
   def coords(self):
         xy=self.canvas.coords(self.image)
         pos_p=[]
         pos_p.append(xy[0])
         pos_p.append(xy[1])
         pos_p.append(xy[0]+100)
         pos_p.append(xy[1]+111)
         return pos_p

   def judge_hit(self,pos):   #当たり判定
         pos_b=self.canvas.coords(self.ball.id)
         if pos_b[2]>=pos[0] and pos_b[0]<=pos[2]:
            if pos_b[3]>=pos[1] and pos_b[3] <= pos[3]:
               return True
         return False

   def calc_move_x(self,pos):
      self.expect_x=(pos[0]+pos[2])/2+self.x*(self.c_turn-10)
      return self.expect_x

   def calc_move_y(self,pos):
      self.expect_y=(pos[1]+pos[3])/2+self.y*(self.c_turn-10)
      return self.expect_y
   
   def move_ball_x(self,pos):
      pos_b=self.canvas.coords(self.ball.id)
      self.ball.x=(self.calc_move_x(pos)-((pos_b[0]+pos_b[2])/2))/(self.c_turn-10)
      return self.ball.x

   def move_ball_y(self,pos):
      pos_b=self.canvas.coords(self.ball.id)
      self.ball.y=(self.calc_move_y(pos)-((pos_b[1]+pos_b[3])/2))/(self.c_turn-10)
      return self.ball.y

   def move_ball_xd(self):
      self.ball.x=self.x
      return self.ball.x

   def move_ball_yd(self):
      self.ball.y=self.y
      return self.ball.y
      
   def shoot_ball_x(self,team):
      pos_b=self.canvas.coords(self.ball.id)
      if team:
         self.ball.x=(1475-(pos_b[0]+pos_b[2])/2)/10
      else:
         self.ball.x=(25-(pos_b[0]+pos_b[2])/2)/10
      return self.ball.x

   def shoot_ball_y(self):
      pos_b=self.canvas.coords(self.ball.id)
      self.ball.y=(450-(pos_b[1]+pos_b[3])/2)/10
      return self.ball.y

   def keeper_ball_x(self,pos,team):
      if not team:
         self.ball.x=((pos[0]+pos[2])/2-1475)/10
      else:
         self.ball.x=((pos[0]+pos[2])/2-25)/10
      return self.ball.x

   def keeper_ball_y(self,pos):
      self.ball.y=((pos[1]+pos[3])/2-450)/10+self.y
      return self.ball.y

   def def_y(self,pos_p,sx):
      if pos_p[1]>sx:
         self.y=-(abs((pos_p[1]+pos_p[3])/2-sx)/100)
      else:
         self.y=abs((pos_p[1]+pos_p[3])/2-sx)/100

   def bounce(self,pos):
      if pos[1]<=0:
            self.y=6
      if pos[3]>=self.canvas_height: 
            self.y=-6
      if pos[0]<=0:
         self.x=6
      if pos[2]>=self.canvas_width:
         self.x=-6

   def animate(self,team,con):
         if time.time()-self.last_time>0.1:
            self.last_time=time.time()
            self.current_image=self.next_image
            if self.current_image==0:
               self.next_image=1
            elif self.current_image==1:
               self.next_image=0


            if team==True:
               if con==True:
                  self.canvas.itemconfig(self.image,\
                                         image=self.images_t[self.next_image])
               else:
                  self.current_image1=self.next_image1
                  if self.current_image1==2:
                     self.next_image1=3
                  elif self.current_image1==3:
                     self.next_image1=2
                  self.canvas.itemconfig(self.image,\
                                         image=self.images_t[self.next_image1])
               
            else:
               if con==True:
                   self.canvas.itemconfig(self.image,\
                                      image=self.images_f[self.next_image])
               else:
                  self.current_image1=self.next_image1
                  if self.current_image1==2:
                     self.next_image1=3
                  elif self.current_image1==3:
                     self.next_image1=2
                  self.canvas.itemconfig(self.image,\
                                         image=self.images_f[self.next_image1])




