import xarray as xr
import cartopy.crs as ccrs
import matplotlib.pyplot as plt


air = xr.tutorial.open_dataset('air_temperature').air
ax = plt.axes(projection=ccrs.Orthographic(-80, 35))
air.isel(time=0).plot.contourf(ax=ax, transform=ccrs.PlateCarree())
ax.set_global()
ax.coastlines()
plt.show()
