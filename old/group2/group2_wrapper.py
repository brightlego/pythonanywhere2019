 def wrapper():
#calculate the observed stats
    obs_stats = analysis()

    gen1= generated(obs_stats)
#perturb statistics
    perturbstats = obs_stats*np.array([1,0.75,2,1])
    gen2= generated(perturbstats)

#count flood
    number_floods1 = floodevents(gen1)
    number_floods2 = floodevents(gen2)


    comp_stat=comp(gen1,gen2)
