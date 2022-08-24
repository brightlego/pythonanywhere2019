import numpy as np
for i in xrange(0,100):
    execfile('O_and_X.py')
print 'small priority:', np.load('small_priority_o.npy'), 'medium priority:', np.load('medium_priority_o.npy'),'high priority:',np.load('high_priority_o.npy'),'blocker priority:',np.load('blocker.npy')