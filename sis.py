from vector import Vector
import matplotlib.pyplot as plt
import math
import numpy as np

G = 6.67E-11
c = 3E8

'''
def diff_deflection(field_vector, mass, mass_vector):
    difference_vector = field_vector - mass_vector

    numerator = -2*G*mass
    denominator = (abs(difference_vector.magnitude())**3)


    displacement_vect = difference_vector*numerator*(1/denominator)

    return displacement_vect
'''

def diff_deflection(field_vector, mass, mass_vector):
    G = 6.67E-11
    c = 3E8


    radius_enclosed = field_vector.magnitude()

    velocity_dispersion = 9000000
    mass_enclosed = 2*(velocity_dispersion**2)*radius_enclosed/G

    numerator = -2*G*mass_enclosed
    denominator = (abs(field_vector.magnitude())**3)


    displacement_vect = field_vector*numerator*(1/denominator)

    return displacement_vect


def get_density_field():
    velocity_dispersion = 9000000
    G = 6.67E-11
    c = 3E8

    array = []
    for x in range(int(-3E9), int(3E9), int(1E8)):
        column = []
        for y in range(int(-3E9), int(3E9), int(1E8)):
            radius = math.sqrt(x**2 + y**2)
            if radius > int(0.2E9):
                rho = (velocity_dispersion**2)/(2*math.pi*G*radius**2)
                column.append(rho)
            else:
                column.append(0)
        
        array.append(column)

    return array








def calculate_deflection(initial_distance,light_position,number,mass,mass_vectors):
    G = 6.67E-11
    c = 3E8

    light_velocity = [Vector(0,0,c) for i in range(len(light_position))]
    light_history = [[i.duplicate()] for i in light_position]


    for i in range(int(number)):
        for index in range(len(light_position)):
            for mass_vector in mass_vectors:
                light_velocity[index] += diff_deflection(light_position[index], mass[0], mass_vector)*step_time
                light_velocity[index] = light_velocity[index].unit()*c

            light_history[index].append(light_position[index].duplicate())


        # update light z positions
        for i in range(len(light_position)):
            light_position[i] += light_velocity[i]*step_time



    x_pos=[]
    y_pos=[]
    z_pos=[]
    for i in light_history:
        temp_x=[]
        temp_y=[]
        temp_z=[]
        for y in i:
            temp_x.append(y.x)
            temp_y.append(y.y)
            temp_z.append(y.z)
        
        x_pos.append(temp_x)
        y_pos.append(temp_y)
        z_pos.append(temp_z)

    return x_pos, y_pos, z_pos



















mass = [5E33]
mass_vectors = [Vector(0,0,0)]
iterate = 1E5


number = 5000
initial_distance = -10E21
step_spatial = (abs(initial_distance)/number)*2
step_time = step_spatial/c



'''
light_position = [Vector(x,y,initial_distance) for x,y in zip(range(int(0.7E9),int(0.7E10),int(1E9)), range(int(0.7E9),int(0.7E10),int(1E9)))]

light_position = []
for x in range(int(-0.7E10),int(0.7E10),int(2.5E8)):
    for y in range(int(-0.7E10),int(0.7E10),int(2.5E8)):
        if x**2 + y**2 > 5E8:
            light_position.append(Vector(x,y,initial_distance))
'''

x_raw=[]
y_raw=[]
radius = 1E20
light_position = []

for i in np.linspace(0,2*math.pi,200):
    x_raw.append(math.cos(i)*radius + 0.2E21)
    y_raw.append(-math.sin(i)*radius + 0.2E21)

for i in range(len(x_raw)):
    light_position.append(Vector(x_raw[i],y_raw[i],initial_distance))




x_pos, y_pos, z_pos = calculate_deflection(initial_distance, light_position, number, mass, mass_vectors)





galaxy = get_density_field()




for i in range(len(x_pos)):
    plt.scatter(x_pos[i][0],y_pos[i][0], color='blue', s=10)
    plt.scatter(x_pos[i][-1],y_pos[i][-1], color='red', s=10)
    
ax = plt.gca()
ax.set_aspect('equal', adjustable='box')
plt.xlim(-8E20,8E20)
plt.ylim(-8E20,8E20)


#plt.contourf(galaxy)


plt.show()
