from math import cos, sin, atan, pi

def d_r(angle):
    return (angle/360.0)*2*pi
def r_d(angle):
    return (angle/(2*pi))*360.0

def fire(speed,angle):
    def tick(proj_position,proj_momentum,a,tps):
        proj_position[0] += (proj_momentum[0]/tps)
        proj_position[1] += (proj_momentum[1]/tps)
        proj_momentum[1] += a/tps
        return(proj_position,proj_momentum)
    a = -9.81
    proj_position = [0.0,0.0]
    proj_momentum = [cos(d_r(angle))*speed,sin(d_r(angle))*speed]
    tps = 1000
    (proj_position,proj_momentum) = tick(proj_position,proj_momentum,a,tps)
    while proj_position[1] > 0:
        (proj_position,proj_momentum) = tick(proj_position,proj_momentum,a,tps)
        print proj_position
    return(proj_position[0])

def calculate_angle(force,distance,preference):
    angle = [45.0/2,45.0/2+45][preference]
    a_distance = fire(speed,angle)
    step = 2
    while round(a_distance,3) != round(distance,3) and round(45.0/(2**step),100):
        angle += (45.0/(2**step))*[1,-1][(a_distance > distance)^preference]
        a_distance = fire(force,angle)
        step += 1
    return(angle)


print('All angles in degrees.')
print('All co-ordinates in the form: x y.')

loc_from = raw_input('What co-ordinates do you want to fire from? ').split()
loc_to = raw_input('What co-ordinates do you want to fire to? ').split()
speed = float(raw_input('What speed does your cannon fire at? '))
preference = int(raw_input('Would you prefer low [0] or high [1] firing? '))

loc_to = [float(loc_to[0]),float(loc_to[1])]
loc_from = [float(loc_from[0]),float(loc_from[1])]

loc_dif = [loc_to[0]-loc_from[0],loc_to[1]-loc_from[1]]

distance = (loc_dif[0]**2 + loc_dif[1]**2)**0.5

if fire(speed,45) < distance:
    print('Speed to slow for projectile to ever reach target.')
else:
    v_angle = calculate_angle(speed,distance,preference)
    h_angle = r_d(atan(loc_dif[1]/loc_dif[0]))
    print 'Fire at an angle of',round(v_angle,3),'at a bearing of',round(h_angle,3)