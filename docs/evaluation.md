# Data Evaluation

## Mouth Breathing

![mouth evaluation](/docs/images/mouth_breathing/mouth_c9.png)

The graph represents the measurement of breathing using a thermal camera, specifically aiming to identify inhale and exhale events. The brathing was mesaured at the mouth. Therefore mediapipe is used to detect the mouth. The frame that represents the mouth is then cut and zoomed in the center of the frame (1/3 of the mouth frame). Here the 200 coolest points are used to calculate the mean temperature. The zoom is done to really only focus on the breath and to exclude external factores.

### What the Graph Shows:
**Blue Line with Crosses (Mean Temperature in °C):**

- This line shows the mean temperature detected by the thermal camera over time.

**Red Dashed Line (Threshold in °C):**

- This threshold line is recalculated every 6 seconds based on the previous 6 seconds of temperature data.
It helps to differentiate between the inhale and exhale phases of breathing.

**X-Axis (Time in s):**

- Represents time in seconds.

**Y-Axis (Temperature in °C):**

- Represents the temperature in degrees Celsius.

### Reasons for Temperature Fluctuations:
**Breath Cycle (Inhalation and Exhalation):**

Inhalation usually involves cooler air being drawn in, which may cause a drop in temperature detected by the camera.
Exhalation releases warmer air, often resulting in a rise in temperature.


**Environmental Factors:**

The surrounding environment and the position of the thermal camera can influence the temperature readings.
Sudden changes in ambient temperature or movement of the subject can cause fluctuations. This can lead to problems if the calibration of the camera is off.


**Threshold Recalculation:**

The threshold is recalculated every 6 seconds, which might introduce abrupt changes if the recent past had significant temperature variations.

### Detailed Observations:
- Initial Temperature Drop (0-10 seconds):
    -   A sharp drop in temperature is seen initially, due to the calibration phase. This algorithm does not work in the first 6 seconds because of no real threshold. It also often takes two cycles to get a reliable threshold. Therefore the data is often only usable after at least 12 seconds.

- Temperature Stabilization and Rhythmic Pattern (After 10 seconds):
    -  The temperature starts to show a rhythmic pattern, corresponding to regular breathing cycles.
- The threshold line adjusts to these changes, staying above the lower dips in temperature.

Overall, the graph effectively captures the dynamics of breathing through temperature changes, depicting the inhalation and exhalation. The large temperature fluctuations are mainly due to the natural breathing cycle and environmental influences on the thermal measurements.


## Nose Breathing
Not as percise as mouth breathing!
