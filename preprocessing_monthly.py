import numpy as np
from netCDF4 import Dataset

# ERA5 monthly averaged data on single levels from 1979 to present 

years = np.array(range(1979,2023))
grid_step = 0.25

#lat, lon, name = 25.473034, 81.878357, 'Prayagraj'
#lat, lon, name = 28.644800, 77.216721, 'Dehli'
#lat, lon, name = 44.494887, 11.342616, 'Bologna'
#lat, lon, name = 48.864716, 2.349014, 'Paris'
#lat, lon, name = 51.454265, -0.978130, 'Reading'
#lat, lon, name = 40.730610, -73.935242, 'NY'
#lat, lon, name = -33.865143, 151.209900, 'Sydney'
#lat, lon, name = 55.751244, 37.618423, 'Moscow'
#lat, lon, name = -23.533773, -46.625290, 'SaoPaulo'
#lat, lon, name = 37.78, -122.30, 'SanFransisco', 
#lat, lon, name = -1.53, 22.84, 'DRC'
#lat, lon, name = 71.88, 106.34, 'Unknown'
#lat, lon, name = 70.58, -41.48, 'Greenland'
lat, lon, name = 40.33, 116.35, 'Beijing'
data_file = '/home/lam/Téléchargements/data/monthly_Global_april_1979_2022.nc'

# April 2022 -> data has not been validated
# When we request data from years before 2022 with data that has not been validated yet like April 2022,
# it adds a dimension called "expver" of size 2
# We have to keep v1 for years before 2022 else v2
nc = Dataset(data_file, 'r')

temp = nc['t2m'][:]

# Keep v1 for years before 2022 else v2
temp = np.concatenate([nc['t2m'][:len(years)-1,0,:,:], nc['t2m'][-1:,1,:,:]])
temp = temp-273.15 # kelvin to degree

# Get indices of the closest cell from given lat/lon
lat = round(lat/grid_step)*grid_step
lon = round(lon%360/grid_step)*grid_step
print(name, lat, lon)
ilat = np.where(nc['latitude'][:]==lat)[0].item()
ilon = np.where(nc['longitude'][:]==lon)[0].item()

# Save data in csv format with header
np.savetxt(f'/home/lam/Téléchargements/preprocessed_data/monthly_average_{name}_april.csv', temp[:,ilat,ilon], header='temp', comments='')
