import RPi.GPIO as GPIO
import time

# Pin configuration
ENA = 18  # PWM for Motor A
ENB = 12  # PWM for Motor B
IN1 = 23  # Motor A direction
IN2 = 24  # Motor A direction
IN3 = 25  # Motor B direction
IN4 = 8   # Motor B direction

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup([ENA, ENB, IN1, IN2, IN3, IN4], GPIO.OUT)

# Set up PWM
pwm_A = GPIO.PWM(ENA, 1000)  # 1 kHz frequency
pwm_B = GPIO.PWM(ENB, 1000)

pwm_A.start(0)  # Start PWM with 0% duty cycle (off)
pwm_B.start(0)

def set_motor_a(direction, speed):
    # Left motor
    if direction == "forward":
        GPIO.output(IN1, GPIO.LOW)
        GPIO.output(IN2, GPIO.HIGH)
    elif direction == "backward":
        GPIO.output(IN1, GPIO.HIGH)
        GPIO.output(IN2, GPIO.LOW)
    pwm_A.ChangeDutyCycle(speed)

def set_motor_b(direction, speed):
    # Right motor
    if direction == "forward":
        GPIO.output(IN3, GPIO.LOW)
        GPIO.output(IN4, GPIO.HIGH)
    elif direction == "backward":
        GPIO.output(IN3, GPIO.HIGH)
        GPIO.output(IN4, GPIO.LOW)
    pwm_B.ChangeDutyCycle(speed)

def stop_motors():
    """Stops both motors."""
    pwm_A.ChangeDutyCycle(0)
    pwm_B.ChangeDutyCycle(0)
    time.sleep(1)

# Example Usage
try:
    print("Motors running at max speed...")

    set_motor_a("forward", 100)  # Max speed (100%)
    set_motor_b("forward", 100)  # Max speed (100%)
    time.sleep(2)
    stop_motors()
    print("backwards at max speed?")
    set_motor_a("backward", 100)  # Max speed (100%)
    set_motor_b("backward", 100)  # Max speed (100%)
    time.sleep(2)
    stop_motors()
    print("Turn one")
    set_motor_a("forward", 100)  # Max speed (100%)
    set_motor_b("backward", 100)  # Max speed (100%)
    time.sleep(2)
    stop_motors()
    print("Turn two")
    set_motor_a("backward", 100)  # Max speed (100%)
    set_motor_b("forward", 100)  # Max speed (100%)
    time.sleep(2)

    # Stop motors
    stop_motors()

except KeyboardInterrupt:
    print("Stopping motors...")

finally:
    print("Cleaning up GPIO...")

    # Clean up GPIO pins
    GPIO.cleanup

