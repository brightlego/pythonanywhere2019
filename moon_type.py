from time import time

moons = [
  r"    ..--..    ",
  r"  .` oo  .`.  ",
  r" .o~.    O ). ",
  r" .c`_..() ||. ",
  r"  `..o....'/  ",
  r"    `'--''    ",
]
#day = int(time()/(24*60*60))
#moontype = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
day = input()
week4 = day%28
moons_ = []
for i in range(0,len(moons)):
    moons_.append(list(moons[i]))
