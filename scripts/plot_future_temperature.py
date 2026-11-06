
import xarray as xr
import numpy as np
import matplotlib.pyplot as plt

# Study period
years = np.arange(2015, 2051)

# Future climate scenarios
scenarios = ["ssp126", "ssp245", "ssp585"]

# Only the ensemble mean
model = "Ensemble"

# Scenario colours and styles
colors = {
    "ssp126": "blue",
    "ssp245": "orange",
    "ssp585": "green"
}

plt.figure(figsize=(12, 6))

# Plot the three ensemble scenario curves
for ssp in scenarios:

    filename = f"{model}_{ssp}_Mali_annual.nc"

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

# Graph formatting
plt.title(
    "Future Annual Mean Temperature over Mali (2015–2050)",
    fontsize=14,
    fontweight="bold"
)

plt.xlabel("Year", fontsize=11)
plt.ylabel("Temperature (°C)", fontsize=11)

plt.xticks(np.arange(2015, 2051, 5))

plt.grid(
    True,
    linestyle="--",
    alpha=0.3
)

plt.legend(
    title="Climate Scenarios",
    fontsize=10
)

plt.tight_layout()

# Save the figure
plt.savefig(
    "Future_Temperature_Comparison_2015_2050.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
