import numpy as np
import matplotlib.pyplot as plt
import csv
n_joints = 7
n_waypoints = 60
with open("stomp_ros/files/duration.txt") as f:
    duration = f.read().split()
with open("stomp_ros/files/traj.txt") as f:
    traj = f.read().split()
n_waypoints = len(duration)
trajectories = np.zeros((n_waypoints,n_joints))
n_total = len(traj)
i = 0
w = 0
for n in range(n_total):
    if i==n_joints:
        i=0
    if w==n_waypoints:
        w=0
    trajectories[w,i] = traj[n]
    i+=1
    w+=1
for iter,d in enumerate(duration):
    for j in range(trajectories.shape[1]):
        plt.bar(d, trajectories[iter,j])
    plt.xlabel('time')
    plt.ylabel('trajs')
plt.show()
