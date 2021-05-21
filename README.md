# HandheldAR

## Project Description
<p> Augmented reality is a form of technology that was created to create a computer generated overlay on top of the real world view of the user. This is usually accomplished through a phone or large glasses that can hold a camera and a small processing to find markers in the camera frame and produce an image. While this method is effective it is difficult to share among multiple users with single device.</p>
<p> The focus of this project was to create a handheld AR device that could be portable and easily shared. It would read a video input from the camera and pull up relevant information based on the ID of a marker within that frame. The device would generate a graphic based on the returned data and would finally project the graphic back into the world positioned relative to the marker. </p>
<p> To accomplish this, our team utilized Python OpenCV and ArUco (Augmented Reality University of Cordoba) markers alongside the inexpensive hardware afforded by a Raspberry Pi computer. The Raspberry Pi camera module was used to take in video input and read the ArUco markers found in the frame. The device would then use a homography (a 3x3 matrix that could be used to understand the change in distance due to perspective) to correct the graphic. The ArUco markers found through OpenCV are excellent for this and would allow for the projection of certain graphics in a predictable location relative to the ArUco marker. </p>
<p> An example of this device in use would be in situations where a visual representation might be helpful, such as in a construction site. This device could be programmed to show anything from pipes, wiring, or studs behind a wall to a proposed design for a building. </p>
<br>
<p> During our time with this project our scope has changed, and we are no longer trying to create a complicated graphic that is projected. Instead, we have spent our time creating a simple image that is placed in the correct location and warps properly with perspective. </p>

## Hardware
### Raspberry Pi 4
<ul>
  <li> Raspberry Pi 4 Model B - 4 GB RAM </li>
  <li> Raspberry Pi Camera Board v2 - 8 Megapixels </li>
  <li> Official Raspberry Pi Power Supply 5.1V 3A with USB C </li>
  <li> Aluminum Heat Sink for Raspberry Pi 3 or 4 - 15 x 15 x 15 mm </li>
  <li> Official Raspberry Pi Foundation Raspberry PI 4 Case </li>
  <li> Micro SD - 16GB </li>
  <li> Micro-HDMI to HDMI Socket Adapter Cable </li>
  <li> Any USB A Mouse and Keyboard </li>
  <li> Any monitor </li>
</ul>

### Setup
<ol>
  <li> Place the rubber feet included with the Raspberry Pi Case onto the proper spots on the bottom of the Raspberry Pi </li>
  <li> Set the Raspberry Pi into the bottom of the case, lining the holes on the Pi with the pegs on the case </li>
  <li> Take out the Raspberry PI 4. Remove protector layer from bottom of heat sink and stick the heat sink on top of the Pi's processor. </li>
  <li> Install the Raspberry Pi OS onto the Micro SD card: https://projects.raspberrypi.org/en/projects/raspberry-pi-setting-up/2 </li>
  <li> Insert the Micro SD card into the proper slot on the bottom of the Raspberry pi.
  <li> Follow this tutorial to set up the Camera Module: https://projects.raspberrypi.org/en/projects/getting-started-with-picamera </li>
  <li> Connect Raspberry Pi to monitor through micro HDMI to HDMI adapter. Use Micro HDMI port 1 </li>
  <li> Connect to mouse and keyboard to any avaliable USB ports </li>
  <li> Connect power supply to the pi </li>
  <li> Congrats, the hardware is now ready </li>
</ol>

## Software

### OpenCV - 4.5.0
#### Open CV Installation and Compilation
Follow the tutorial at: https://pimylifeup.com/raspberry-pi-opencv/

### Python3
#### Python Download
Download from:
https://www.python.org/downloads/ <br>
Any version past 3.7.3

### NumPy
#### numpy install
Run `pip install numpy`


### Running ArUco recognition code
<ol>
  <li> Follow the above installation and compilations </li>
  <li> Clone the repository at https://github.com/thomlane/HandheldAR </li>
  <li> Navigate to the ArUcoMarkers Folder </li>
  <li> Run `python3 ./arMarkerWrite.py <id>`  where id is the desired marker</li>
  <li> Print out the marker saved in folder markers or just open it on the monitor </li>
  <li> Navigate back to the ArUcoMarkers Folder </li>
  <li> Run `python3 ./arMarkerRecognition.py` and point the camera at the marker </li>
  <li> The window opened by the program should show the marker being found and the corner and id being printed on the screen </li>
  <li> Press `q` to end the program </li>
</ol>
   

## Files
### Archive
#### QR Recognition
Beginning of the project. Recognizes qr codes but cannot orient the marker

### ArUcoMarkers
<p> A folder of two files: </p>
<p> arMarkerWrite.py takes in one argument, the id of marker. It will then produce a folder called markers in the same location as this file. </p>
<p> arMarkerRecognition.py activates the Pi's camera and start searching for markers in the frame. After finding a marker it will place circles in the top left and bottom right corners. The marker's ID will also be printed in the marker's bottom right corner. </p>
