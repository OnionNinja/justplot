#!/usr/bin/python
# -*- encoding: utf-8 -*-

import xarray
import numpy as np
from justplot import justplot as jp
from matplotlib.ticker import AutoMinorLocator


data = xarray.open_dataset('sresa1b_ncar_ccsm3-example.nc', decode_times=False) #pretty cryptic, I know
lat = data.lat.data
lon = data.lon.data
temp = data.tas.data[0,:,:]
wind = data.ua.data[0,4,:,:]
xlat,xlon = np.meshgrid(lon,lat)

blueprint = jp.JustPlot(
    title = "Where is it hot?",
    ylabel = "Latitude",
    xlabel = "Longitude",
    # add more options here
)

blueprint.add_contourf(xlat,xlon,temp,label="Temperature")
blueprint.save('blueprint-1.png','png')

blueprint(title={"label":"World Temperature","fontsize":19},
          xticks=np.arange(0,361,30),
          yticks=np.arange(-90,91,30),
          xminor=AutoMinorLocator(3),
          yminor=AutoMinorLocator(3),
)
blueprint.save("blueprint-2.png",'png')

windy = blueprint.copy()
windy(title={"label":"Wind","fontsize":19})
windy.add_contour(xlat,xlon,wind,label="Wind")
windy.save("windy.png","png")

both = windy.copy()
both(title={"label":"World Temperature + Wind","fontsize":19})
both.add_contourf(xlat,xlon,temp,label="Temperature")
both.add_contour(xlat,xlon,wind,label="Wind",colors=('k'))
blueprint.save("both.png","png")
