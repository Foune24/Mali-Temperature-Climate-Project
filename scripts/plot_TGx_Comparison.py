import xarray as xr
import matplotlib.pyplot as plt
import numpy as np

files = {
    "ACCESS": "ACCESS_TGx_annual.nc",
    "MPI": "MPI_TGx_annual.nc",
    "Ensemble": "Ensemble_TGx_annual.nc"
}

plt.figure(figsize=(12, 6))

for name, file in files.items():
    ds = xr.open_dataset(file)
    variable = "tas"
    values = ds[variable].values.flatten()
    years = np.arange(1960, 2015)

    plt.plot(years, values, label=name)

plt.xlabel("Year")
plt.ylabel("Temperature (°C)")
plt.title("Historical TGx Comparison – Mali (1960–2014)")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()

plt.savefig("TGx_Comparison_1960_2014.png", dpi=300)
plt.show()
