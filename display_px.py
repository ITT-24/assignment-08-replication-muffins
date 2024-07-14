import pyautogui
import time

try:
    while True:
        x, y = pyautogui.position()
        print(f"Cursor Coordinates: ({x}, {y})", end='\r')
        # Sleep for a short while to reduce CPU usage
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\nProgram exited.")
