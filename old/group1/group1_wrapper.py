import numpy as np
import matplotlib.pyplot as plt

def wrapper():
    print 'weathergen.py version ',version, '\n'

    #Setting the threshold and 2 sets of perturbations
    threshold = 20
    perturbations_mean = np.array([[1,0.75,1,1],[1,0.75,1.5,1],[1,0.75,2,1],[1,0.75,2.5,1],[1,0.75,3,1],[1,0.75,10,1]])
    perturbations_sd = np.array([[1.075,1,1],[1,0.75,1,1.5],[1,0.75,1,2],[1,0.75,1,2.5],[1,0.75,1,3],[1,0.75,1,10]])

    output_mean = np.array([0.0])
    output_sd = np.array([0.0])

    #Control simulation
    control = np.array([1,1,1,1])
    floodrisk_control = perturb_stats(control,threshold)
    print 'Control floodrisk: ',floodrisk_control, '\n'

    #Looping over perturbations
    dims = np.shape(perturbations_mean)
    for i in np.arange(0,dims[0]):
        tmp = perturb_stats(perturbations_mean[i,],threshold)
        print '...gives this floodrisk for perturbations of the means: ', tmp/floodrisk_control, '\n'
        output_mean = np.append(output_mean,tmp)

    dims = np.shape(perturbations_sd)
    for i in arange(0,dims[0]):
        tmp = perturb_stats(perturbations_mean[i,],threshold)
        print '...gives this floodrisk for perturbations of the mean: ',tmp/floodrisk_control, '\n'
        output_sd = np.append(output_sd,tmp)

    #scaling by the control flood risk
    floodrisks_mean = output_mean[1:dims[0]+1]/floodrisk_control
    floodrisks_sd = output_sd[1:dims[0]+1]/floodrisk_control

    #plotting
    fig,ax = plt.subplots()
    plt.plot(perturbations_mean[:,2],floodrisks_mean,colRed)
    plt.plot(perturbations_sd[:,3],floodrisks_sd,colBlue)
    plt.xlabel('Perturbations')
    plt.ylabel('Flood risk')
    ax.text(6, 0.8, '   -floodrisks_sd',
        verticalalignment='bottom', horizontalalignment='left',
        color=colBlue, fontsize=15)
    ax.text(6, 0.9, '   -floodrisks_mean',
        verticalalignment='bottom', horizontalalignment='left',
        color=colRed, fontsize=15)
    fig.savefig("floodrisk_vs_perturbed_mean.png")
    plt.close(fig)
