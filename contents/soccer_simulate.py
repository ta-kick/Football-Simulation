from tkinter import*
import random
import time
from contents.ball import *
from contents.player_def import *

class Player(Player_def):
   catchball=movestartOK=intersept=switch=f_change=returning=False
   shooting=keeper_p=dribble=False
   offence=True
   d=e=intersept_num=0
   c_list=[20,25,30,]
   def __init__(self,canvas,team,num,ball):
      self.canvas=canvas
      self.team=team
      self.num=num
      self.ball=ball
      self.player=Player_def(self.canvas,self.team,self.num,self.ball)
      self.canvas_height=self.canvas.winfo_height()
      self.canvas_width=self.canvas.winfo_width()
      self.last_time=time.time()
      self.offence=1
      self.c1=self.cd=0
      self.shoot_num=-1

   def do_switch(self,pos):
      Player.f_change=Player.returning=Player.intersept=True
      self.player.c=self.player.x=self.player.y=0
      Player.switch=True
      self.ball.x=self.ball.y=0
      if not Player.keeper_p:
         Player.intersept_num=self.player.num
      if Player.intersept:
         Player.offence=not(Player.offence)

   def set_switch(self):
      if Player.switch==True:
         Player.d+=1
         self.player.c=0
         if self.player.team!=Player.offence:
            self.player.movestart=False
         else:
            if self.player.num!=Player.intersept_num and not Player.keeper_p:
               self.player.movestart=True
         if Player.d==4:
            Player.switch=False
            Player.d=0

   def def_anime(self):
      if self.team==True:  
         self.canvas.itemconfig(self.player.image,\
                                image=self.player.images_t[0])
      else:
         self.canvas.itemconfig(self.player.image,\
                                image=self.player.images_f[0])
         
   def pre_def(self,pos):
      if self.cd==99 and not Player.intersept:
         self.cd=self.player.x=0
         self.def_anime()
         self.player.y=6
         
      if self.player.team!=Player.offence and Player.intersept:
         self.player.animate(self.player.team,False)
         self.cd+=1
         if self.cd==1:
            if self.player.team:
               if self.player.num==0:
                  self.player.x=-((abs(pos[0]-300))/100)
                  self.player.def_y(pos,200)
               elif self.player.num==1:
                  self.player.x=-((abs(pos[0]-300))/100)
                  self.player.def_y(pos,600)
            elif not self.player.team:
               if self.player.num==0:
                  self.player.x=(1130-pos[0])/100
                  self.player.def_y(pos,200)
               elif self.player.num==1:
                  self.player.x=(1130-pos[0])/100
                  self.player.def_y(pos,600)
                  
         if self.cd==100:
            Player.returning=False
            self.cd=self.player.x=0
            self.def_anime()
            if self.player.num==0:
               self.player.y=6
            if self.player.num==1:
               self.player.y=-6
               Player.intersept=False
               
   def shoot(self):
      self.c1+=1
      if self.c1==1:
         self.player.shoot_ball_x(self.player.team)
         self.player.shoot_ball_y()
      if self.c1==10:
         self.c1=0
         self.ball.x=self.ball.y=0
         self.shoot_num=-1
         Player.shooting=False
         Player.keeper_p=True

   def shoot_judge(self,pos):
      if (pos[0]+pos[2]<650 and not self.player.team)\
         or (pos[0]+pos[2]>2300 and self.player.team):
         Player.shooting=True
         self.shoot_num=self.player.num
         return True
      return False
      
   def shoot_run(self,pos_b,pos_p):
      if not Player.keeper_p:
         self.shoot()

   def kpass_run(self,pos):
      if Player.keeper_p:
         self.keeper_pass(pos)

   def keeper_pass(self,pos):
      if self.player.num==0:
         self.c1+=1
         if self.c1==15:
            self.player.keeper_ball_x(pos,self.player.team)
            self.player.keeper_ball_y(pos)
         if self.c1==25: 
            self.c1=self.ball.x=self.ball.y=0
            Player.keeper_p=False
            Player.e=1
      else:
         if not self.player.movestart:
            self.player.movestart=True

   def draw(self): 
      self.player.canvas.move(self.player.image,self.player.x,self.player.y)
      pos_p=self.player.coords()
      pos_b=self.player.canvas.coords(self.player.ball.id)
      
      self.player.bounce(pos_p)

      if self.player.team==Player.offence and Player.movestartOK:
         if not Player.shooting:
            self.shoot_judge(pos_b)
         if Player.shooting and self.shoot_num==self.player.num:
            self.shoot_run(pos_b,pos_p)
           
      if Player.keeper_p:
         if not Player.returning:
            self.do_switch(pos_p)
         self.set_switch()
         self.pre_def(pos_p)
         if self.player.team==Player.offence:
            self.kpass_run(pos_p)

      if not Player.shooting and not Player.keeper_p:
         if self.player.judge_hit(pos_p) and \
            self.player.team!=Player.offence and not Player.returning:
            self.do_switch(pos_p)
         self.set_switch()
         self.pre_def(pos_p)
         if Player.movestartOK and self.player.team==Player.offence:
            if Player.e==0:
               self.player.movestart=True
               Player.movestartOK=False
            else:
               Player.e=0
               Player.movestartOK=True

         if self.player.team==Player.offence:
            if not self.player.movestart:
               self.player.animate(self.player.team,True)
               if not Player.dribble:
                  if self.player.team==True:
                     self.player.x=random.randint(2,8)
                  else:
                     self.player.x=-random.randint(2,8)
                  self.player.y=random.randint(-5,5)
                  self.player.move_ball_xd()
                  self.player.move_ball_yd()
                  Player.dribble=True
            else:
               self.player.animate(self.player.team,True)
               self.player.c+=1
               if self.player.c==1:
                  random.shuffle(Player.c_list)
                  self.player.c_turn=Player.c_list[0]
                  if self.player.team==True:
                     self.player.x=random.randint(0,7)
                  else:
                     self.player.x=-random.randint(0,7)
                  
                  self.player.y=random.randint(-4,4)
               if self.player.c==10:
                  self.player.move_ball_x(pos_p)
                  self.player.move_ball_y(pos_p)
                  
               if self.player.c==self.player.c_turn:
                  self.player.c=0
                  self.ball.x=self.ball.y=self.player.x=self.player.y=0
                  self.player.movestart=False
                  Player.catchball=True
                  Player.dribble=False
                     
            if Player.catchball==True and self.player.c==0:
               Player.movestartOK=True
               Player.catchball=False
               


