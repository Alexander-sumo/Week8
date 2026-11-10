from machine import ADC, Pin
from time import sleep
adc = ADC(Pin(34))
adc.atten(ADC.ATTN_11DB)
DARK = 1800        
BRIGHT = 52000     
def light_pct(raw):
    pct = (raw - DARK) / (BRIGHT - DARK) * 100
    return max(0, min(100, pct))
def read_avg(adc, n=16):
    total = 0
    for _ in range(n):
        total += adc.read_u16()
    return total // n
while True:
    raw = adc.read_u16()
    volts = raw / 65535 * 3.3
    print(f"raw={raw:5d}   v={volts:.2f}")
    sleep(0.2)
