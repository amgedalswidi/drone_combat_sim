
from controller import Robot

robot = Robot()
timestep = int(robot.getBasicTimeStep())

print("🔄 Starting Autonomous Drone...")

counter = 0

while robot.step(timestep) != -1:
    print(f"🚁 Drone is flying... Targets hit: {counter}")
