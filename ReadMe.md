# Arm Robot Kinematics 
 
This library provides classes and methods for performing kinematics calculations on an articulated robot arm. 
 
## Files 
 
-  `ArmRobot.py`  - Contains the  `ArmRobot`  class which represents a specific robot arm configuration. It inherits from  `ArmRobotKinematics`. 
 
-  `ArmRobotKinematics.py`  - Contains the  `ArmRobotKinematics`  base class with methods for forward kinematics, inverse kinematics, calculating Jacobians etc. 
 
-  `Frame.py`  - Contains the  `Frame`  class to represent each frame/link in the robot arm. 
 
## Usage 
 
To use the library: 
 
1. Define the robot configuration by instantiating  `ArmRobot`  and adding  Frame  objects in the  `__init__`  method. 
 
2. Import  `ArmRobot`. 
 
3. Create an instance of  `ArmRobot`. 
 
4. Use methods  `forward_kinematics()`,  `iterative_inverse_kinematics()`, or create your own geometry based inverse kinematics equation. 
 
5. Joint values can be updated with the  `move_joint()`  method. 
 
See docstrings and comments in code for more details. 
 
## Features 
 
- Forward and inverse kinematics calculation. 
 
- Jacobian calculation. 
 
- Handles revolute, prismatic and fixed joints. 
 
- Flexible robot arm configuration through links defined in  `ArmRobot`. 

## Author
- Name: Ryan Barry
- Date created: June 26, 2023