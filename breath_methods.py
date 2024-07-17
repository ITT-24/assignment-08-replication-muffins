import numpy as np
import cv2
import matplotlib.pyplot as plt

def kelvin_to_celsius(val):
    #return (val - 27315) / 100.0
    return val
    return (val - 27315) / 1500.0

def get_coolest_points_and_temperatures(data):

    minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(data)
    #print("MIN:", minVal)
    #print("MIN_Loc:", minLoc)
    #print("MAX:", maxVal)

    flattened_data = data.flatten()
    #grid_points = flattened_data[::4]
    sorted_indices = np.argsort(flattened_data)
    coldest_indices = sorted_indices[:200]

    positions = np.unravel_index(coldest_indices, data.shape)

    coldest_points = list(zip(positions[0], positions[1], kelvin_to_celsius(flattened_data[coldest_indices])))
    #for point in coldest_points:
        #print(f"Position: ({point[0]}, {point[1]}), Temperaturwert: {point[2]}")

    #return coldest_points

    # Erstellen einer Kopie des Bildes zum Markieren
    marked_image = data.copy()

    # Markieren der kältesten Punkte (z.B. mit roten Kreisen)
    for point in coldest_points:
        cv2.circle(marked_image, (point[1], point[0]), 5, (0, 0, 255), -1)

    # Anzeigen des markierten Bildes
    cv2.imshow("Bild", marked_image)
    #plt.title("50 kälteste Punkte")
    #plt.show()

    return coldest_points

def calculate_average_temperature(coldest_points):
    temperatures = [point[2] for point in coldest_points]
    average_temperature = np.mean(temperatures)
    #print(f"Durchschnittstemperatur der 50 kältesten Punkte: {average_temperature:.2f} °C")
    return average_temperature