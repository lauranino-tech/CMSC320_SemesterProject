import xarray as xr
import cfgrib

if __name__ == '__main__':
    
    datasets = cfgrib.open_datasets('era5_subset.grib')
    ds = xr.merge(datasets, compat='override', combine_attrs='drop')

    df = ds.to_dataframe()
    df.to_csv('era5_dataset.csv')