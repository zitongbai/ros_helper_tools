#! /usr/bin/env python

import time
import numpy as np

from tf.transformations import quaternion_matrix, quaternion_from_euler

# use meshcat to visualize the attitude
import meshcat
import meshcat.geometry as g
import meshcat.transformations as m_tf


class VizAttitude:
    def __init__(self):
        self.vis = meshcat.Visualizer()
        self.vis.open()
        
        ax_length = 0.5
        ax_width = 0.05
        
        self.vis["ax"].set_object(g.Sphere(radius=ax_width))
        self.vis["ax"]["x"].set_object(g.Box([ax_length, ax_width, ax_width]), g.MeshLambertMaterial(color=0xff0000))
        self.vis["ax"]["x"].set_transform(m_tf.translation_matrix([ax_length/2, 0, 0]))
        self.vis["ax"]["y"].set_object(g.Box([ax_width, ax_length, ax_width]), g.MeshLambertMaterial(color=0x00ff00))
        self.vis["ax"]["y"].set_transform(m_tf.translation_matrix([0, ax_length/2, 0]))
        self.vis["ax"]["z"].set_object(g.Box([ax_width, ax_width, ax_length]), g.MeshLambertMaterial(color=0x0000ff))
        self.vis["ax"]["z"].set_transform(m_tf.translation_matrix([0, 0, ax_length/2]))
        
    def update_from_quaternion(self, q):
        """Update the attitude visualization from a quaternion
        quaternion convention: [x, y, z, w]
        
        Args:
            q (list): quaternion
        """
        
        R = quaternion_matrix(q)
        self.vis["ax"].set_transform(R)
        
    def update_from_euler(self, x, y, z, axes='sxyz'):
        """Update the attitude visualization from euler angles
        
        Args:
            x (float): roll
            y (float): pitch
            z (float): yaw
            axes (str, optional): euler angles order. Defaults to 'sxyz'.
        """
        
        q = quaternion_from_euler(x, y, z, axes=axes)
        self.update_from_quaternion(q)
        
        

if __name__ == '__main__':
    
    viz = VizAttitude()
    
    time.sleep(1)
    
    for euler_z in np.linspace(0, 2*np.pi, 1000):
        viz.update_from_euler(0, 0, euler_z)
        time.sleep(0.01)