import cv2
import numpy as np
import math

def find_max_three(image, w, h, channels, i):
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


def generate_sphere(s, h, height_coeff):
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


def apply_sphere(img, w, h, array, coeff):
    
    wid, hei= np.shape(array)
    startx = int(w - wid/2)
    starty = int(h - hei/2)

    imgwid, imghei, imgdep = np.shape(img)
    for i in range(0, wid):
        for j in range(0, hei):
            if startx + i > 0 and startx + i < imgwid \
                and starty + j > 0 and starty + j < imghei:
                img[startx+i][starty + j] += coeff * array[i][j]


def test_circle():
    s = 9
    h = 1
    arr = generate_sphere(s, h, 100)
    cv2.imwrite("circle_test_100.jpg", arr)


def test_conversion():
    img_path = input("Enter Image Path: ")
    image = cv2.imread(img_path[1:-1])
    # print(type(image))

    # Read Height
    wid, hei, col_channels = np.shape(image)
    col_max = np.amax(image)
    print(wid, hei)

    # Process Image
    square_len = 10

    new_image = np.zeros([wid, hei, col_channels])
    for w in range(0, wid-square_len):
        for h in range(0, hei-square_len):
            new_image[w][h][find_max_three(image, w, h, col_channels, square_len)] = col_max

    cv2.imwrite("proc_" + str(square_len) + ".jpg", new_image)




def test_application():
    img_path = input("Enter Image Path: ")
    image = cv2.imread(img_path[1:-1])

    # Read Height
    wid, hei, col_channels = np.shape(image)
    col_max = np.amax(image)
    print(wid, hei)

    # Process Image
    step = 20
    s = 9
    h = 1
    height_coeff = 100

    circle_arr = generate_sphere(s, h, height_coeff)
    test_circle()

    new_image = np.ndarray([wid, hei, col_channels])
    new_image.fill(127)
    for w in range(int(step / 2), wid, step):
        for h in range(int(step / 2), hei, step):
            if image[w][h][0] > 0:
                apply_sphere(new_image, w, h, circle_arr, -1)
            elif image[w][h][1] > 0:
                apply_sphere(new_image, w, h, circle_arr, 0)
            else:
                apply_sphere(new_image, w, h, circle_arr, 1)

    cv2.imwrite("apply_circ_" + str(step) + ".jpg", new_image)



if __name__ == "__main__":
    # test_conversion()
    # test_circle()
    test_application()