import random
#random.seed(1)  # Setting random number generator seed for repeatability

NUM_DRONES = 10000
AIRSPACE_SIZE = 128000  # Meters.
CONFLICT_RADIUS = 500  # Meters.

def count_conflicts(drones, conflict_radius): # Worst case O(n^2) Best case O(n log n) 
    drones.sort() #O(n log n)
    count = 0
    for i in range(0,len(drones)): #O(n^2)
        min_drone = drones[i]
        for j in range(i+1,len(drones)):
            curr_drone = drones[j]
            if abs(min_drone[0] - curr_drone[0]) < conflict_radius:
                if abs(min_drone[1] - curr_drone[1]) < conflict_radius:
                    count += 1
            else:
                break
    return count

def count_conflicts_quad(drones, conflict_radius):
    holder = []
    count = 0
    for i in range(0,len(drones)):
        for j in range(0,len(drones)):
            if i == j:
                continue
            d_a = drones[i]
            d_b = drones[j]
            d = (d_a[1] - d_b[1])/(d_a[0]-d_b[0])
            if d < conflict_radius:
                r = (d_a,d_b)
                if (d_b,d_a) not in holder:
                    count += 1
                    holder.append(r)
    #print drones
    #print holder
    return count
                

def gen_coord():
    return int(random.random() * AIRSPACE_SIZE)

positions = [[gen_coord(), gen_coord()] for i in range(NUM_DRONES)]
conflicts =  0 #count_conflicts_quad(positions, CONFLICT_RADIUS)
conflicts_2 = count_conflicts(positions, CONFLICT_RADIUS)
print "Drones in conflict: {0} {1}".format(conflicts,conflicts_2)