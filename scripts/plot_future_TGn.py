import xarray as xr
import numpy as np
import matplotlib.pyplot as plt

years = np.arange(2015, 2051)

scenarios = ["ssp126", "ssp245", "ssp585"]
model = "Ensemble"

colors = {
    "ssp126": "blue",
    "ssp245": "orange",
    "ssp585": "green"
}

plt.figure(figsize=(12, 6))

for ssp in scenarios:

    filename = f"{model}_{ssp}_TGn_annual.nc"

    ds = xr.open_dataset(filename)
    values = ds["tas"].values.flatten()
    ds.close()

    if len(values) != len(years):
        raise ValueError(f"Incorrect number of values in {filename}")

    plt.plot(
        years,
        values,
        color=colors[ssp],
        marker="o",
        markersize=3,
        linewidth=2,
        label=ssp.upper()
    )

plt.title(
    "Future Annual Minimum of Daily Mean Temperature (TGn) over Mali (2015–2050)",
    fontsize=13,
    fontweight="bold"
)

plt.xlabel("Year")
plt.ylabel("Temperature (°C)")

plt.xticks(np.arange(2015, 2051, 5))

plt.grid(True, linestyle="--", alpha=0.3)
plt.legend(title="Climate Scenarios")

plt.tight_layout()

plt.savefig(
    "Future_TGn_Comparison_2015_2050.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
