import folium
import pandas as pd
from selenium import webdriver
from time import sleep

# Read the data
df = pd.read_csv('coordinates_kerkhoflaan.csv')

# Initialize a map centered around the first sensor
m = folium.Map(location=[df.iloc[0]['lat'], df.iloc[0]['lon']], zoom_start=13)

# Add markers for each sensor
for _, row in df.iterrows():
    folium.map.Marker(
        [row['lat'], row['lon']],
        icon=folium.map.Icon(icon='circle', prefix='fa'),
        popup=folium.Popup(folium.IFrame(f'<div>{row["sensor"]}</div>', width=100, height=50), max_width=100)
    ).add_to(m)

# Save it as html
m.save("sensors_map.html")

# Use selenium to save the map as a PNG
driver = webdriver.Chrome()  # or webdriver.Chrome(), depending on your installed browser
driver.get("D:/scriptie/sensor_analysis/CNN-training/csv files/sensors_map.html")  # replace with the actual path
sleep(5)  # Allow the map to load
driver.save_screenshot("sensors_map.png")
driver.quit()

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Let's consider an example percentage decline in picked up firework noise from sensor 1 to 9
# You should replace this with your actual data
percentages = [100, 90, 85, 75, 70, 60, 50, 40, 35]

fig, ax = plt.subplots()
line, = ax.plot(range(1, 10), percentages)

def update(num):
    line.set_ydata([np.random.random() * 100 for i in range(1, 10)])  # update the data.
    return line,

ani = animation.FuncAnimation(fig, update, frames=range(1, 10), interval=1000, repeat=True)

plt.xlabel('Sensor')
plt.ylabel('Percentage of Firework Noise')
plt.title('Decline in picked up Firework Noise from Sensor 1 to 9')

plt.show()







