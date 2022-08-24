

import matplotlib.pyplot as plt
from netCDF4 import Dataset
import numpy as np

if __name__ in '__main__':

    filename = '/home/emilyblack/session_4_claire/l4_sst_indianocean.nc'
    data = Dataset(filename,'r')

    print data.description
    print data.dimensions
    print data.variables

    #Students should look at the information from the print statements above
    # to find out what is in the file.

    #They can then do:
    # sst = data.variables['sea_water_temperature']
    # print sst
    #
    # This method is described in the lecture to find the dimensions of the
    # array so if possible let them try this out rather than
    # telling them the dimensions.

    lat = data.variables['latitude'][:]
    lon = data.variables['longitude'][:]
    sst = data.variables['sea_water_temperature'][:,:]
    uncert = data.variables['sea_water_temperature_uncertainty'][:,:]

    data.close()

    sst_eq = sst[800,:]
    sst_tropic = sst[1200,:]


    fig = plt.figure()
    plt.plot(lon,sst_eq,label='Equator')
    plt.plot(lon,sst_tropic,'--',label='Tropics')
    plt.xlabel('Longitude / degrees')
    plt.ylabel('Sea Water Temperature / K')
    plt.legend(loc=4)
    fig.savefig("myplot1.png")

    fig_two = plt.figure()
    plt.imshow(np.flipud(sst))
    plt.title('Sea Water Temperature')
    plt.colorbar()
    plt.show()
    fig_two.savefig("myplot2.png")

    fig_three = plt.figure()
    plt.title('Sea Water Temperature')
    plt.imshow(np.flipud(sst),cmap='bwr')
    plt.colorbar()
    fig_three.savefig("myplot3.png")

    sst = sst-273.15

    # Student's aren't asked to plot their SST map in Celsius in the exercises
    # but its good to get them in the habit of checking what their code is
    # doing.

    fig_four = plt.figure()
    plt.title('Sea Water Temperature')
    plt.imshow(np.flipud(sst),cmap='bwr')
    plt.colorbar()
    fig_four.savefig("myplot4.png")


    outfile = 'modified_l4_sst.nc'
    rootgrp = Dataset(outfile,mode='w')

    # You can encourage students to add more global metadata
    rootgrp.description = 'Modified asea water temperature file from session 4 practical'

    dim_a = sst.shape[0]
    dim_b = sst.shape[1]

    rootgrp.createDimension('lat',dim_a)
    rootgrp.createDimension('lon',dim_b)
    varDims1 = ('lat','lon')

    # Students should try writing out multiple arrays into their file
    # (using this method) - include lat, lon and uncertainty

    var1 = rootgrp.createVariable('sst','f',varDims1)
    var1.units = 'Celsius'
    var1.long_name = 'Sea Water Temperature'
    var1[:,:] = sst

    rootgrp.close()


    # Extension exercise

    from mpl_toolkits.basemap import Basemap

    fig_five = plt.figure()
    m = Basemap(projection='cea')
    x,y = m(*np.meshgrid(lon,lat))
    m.imshow(sst)
    plt.title('Sea Water Temperature')
    fig_five.savefig("myplot5.png")





