# Gesture Based UI Project
<p>Authors: Michael Kidd & Kevin Moran <br>
Lecturer: Damien Costello</p>
Hardware: 4Tronix Initio Car, Myo Armband, Raspberry Pi

### Project Requirements
<hr/>
Due Date: 12th April 2019 (or earlier is acceptable)

Develop an application with a Natural User Interface.  There are a number of options available to you and this is an opportunity to combine a lot of technology that you have worked with over the past four years.

At the very least, this should be a local implementation of the application using gestures to interact with it.  For example, a voice controlled application fits the parameters of gesture based control. You can expand out to include real-world hardware and use this as an opportunity to prove a concept.  The Internet of Things is a common phrase, so you could implement a solution taking advantage of hardware like the Raspberry Pi, using the cloud for data transfer and creating a real-world scenario through this medium.

### Project Overview
<hr/>

We have decided to attempt to control a robotic car with a Myo Armband, this would allow a person to use hard and arm gestures to control a remote vehicle.

For the Project we will need a small vehicle that can connect in some manner to a mini programmable computer such as the raspberry pi.
The vehicle will need to have DC motors and if possible 4 or more wheels, which can be rotated from those motors.

We will be using a raspberry pi with an external power source, such as the batteries attached to the car or another external power pack designed to be used for phones with a micro USB port.

On the Raspberry Pi we will install the Raspbian Operating system, previously I have used a Raspberry Pi with the windows IOT operating system, but found that the Pi struggle somewhat with processing.

Raspbian will allow us to use Python as a programming language and unlike the windows version, can come with a full desktop GUI install.

#### Gestures
* Make a Fist - This will accelerate the vehicle Forward.
* Wave Out (Eg. Stop motion) - This will make the car reverse.
* Rest hand - This will stop the motors, bring the vehicle to a stop but also will reset the box positioning for the Myo Armband.
* Make a fist and move Arm to box position 7 - This will turn the vehicle to the right
* Make a fist and move Arm to box position 3 - This will move the vehicle left.  

#### Video Demonstration

