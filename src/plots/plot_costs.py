import numpy as np
import matplotlib.pyplot as plt
import csv
n_waypoints = 60
with open("stomp_ros/files/mat_cost1.txt") as f:
    data = f.read().split()
print("size of data:",len(data))
n_iterations = len(data)/n_waypoints
iters = np.zeros((n_iterations,n_waypoints))
waypoints = [i for i in range(0,n_waypoints)]
n = 0
for i in range(iters.shape[0]):
    for j in range(iters.shape[1]):
        iters[i,j] = data[n]
        n+=1
for i in range(iters.shape[0]):
    plt.plot(waypoints, iters[i,:], label='Iter '+str(i))
    plt.xlabel('waypoints', fontsize = 30)
    plt.ylabel('Collision cost',fontsize = 30)
plt.title('Collision Cost vs Waypoint', fontsize = 50)
plt.legend()
plt.show()