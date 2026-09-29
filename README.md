# Distance-Based Servo Control with ROS 2 and Arduino

This repository contains the full source code for controlling a Servo Motor based on Ultrasonic Distance Sensor readings using Arduino and ROS 2.

## Hardware Components
- Arduino Uno / Nano
- HC-SR04 Ultrasonic Distance Sensor
- Servo Motor (SG90 or similar)
- Connecting Wires & Breadboard

## System Architecture
1. **Arduino Sketch**: Reads HC-SR04 sensor distance (cm), sends value via Serial (9600 baud), and receives target angle commands (0–180°) to drive the servo attached to pin 6.
2. **`bridge_node` (ROS 2)**: Handles Serial communication between PC and Arduino. Publishes distance data to `/distance` and forwards target angles from `/servo_angle` to Serial.
3. **`controller_node` (ROS 2)**: Subscribes to `/distance`, maps distance (5–50 cm) to servo angle (0–180°), and publishes the command to `/servo_angle`.

---

## Hardware Setup
- **Trig Pin**: Pin 9
- **Echo Pin**: Pin 10
- **Servo Signal Pin**: Pin 6

---

## Installation & Running

### 1. Upload Arduino Code
Open `arduino/servo_distance/servo_distance.ino` in Arduino IDE and upload it to your board.

### 2. Build ROS 2 Package
```bash
cd ~/ros2_ws/src
# Copy ros2_servo_control into src directory
cd ~/ros2_ws
colcon build --packages-select ros2_servo_control
source install/setup.bash