Project Demonstration - Finished Project
[![Youtube Video](https://img.youtube.com/vi/w5ymBcMpCew/maxresdefault.jpg)](https://www.youtube.com/watch?v=w5ymBcMpCew)



<hr/>

#### Installing Raspbian on Raspberry Pi
![Raspbian](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTJKvaSQWW0ItMDx4x1n0Z-0aVbKYBJDhNRvLQCElLF4ZHV__Vjlw)

To get started, you will need a Raspberry pi running some form of Operating System. For our project we used Raspbian, which is a compact Debian derivative designed to be used with small hardware like the Raspberry pi 3.

Download Raspbian OS
[Here](https://www.raspberrypi.org/downloads/raspbian/)

Once you have Raspbian Downloaded, You will need to install it to a micro SD card that can be inserted into the raspberry pi. To do this with windows I used a program called BalenaEtcher, this can also be used with a Linux OS.

#### Installing BalenaEtcher on Windows

Download BalenaEtcher [Here](https://www.balena.io/etcher/)

With BalenaEtcher you can flash an OS straight to an external drive, in our case we used a micro SD that came with the Raspberry Pi.

#### Installing Raspbian on to MicroSD

![blanEtcher](https://user-images.githubusercontent.com/22493191/56132853-f3ab7c80-5f82-11e9-975b-e554f0857125.gif)
Using BalenaEtcher you will first select the image in our case the Raspbian image. Then you will select the drive, for us it was the micro SD card and then finally you click flash. 

#### Setting up Myo with Raspberry Pi
As MyoConnect is designed for Windows to use the Myo with Raspbian (a linux system) we had to find an alternative. We chose  PyoConnect which is a linux alternative to what MyoConnect scripting does for windows. The installation is a simple enough process just follow the steps [here](http://www.fernandocosentino.net/pyoconnect/) and you can start writing code. 

#### Wiring the Car to work with Pi

#### Interface for Light Matrix on Sense Hat

During the project we started by using a sense hat for the raspberry pi which has a 8x8 light matrix. This would show an arrow on the matrix to indicate which gesture the wearer of the Armband was trying to activate.  Example we had the left arrow show when the wearer activate the left gesture. One problem here was that neither motor controller we were using would be replacing the sense hat as there was no way to attach it to the unit while the motor controllers were also attached without adding an adapter of some sort.

#### Issues that occurred during the project

#####  Purchased the incorrect motor controller.

During the project we needed to purchase a motor controller that could run the motors on the vehicle, unfortunately we bought a stepper motor which is more suited to operating motors that operate in phases, such as a walking mechanism or 3d printed that much switch between going forwards and backwards quickly. This did not work with our car as the motors were straight forward DC motors, so hopefully the new motor controller will work. We decide against this project as we are currently working on another project that is using the oculus rift and have only one unit, takes a lot to setup the equipment each time. Can be disorienting over long periods of time, can often become distracting and prevent actual work being done.

#####  Using the light matrix with raspberry pi.

We originally were using the light matrix on the raspberry pi as a testing tool, in place of using the actual vehicle. This worked but later the sense hat stopped responding and was no longer seen by the program.
This may be due to some firmware change, or potentially due to a short in device itself. After looking online for similar issues, there is a possible fix for this issue that resets the EPROM on the chip. As we wont be using this within the final project and the light matrix cannot be affixed to the top of the motor controller, since there are no pins in place to addon hats, we stopped trying to fix the issue.

#####  Adding Atom to the raspberry pi.
We decided to use atom as a compiler due to its ability to code together. It does have windows and Linux support. But due to the fact that our pi is using a arm CPU and the Linux support is only for amd64 architecture. We were unable to install it on the pi. Here is a link to a GitHub account that is trying to create a runnable build for arm it unfortunately doesn't yet have a pi buildable. [Atom for ARM](https://github.com/atom/atom/issues/15881)

<hr/>

### Research

#### Myo Armband
![Myo](https://images.techhive.com/images/article/2015/06/thalmic-labs-myo-armband-100590953-primary.idge.jpg)

##### Installing Myo Armband On Windows
First you will need to download the Myo Installed from the Myo install page [Here](https://support.getmyo.com/hc/en-us/articles/360018409792)
![MyoInstallPage](https://user-images.githubusercontent.com/22493191/54996439-37811680-4fc1-11e9-8041-bdcce471abb8.png)
Then click on Myo Connect for Windows 1.0.1 after it downloads. Double click on the file. Agree to the license agreement and then choose where to install. The default location is okay to use (it will require 137.3mb of free space). Wait for it to install. Make sure that launch Myo Connect is ticked. Then click on finish. You should then see this screen.
![MyoArmbandManger](https://user-images.githubusercontent.com/22493191/54997131-effb8a00-4fc2-11e9-994e-71f5cf0addaa.png)
If you don't or see that Myo is disconnected make sure the Bluetooth dongle is plugged in to a poweredUSB port. Then tap the logo of the MYO armband against the dongle and it should start connecting. When connected you can ping the device and you should feel it vibrate to know its connected.

**Sensors** 	

* Medical grade stainless steel EMG sensors
* Highly sensitive nine-axis IMU containing three-axis gyroscope, three-axis accelerometer, three-axis magnetometer.

* **LEDs** 	- Dual indicator LEDs
* **Processor** -	ARM Cortex M4 processor

* **Haptic Feedback** -	Short, medium, long vibrations

##### Potential Myo Project
Our first idea for using the Myo was to use the device as a fall sensor for elderly people or people with physical disabilities. The idea was based on a par written by Shalom Greene, Himanshu Thapliyal and David Carpenter. Titled [IoT-Based Fall Detection for Smart Home Environments](https://www.researchgate.net/publication/312962914_IoT-Based_Fall_Detection_for_Smart_Home_Environments). It covered the benefits of using IoT devices as fall detector and for contacting emergency services in the event of an accident where the person was unable to respond physically or verbally.

We decided against this because the idea of constantly wearing an armband for an elderly or physically disabled person, could cause health risks with blood flow on that arm for the wearer. The idea may be worth revisiting with a wrist worn sensor as many elderly or disabled people wear them already for emergency purposes.  

#### Xbox Kinect Version 1
![Kinect1](http://jordanpelovitz.com/wp-content/uploads/2015/04/Xbox-360-Kinect-Standalone.png)

**Sensor**
Colour and depth-sensing lenses
Voice microphone array
Tilt motor for sensor adjustment
Fully compatible with existing Xbox 360 consoles

**Field of View**
Horizontal field of view: 57 degrees
Vertical field of view: 43 degrees
Physical tilt range: ± 27 degrees
Depth sensor range: 1.2m - 3.5m

**Data Streams**
320x240 16-bit depth @ 30 frames/sec
640x480 32-bit colour@ 30 frames/sec
16-bit audio @ 16 kHz

**Skeletal Tracking System**
Tracks up to 6 people, including 2 active players
Tracks 20 joints per active player
Ability to map active players to LIVE Avatars

**Audio System**
LIVE party chat and in-game voice chat (requires Xbox LIVE Gold Membership)
Echo cancellation system enhances voice input
Speech recognition in multiple

#### Xbox Kinect Version 2
![Kinect2](https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/Xbox-One-Kinect.jpg/1200px-Xbox-One-Kinect.jpg)
Kinect 2 specs

**Field of View:** 70˚ horizontal by 60˚ vertical<br/>
**Resolvable Depth:** 0.8 m -> 4.0 m<br/>
**Colour Stream:** 1920 x 1080 x 16 bpp 16:9 YUY2 @ 30 fps<br/>
**Depth Stream:** 512 x 424 x 16 bpp, 13-bit depth<br/>
**Infrared Stream:** 512 x 424, 11-bit dynamic range<br/>
**Registration:** Colour <-> depth and active IR<br/>
**Audio Capture:** 4-mic array returning 48K Hz audio<br/>
**Data Path:** USB 3.0<br/>
**Latency:** ~60 ms with processing<br/>
**Tilt Motor:** No tilt motor

##### Potential Kinect and Kinect 2 Project
We looked at using the Kinect as a game controller. The idea was as a controller for an endless runner similar to [this](https://github.com/KatVHarris/GravityInfiniteRunnerUnity5). We decided against it in the end due to the amount of  versions of this that we saw had already being created online.

#### PlayStation Move motion controller
![PSMove](https://a1.amlimg.com/YTE2NjIxMmY4NmFmODc5ZGFhNTU5YmU1ZjRkYWM5MmahFiLVOp7WOJ1JtiqNVPzRaHR0cDovL21lZGlhLmFkc2ltZy5jb20vODg2ZTJlMjI2ZDFmZmZkMGY5M2U1NmYwNTkyMTFkNTE5MTdiODkxY2IyN2RjOGU4OTczMGU1NzVkNjBkODdiMi5qcGd8fHx8fHwzOTZ4MjkyfGh0dHA6Ly93d3cuYWR2ZXJ0cy5pZS9zdGF0aWMvaS93YXRlcm1hcmsucG5nfHx8.jpg)<br/>

**PlayStation® Move motion controller**<br/>
Three-axis gyroscope<br/>
Three-axis accelerometer<br/>
Terrestrial magnetic field sensor<br/>
Colour-changing sphere for PlayStation Eye tracking<br/>
Bluetooth® technology<br/>
Vibration feedback

**PlayStation® Move sub-controller**<br/>
Built-in lithium-ion rechargeable battery<br/>
Bluetooth® technology<br/>
2 DUALSHOCK® or SIXAXIS® Wireless Controller replacement capability.<br/>

**PlayStation® Eye**<br/>
Built-in four-capsule microphone array<br/>
Echo cancellation<br/>
Background noise suppression<br/>

##### Potential Playstation Moves Projects
We could not compose of an idea that would truly be gesture based due to the need to use the move controllers to interact with the PlayStation. We could have used the PlayStation Camera but we didn't have access to one and it would have being largely similar to any project we could build on the Kinect.  

##### Leap motion
![Leap Motion](https://i.nextmedia.com.au/Utils/ImageResizer.ashx?n=http%3A%2F%2Fi.nextmedia.com.au%2FNews%2Fleap-motion-review.jpg&w=600&c=0&s=1)

**Connectivity Technology** wired<br/>
**Interface** USB<br/>
**Accuracy** ± 0.00039 in<br/>
**Performance** 200 reports per second<br/>

##### Potential Leap Projects

One potential project we thought of for the leap motion controller was to interface hand gestures for virtual reality games such as Elite Dangerous, which is a space flight simulator. This game currently uses physical flight controller. Using the leap motion could allow players flight the ship without any controllers and would give a more natural experience.

#### Microsoft HoloLens
![Hololens](https://cdn-images-1.medium.com/max/1600/1*Oltg1ajoJ1Xbs2fK0N644g.jpeg)

**Display** 	See-through holographic lenses (waveguides)
2x HD 16:9 light engines
Automatic pupillary distance calibration
2.3M total light points holographic resolution, 2.5k light points per radian.<br/>
**Sensors** 	Inertial Measurement Unit, 4x environment understanding cameras, mixed reality capture, 4x microphones, ambient light sensor<br/>
**Processor** 	Custom Microsoft Holographic Processing Unit HPU 1.0, Intel 32-bit architecture<br/>
**RAM** 	2GB<br/>
**Storage** 	64GB<br/>
**Weight** 	579g (1.2lbs)<br/>
**Camera** 	2MP photos, HD video<br/>
**Audio** 	External speakers, 3.5mm audio jack<br/>
**Connectivity** 	Wi-Fi 802.11ac, Bluetooth 4.1 LE, Micro-USB 2.0<br/>
**Power** 	2-3 hour active use battery life, 2 weeks standby, passive cooling<br/>
**OS** 	Windows 10 with Windows Store<br/>
**Human Understanding:** spatial sound, gaze tracking, gesture input, voice support<br/>

#### Microsoft HoloLens 2
![Hololens2](https://cdn.uploadvr.com/wp-content/uploads/2019/02/HoloLens-2-MWC-1024x597.jpg)
**Display**

* **Optics:** See-through holographic lenses (waveguides)
* **Resolution:** 2K 3:2 light engines
* **Holographic Density:** >2.5k radiant (light points per radian)
* **Eye-based rendering:** Display optimization for 3D eye position

**Sensors**

* An Azure Kinect sensor to track depth
* An accelerometer, gyroscope, and magnetometer to track body motions
* Camera capable of 8 megapixel photos and 1080p video at 30 frames per second

**Audio & Speech**

* Microphone array: 5 channels
* Speakers: built-in, spatial audio

**Human and Environment Understanding**

* Voice command and control capabilities on-device, natural language processing with internet connectivity
* 6 degrees of freedom tracking: world-scale positional tracking
* Spatial mapping: real-time environment mesh
* Mixed reality capture: mixed hologram and physical environment photos and videos

**Compute & Connectivity**
* Qualcomm Snapdragon 850 Compute Platform
* Microsoft’s proprietary holographic processing unit
* Bluetooth 5.0
* USB-C Charging
<hr/>

##### Potential HoloLens Projects

Fishing training program with HoloLens

Last year as part of a college assignment, I took part in a project to create a UWP program that could be used as a training tool to teach someone how to fly fish by using a fly fishing rod that would have an accelerometer attached to the top of the rod and a raspberry pi attached to the handle of the rod. This would allow the Pi to retrieve the data from the accelerometer and send it over a network and could be visualized in the HoloLens. This would allow the teacher to adapt the training style in a more appropriate way to help the student. the project worked somewhat. The Pi retrieved the data and sent over the network and could be seen in a unity program that could be run in any unity compatible device as long as a compiled build was created. This could be adapted to the HoloLens as a gesture recognition project, where in place of an entire rod, Raspberry pi and accelerometer, the HoloLens could extrapolate the data from the movement that user makes, possibly even go further and monitor the users entire body. This would definitely be a better way to implement that project as there would be less hardware involved and could allow for video playback through the HoloLens cameras. This project could also be done in parts using the Kinect or the leap motion, however it would seem to be a better fit for the HoloLens as the current features of the program also could be implemented.

The reason we haven't chosen this project is due to the level of complexity being very high and less likely to give a result in the short time frame.


### References
[Endless Runner Kinect](https://github.com/KatVHarris/GravityInfiniteRunnerUnity5)<br>
[Titled IoT-Based Fall Detection for Smart Home Environments](https://www.researchgate.net/publication/312962914_IoT-Based_Fall_Detection_for_Smart_Home_Environments)<br>
[PyoConnect](http://www.fernandocosentino.net/pyoconnect/)<br>
