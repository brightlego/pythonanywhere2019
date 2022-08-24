import random
import matplotlib.pyplot as plt

def init_sim(particle_count):
    rand = random.SystemRandom()
    particles = []
    output = []
    _50_50 = [50]
    for i in range(particle_count):
        particles.append([-1,1][rand.randint(0,1)])
    output.append((particles.count(1)/float(particle_count)*100))
    flag = True
    while flag:
        particles = run_sim(particles)
        output.append((particles.count(1)/float(particle_count)*100))
        _50_50.append(50)
        flag = output[len(output)-1]%100
    plt.clf()
    plt.plot(output)
    #plt.plot(_50_50)
    plt.ylabel('Percentage Matter (%)')
    plt.xlabel('Time (Generation)')
    plt.yticks(range(0,101,10))
    plt.grid(b=None, which='both', axis='y')
    plt.grid(b=None, which='minor', axis='y')
    plt.ylim(top=100,bottom=0)
    plt.axhline(50,color = 'red')
    plt.savefig("/home/emilyblack/matter_or_antimatter_time.png")
    return len(output),[-1,1][bool(output[len(output)-1])]
def run_sim(particles):
    rand = random.SystemRandom()
    count = {-1:0,1:0}
    for i in particles:
        count[i] += 1
    count = min(count.values())
    remaining = {-1:count,1:count}
    for i in range(len(particles)):
        if remaining[particles[i]]:
            remaining[particles[i]] -= 1
            particles[i] = [-1,1][rand.randint(0,1)]
        elif not(remaining[-1] or remaining[1]):
            break
    return(particles)

