import time, array, rp2
from machine import Pin
import config

############################################
# RP2040 setup
############################################
@rp2.asm_pio(sideset_init=rp2.PIO.OUT_LOW, out_shiftdir=rp2.PIO.SHIFT_LEFT,
             autopull=True, pull_thresh=24) # PIO configuration

def ws2812():
    T1 = 2
    T2 = 5
    T3 = 3
    wrap_target()
    label("bitloop")
    out(x, 1)               .side(0)    [T3 - 1]
    jmp(not_x, "do_zero")   .side(1)    [T1 - 1]
    jmp("bitloop")          .side(1)    [T2 - 1]
    label("do_zero")
    nop()                   .side(0)    [T2 - 1]
    wrap()
    
sm = rp2.StateMachine(0, ws2812, freq=8_000_000, sideset_base=Pin(config.PIN_NUM))
sm.active(1)

ar = array.array("I", [0 for _ in range(config.led_count)])

############################################
# Functions for RGB Coloring
############################################
#
def pixels_show(brightness_input=config.brightness):
    dimmer_ar = array.array("I", [0 for _ in range(config.led_count)])
    for ii,cc in enumerate(ar):
        r = int(((cc >> 8) & 0xFF) * brightness_input) # 8-bit red dimmed to brightness
        g = int(((cc >> 16) & 0xFF) * brightness_input) # 8-bit green dimmed to brightness
        b = int((cc & 0xFF) * brightness_input) # 8-bit blue dimmed to brightness
        dimmer_ar[ii] = (g<<16) + (r<<8) + b # 24-bit color dimmed to brightness
    sm.put(dimmer_ar, 8) # update the state machine with new colors
    time.sleep_ms(10)

def pixels_set(i, color):
    ar[i] = (color[1]<<16) + (color[0]<<8) + color[2]
   
def set_color(color,count):
    for jj in range(int(count)):
        pixels_set(jj, color)
    pixels_show(1)
    
def blink(count, color):
    for _ in range(count):
        set_color(color)
        time.sleep(0.2)
        set_color(config.blank)
        time.sleep(0.2)

############################################