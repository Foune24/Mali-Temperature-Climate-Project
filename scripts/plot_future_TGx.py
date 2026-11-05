
import xarray as xr
import numpy as np
import matplotlib.pyplot as plt

years = np.arange(2015, 2051)

models = ["ACCESS", "MPI", "Ensemble"]
scenarios = ["ssp126", "ssp245", "ssp585"]

plt.figure(figsize=(14, 7))

for ssp in scenarios:
    for model in models:

        filename = f"{model}_{ssp}_TGx_annual.nc"

        ds = xr.open_dataset(filename)
        values = ds["tas"].values.flatten()
        ds.close()

        if len(values) != 36:
            raise ValueError(f"Incorrect number of values: {filename}")

        plt.plot(
            years, values,
            marker=".",
            linewidth=1.5,
            label=f"{model} - {ssp.upper()}"
        )

plt.title("Future Annual Maximum Temperature (TGx) over Mali (2015–2050)")
plt.xlabel("Year")
plt.ylabel("TGx (°C)")
plt.grid(True, linestyle="--", alpha=0.5)
plt.legend(ncol=3, fontsize=8)
plt.tight_layout()

plt.savefig("Future_TGx_Comparison_2015_2050.png", dpi=300)
plt.show()
