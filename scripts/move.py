import rospy
import roslib; roslib.load_manifest('sample_python')
from std_msgs.msg import Empty
from geometry_msgs.msg import Twist, Vector3

if __name__ == '__main__':
    rospy.init_node('example_node', anonymous=True)
    
    # publish commands (send to quadrotor)
    pub_velocity = rospy.Publisher('/cmd_vel', Twist)
    pub_takeoff = rospy.Publisher('/ardrone/takeoff', Empty)
    pub_land = rospy.Publisher('/ardrone/land', Empty)
    pub_reset = rospy.Publisher('/ardrone/reset', Empty)
    rospy.sleep(1.0) 
    pub_takeoff.publish(Empty())   #take off 
    rospy.sleep(5.0)

    pub_velocity.publish(Twist(Vector3(0.05,0,0),Vector3(0,0,0))) #fly forward
    rospy.sleep(2.0)

    pub_velocity.publish(Twist(Vector3(0,0,0),Vector3(0,0,1)))    #yaw
    rospy.sleep(2.0)
    
    pub_velocity.publish(Twist(Vector3(0.05,0,0),Vector3(0,0,0))) #fly forward
    rospy.sleep(2.0)
	
    pub_velocity.publish(Twist(Vector3(0,0,0),Vector3(0,0,0)))	  #stop
    rospy.sleep(5.0)
    
    pub_land.publish(Empty())			#land
    
