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
    """Controls Motor A (left motor)."""
    GPIO.output(IN1, GPIO.HIGH if direction == "forward" else GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW if direction == "forward" else GPIO.HIGH)
    pwm_A.ChangeDutyCycle(speed)  # Set speed (0-100)

def set_motor_b(direction, speed):
    """Controls Motor B (right motor)."""
    GPIO.output(IN3, GPIO.HIGH if direction == "forward" else GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW if direction == "forward" else GPIO.HIGH)
    pwm_B.ChangeDutyCycle(speed)  # Set speed (0-100)

def stop_motors():
    """Stops both motors."""
    pwm_A.ChangeDutyCycle(0)
    pwm_B.ChangeDutyCycle(0)

# Example Usage
try:
    print("Motors running...")
    
    # Move forward at 50% speed
    set_motor_a("forward", 100)
    set_motor_b("forward", 100)
    time.sleep(2)

    # Move backward at 75% speed
    set_motor_a("forward", 100)
    set_motor_b("forward", 100)
    time.sleep(2)

    # Stop
    stop_motors()

except KeyboardInterrupt:
    print("Stopping motors...")

finally:
    print("Cleaning up GPIO...")
    stop_motors()
    pwm_A.stop()  # Stop PWM before cleanup
    pwm_B.stop()
    GPIO.cleanup()
