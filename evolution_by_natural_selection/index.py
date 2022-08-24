import numpy as np
import matplotlib.pyplot as plt

class Thing:
    def __init__(self, g_variation,h_base=0.0,t_base=0.0):
        self.h_resistance = np.random.normal(h_base,g_variation,1)[0]
        self.t_resistance = np.random.normal(t_base,g_variation,1)[0]
    def reproduce(self, g_variation,things):
        things.append(Thing(g_variation,self.h_resistance,self.t_resistance))
        return things
    def kill(self,humidity,temperature,things):
        if (abs(humidity-self.h_resistance)/humidity)*np.random.random() > np.random.random()*0.01:
            things[things.index(self)] = None
        elif (abs(temperature-self.t_resistance)/temperature)*np.random.random() > np.random.random()*0.01:
            things[things.index(self)] = None
g_variation = float(raw_input("Genetic Variation: "))
humidity = float(raw_input("Humidity (%): "))
temperature = float(raw_input("Temperature (C): "))
count = int(raw_input("Count: "))
thing_count = [count]
things = []
for i in range(count):
    things.append(Thing(g_variation))
for i in range(1000):
    for i in things:
        things = things[i].kill(humitity,temperature,things)
        if things[i]:
            things = things[i].reproduce(g_variation,things)
    temp = []
    for i in things:
        if i != None:
            temp.append(i)
    things = temp[:]
