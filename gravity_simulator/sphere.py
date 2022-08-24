from math import sin,cos,tan,asin,acos,atan

import numpy as np

def angle_to_3D(angle,r):
    y = sin(np.deg2rad(angle[1]))*r
    mini_r = cos(np.deg2rad(angle[1]))*r
    z = sin(np.deg2rad(angle[0]))*mini_r
    x = cos(np.deg2rad(angle[0]))*mini_r
    return [round(x,10),round(y,10),round(z,10)]

def tick(proj,v,m,tps):
    G = 6.67408e-11
    d = (proj[0]**2+proj[1]**2)**0.5
    a = (G*m)/d**2
    angle = acos(proj[1]/d)
    a = [cos(angle)*a,sin(angle)*a]
    v[0] += a[0]/tps
    v[1] += a[1]/tps
    proj[0] += v[0]/tps
    proj[1] += v[1]/tps
    return proj

def launch(m,r,start_coordinate,end_coordinate,v,angle,mode):
    v = n
    tps = 1000
    max_t = 1000*tps
    ticks = 1
    proj = start_coordinate[:]
    proj = tick(proj,v,m,tps)
    while proj[0]**2+proj[1]**2 >= r**2 and ticks < max_t:
        proj = tick(proj,v,m,tps)
        ticks += 1
    if ticks < max_t:
        return 0
    elif atan(proj[1]/proj[0]) > end_coordinate:

start_coordinate = raw_input('Start co-ordinate: ').split(' ')
end_coordinate = raw_input('End co-ordinate: ').split(' ')
v = int(raw_input('Initial speed: '))
r = int(raw_input('Sphere radius: '))
m = int(raw_input('Sphere mass: '))

start_coordinate = angle_to_3D(start_coordinate,r)
