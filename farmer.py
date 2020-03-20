import numpy as np

Farmer=([[1,0]])
Goose=([[1,0]])
Grain=([[0,1,0]])
Fox=([[0,1,0]])
Goal=([1,0,0])

River=([[0,1]])

print(Farmer)
print(Goose)
print(Grain)
print(Fox)

print(River)

if(Farmer<Goose):
       print(Goose)
else:
  print(Farmer )
if(River<Farmer):
      print(Farmer)
else:
    print(River)

if(Goal==0):
    print(River)
else:
    print(Goal)
if(Goose<Farmer):
    print(Farmer)
else:
    print(Goose)
if(Grain>Goose):
    print(Grain)
else:
    print(Goose)
if(Fox>Goose):
    print(Fox)
else:
    print(Goose)

