# Gesture Based UI Project
<p>Authors: Michael Kidd & Kevin Moran<br>
Lecturer: Damien Costello</p>
Test Commit
Test Edit Number 2
### Project Requirements
<hr/>
Due Date: 12th April 2019 (or earlier is acceptable)

Develop an application with a Natural User Interface.  There are a number of options available to you and this is an opportunity to combine a lot of technology that you have worked with over the past four years.

At the very least, this should be a local implementation of the application using gestures to interact with it.  For example, a voice controlled application fits the parameters of gesture based control. You can expand out to include real-world hardware and use this as an opportunity to prove a concept.  The Internet of Things is a common phrase, so you could implement a solution taking advantage of hardware like the Raspberry Pi, using the cloudfor data transfer and creating a real-world scenario through this medium.

  You can reproducea classic game or system using a gesture-based interface.  For example, a platformer game or a navigation application using Kinect or voice control.  Maybe Tetris using the Myo armbands to control the blocks, or Flappy Bird using the Kinect as the controller.  Applications with multiple users are also acceptable.Voice control applications need to be more complex and achieve something.  Creating a skill in Alexa for the sake of creating a skill is not enough.  You need to take the application further than this.  You could, for example, implement a simple learning mechanism that will build a conversational skill as time progresses and demonstrate this.  You could use the voice control to progress through a game or achieve a task.  If you are doing this, then you need to distinguish the code you write from the samples available.The programming language is your choice.

#### Hardware available
  * (9) Myo Armbands
  * (2) Leap Motion Controllers,
  * (2) Kinect V2,
  * (2) Hololens,
  * (6) Durovis Dive which are similar to Google Cardboard
  * Raspberry Pi, Arduino,
  * Lego Mindstorms
  * (open to you)Other stuff you may have.........

#### Requirements
Write up the project under the following headings including all references as evidence of your research.Purpose of the application–design of the application including the screens of the user interface and how it works.  The application can be an experimentation process for you, testing how pieces of hardware could interact or be combined with gestures.  

You don’t have to solve the world economic crisis just yet.  Gestures identified as appropriate for this application–consider how gestures can be incorporated into the application, providinga justification for the ones that you pick.

 This is an important research element for the project and needs to explain how the gestures fit into the solution you are creating.Hardware used in creating the application–You are not limited to the hardware listed above.  If you have your own hardware, or hardware simulator that you wish to use, then feel free.  The purpose of each piece of hardware should be given with a comparison to other options available.Architecture for the solution–the full architecture for the solution, including the class diagrams, any data models, communications and distributed elements that you are creating.

 The architecture must make sense when the gestures and the hardware are combined. Justification is necessary in the documentation for this.You need to include a list of relevant libraries that you used in the project.Conclusions & Recommendations–Conclusions are what you have learned from this project and the associated research.  Recommendations are what you would do differently if you were to undertake the project again.  The Reflective Piece–what I learned and “enjoyed”! This gives scope for a critical evaluation of the project and the objective that you tried to achieve

### Project Overview
<hr/>


We have decided to Attempt to control a robotic car with a Myo Armband, this would allow a person to use hard and arm gestures to control a remote vehicle.

For the Project we will need a small vehicle that can connect in some manner to a mini programmable computer such as the raspberry pi.
The vehicle will need to have DC motors and if possible 4 or more wheels, which can be rotated from those motors.

We will be using a raspberry pi with an external power source, such as the batteries attached to the car or another extenal power pack designed to be used for phones with a micro USB port.

On the Raspberry Pi we will install the Raspbian Operating system, Previously I have used a Raspberry Pi with the windows IOT operating system, but found that the Pi struggle somewhat with processing.

Raspbian will allow us to use Python as a programming language and unlike the windows version, can come with a full desktop GUI install.

#### Gestures
* Make a Fist - This will accelerate the vehcile Forward.
* Wave Out (Eg. Stop motion) - This will make the car reverse.
* Rest hand - This will stop the motors, bring the vehicle to a stop but also will reset the box positioning for the Myo Armaband.
* Make a fist and move Arm to box position 7 - This will turn the vechicle to the right
* Make a fist and move Arm to box position 3 - This will move the vehicle left.  

#### Video Demonstration

