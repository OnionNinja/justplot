# justplot
A thin wrapper around matplotlib, which lets you save figure and axes settings for plot reuse.

## How to install the module
`pip` with `--pre` as option cause this is still an alpha build.
```
python3.4 -m pip install justplot --pre
```
-- or --
```
git clone https://github.com/OnionNinja/justplot
cd justplot
python3.4 setup.py install
```

## How to use the module ~~(as intended)~~

#### TL;DR
```python
from justplot import justplot as jp
import numpy

lat = np.asarray([-90,-60,-30,0,30,60,90])
lon = np.asarray([-180,-150,-120,-90,-60,-30,0,30,60,90,120,150,180])
lat,lon = np.meshgrid(lat, lon)
temp = np.random.randint(10,35,(13,7))
wind = np.random.randint(100,300,(13,7))

awesome = jp.JustPlot(
    title = "Where is it hot?",
    xlabel = "Latitude",
    ylabel = "Longitude",
    # add more options here
)
awesome.add_contourf(lat,lon,temp,ylabel="Temperature (K)", colorbar=True)
awesome.save("Sun.pdf","pdf")

windy = awesome.copy()
windy(title="A little bit windy don't ya think?")
windy.add_contour(lat,lon,wind,ylabel="Wind")
windy.save("Wind.pdf","pdf")
```
#### Usage
Let's say we have some data we want to plot (suprise!). As an example I will use
a small data set from [ucar](https://www.unidata.ucar.edu/software/netcdf/examples/sresa1b_ncar_ccsm3-example.nc).
First off we have to load the data:
```python
import xarray

data = xarray.open_dataset('sresa1b_ncar_ccsm3-example.nc', decode_times=False) #pretty cryptic, I know
lat = data.lat.data
lon = data.lon.data
temp = data.tas.data[0,:,:]
wind = data.ua.data
xlat,xlon = np.meshgrid(lat,lon)
```
Now we will create a plot which we will be reusing for other plots:
```python
from justplot import justplot as jp

blueprint = jp.JustPlot(
    title = "Where is it hot?",
    xlabel = "Latitude",
    ylabel = "Longitude",
    # add more options here
)
```
Now we can actually build the plot:
```python
blueprint.add_contourf(xlat,xlon,temp,label="Temperature [K]")
```



## How to improve the module (aka **our** todo list)

- [ ] Save settings from y axes
- [ ] Restructure
- [ ] Write import function from preconfigured or used figures/axes
- [x] Write README.md
