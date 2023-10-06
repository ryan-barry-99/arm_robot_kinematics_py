# Arm Robot

This repository contains the code for the  `ArmRobot`  module, which represents an arm robot with multiple joints. It provides functionality to add links to the arm, move individual joints, update the Denavit-Hartenberg (DH) table, and perform forward and inverse kinematics calculations.

## File Structure

-  `ArmRobot.py` : The main module file that contains the  `ArmRobot`  class.
-  `ArmRobotKinematics.py` : The module that defines the  `ArmRobotKinematics`  class.
-  `README.md` : This readme file to provide information about the repository.

## Usage

To use the  `ArmRobot`  module, follow these steps:

1. Import the module:
from ArmRobot import ArmRobot
2. Create an instance of the  `ArmRobot`  class:
arm = ArmRobot()
3. Add links to the arm using the  `addLink`  method:
arm.link0 = arm.addLink(joint_type=REVOLUTE, length=1)
   arm.link1 = arm.addLink(joint_type=PRISMATIC, length=1)
4. Move individual joints using the  `moveJoint`  method (inherited from  `ArmRobotKinematics`  class):
arm.moveJoint(joint, angle_or_distance)
-  `joint` : The number of the joint to move.
   -  `angle_or_distance` : The angle (for revolute joints) or distance (for prismatic joints) to move the joint.

5. Update the DH table using the  `updateDHTable`  method (inherited from  `ArmRobotKinematics`  class):
arm.updateDHTable()
6. Perform forward kinematics to compute the end-effector position and orientation using the  `forward_kinematics`  method (inherited from  `ArmRobotKinematics`  class):
transformation_matrix = arm.forward_kinematics()
- Returns the 4x4 transformation matrix representing the end-effector position and orientation.

7. Perform inverse kinematics (must be implemented specific to robot configuration) using the  `inverse_kinematics`  method (override from  `ArmRobotKinematics`  class).

## Author

- Name: Ryan Barry
- Date created: June 26, 2023
