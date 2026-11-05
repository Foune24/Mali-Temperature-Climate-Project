import xarray as xr
import matplotlib.pyplot as plt
import numpy as np

files = {
    "ACCESS": "ACCESS_TGn_annual.nc",
    "MPI": "MPI_TGn_annual.nc",
    "Ensemble": "Ensemble_TGn_annual.nc"
}

plt.figure(figsize=(12, 6))

for name, file in files.items():
    ds = xr.open_dataset(file)
    values = ds["tas"].values.flatten()
    years = np.arange(1960, 2015)

    plt.plot(years, values, label=name)

plt.xlabel("Year")
plt.ylabel("Temperature (°C)")
plt.title("Historical TGn Comparison – Mali (1960–2014)")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()

plt.savefig("TGn_Comparison_1960_2014.png", dpi=300)
plt.show()
