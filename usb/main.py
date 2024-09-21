import select
import sys
import time

import config
import ringController

poll_obj = select.poll()
poll_obj.register(sys.stdin, select.POLLIN)

while True:
    poll_results = poll_obj.poll(1)
    if poll_results:
        txt = sys.stdin.readline().strip()
        x = txt.split("#")
        data = x[0]
        count = x[1]
        if data == 'red':
            ringController.set_color(config.blank,config.led_count)
            ringController.set_color(config.red,count)
        elif data == 'green':
            ringController.set_color(config.blank,config.led_count)
            ringController.set_color(config.green,count)
        elif data == 'blue':
            ringController.set_color(config.blank,config.led_count)
            ringController.set_color(config.blue,count)
        elif data == 'yellow':
            ringController.set_color(config.blank,config.led_count)
            ringController.set_color(config.yellow,count)
        elif data == 'pink':
            ringController.set_color(config.blank,config.led_count)
            ringController.set_color(config.pink,count)
        elif data == 'cyan':
            ringController.set_color(config.blank,config.led_count)
            ringController.set_color(config.cyan,count)
        elif data == 'purple':
            ringController.set_color(config.blank,config.led_count)
            ringController.set_color(config.purple,count)
        elif data == 'white':
            ringController.set_color(config.blank,config.led_count)
            ringController.set_color(config.white,count)
        elif data == 'orange':
            ringController.set_color(config.blank,config.led_count)
            ringController.set_color(config.orange,count)
        else:
            ringController.set_color(config.blank,config.led_count)
    else:
        continue