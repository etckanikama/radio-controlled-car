import RPi.GPIO as GPIO
from time import sleep

L_vref = 16
L_in1 = 20
L_in2 = 21

R_vref = 13
R_in1 = 19
R_in2 = 26

motor_ports = [
    [L_in1,L_in2,L_vref],
    [R_in1,R_in2,R_vref]
]

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False) 
for ports in motor_ports:
    GPIO.setup(ports, GPIO.OUT)


# function motor 
def set_motor(pno,job):
    ta_switch = [
        [0,0], #stop
        [1,0], #cw
        [0,1] #ccw
    ]
    ports = motor_ports[pno]
    sw = ta_switch[job]
    GPIO.output(ports[0], sw[0])
    GPIO.output(ports[1], sw[1])

# operate both motor 
def set_motor2(job):
    set_motor(0, job)
    set_motor(1, job)

# roll speed
pwm_l = GPIO.PWM(L_vref, 1000)
pwm_r = GPIO.PWM(R_vref, 1000)
pwm_l.start(100)
pwm_r.start(100)

if __name__ == "__main__":
    try:
        while True:
            set_motor2(1)
            sleep(1.5)
            set_motor2(2)
            sleep(1.5)
            set_motor2(0)
            sleep(1.5)
    except KeyboardInterrupt:
        pass
    GPIO.cleanup()
