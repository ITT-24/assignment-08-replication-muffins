# Problems and some troubleshooting

## Camera
- Camera did not work out of the box. It took us 3 to 4 days to make it work
- Camera sometimes reboots all by itself. This can not be changed which leads to no data for some seconds. Since this rarely happens it`s no real problem. Also a manual reboot can be performed by pressing the space button.
- Initial calibration is difficult:
    - the best way to do the initial calibraion is to direct it to a smooth and cold surface and after that at yourself
    - if some cuts are detected in the initial booting images this might modify the temperature data and lead to temperatures that are far from reality

- **Temperature:**
    - the initial captured temperature is way off from being realitic. It shows skin temperature of a 1000 °C and above
    - we tried to more or less get the temperature to around 30 - 40 °C but ended with temperatures between 0 and 40 °C. Even though our calculations are not correct for the temperature it still is way easier to work with the data we get now and to get a feeling of our data / results.
    
## Nose detection
- mediapipe has a hard time detecting the nose holse with the thermal camera. But it detects more or less the nose tip. This is why we calculate the nose holes based on the nose tips. But since noses are very differen the square might have to be shifted some pixels up or down. This can be done in face_detection.py. This seems to work fine!
