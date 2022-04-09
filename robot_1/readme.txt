How to run the package

    • Install your package in the catkin_ws/src of your workspace
      
    • Make sure you have all the dependencies like python3, ros noetic and gazebo environment
      
    •  Run catkin_make clean && catkin_make in the catkin_ws folder followed by 
       source ~/catkin_ws/devel.setup.bash

    • To perform Teleop, run the following command in the catkin_ws

	roslaunch robot_1 template_launch.launch
	
 	This will launch the robot in gazebo environment

      Now go to catkin_ws/src/robot_1 folder on the command prompt and run the following command
      
      python3 teleop_template.py 

    • To run robot on a predefined path , run the following command in the catkin_ws
      
      roslaunch robot_1 template_launch.launch
      
      This will launch the robot in gazebo environment
      
      Now go to catkin_ws/src/robot_1 folder on the command prompt and run the following command
      
      python3 publisher.py 
      	
