import numpy as np
import cv2
import matplotlib.pyplot as plt

NUMBER_OF_COLDEST_POINTS = 200

def kelvin_to_celsius(val):
    # return (val - 27315) / 100.0 #original code
    return (val - 27315) / 750.0 # changed this for more realistic values

def get_coolest_points_and_temperatures(data):

    flattened_data = data.flatten()
    sorted_indices = np.argsort(flattened_data)
    coldest_indices = sorted_indices[:NUMBER_OF_COLDEST_POINTS] #used 50 in the paper, but 200 is more robust

    positions = np.unravel_index(coldest_indices, data.shape)

    coldest_points = list(zip(positions[0], positions[1], kelvin_to_celsius(flattened_data[coldest_indices])))

    # -------- show marked image with coldest points ----------
    # marked_image = data.copy()

    # for point in coldest_points:
    #     cv2.circle(marked_image, (point[1], point[0]), 5, (0, 0, 255), -1)
    
    # cv2.imshow("Bild", marked_image)
    #plt.title("50 kälteste Punkte")
    #plt.show()

    return coldest_points

def calculate_average_temperature(coldest_points):
    temperatures = [point[2] for point in coldest_points]
    average_temperature = np.mean(temperatures)
    #print(f"Durchschnittstemperatur der 50 kältesten Punkte: {average_temperature:.2f} °C")
    return average_temperature