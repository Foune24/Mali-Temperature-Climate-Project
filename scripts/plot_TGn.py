import numpy as np
import matplotlib.pyplot as plt

years = np.arange(1960, 2015)

tgn = [
14.24772, 16.15993, 15.05945, 16.56149, 15.59683,
16.32366, 16.68819, 15.79809, 16.64747, 18.96719,
12.57486, 16.81756, 11.98478, 18.3571, 15.67958,
16.19419, 17.06653, 15.36654, 12.50108, 17.98111,
18.08322, 17.57125, 18.30109, 17.52714, 17.80733,
16.96958, 16.41011, 18.19303, 17.84154, 17.88219,
18.27499, 16.91532, 17.00981, 16.7903, 17.9515,
17.2507, 17.21245, 16.23184, 18.08961, 19.66585,
16.96578, 18.12799, 17.9017, 17.95056, 18.58164,
18.93661, 18.79403, 17.13812, 17.24671, 17.68731,
17.88209, 18.24641, 17.85775, 17.02145, 19.04614
]
import numpy as np
import matplotlib.pyplot as plt
years = np.arange(1960, 2015)
slope, intercept = np.polyfit(years, tgn, 1)
trend = slope * years + intercept

plt.figure(figsize=(12, 6))

plt.plot(years, tgn, marker='o', markersize=4,
         label='Annual TGn (ACCESS-CM2)')

plt.plot(years, trend, linestyle='--',
         label=f'Linear trend: {slope*10:.2f} °C/decade')

plt.xlabel('Year')
plt.ylabel('Temperature (°C)')
plt.title('Historical Annual TGn – Mali (1960–2014)')
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()

plt.savefig('ACCESS_TGn_1960_2014.png', dpi=300)
plt.show()
