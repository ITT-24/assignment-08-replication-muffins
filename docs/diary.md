# Diary

## Key Points
- Paper Decision → See selection!

- Are we getting a thermal camera?
    - Yes! Andi found a PureThermal Mini Pro JST-SR (with FLIR Lepton 3.5) for us! PureThermal Mini Pro JST-SR (with FLIR Lepton 3.5)

- Can we get the thermal camera to work?
    - Initially very difficult. We spent 4 full days on it. As of July 11, 2024, we have a video stream and can see the temperature.

- Still need to check if:
    - we can read the temperature at specific points

- Next TODOS:
    - Possibly eye tracking? -> No this is to time consuming!
    - Exclude the nose and mouth area using cv2
    - Measure temperature at the nasal wings
    - Detect exhale and inhale
    - Detect long exhale and long inhale
- If there's time:
    - Implement improvements mentioned by Emma in her presentation

## Daily Decisions

### July 11, 2024

- Mouth and nose coordinates can be detected. 
- The thermal camera seems to be working.
- The thermal camera is quite frustrating → meh!

### July 15, 2024

- The camera captures temperature rather inaccurately → the coldest 50 points are not sufficient.
    - Maybe write an algorithm that uses only every 4th pixel from the image for calculation.
        - workn neither better nor worse
- Temperature display is unreliable → the camera needs calibration; our body temperature is not 400°C.
    - recalculated the temperature. Now we are between 30 and 40 °C.
- A new discovery is that the face doesn't need to be still. It is well-detected by MediaPipe.
- So far, only mouth breathing is detected. But we can switch them with the nose coordinates    

#### Interim Status
- Nose can be detceted and breath can be seen (more or less good)
- Mouth can be detceted and breath can be seen (more or less good)
- Thermal camera seems to not be very accurate! Although we have a picture of the mouth and nose the temperature change when inhaling or exhaling can not be seen very clearly. Maybe our thermal camera detects not accurate enough. The paper used a way more expensive and better camera.
    - Thermal camera might be too bad.
    - Thermal camera might have to be recalibrated (values seem to be way off)
        - this might fiddle with our percision but in total we only need to capture the temperature change not the percise temperature

#### Discoveries
- With a better and calibrated camera, we would achieve better results.
- Inhale is well-detected.
- Exhale generates too little cooling → the camera is too poor → it can only be detected very roughly.

- Breathing pattern discovered:
    - Inhaling → cold points move to the left and right.
    - Exhaling → cold points move to the center of the mouth.
    - We could detcet the breathing with these patterns **BUT** this would be too far off of the paper.
