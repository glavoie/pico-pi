from machine import Pin, PWM
import time
import _thread

DUTY_ON = 16383
DUTY_OFF = 0

# In microseconds (us)
START_LEN = 2400
ONE_LEN = 1200
ZERO_LEN = 600
OFF_LEN = 600
TOTAL_CODE_LEN = 45000
SLEEP_ADJUST = -30 # Updating the PWM duty cycle takes ~30 us

pwm = PWM(Pin(13))

# Carrier frequency
pwm.freq(40000)

# SONY 12 bits codes
HARDWARE_TYPE = (1, 0, 0, 0, 0) # TV

POWER = (1, 0, 1, 0, 1, 0, 0) + HARDWARE_TYPE
CHANNEL_UP = (0, 0, 0, 0, 1, 0, 0) + HARDWARE_TYPE
CHANNEL_DOWN = (1, 0, 0, 0, 1, 0, 0) + HARDWARE_TYPE

TV = (0, 0, 1, 0, 0, 1, 0) + HARDWARE_TYPE

# SONY 15 bits codes
HDMI_1 = (0, 1, 0, 1, 1, 0, 1) + (0, 1, 0, 1, 1, 0, 0, 0)
HDMI_2 = (1, 1, 0, 1, 1, 0, 1) + (0, 1, 0, 1, 1, 0, 0, 0)
HDMI_3 = (0, 0, 1, 1, 1, 0, 1) + (0, 1, 0, 1, 1, 0, 0, 0)


def send_code(code):
    for i in range(3):
        code_length = 0

        # Sending START pulse
        code_length += send_signal(DUTY_ON, START_LEN)
        code_length += send_signal(DUTY_OFF, OFF_LEN)

        # Sending command
        for i in range(len(code)):
            code_length += send_signal(DUTY_ON, ONE_LEN if code[i] == 1 else ZERO_LEN)
            code_length += send_signal(DUTY_OFF, OFF_LEN)

        # Total code length == 45ms
        time.sleep_us(TOTAL_CODE_LEN - code_length)

def send_signal(signal, length):
    length += SLEEP_ADJUST
    pwm.duty_u16(signal)
    time.sleep_us(length)

    return length

send_code(TV)

print("Signal sent")