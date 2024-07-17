# Methods
## Face Detection

To only see the temperature change at the mouth or nose we used mediapipe to detect mouth and nose. Therefore a frame is cut that represents for example the mouth area. Inside of this area then we zoomed in the center of the frame (1/3 of the  frame) to further exclude outside noise of the breathing. Here the 200 coolest points are used to calculate the mean temperature. The zoom is done to really only focus on the breath and to exclude external factores.

Due to the less reliable face detection when using a thermal camera the nose holes could not really be identified. But the nose tip is identified more or less reliable. This why we decided to estimate the nose holes based on the nose tip. The frames we are getting you cann see in the following pictures.

### Detection with thermal camera:
![thermal_image](/docs/images/detection_thermal.png)
### Detection with a normal webcam:
![webcam_image](/docs/images/face_detection_normal.jpg)



# Improvements

We attempted to improve the paper by allowing subjects to move their faces more freely compared to the original setup, where subjects had to keep their faces fixed at a specific point directed towards the camera. Our method enables a more natural range of motion for the face.

However, this approach may encounter issues if the overlaid image from the calibration phase is not precise enough. Despite this, users can hold their heads normally, allowing for comfortable and natural laptop usage. This makes the application significantly more realistic and user-friendly.