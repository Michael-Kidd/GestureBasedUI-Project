# Gesture Based UI Project

<p>Authors: Michael Kidd & Kevin Moran<br>
Lecturer: Damien Costello</p>

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
![Pi](https://images-na.ssl-images-amazon.com/images/I/91zSu44%2B34L._SX466_.jpg "Raspberry Pi")

###### Myo Armband
![Myo](https://images.techhive.com/images/article/2015/06/thalmic-labs-myo-armband-100590953-primary.idge.jpg "Myo Armband")

###### 4Tronix Initio Car
![Car](https://cdn.shopify.com/s/files/1/0271/0223/products/initio_03b_1024x1024.jpg?v=1502448974 "Initio Car")

<hr/>

#### Installing Raspbian on Raspberry Pi
![Raspbian](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTJKvaSQWW0ItMDx4x1n0Z-0aVbKYBJDhNRvLQCElLF4ZHV__Vjlw "Raspbian")

#### Setting up Myo with Raspberry Pi

#### Myo Interface in Python

#### Wiring the Car to work with Pi

#### Interface to Operate the Car

#### Interface for Light Matrix on Sense Hat

#### Issues that occured during the project
<hr/>

### Research
