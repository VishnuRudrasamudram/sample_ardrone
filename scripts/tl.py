#ROS Libraries
import rospy
import roslib; roslib.load_manifest('sample_ardrone')


from std_msgs.msg import Empty
from ardrone_autonomy.msg import Navdata

if __name__=='__main__':
	rospy.init_node('sample_node',anonymous = 'True')
	pubTakeoff = rospy.Publisher('/ardrone/takeoff',Empty)
	pubLand = rospy.Publisher('/ardrone/land',Empty)
	
	rospy.sleep(1)
	pubTakeoff.publish(Empty())
	rospy.sleep(10)
	pubLand.publish(Empty())
