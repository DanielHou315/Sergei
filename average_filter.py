import numpy as np
import math

def find_max_of_average(image, w, h, channels, i):
    print("Processing Pixel ", w, h)
    # Aggregate Image Colors
    sum = []
    for k in range(0, channels):
        sum.append(0)
        for tw in range(w, w+i):
            for th in range(h, h+i):
                sum[k] += image[tw][th][k]
    # Process
    max_channel = 0
    max_colorval = 0
    for k in range(0, channels):
        if sum[k] > max_colorval:
            max_channel = k
            max_colorval = sum[k]
    return max_channel