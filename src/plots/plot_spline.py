import numpy as np
import matplotlib.pyplot as plt
import csv
from scipy.interpolate import interp1d
n_joints = 7
n_waypoints = 30
with open("stomp_ros/files/duration.txt") as f:
    duration = f.read().split()
with open("stomp_ros/files/traj.txt") as f:
    traj = f.read().split()
n_waypoints = len(duration)
trajectories = np.zeros((n_waypoints,n_joints))
n_total = len(traj)
i = 0
w = 0
n=0
for i in range(n_waypoints):
    for j in range(n_joints):
        trajectories[i,j] = traj[n]
        n+=1
end_eff = np.zeros((trajectories.shape[0]))
for r in range(trajectories.shape[0]):
    end_eff[r] = trajectories[r,6]
print("end eff shape: ",end_eff)

for iter, d in enumerate(duration):
    plt.scatter(d, end_eff[iter])
    plt.xlabel('Time',fontsize = 30)
    plt.ylabel('End effector values', fontsize = 30)
    plt.rcParams.update({'font.size': 1000})
plt.title('Joint values vs Duration', fontsize = 50)
plt.show()
