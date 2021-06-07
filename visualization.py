import matplotlib.pyplot as plt
import numpy as np
import cv2


if __name__ == "__main__":

    background = np.zeros((700, 1000, 3), np.uint8)

    print('omgomg the script is starting now enjoooooy!!!')

    while True:
        frame = background.copy()
        rand_x = int(np.random.uniform(low=100, high=500))
        rand_y = int(np.random.uniform(low=100, high=700))
        frame[rand_x : rand_x + 10, rand_y : rand_y + 10] = [0, 0, 255]

        cv2.imshow("frame", frame)

        key = chr(cv2.waitKey(1) & 0xFF)
        if key == "q":
            print('I break now, goodbye')

            break
