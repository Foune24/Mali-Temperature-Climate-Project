import xarray as xr
import pandas as pd

indicators = {
    "Mean temperature": "Mali",
    "TGx": "TGx",
    "TGn": "TGn"
}

models = ["ACCESS", "MPI", "Ensemble"]
scenarios = ["ssp126", "ssp245", "ssp585"]

def get_mean(filename):
    with xr.open_dataset(filename) as ds:
        values = ds["tas"].values.squeeze()
        return float(values.mean())

results = []

for indicator, suffix in indicators.items():

    for model in models:

        historical_file = f"{model}_{suffix}_annual.nc"
        historical_mean = get_mean(historical_file)

        for scenario in scenarios:

            future_file = f"{model}_{scenario}_{suffix}_annual.nc"
            future_mean = get_mean(future_file)

            change = future_mean - historical_mean

            results.append({
                "Indicator": indicator,
                "Model": model,
                "Scenario": scenario.upper(),
                "Historical_mean_C": historical_mean,
                "Future_mean_C": future_mean,
                "Absolute_change_C": change
            })

            print(
                f"{indicator} | {model} | {scenario.upper()} | "
                f"Historical: {historical_mean:.2f} °C | "
                f"Future: {future_mean:.2f} °C | "
                f"Change: {change:+.2f} °C"
            )

df = pd.DataFrame(results)
df.to_csv("Absolute_Temperature_Changes_2015_2050.csv", index=False)

print("\nCalculation completed successfully.")
print("CSV file created successfully.")
