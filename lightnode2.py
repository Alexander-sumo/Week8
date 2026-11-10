from machine import ADC, Pin, PWM
from time import sleep

adc = ADC(Pin(34))
adc.atten(ADC.ATTN_11DB)

pwm = PWM(Pin(25), freq=1000)

while True:
    raw = adc.read_u16()
    pwm.duty_u16(raw)
    
    # Convert raw 16-bit value (0-65535) to approximate voltage (0-3.3V)
    voltage = (raw / 65535) * 3.3
    
    # Print to the shell
    print(f"Raw: {raw} | Voltage: {voltage:.2f}V")
    
    sleep(0.05)
