# Data Evaluation

## Mouth Breathing

![mouth evaluation](/docs/images/mouth_breathing/mouth_exhale_inhale.jpg)

The graph represents the measurement of breathing using a thermal camera, specifically aiming to identify inhale and exhale events. The brathing was mesaured at the mouth. Therefore mediapipe is used to detect the mouth. The frame that represents the mouth is then cut and zoomed in the center of the frame (1/3 of the mouth frame). Here the 200 coolest points are used to calculate the mean temperature. The zoom is done to really only focus on the breath and to exclude external noise.

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
Exhalation releases warmer air, resulting in a rise in temperature.


**Environmental Factors:**

The surrounding environment, the calibration or boot of the camera and the position of the thermal camera can influence the temperature readings.
Sudden changes in ambient temperature or movement of the subject can cause fluctuations. This can lead to problems if the calibration of the camera is off.


**Threshold Recalculation:**

The threshold is recalculated every 6 seconds, which might introduce abrupt changes if the recent past had significant temperature variations. 

### Observations:
- Initial Temperature Drop (0-6 seconds):
    -   A sharp drop in temperature is seen initially, due to the calibration phase. 
- After 12 seconds a threshold can be seen
    - This algorithm does not work in the first 6 to 12 seconds because of no real threshold. This is due to the calclulation which calculates the threshold newly based on the last 6 seconds of temperature date. It also often takes two cycles to get a reliable threshold. Therefore the data is often only usable/readable after at 12 seconds.

- Temperature Stabilization and Rhythmic Pattern (After 06 seconds):
    -  The temperature starts to show a rhythmic pattern, corresponding to regular breathing cycles.

- After 12 seconds:
    - The threshold line adjusts to these changes, staying above the lower dips in temperature.

Overall, the graph effectively captures the dynamics of breathing through temperature changes, depicting the inhalation and exhalation. 
We believe that our data is accurate beacuse hile using the code we were able to successfully detect the inhalation and exhalation of the participant. Furthermore the similarity of the captured data to the captured data of the paper itself also is in favor for our data. For comparison the following picture is from the paper itself:

![paper_data_mouth](/docs/images/paper/paper_data_mouth.png)
Image Source: ["Gaze Breath: Combining Eye Tracking and Breath Input for Real-time Interaction"](https://dl.acm.org/doi/abs/10.1145/3519391.3519405)

But it has to be said that our thermal camera did get some weird data in the temperature. Normally the captured temperature should be around 32 - 36 °C but out camera captured degrees celsius between 0 and 30.


## Nose Breathing
![nose_breathing](/docs/images/nose_breathing/nose_02.png)

Nose breathing is not as percise and reliable as mouth breathing, which makes sense since for one mediapipe has a hard time detecting the nose and since the nose does not breath as strong as the mouth does. This graph was created the same way mouth breathing was created. Only the frame that was captured was not the mouth but the nose and no zoom (no 1/3 zoom of the frame) was used. Here we used the whole nose frame since two nose holes are used for breathing.

### Observations
The graph shows a decrease initially, stabilizing into a repeating pattern in which exhale and inhale can clearly be detected. There are noticeable variations at the beginning, which smooth out into a more regular cyclical pattern as time progresses. 

This data also seems to be reliabla because again the similarities to the captured data of the paper can be seen. For comparison here is the graph of the nose breathing data from the paper (x axis is time in seconds):

![paper_data_nose](/docs/images/paper/paper_data_nose.png)
Image Source: ["Gaze Breath: Combining Eye Tracking and Breath Input for Real-time Interaction"](https://dl.acm.org/doi/abs/10.1145/3519391.3519405)

But again the temperature is too low to be realistic.

# Summary

Overall, we successfully developed a robust method for detecting breathing. The data indicates that even if the absolute temperature isn't captured good, the relative temperature differences are accurately detected. Additionally, the data shows that mouth breathing is more precise than nose breathing.

Also the threshold remains realistic, and the algorithm appears to function well overall.