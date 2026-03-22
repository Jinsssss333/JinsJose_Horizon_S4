# 🚀 Horizon Navigation - Task 3  
### ROS 2 Multi-Node Communication System  

This project demonstrates a basic autonomous navigation workflow using **ROS 2 Humble** on **Ubuntu 22.04**. It simulates a rover’s **Sense → Think → Act** cycle using two independent nodes communicating via ROS 2 topics.

---

## 🏗️ System Architecture  

The system is composed of two main nodes:

### 🔹 Sensor Node (`sensor_node.py`)
- Simulates a distance sensor (LiDAR/Ultrasonic)
- Publishes random distance values (**10 cm – 100 cm**)  
- Topic: `/distance`  
- Frequency: **1 Hz**

### 🔹 Decision Node (`decision_node.py`)
- Acts as the rover’s decision-making unit  
- Subscribes to `/distance`  
- Publishes movement commands  
- Topic: `/rover_command`  

---

## 🧠 Navigation Logic  

| Distance Condition | Action |
|------------------|--------|
| `< 30 cm`        | 🛑 STOP |
| `≥ 30 cm`        | ▶️ MOVE_FORWARD |

---

## ⚙️ How to Run  

### 1️⃣ Open Terminal 1
```bash
cd ~/jinsjose_horizon_s4
colcon build
source install/setup.bash
ros2 run horizon_navigation sensor

### 2️⃣ Open Terminal 2
cd ~/jinsjose_horizon_s4
source install/setup.bash
ros2 run horizon_navigation decision