import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
import random

resorces = 100000

global pops
pops = [[],[]]

global terrain
terrain = open('/home/emilyblack/bipopulational_abm/terrain.txt').read().strip().split('\n')
max_x = len(terrain[0])
max_y = len(terrain)


class Pop:
    def __init__(self,mode,data):
        if mode:
            self.hunger = 100
            self.x = max_x/2
            self.y = max_y/2
            self.type = bool(random.randint(0,5))
        else:
            self.hunger = 50
            self.x = data.x
            self.y = data.y
            self.type = data.type
        pops[self.type].append(self)
    def reproduce(self):
        Pop(0,self)
    def move(self):
        x_move = random.choice([-1,1])
        y_move = random.choice([-1,1])
        if terrain[self.y+y_move][self.x+x_move] == ' ':
            if random.randint(0,1):
                self.x += x_move
            else:
                self.y += y_move
        self.hunger -= 10
        if self.hunger < 0:
            self.hunger = 0
    def eat(self,resorces):
        if self.type:
            if resorces > 100-self.hunger:
                resorces -= 100-self.hunger
                self.hunger = 100
            else:
                self.hunger += resorces
                resorces = 0
        else:
            if pops[1] and 100-self.hunger and not random.randint(0,8):
                resorces = pops[1][random.randint(0,len(pops[1])-1)].die(resorces)
                self.hunger = 100
        return resorces
    def die(self,resorces):
        resorces += self.hunger
        del pops[self.type][pops[self.type].index(self)]
        return resorces
    def tick(self,resorces):
        if self.hunger < 80:
            resorces = self.eat(resorces)
        if self.hunger > 50 and random.randint(-4,0) < 0:
            self.move()
            resorces += 10
        self.hunger -= random.randint(0,8)
        if self.hunger <= 0:
            resorces = self.die(resorces)
        if self.hunger == 100 and random.randint(0,3) == 0:
            for i in range(random.randint(0,3)):
                self.reproduce()
        return resorces

for i in range(int(raw_input('Initial pop count: '))):
    Pop(1,[])

data = [[],[],[]]

for i in range(int(raw_input('Simulation time: '))):
    j = 0
    while j < len(pops[1]):
        resorces = pops[1][j].tick(resorces)
        j += 1
    j = 0
    while j < len(pops[0]):
        resorces = pops[0][j].tick(resorces)
        j += 1
    resorces += (len(pops[0])+len(pops[1]))*100
    data[0].append(len(pops[0]))
    data[1].append(len(pops[1]))
    data[2].append(resorces)


plt.clf()
fig, ax1 = plt.subplots()

ax1.plot(data[0])
ax1.plot(data[1])

ax2 = ax1.twinx()

ax2.plot(data[2])

fig.tight_layout()
plt.savefig('/home/emilyblack/bipopulational_abm/pop_graph.png')

frequency = [[],[]]
for h in [0,1]:
    for i in range(len(terrain)):
        frequency[h].append([])
        for j in range(len(terrain[i])):
            if terrain[i][j] == ' ':
                frequency[h][i].append(0)
            else:
                frequency[h][i].append(-1)


m_f = 0
for i in pops:
    for j in i:
        frequency[j.type][j.y][j.x] += 1
        m_f = max([m_f,frequency[j.type][j.y][j.x]])

plt.clf()
viridis = cm.get_cmap('Reds', 256)
viridis = viridis(np.linspace(0, 1, 256))
black = np.array([0/256, 0/256, 0/256, 1])
viridis[:(m_f+1)/256.0,:] = black
viridis = ListedColormap(viridis)

def plot_examples(cms):
    data = [np.array(frequency[0]),np.array(frequency[1])]
    fig , axs = plt.subplots(1, 2, figsize=(12, 6))
    for [ax, dat] in zip(axs, data):
        psm = ax.pcolormesh(dat, cmap=cms, rasterized=True, vmin=-1, vmax=m_f)
        fig.colorbar(psm, ax=ax)
    plt.savefig('/home/emilyblack/bipopulational_abm/colormap.png')

plot_examples(viridis)