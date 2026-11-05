import xarray as xr
import matplotlib.pyplot as plt

files = {
    "ACCESS-CM2": "ACCESS_Mali_annual.nc",
    "MPI-ESM1-2-HR": "MPI_Mali_annual.nc",
    "Ensemble Mean": "Ensemble_Mali_annual.nc"
}

plt.figure(figsize=(12, 6))

for name, filename in files.items():
    ds = xr.open_dataset(filename)
    values = ds["tas"].values.flatten()
    years = ds["time"].dt.year.values

    plt.plot(years, values, label=name)

plt.title("Historical Annual Mean Temperature (1960–2014)")
plt.xlabel("Year")
plt.ylabel("Temperature (°C)")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("Historical_Temperature_Comparison.png", dpi=300)
plt.show()
