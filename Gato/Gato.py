import numpy as np

_ = np.array([1,2,3,4,5,6,7,8,9])

i = 0
while i < 9:
	print("[",_[i],"]","[",_[i+1],"]",[i+2])
	i = i + 2
