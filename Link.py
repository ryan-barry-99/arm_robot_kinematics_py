"""
File: Link.py

Description: This module defines the Link class which represents a single link in an arm robot.  
It contains the joint type, length, angle and methods to move the joint.

Author: Ryan Barry 
Date Created: October 6, 2023
"""
PRISMATIC = 0
REVOLUTE = 1

class Link:
    def __init__(self, joint_type, length, alpha=0):
        self.joint_type = joint_type
        self.theta = 0
        self.a = 0
        self.d = 0
        # rotate around the x1 axis an angle alpha to make z1 parallel to z2
        self.alpha = alpha
        if self.joint_type == PRISMATIC:
            self.d = length
        elif self.joint_type == REVOLUTE:
            self.a = length
        else:
            print(f"Invalid joint type at joint {i}")
            
        
    def moveJoint(self, joint_value):
        if self.joint_type == REVOLUTE:
            self.theta = joint_value
        elif self.joint_type == PRISMATIC:
            self.d = joint_value
        else:
            print(f"Invalid joint type at joint {joint}")
            return None
        
        
    def transform_matrix(self):
        ct = np.cos(self.theta)  # Compute the cosine of theta
        st = np.sin(self.theta)  # Compute the sine of theta
        ca = np.cos(self.alpha)  # Compute the cosine of alpha
        sa = np.sin(self.alpha)  # Compute the sine of alpha
        a = self.a
        d = self.d

        if self.joint_type == REVOLUTE:  # Check if the joint type is revolute
            return np.array(
                            [
                                [ct, -st * ca, st * sa, a * ct],  # Create the transformation matrix A
                                [st, ct * ca, -ct * sa, a * st],
                                [0, sa, ca, d],
                                [0, 0, 0, 1]
                            ]
                        )

        elif self.joint_type == PRISMATIC:  # Check if the joint type is prismatic
            return np.array(
                            [
                                [ct, -st * ca, st * sa, ct * d],  # Create the transformation matrix A
                                [st, ct * ca, -ct * sa, st * d],
                                [0, sa, ca, a],
                                [0, 0, 0, 1]
                            ]
                        )