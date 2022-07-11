import numpy as np
import matplotlib.pyplot as plt
import csv
n_waypoints = 30
n_rollouts = 5
n_iters = 5
with open("stomp_ros/files/experiment_cost.txt") as f:
    data = f.read().split()
n = 0
cost_dict = {}
print("data length:",len(data))
iter_n = 0
while(n<len(data)):
    
    costs = np.zeros([n_rollouts,n_waypoints])
    for i in range(costs.shape[0]):
        for j in range(costs.shape[1]):
            costs[i,j] = data[n]
            n+=1
    cost_dict['Iter'+str(iter_n)] = costs
    iter_n +=1
    print("n value: ",n,"iter n value:",iter_n)
waypoints = [i for i in range(0,n_waypoints)]
costs = cost_dict['Iter4']
print("shape of costs:",costs.shape)
for i in range(costs.shape[0]):
    plt.plot(waypoints, costs[i,:], label='Rollout '+str(i))
    plt.xlabel('waypoints', fontsize = 30)
    plt.ylabel('End eff cost',fontsize = 30)
plt.title('End eff Cost vs Waypoint', fontsize = 50)
plt.legend()
plt.show()