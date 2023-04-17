from vector import Vector
import matplotlib.pyplot as plt
import math

G = 6.67E-11
c = 3E8

def diff_deflection(field_vector, mass, mass_vector):
    difference_vector = field_vector - mass_vector

    numerator = -2*G*mass
    denominator = (abs(difference_vector.magnitude())**3)


    displacement_vect = difference_vector*numerator*(1/denominator)

    return displacement_vect






mass = [2E33]
mass_vectors = [Vector(0,0,0)]
iterate = 1E5


number = 100000
initial_distance = -150E9
step_spatial = (abs(initial_distance)/number)*2
step_time = step_spatial/c


light_position = [Vector(i,0,initial_distance) for i in range(int(0.7E9),int(0.7E10),int(1E9))]
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


print(math.atan(light_velocity[0].x/light_velocity[0].z))

for i in range(2):
    plt.plot(z_pos[i],x_pos[i])
    
plt.show()
