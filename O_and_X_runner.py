import numpy as np

for i in range(1,100):
    execfile('O_and_X_AI.py')
print 'Small priority:', np.load('small_priority_o.npy')
print 'Medium priority:', np.load('medium_priority_o.npy')
print 'High priority:', np.load('high_priority_o.npy')
print 'Blocked priority:', np.load('blocked.npy')