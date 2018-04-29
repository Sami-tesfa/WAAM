Introduction

This is a .txt editor written to read the output script from SprutCAM Robot 11 using the KRL post processor. It appends controls for the welding head mounted on the KUKA robotic arm being used for WAAM by searching for the when the weld head speed is changed within the script. It also deletes the standard header to the code and adds initialisation for the robotic arm and welding torch using the RCU 5000i control system and DeviceNet.

Instructions

The file directory for the .txt file to be processed needs to be input as the 'fname' variable on line 14.
The traverse speed for the robot arm needs to be input 'tspeed' on line 16 as a string.
The working speed for the robot arm needs to be input 'wspeed' on line 17 as a string.
The original file header is deleted by line 32 and may require adjustment if a different robot arm is to be used as the size of the header may vary.
 
Requirements

python 2.7.10
