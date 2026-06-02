from Line_Follower_Sensor import get_sensor_values
from Line_Follower_Movement import robot_action

sensors, active = get_sensor_values()

print("Sensor Values:", sensors)
print("Active Sensors:", active)

print("Robot Action:", robot_action(sensors))