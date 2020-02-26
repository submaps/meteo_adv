import matplotlib.pyplot as plt
import xarray as xr
import cartopy.crs as ccrs


def get_data(ifile_path, pq):
    ds = xr.open_dataset(ifile_path)
    return ds


def plot_map(ds, pq='t2m', timestep=0, ofile_path='test_plot.png'):
    air = ds[pq]
    ax = plt.axes(projection=ccrs.Orthographic(0, 35))
    air.isel(time=timestep).plot.contourf(ax=ax, transform=ccrs.PlateCarree())
    ax.set_global()
    ax.coastlines()
    plt.show()
    plt.savefig(ofile_path)


if __name__ == '__main__':
    ifile_path = 'era_interim_europe_t2m_psfc_u10m_v10m_20_test.nc'
    pq = 't2m'
    ds = get_data(ifile_path, pq)
    print(ds)
    ds.t2m[0].plot()
    plt.show()
    plot_map(ds)

