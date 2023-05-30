#!/usr/bin/env python3

import rospy
from turtlesim.msg import Pose
from std_msgs.msg import String, Bool
from geometry_msgs.msg import Twist

from turtle_regulation_kritika_yassir.srv import setWaypointService, setWaypointServiceRequest

import math



# Variable globale pour stocker la pose de la tortue
turtle_pose = Pose()

kpl = 1.0
distance_tolerance = 0.2

def change_waypoint(request):
	waypoint = request
	return setWaypointServiceResponse(True)

def pose_callback(data):
    	# Mettre à jour la variable globale avec la pose de la tortue
	global turtle_pose
	turtle_pose = data


def main():
    	# Initialiser le nœud ROS
	rospy.init_node('set_way_point')

    	# Souscrire au topic "pose" et définir la fonction de rappel
	rospy.Subscriber('/turtle1/pose', Pose, pose_callback)

    	# Publier la commande cmd_vel avec la vitesse angulaire en z
	cmd_vel_pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

	is_moving = Bool()
	cmd_vel_msg = Twist()
	#cmd_vel_msg.angular.z = u

	#cmd_vel_msg.linear.x = 3


	is_moving.data = True

	moving_pub = rospy.Publisher('is_moving', Bool, queue_size=1)
	srv = rospy.Service('set_waypoint_srv', setWaypointService, change_waypoint)


	moving_pub.publish(is_moving)

	global waypoint
	waypoint  = Pose()
	waypoint.x = 7
	waypoint.y = 7

	err_lin = 0

	while not rospy.is_shutdown():

		if is_moving.data == True:
			# Calculer l'angle désiré
			theta_desired = math.atan2(waypoint.y - turtle_pose.y, waypoint.x - turtle_pose.x)
			eu_dist  = math.sqrt(math.pow(waypoint.y - turtle_pose.y,2) + math.pow(waypoint.x - turtle_pose.x,2))
			err_lin  = kpl * eu_dist


			# Calculer l'erreur en cap
			theta = turtle_pose.theta
			e = math.atan(math.tan(theta_desired - theta))

   			# Définir la constante proportionnelle Kp
			Kp = 1.0

   			# Calculer la commande en cap
			u = Kp * e
			cmd_vel_msg.angular.z = u
			cmd_vel_msg.linear.x = err_lin
			print(err_lin)
		else:
			cmd_vel_msg = 0


		if  err_lin >  distance_tolerance:
			cmd_vel_pub.publish(cmd_vel_msg)
		else:
			is_moving.data = False
			moving_pub.publish(is_moving)
			print(f"past tolerance! {err_lin}")

def calcDesiredAngle(pointA:tuple, pointB:tuple) -> float:
	xA = pointA[0]
	yA = pointA[1]

	xB = pointB[0]
	yB = pointB[1]

	return math.atan2(yB - yA, xB - xA)


if __name__ == '__main__':
	 main()

