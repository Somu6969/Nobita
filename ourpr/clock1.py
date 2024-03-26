import time
x=input("What is your name?")
print("hello ma ki chut",x)
recenttime=time.strftime("%H:%M:%S")
Recenttime=int(time.strftime('%H'))
if (4<=Recenttime<9):
  print ("hello motherfucker its morning")
elif (14<=Recenttime<17):
  print("hello motherfucker its afternoon")
elif (17<=Recenttime<19):
  print("hello motherfucker its evening")
elif (19<=Recenttime<24):
  print("hello motherfucker its night")
