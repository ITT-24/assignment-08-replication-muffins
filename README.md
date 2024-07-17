# Documentation
In this project we tried to rebuild and improve the interaction technology of ["Gaze Breath: Combining Eye Tracking and Breath Input for Real-time Interaction"](https://dl.acm.org/doi/abs/10.1145/3519391.3519405).

![video](/docs/images/live.gif)

## Decision Process

In the end we decieded to rebuild and improve on the paper **["Gaze Breath: Combining Eye Tracking and Breath Input for Real-time Interaction"](https://dl.acm.org/doi/abs/10.1145/3519391.3519405)**.

### Resons for our decision:

- it seems doable in 2 weeks
- we already have knowledge about the paper
- we already have ideas for improving on the paper
- Andi told us that he found a thermal camera
- we do not have to collect a ton of data!

**For more informations about our decision process please read our documentation [here](https://github.com/ITT-24/assignment-08-replication-muffins/tree/master/docs/decision.md).**

## Manual
1. To install all dependencies do the following:
```
pip install -r requirements.txt
```

2. Connect a thermal camera to your computer. We used the [PureThermal Mini Pro JST-SR (with FLIR Lepton 3.5](https://www.antratek.de/purethermal-mini-pro-jst-sr-with-flir-lepton-3-5)

3. To start the code run the follwing:
```
sudo python flir_lepton.py
```
It is important to use sudo. Otherwise it is not possible to use the thermal camera.

4. Before the camera is activated face it at a smooth and more or less cold surface until you can see a video.

5. Face the camera at yourself. The camera will detect your mouth or nose (based on your choice) all by itself. 

6. Look at the camera and breath normally or if you want to perform a click perform a short or long inhale or exhale

## Evaluation

You can find our breathing results and evaluation **[here](https://github.com/ITT-24/assignment-08-replication-muffins/tree/master/docs/evaluation.md).**

Overall we get very similar data to the paper. Even the breathing curves look almost identically. But we still had some problems which can be read at the problems section **[here](https://github.com/ITT-24/assignment-08-replication-muffins/tree/master/docs/problems.md).**

For example as can be seen in the graph below. The temperature is way off from reality. The temperature should be around 32 - 38 °C. However this sometimes workes better and has no real influence on this project since we only capture the relative temperature change and not the absolute change.

**Breathing Overview:**
![Mouth Breathing](/docs/images/mouth_breathing/mouth_breathing.png)

**Short & Long Exhales**
![Exhales](/docs/images/mouth_breathing/mouth_exhale_inhale.jpg)

## Improvements and Methods

Here you can read what we did improve from the paper and what methods we used: **[Improvements & Methods](https://github.com/ITT-24/assignment-08-replication-muffins/tree/master/docs/methods.md).**


## Development Documentation
We documented our thoughts and daily process. If you want to see out process you can read here in the **[documentation](https://github.com/ITT-24/assignment-08-replication-muffins/tree/master/docs/diary.md).**



# Troubleshooting:
- The camera sometimes goes into sleep mode → the queue is empty → just restart the program and it will work.
- To recalibrate the image press the space button and face the camera to smooth and more or less cold surface

## Initial camera boot
If your data seems way off or does some sudden jumps as for example in the following picture read the following:

![jumping_data](/docs/images/mouth_breathing/mouth_c0.png)

Here the camera was directly facing the person when booting. This creates an overlay to the video_frames the camera is capturing. If you move your mouth to a another position of the initial frame, mediapipe might detect the mouth from the inital frame and not the live frame. Since the data here is fixed but still change a little bit for example though movement of the person itself this might happen. 

Another interesting aspect is the following. If you face the camera on a smooth surface at the initial booting face, the temperature detection is way colder (between 0 and 30°C) than if first faced at a person. See for example this picture:

![boot_table](/docs/images/mouth_breathing/mouth_breathing.png)

If you face the camera at yourself when the camera is booting you will get data like this:

![boot_person](/docs/images/mouth_breathing/mouth_c9.png)

As mentioned before if one does the boot like this jumps might occur (see seconds 0 to 10). BUT it can be seen that temperature now is way more realitstic between 30 and 40 °C.

**Therefor it is important how you calibrate/boot the camera before starting the measurements!**


[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/vWu16Gbh)