Project Demonstration - Finished Project
[![Youtube Video](https://static-news.moneycontrol.com/static-mcnews/2018/09/youtube-770x433.jpg)](http://example.net/)

Other Video
[![Youtube Video](https://static-news.moneycontrol.com/static-mcnews/2018/09/youtube-770x433.jpg)](http://example.net/)

#### Hardware Used

###### Raspberry Pi
![Pi](https://images-na.ssl-images-amazon.com/images/I/91zSu44%2B34L._SX466_.jpg)

###### Myo Armband
![Myo](https://images.techhive.com/images/article/2015/06/thalmic-labs-myo-armband-100590953-primary.idge.jpg)

**Sensors** 	

* Medical grade stainless steel EMG sensors
* Highly sensitive nine-axis IMU containing three-axis gyroscope, three-axis accelerometer, three-axis magnetometer.

* **LEDs** 	- Dual indicator LEDs
* **Processor** -	ARM Cortex M4 processor

* **Haptic Feedback** -	Short, medium, long vibrations


###### 4Tronix Initio Car
![Car](https://cdn.shopify.com/s/files/1/0271/0223/products/initio_03b_1024x1024.jpg?v=1502448974 v =200x)

<hr/>

#### Installing Raspbian on Raspberry Pi
![Raspbian](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTJKvaSQWW0ItMDx4x1n0Z-0aVbKYBJDhNRvLQCElLF4ZHV__Vjlw)

To get started, you will need a Raspberry pi running some form of Operating System. For our project we used Raspbian, which is a compact Debian derivative designed to be used with small hardware like the Raspberry pi 3.

Download Rasbian OS
[Here](https://www.raspberrypi.org/downloads/raspbian/)

Once you have Rasbian Downloaded, You will need to install it to a micro SD card that can be inserted into the raspberry pi. To do this with windows I used a program called BelenaEtcher, this can also be used with a Linux OS.

Download BalenaEtcher [Here](https://www.balena.io/etcher/)

With BalenaEtcher you can flash an OS straight to an external drive, in our case we used a mirco SD that came with the Rapberry Pi.



#### Setting up Myo with Raspberry Pi

#### Myo Interface in Python

#### Wiring the Car to work with Pi

#### Interface to Operate the Car

#### Interface for Light Matrix on Sense Hat

#### Issues that occured during the project
#####  Adding Atom to the rasperry pi. 
We decided to use atom as a compiler due to its ability to code together. It does have windows and linux support. But due to the fact that our pi is using a armhf and the linux support is only for amd64 architecture. We were unable to install it on the pi. Here is a link to a github account thaat is trying to create a runnable build for arm it unfortunatley doesnt yet have a pi buildable. [Atom for ARM] https://github.com/atom/atom/issues/15881


<hr/>

### Research

#### Myo Armband
![Myo](https://images.techhive.com/images/article/2015/06/thalmic-labs-myo-armband-100590953-primary.idge.jpg)

##### Installing Myo Armband On Windows
First you will need to download the Myo Installed from the Myo install page [Here](https://support.getmyo.com/hc/en-us/articles/360018409792) 
![MyoInstallPage](https://user-images.githubusercontent.com/22493191/54996439-37811680-4fc1-11e9-8041-bdcce471abb8.png)
Then click on Myo Connect for Windows 1.0.1 after it downloads. Double click on the file. Agree to the license agreement and then choose where to install. The default location is okay to use (it will require 137.3mb of free space). Wait for it to install. Make sure that launch Myo Connect is ticked. Then click on finish. You should then see this screen. 
![MyoArmbandManger](https://user-images.githubusercontent.com/22493191/54997131-effb8a00-4fc2-11e9-994e-71f5cf0addaa.png) 
If you dont or see that Myo is diconnected make sure the bluetooth dongle is plugged in to a powered usb port. Then tap the logo of the myo armband against the dongle and it should start connecting. When connected you can ping the device and you should feel it vibrate to know its connected. 

**Sensors** 	

* Medical grade stainless steel EMG sensors
* Highly sensitive nine-axis IMU containing three-axis gyroscope, three-axis accelerometer, three-axis magnetometer.

* **LEDs** 	- Dual indicator LEDs
* **Processor** -	ARM Cortex M4 processor

* **Haptic Feedback** -	Short, medium, long vibrations

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

#### PlayStation Move motion controller
![PSMove](https://a1.amlimg.com/YTE2NjIxMmY4NmFmODc5ZGFhNTU5YmU1ZjRkYWM5MmahFiLVOp7WOJ1JtiqNVPzRaHR0cDovL21lZGlhLmFkc2ltZy5jb20vODg2ZTJlMjI2ZDFmZmZkMGY5M2U1NmYwNTkyMTFkNTE5MTdiODkxY2IyN2RjOGU4OTczMGU1NzVkNjBkODdiMi5qcGd8fHx8fHwzOTZ4MjkyfGh0dHA6Ly93d3cuYWR2ZXJ0cy5pZS9zdGF0aWMvaS93YXRlcm1hcmsucG5nfHx8.jpg)<br/>
**PlayStation®Move motion controller**<br/>
Three-axis gyroscope<br/>
Three-axis accelerometer<br/>
Terrestrial megnetic field sensor<br/>
Colour-changing sphere for Playstation Eye tracking<br/>
Bluetooth® technology<br/>
Vibration feedback

**PlayStation®Move sub-controller**<br/>
Built-in lithium-ion rechargeable battery<br/>
Bluetooth® technology<br/>
2 DUALSHOCK® or SIXAXIS® Wireless Controller replacement capability.<br/>

**PlayStation® Eye**<br/>
Built-in four-capsule microphone array<br/>
Echo cancellation<br/>
Background noise suppression<br/>

##### Leap motion
![Leap Motion](https://i.nextmedia.com.au/Utils/ImageResizer.ashx?n=http%3A%2F%2Fi.nextmedia.com.au%2FNews%2Fleap-motion-review.jpg&w=600&c=0&s=1)

**Connectivity Technology** wired<br/>
**Interface** USB<br/>
**Accuracy** ± 0.00039 in<br/>
**Performance** 200 reports per second<br/>


#### Microsoft Hololens
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

#### Microsoft Hololens 2
![Hololens2](https://cdn.uploadvr.com/wp-content/uploads/2019/02/HoloLens-2-MWC-1024x597.jpg)
**Display**

* **Optics:** See-through holographic lenses (waveguides)
* **Resolution:** 2K 3:2 light engines
* **Holographic Density:** >2.5k radiants (light points per radian)
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
* BlueTooth 5.0
* USB-C Charging
<hr/>
### References
