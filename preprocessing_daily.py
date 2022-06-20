import numpy as np
from netCDF4 import Dataset

# ERA5 hourly data on single levels from 1979 to present

years = np.array(range(1979,2023))
nb_hours = 24
grid_step = 0.25

#lat, lon, name = 25.473034, 81.878357, 'Prayagraj'
#lat, lon, name = 28.644800, 77.216721, 'Dehli'
#data_file = '/home/lam/Téléchargements/data/India_27_april_1979_2022.nc'

#lat, lon, name = 44.494887, 11.342616, 'Bologna'
#lat, lon, name = 48.864716, 2.349014, 'Paris'
#lat, lon, name = 51.454265, -0.978130, 'Reading'
#data_file = '/home/lam/Téléchargements/data/Europe_27_april_1979_2022.nc'

lat, lon, name = 40.730610, -73.935242, 'NY'
data_file = '/home/lam/Téléchargements/data/US_27_april_1979_2022.nc'

# April 2022 -> data has not been validated
# When we request data from years before 2022 with data that has not been validated yet like April 2022,
# it adds a dimension called "expver" of size 2
# We have to keep v1 for years before 2022 else v2
nc = Dataset(data_file, 'r')

temp = nc['t2m'][:]

# Keep v1 for years before 2022 else v2
nb_years_v1 = (years<2022).sum()
temp = np.concatenate([nc['t2m'][:nb_years_v1*nb_hours,0,:,:], nc['t2m'][-nb_hours:,1,:,:]])
temp = temp-273.15 # kelvin to degree

# Get indices of the closest cell from given lat/lon
lat = round(lat/grid_step)*grid_step
lon = round(lon/grid_step)*grid_step
print(name, lat, lon)
ilat = np.where(nc['latitude'][:]==lat)[0].item()
ilon = np.where(nc['longitude'][:]==lon)[0].item()

# Compute max/mean of each year
data_max = np.zeros(len(years))
data_mean = np.zeros(len(years))
for i in range(len(years)):
    x = temp[i*nb_hours:(i+1)*nb_hours,ilat,ilon]
    data_max[i] = np.max(x)
    data_mean[i] = np.mean(x)
    
# Save data in csv format with header
np.savetxt(f'/home/lam/Téléchargements/preprocessed_data/{name}_27_april_max.csv', data_max, header='temp', comments='')
np.savetxt(f'/home/lam/Téléchargements/preprocessed_data/{name}_27_april_mean.csv', data_mean, header='temp', comments='')
