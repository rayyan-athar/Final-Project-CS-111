# Final Project
# CS 111, Reckinger
# Rinor Dana, Rayyan Athar, DATE, CS 111, Fall 2022
# World Cup Predictor    

import turtle
global notStarted
global country1
country1 = False

def start(x, y):
  global notStarted
  notStarted = False 

def choose(x, y):
  global country1
  if x > 0:
    if y > 0:
      global B
      global c2        
      B = False
      list.append(c2)
    else:
      global D 
      global c4     
      D = False
      list.append(c4)
  else:
    if y > 0:
      global A
      global c1      
      A = False
      list.append(c1)    
    else:
      global C
      global c3      
      C = False
      list.append(c3)
  country1 = False

def chooseA(x,y):
  global country1
  if x > 0:
    if y > 0:
        global c2        
        list.append(c2)
        country1 = False
    else:
        global c4     
        list.append(c4)
        country1 = False
  else:
    if y < 0:
        global c3      
        list.append(c3)
        country1 = False
      
def chooseB(x,y):
  global country1
  if x > 0:
    if y < 0:
        global c4     
        list.append(c4)
        country1 = False
  else:
    if y > 0:
        global c1      
        list.append(c1)    
        country1 = False
    else:
        global c3      
        list.append(c3)
        country1 = False
      
def chooseC(x,y):
  global country1
  if x > 0:
    if y > 0:
        global c2        
        list.append(c2)
        country1 = False
    else:
        global c4     
        list.append(c4)
        country1 = False
  else:
    if y > 0:
        global c1      
        list.append(c1)    
        country1 = False
      
def chooseD(x,y):
  global country1
  if x > 0:
    if y > 0:
        global c2        
        list.append(c2)
        country1 = False
  else:
    if y > 0:
        global c1      
        list.append(c1)    
        country1 = False
    else:
        global c3      
        list.append(c3)
        country1 = False
      
def choose2(x, y):
  global country1
  if x > 0:
    global c2
    list.append(c2)
  else:    
    global c1
    list.append(c1)
  country1 = False
  
def group(t1,t2,t3,t4):
  global c1
  global c2
  global c3
  global c4
  
  c1 = t1
  c2 = t2
  c3 = t3
  c4 = t4
  
  A1 = turtle.Turtle()
  turtle.addshape(t1)
  A1.shape(t1)
  A1.penup()
  A1.goto(-150, 100)
  t.goto(-150,150)
  t.write(t1[:-4], move = False, align = "center", font = ("Roboto", 20, "bold",))  
  
  A2 = turtle.Turtle()
  turtle.addshape(t2)
  A2.shape(t2)
  A2.penup()
  A2.goto(200, 100)
  t.goto(200,150)
  t.write(t2[:-4], move = False, align = "center", font = ("Roboto", 20, "bold",)) 
  
  A3 = turtle.Turtle()
  turtle.addshape(t3)
  A3.shape(t3)
  A3.penup()
  A3.goto(-150, -100)
  t.goto(-150,-50)
  t.write(t3[:-4], move = False, align = "center", font = ("Roboto", 20, "bold",)) 

  A4 = turtle.Turtle()
  turtle.addshape(t4)
  A4.shape(t4)
  A4.penup()
  A4.goto(200, -100) 
  t.goto(200,-50)
  t.write(t4[:-4], move = False, align = "center", font = ("Roboto", 20, "bold",))

  global A
  global B
  global C
  global D
  A=True
  B=True
  C=True
  D=True
  
  global country1
  country1 = True
  while country1:
    A1.onclick(choose)
    A2.onclick(choose)
    A3.onclick(choose)
    A4.onclick(choose)

  if A == False:
    country1 = True
    while country1:
      A1.onclick(chooseA)
  elif B == False:
    country1 = True
    while country1:
      A2.onclick(chooseB)
  elif C == False:
    country1 = True
    while country1:
      A3.onclick(chooseC)
  elif D == False:
    country1 = True
    while country1:
      A4.onclick(chooseD)    
  
def knockout(k1,k2):
  global c1
  global c2
  c1 = k1
  c2 = k2
  
  A1 = turtle.Turtle()
  turtle.addshape(k1)
  A1.shape(k1)
  A1.penup()
  A1.goto(-150, 0)
  t.goto(-150,50)
  t.write(k1[:-4], move = False, align = "center", font = ("Roboto", 20, "bold",))  
  
  A2 = turtle.Turtle()
  turtle.addshape(k2)
  A2.shape(k2)
  A2.penup()
  A2.goto(200, 0)
  t.goto(200,50)
  t.write(k2[:-4], move = False, align = "center", font = ("Roboto", 20, "bold",))

  global country1
  country1 = True
  while country1:
    A1.onclick(choose2)
    A2.onclick(choose2)
  
