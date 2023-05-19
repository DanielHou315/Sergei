import numpy as np
import math

'''Some Math Involved in generating patterns'''

def generate_sphere(s, h, height_coeff):
    '''
    Generates Part of a Sphere with Height h and cross-section radius s. 
    
    height_coeff adjusts the height of the sphere cutout once the calculations are done,
    shape post-adjustment looks like a paraboloid.
    '''
    r = (s**2 - 4*h**2) / 8 / h
    array = np.zeros([s,s])
    center = [s/2, s/2]
    for i in range(0, s):
        for j in range(0,s):
            d2 = (i - s/2)**2 + (j - s/2)**2
            x = math.sqrt(r**2 - d2) - r + h
            if x < 0:
                x = 0
            array[i][j] = x * height_coeff
    return array
