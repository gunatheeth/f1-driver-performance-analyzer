import fastf1
import matplotlib.pyplot as plt

# Load race session
session = fastf1.get_session(2023, "Monza", "R")
session.load()

# Select a driver
driver = "VER"

# Get driver's laps
laps = session.laps.pick_driver(driver)

# Convert lap time to seconds
lap_times = laps["LapTime"].dt.total_seconds()

# Plot graph
plt.plot(laps["LapNumber"], lap_times)

plt.xlabel("Lap Number")
plt.ylabel("Lap Time (seconds)")
plt.title("Lap Time Trend - Max Verstappen")

plt.show()