#!/usr/bin/env python3

import rospy

from turtle_regulation_kritika_yassir.srv import setWaypointService, setWaypointServiceResponse

def test_srv(request):
	return setWaypointServiceReponse(True)


rospy.init_node('test_service')

srv = rospy.Service('srv_test', setWaypointService, test_srv)

rospy.spin()
