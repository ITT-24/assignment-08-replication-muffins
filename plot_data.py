import matplotlib.pyplot as plt

# format: tuple -> time, temperature
def plot_temperature(data_points, thresholds=None):
    times, temperatures = zip(*data_points)
    
    plt.figure(figsize=(10, 5))
    plt.plot(times, temperatures, marker='x', linestyle='-', color='b', label=f'Mean Temperature in °C')
    
    if thresholds is not None:
        time, threshold = zip(*thresholds)
        plt.plot(time, threshold, color='r', linestyle='--', label=f'Threshold in °C')
    
    plt.xlabel('Time in s')
    plt.ylabel('Temperature in °C')
    plt.title('Breath Rhythm')
    plt.legend
    
    plt.grid(True)
    plt.legend()
    plt.show()
