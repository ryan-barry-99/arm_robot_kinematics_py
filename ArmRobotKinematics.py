"""
File: ArmRobotKinematics.py

This module defines the ArmRobot class, which represents an arm robot with multiple joints.
It provides functionality to add links to the arm, move individual joints, update the
Denavit-Hartenberg (DH) table, and perform forward kinematics to compute the end-effector
position and orientation.

Author: Ryan Barry
Date created: June, 26 2023
"""

import numpy as np  # Importing the NumPy library for mathematical operations
from Link import PRISMATIC, REVOLUTE, Link


class ArmRobotKinematics:
    def __init__(self):
        self.links = []

    # Add a link to the arm
    # Parameters:
    #   joint_type:
    #       - REVOLUTE
    #       - PRISMATIC
    #   length (meters)
    #   alpha (radians)
    #       - rotate around the x1 axis an angle alpha to make z1 parallel to z2
    def addLink(self, joint_type, length, alpha):
        new_link = Link(joint_type=joint_type, length=length, alpha=alpha)
        self.links.append(new_link)
        return new_link

    def forward_kinematics(self):
        self.__T = np.identity(4)  # Initialize the transformation matrix as an identity matrix

        for link in self.links:
            self.__T = np.dot(self.__T, link.transform_matrix())  # Multiply the transformation matrix T by A

        return self.__T  # Return the final transformation matrix

    def inverse_kinematics(self, target_position, target_orientation):
        pass
