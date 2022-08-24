import random

max_x = 40
max_y = 40

seed = hash(raw_input("Seed: "))
#block_chr = unichr(9608)
#free_chr = unichr(32)
block_chr = 'X'
free_chr = ' '
if not seed:
    seed = random.random()
random.seed(seed)
def gen_terrain():
    terrain = [list(block_chr*max_x)]
    for i in range(1,max_y-1):
        terrain.append([block_chr])
        for j in range(1,max_x-1):
            terrain_score = int(terrain[i][j-1] == block_chr) + int(terrain[i-1][j] == block_chr)
            if terrain_score == 0 and random.random() < 0.999:
                terrain[i].append(free_chr)
            elif terrain_score == 1 and random.random() < 0.6:
                terrain[i].append(free_chr)
            elif (terrain_score == 2 and random.random() < 0.1):
                terrain[i].append(free_chr)
            elif (i > max_y/3 and i < 2*max_y/3 and j > max_x/3 and j < 2*max_x/3):
                terrain[i].append(free_chr)
            else:
                terrain[i].append(block_chr)
        terrain[i].append(block_chr)
    terrain.append(list(block_chr*max_x))
    return(terrain)

terrains = [gen_terrain(),gen_terrain()]

terrains[1].reverse()
for i in range(len(terrains[1])):
    terrains[1][i].reverse()
print(len(terrains[0]))

terrain = []
for i in range(max_y):
    terrain.append([])
    for j in range(max_x):
        if terrains[0][i][j] == block_chr or terrains[1][i][j] == block_chr:
            terrain[i].append(block_chr)
            #print(block_chr)
        else:
            terrain[i].append(free_chr)
    #print i,j

for i in range(len(terrain)):
    terrain[i] = ''.join(terrain[i])
terrain = '\n'.join(terrain)

f = open('/home/emilyblack/bipopulational_abm/terrain.txt','w')
f.write(terrain)
f.close()
