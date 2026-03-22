# Converts a .grib file into a .csv file.
#
# Note that GRIB is a format used for gridded weather data, it is highly condensed, 
# meaning that the resulting CSV with be several times larger than the original file.

import xarray as xr
import cfgrib

if __name__ == '__main__':
    
    datasets = cfgrib.open_datasets('era5_subset.grib')
    ds = xr.merge(datasets, compat='override', combine_attrs='drop')

    # converting to DataFrame object risks memory overload due to limited RAM capacity for some computers
    df = ds.to_dataframe()
    df.to_csv('era5_dataset.csv')