import rclpy
from rclpy.node import Node
from autopatol_interfaces.srv import SpeechText
import espeakng

class Speaker(Node):
    def __init__(self,node_name):
        super().__init__(node_name)
        self.speech_service_ = self.create_service(SpeechText,'speech_text',self.speech_text_callback)
        self.speaker_ = espeakng.Speaker()
        # espeak-ng 1.50 起普通话的语音名由 zh 改为 cmn
        self.speaker_.voice = 'cmn'

    def speech_text_callback(self,request,response):
        self.get_logger().info(f'正在准备朗读{request.text}') 
        self.speaker_.say(request.text)
        self.speaker_.wait()
        response.result = True
        return response

def main():
    rclpy.init()
    node = Speaker('speaker')
    rclpy.spin(node)
    rclpy.shutdown()    
