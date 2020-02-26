from ecmwfapi import ECMWFDataServer

ofile_path = 'era_interim_europe_t2m_psfc_u10m_v10m.nc'
server = ECMWFDataServer()

server.retrieve({
    "class": "ei",
    "dataset": "interim",
    "date": "2019-01-01/to/2019-02-31",
    "expver": "1",
    "area": "73.5/-27/33/45",  # lat lon box
    "grid": "0.125/0.125",  # resolution
    "levtype": "sfc",
    "param": "34.128/134.128/165.128/166.128/167.128",  # variables
    "step": "0",
    "stream": "oper",
    "time": "00:00:00/06:00:00/12:00:00/18:00:00",
    "type": "an",
    "format": "netcdf",
    "target": ofile_path,
})
