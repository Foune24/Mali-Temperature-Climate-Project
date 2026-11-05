import numpy as np
import matplotlib.pyplot as plt

# Years: 1960 to 2014
years = np.arange(1960, 2015)

# Annual TGx values from ACCESS-CM2 (°C)
tgx = [
    36.4939, 37.2098, 36.1749, 35.9955, 36.0282,
    34.9981, 35.9086, 35.8722, 37.0964, 36.9974,
    37.2157, 35.9354, 36.4506, 37.0607, 36.2348,
    36.6157, 36.6243, 36.7525, 36.9067, 37.0983,
    37.1903, 36.4452, 36.0537, 36.2290, 36.7602,
    37.1616, 38.5278, 35.7786, 36.3212, 36.9702,
    37.3532, 37.6003, 35.7307, 37.0603, 37.7104,
    36.0563, 36.5923, 37.3018, 37.5870, 37.5526,
    38.7240, 37.8703, 37.3386, 38.7926, 38.0600,
    37.5531, 37.8876, 37.1939, 37.5704, 37.4162,
    38.4847, 38.0650, 39.7644, 37.6996, 38.5936
]

# Calculate linear trend
slope, intercept = np.polyfit(years, tgx, 1)
trend = slope * years + intercept

# Plot
plt.figure(figsize=(12, 6))
plt.plot(years, tgx, marker='o', markersize=4,
         label='Annual TGx (ACCESS-CM2)')
plt.plot(years, trend, linestyle='--',
         label=f'Linear trend: {slope*10:.2f} °C/decade')

plt.xlabel('Year')
plt.ylabel('Temperature (°C)')
plt.title('Historical Annual TGx – Mali (1960–2014)')
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()

plt.savefig('ACCESS_TGx_1960_2014.png', dpi=300)
plt.show()