if __name__ == "__main__":
  t = turtle.getturtle()
  s = turtle.Screen()
  s.bgcolor("#9C1E63")
  t.hideturtle()
  t.penup()
  t.color("black")
  t.goto(0,100)
  t.write("World Cup Predictor Game", move = False, align = "center", font = ("TimesNewRoman", 35, "bold","italic"))
  
  button = turtle.Turtle()
  turtle.addshape("start.gif")
  button.shape("start.gif")
  button.penup()
  button.goto(0, -100)
  
  s.listen()
  
  notStarted = True
  while notStarted:
    button.onclick(start)
  
  list = []
  global i

  file = open('Countries.txt')
  countries = file.readlines()
  file.close()
  teams = [] 
  for i in range(len(countries)): 
    word = countries[i]      
    word = word.strip() 
    teams.append(word)


  for i in range(0,len(teams),4):
    t1 = teams[i]
    t2 = teams[i+1]
    t3 = teams[i+2]
    t4 = teams[i+3]
    s.clearscreen()
    s.bgcolor("#7028BD")
    t.goto(0,190)
    if i == 0:
      Group = "Group A"
    elif i == 4:
      Group = "Group B"
    elif i == 8:
      Group = "Group C"
    elif i == 12:
      Group = "Group D"
    elif i == 16:
      Group = "Group E"
    elif i == 20:
      Group = "Group F"
    elif i == 24:
      Group = "Group G"
    elif i == 28:
      Group = "Group H"
    t.write(Group , move = False, align = "center", font = ("TimesNewRoman", 30))
    group(t1,t2,t3,t4)

  new_list = []
  new_list = list[:]
  list.clear()  

  for i in range(0,len(new_list),4):
    k1 = new_list[i]
    k4 = new_list[i+3]
    s.clearscreen()
    s.bgcolor("#E66229")
    t.goto(0,190)
    t.write("Round of 16", move = False, align = "center", font = ("TimesNewRoman", 35))
    knockout(k1,k4)

  for i in range(0,len(new_list),4):
    k2 = new_list[i+1]
    k3 = new_list[i+2]
    s.clearscreen()
    s.bgcolor("#E66229")
    t.goto(0,190)
    t.write("Round of 16", move = False, align = "center", font = ("TimesNewRoman", 35))
    knockout(k2,k3)

  new_list.clear()
  new_list = list[:]
  list.clear()  

  for i in range(0,len(new_list),2):
    k1 = new_list[i]
    k2 = new_list[i+1]
    s.clearscreen()
    s.bgcolor("#4B8CD6")
    t.goto(0,190)
    t.write("Quater-finals", move = False, align = "center", font = ("TimesNewRoman", 35))
    knockout(k1,k2)  

  new_list.clear()
  new_list = list[:]
  list.clear()  

  for i in range(0,len(new_list),2):
    k1 = new_list[i]
    k2 = new_list[i+1]
    s.clearscreen()
    s.bgcolor("#53B871")
    t.goto(0,190)
    t.write("Semi-finals", move = False, align = "center", font = ("TimesNewRoman", 35))
    knockout(k1,k2)   

  new_list.clear()
  new_list = list[:]
  list.clear()  

  for i in range(0,len(new_list),2):
    k1 = new_list[i]
    k2 = new_list[i+1]
    s.clearscreen()
    s.bgcolor("#F52F9F")
    t.goto(0,190)
    t.write("Finals", move = False, align = "center", font = ("TimesNewRoman", 35))
    knockout(k1,k2)  

  winner = list[0]
  s.clearscreen()
  s.bgcolor("#BF063D")
  t.goto(0,200)
  t.write("Your Predicted Winner!", move = False, align = "center", font = ("TimesNewRoman", 40))
  t.goto(0,50)
  t.write(winner[:-4], move = False, align = "center", font = ("Roboto", 40, "bold"))
  w = turtle.Turtle()
  turtle.addshape(winner)
  w.shape(winner)
  w.penup()
  w.goto(0,0)  
  turtle.mainloop() 