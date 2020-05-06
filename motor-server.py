from http.server import HTTPServer,  BaseHTTPRequestHandler
import motor
import RPi.GPIO as GPIO

class MotorSeverHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        path = self.path
        print('path = {}'.format(self.path))
        body = "ok"
        if path == "/":
            html_f = open("motor-client.html", encoding='utf-8')
            body = html_f.read()
            html_f.close()
        if path == "/forward":
            motor.set_motor2(2) # import motor.py
        elif path == "/back":
            motor.set_motor2(1)
        elif path == "/left":
            motor.set_motor(0,1)
            motor.set_motor(1,0)  
        elif path == "/right":
            motor.set_motor(0,0)
            motor.set_motor(1,1)            
        elif path == "/stop":
            motor.set_motor2(0)
        else:
            print("Unoknown command....")
        self.send_response(200)
        self.send_header('Content-Type', 'text/html;charset=utf-8')
        self.end_headers()
        self.wfile.write(body.encode('utf-8'))
try:
    # start server
    port = ('', 8000)
    httpd = HTTPServer(port, MotorSeverHandler)
    print("Start Server...")
    httpd.serve_forever()
except KeyboardInterrupt:
    pass
httpd.socket.close()
GPIO.cleanup()


