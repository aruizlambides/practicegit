import numpy as np
import pandas as pd

def get_kinematics(q, y):
	dq = q - q.shift()
	dy = y - y.shift()
	d2q = dq - dq.shift()
	d2y = dy - dy.shift()

	speed = np.sqrt(dq**2 + dy**2)
	acceleration = np.sqrt(d2q**2 + d2y**2)

	return speed, acceleration

def remove_outliers(data, m):
	d = np.abs(data - np.nanmedian(data))
    mdev = np.nanmedian(d)
    s = d/mdev if mdev else 0.
    
    return np.where(s < m)