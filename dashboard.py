import streamlit as st
import fastf1
import matplotlib.pyplot as plt

st.title("🏎️ F1 Driver Telemetry Dashboard")

year = st.selectbox("Select Season", [2023, 2024])
race = st.text_input("Enter Race (Example: Monza, Silverstone)")

if race:
    session = fastf1.get_session(year, race, "R")
    session.load()

    drivers = session.laps["Driver"].unique()

    driver = st.selectbox("Select Driver", drivers)

    driver_laps = session.laps.pick_driver(driver)

    lap_times = driver_laps["LapTime"].dt.total_seconds()

    fig, ax = plt.subplots()
    ax.plot(driver_laps["LapNumber"], lap_times)

    ax.set_xlabel("Lap Number")
    ax.set_ylabel("Lap Time (seconds)")
    ax.set_title(f"Lap Time Trend - {driver}")

    st.pyplot(fig)