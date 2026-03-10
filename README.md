# F1 Driver Performance Analyzer 🏎️📊

A Python application for visualizing **Formula 1 race telemetry** and analyzing **driver performance using real telemetry data**.

![Race Replay Preview](./resources/preview.png)

This project replays Formula 1 races using telemetry data and provides insights such as driver position, speed, tyre strategy, and lap performance.

---

## Features

- Race Replay Visualization – watch the race unfold with real-time driver positions on the track.
- Driver Performance Analysis – analyze telemetry like speed, gear, DRS status and lap data.
- Leaderboard – live driver positions and tyre compounds.
- Lap & Time Display – track current lap and race time.
- Driver Status – retired drivers marked as **OUT**.
- Interactive Controls – pause, rewind, fast-forward and change playback speed.
- Telemetry Insights – inspect telemetry data for selected drivers.

---

## Controls

| Action | Key |
|------|------|
Pause / Resume | SPACE  
Rewind | ←  
Fast Forward | →  
Speed Control | ↑ / ↓  
Restart | R  
Toggle DRS Zone | D  
Toggle Progress Bar | B  
Toggle Driver Names | L  

---

## Tech Stack

- Python
- FastF1
- Arcade
- NumPy

---

## Installation

Clone the repository:

```bash
git clone https://github.com/gunatheeth/f1-driver-performance-analyzer.git
cd f1-driver-performance-analyzer