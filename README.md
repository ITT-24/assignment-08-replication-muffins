# Documentation

## Decision Process

In the end we decieded to rebuild and improve on the paper **"Gaze Breath: Combining Eye Tracking and Breath Input for Real-time Interaction"**.

### Resons for our decision:

- it seems doable in 2 weeks
- we already have knowledge about the paper
- we already have ideas for improving on the paper
- Andi told us that he found a thermal camera
- we do not have to collect a ton of data!

**For more informations about our decision process please read our documentation [here](https://github.com/ITT-24/assignment-08-replication-muffins/tree/master/docs/decision.md).**

## Evaluation

You can find our breathing results and evaluation **[here](https://github.com/ITT-24/assignment-08-replication-muffins/tree/master/docs/evaluation.md).**

Overall we get very similar data to the paper. Even the breathing curves look almost identically. But we still had some problems which can be read at the problems section **[here](https://github.com/ITT-24/assignment-08-replication-muffins/tree/master/docs/problems.md).**

For example as can be seen in the graph below. The temperature is way off from reality. The temperature should be around 32 - 38 °C. However this sometimes workes better and has no real influence on this project since we only capture the relative temperature change and not the absolute change.

## Improvements and Methods

Here you can read what we did improve from the paper and what methods we used: **[Improvements & Methods]((https://github.com/ITT-24/assignment-08-replication-muffins/tree/master/docs/methods.md).)**


## Development Documentation
We documented our thoughts and daily process. If you want to see out process you can read here in the **[documentation](https://github.com/ITT-24/assignment-08-replication-muffins/tree/master/docs/diary.md).**

**Breathing Overview:**
![Mouth Breathing](/docs/images/mouth_breathing.png)

# Troubleshooting:
- The camera sometimes goes into sleep mode → the queue is empty → just restart the program and it will work.
- To recalibrate the image press the space button and face the camera to blank and more or less cold surface
- The thermal camera sometimes performs a reboot all by itself. This can sadly not be changed. Therefore it is possible that you won't get any data for the time the camera is rebooting (most of the time just 1 - 3 seconds)



[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/vWu16Gbh)
