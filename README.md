# Animated-XYZ-CNC-LogFile-Using-Python

This code was used to visually debug (and amplify) the tool path of a CNC machine that has low accuracy and deals with small parts. 

Use: Verify if the machine tool path is travelling as intended or wandering. 
Particularly in additive manufacturing, this can be difficult to prove after material is added.

Input: CSV Log file with columns [X, Y, Z] with headers.
Output: 3D matplotlib animation that can be rotated and zoomed for analysis. 

https://user-images.githubusercontent.com/34481500/155578810-70bca7f6-9f84-417c-b1ed-7944ef897b80.mp4

Note: This code runs the positive Z axis direction opposite to conventional axis due to an improper setup on the physical machine that does not affect final functionality, only the log file.
