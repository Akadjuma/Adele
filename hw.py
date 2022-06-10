#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
from flask import Flask, request
import threading

rospy.init_node('pub_node')
pub = rospy.Publisher('/my_topic', String, queue_size=10)
rate = rospy.Rate(10)


app = Flask(__name__)

@app.route('/alice', methods=['POST'])

def resp():
    text = request.json.get('request', {}).get('command')
    response_text = f'вы сказали, {text}'
    pub.publish("You said " + text)
    rate.sleep()
    response = {
        'response':{'text': response_text,'end_session': False},'version': '1.0'}
    return response
    
app.run('0.0.0.0', port=5000, debug=True)
        

        
        