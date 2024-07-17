## Diary

## Daily Decisions

### Key Points (July 08, 2024)

- **Paper Decision**: See selection!

- **Thermal Camera Acquisition**:
  - Yes! Andi found a PureThermal Mini Pro JST-SR (with FLIR Lepton 3.5) for us! [PureThermal Mini Pro JST-SR (with FLIR Lepton 3.5](https://www.antratek.de/purethermal-mini-pro-jst-sr-with-flir-lepton-3-5)

- **Thermal Camera Setup**:
  - Initially very difficult. We spent 4 full days on it. As of July 11, 2024, we have a video stream and can see the temperature.
  - We need to check if we can read the temperature at specific points:
    - Yes, it works but the values seem to be way off.

- **Next TODOS**:
  - Exclude the nose and mouth area using cv2.
  - Measure temperature at the nasal wings.
  - Detect exhale and inhale.
  - Detect long exhale and long inhale.
  - Eye tracking is not feasible due to time constraints.
  - Implement improvements mentioned by Emma in her presentation, if there's time.


#### July 11, 2024

- Mouth and nose coordinates can be detected.
- The thermal camera seems to be working.
- The thermal camera is quite frustrating → meh!

#### July 15, 2024

- **Method Adjustment**: The `raw_to_8bit` method changed data values to 0 - 255 instead of the actual temperature.
  - Fixed this issue.
- **Temperature Accuracy**:
  - The camera captures temperature rather inaccurately. The coldest 50 points are not sufficient.
  - Tried an algorithm using every 4th pixel for calculation; results were neither better nor worse.
  - Temperature display was unreliable, indicating the camera needed calibration.
    - Recalculated temperatures to be between 30 and 40°C.
- **Face Detection**:
  - The face doesn't need to be still; it is well-detected by MediaPipe.
  - Detected mouth breathing so far, but we can switch to nose coordinates.

#### Interim Status

- **Detection**:
  - Nose and mouth can be detected, and breath can be seen (more or less good).
  - The thermal camera seems inaccurate; temperature changes during inhaling or exhaling are not very clear. The paper used a more expensive and better camera.
    - The thermal camera might be too poor.
    - It might need recalibration (values seem way off), which could affect precision but we only need to capture temperature changes, not precise temperatures.

#### Discoveries

- With a better and calibrated camera, we would achieve better results.
- Inhale is well-detected.
- Exhale generates too little cooling; the camera is too poor and can only detect it very roughly.
- **Breathing Pattern**:
  - Inhaling: cold points move to the left and right.
  - Exhaling: cold points move to the center of the mouth.
  - We could detect breathing with these patterns, but this would be too far off from the paper.

---

### Summary at July 15, 2024

- **Progress**:
  - Video stream established.
  - Mouth and nose coordinates detected.
  - Temperature readings adjusted.

- **Challenges**:
  - Accuracy of the thermal camera is questionable.
  - Calibration might be needed.
  - Detection of breathing patterns is possible but not precise.

- **Next Steps**:
  - Exclude unnecessary facial areas using cv2.
  - Focus on measuring temperature changes at specific points.
  - Improve detection algorithms for exhale and inhale.
  - Consider using a better thermal camera for more accurate results.


  ## July 16, 2024

- The data appears accurate, and exhalation and inhalation are generally well detected.
- Calibration is crucial, ideally performed on the individual user.
- The camera needs to acclimate to the ambient temperature; otherwise, there will be jumps in the measurements.

![plot_evolution](/docs/images/plot_evolution.png)