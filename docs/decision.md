# Decision Process Emma & Luca 

## Overview of Reviewed Papers

### 1. Paper Title: "AirDraw: Leveraging Smart Watch Motion Sensors for Mobile Human-Computer Interactions"

This paper explores the potential of using smart watch motion sensors to capture letters drawn in the air, enabling faster text input without a physical device.

**Why We Did Not Choose It:**

Although this idea was innovative and relatively simple to implement with available resources, it was ultimately our second choice. The precision and consistency of motion capture can be challenging, and the need for extensive machine learning to accurately recognize the drawn characters—especially with variations in writing styles—added complexity that could complicate troubleshooting and system reliability. Additionally, we lacked the necessary data, which we would have had to collect ourselves. Nonetheless, it was a doable project, and had we not chosen to pursue gaze breath, this would have been our preferred option.

### 2. Paper Title: "Gaze Breath: Combining Eye Tracking and Breath Input for Real-time Interaction"

This paper presents a novel approach by combining eye tracking and breath input, leveraging natural and intuitive interactions for input selection.

**Why We Chose It:**

The implementation seems straightforward with the required hardware, such as a thermal camera, making it a feasible project within our capabilities. We decided to only focus on the breathing input and ignore the eye tracking since it would be out of scope for 2 weeks. Furthermore Emma already presented this paper so we already had a basic knowledge of the paper. We also already had some ideas how to make it better, like for example using mediapipe for face tracking. Doing this will give the possibility to move the face while tracking the breath instead of being forced at a position.


### 3. Paper Title: "Skinput Bio-Acoustic Sensing Technology: A New Era of Interaction with Electronic Devices"

This paper explores the use of bio-acoustic sensing for interaction through touch inputs on the skin, enabling control of devices by tapping or swiping on the body.

**Why We Did Not Choose It:**

The implementation requires a bio-acoustic sensor, a camera, a pico-projector, and Bluetooth technology. The complexity and necessity of multiple coordinated hardware components make this approach too resource-intensive and challenging to manage within our project constraints.

### 4. Paper Title: "RotoSwype: Word-Gesture Typing using a Ring"

Investigates the use of a ring with sensors to track its position and orientation for word-gesture typing, effectively turning the ring into a versatile input device.

**Why We Did Not Choose It:**

Building the required ring with a camera, infrared sensor, and transmitter, as well as integrating it with a display mounted on glasses, presents significant hardware development challenges. The complexity and time required to develop such a custom device were beyond our current project scope.

### 5. Paper Title: "IBUKI: Gesture Input Method Based on Breathing"

Focuses on using breathing patterns and direction to control devices, aiming to provide an intuitive and hands-free input method.

**Why We Did Not Choose It:**

The necessity of specialized sensors to detect breathing patterns and direction, along with a 9-DoF IMU and a mask for accurate input capture, made this approach impractical. Obtaining and integrating these specific sensors seemed impossible for us in 2 weeks.

### 6. Paper Title: "TongueBoard: An Oral Interface for Subtle Input"

Investigates the use of sensors in the mouth to track tongue movements for subtle input, providing an alternative interface for users with limited mobility.

**Why We Did Not Choose It:**

The requirement of placing sensors inside the mouth raises significant hygiene concerns and practical challenges. Additionally, developing and maintaining such a system in a hygienic and user-friendly manner is impractical within our timeline and scope.

### 7. Paper Title: "Clench Interface: Novel Biting Input Techniques"

This paper explores biting as a novel input technique using a radar-based interaction system.

**Why We Did Not Choose It:**

Access to and integration of FMCW radar technology required for implementing this interaction method is not feasible within our current resource constraints. The complexity and cost of obtaining and setting up the necessary radar system further contributed to the decision to not pursue this paper.


## Decision to Choose "Gaze Breath"

After a thorough review of the papers, we decided to focus on replicating and developing the **"Gaze Breath“** technology. Our decision was influenced by the following key factors:

- it seems doable in 2 weeks
- we already have knowledge about the paper
- we already have ideas for improving on the paper
- Andi told us that he found a thermal camera
- we do not have to collect a ton of data!