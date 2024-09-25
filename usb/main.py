import select, sys, time

import config, ringController

poll_obj = select.poll()
poll_obj.register(sys.stdin, select.POLLIN)

while True:
    poll_results = poll_obj.poll(1)
    if poll_results:
        # Split input
        txt = sys.stdin.readline().strip()
        x = txt.split("#")
        
        # Set Color
        data = x[0]
        if data == 'red':
            color = config.red
        elif data == 'green':
            color = config.green
        elif data == 'blue':
            color = config.blue
        elif data == 'yellow':
            color = config.yellow
        elif data == 'pink':
            color = config.pink
        elif data == 'cyan':
            color = config.cyan
        elif data == 'purple':
            color = config.purple
        elif data == 'white':
            color = config.white
        elif data == 'orange':
            color = config.orange
        else:
            color = config.blank
        
        # Set LED co
        count = int(x[1])
        if count > config.led_count:
            count = config.led_count
            
        ringController.set_color(config.blank,config.led_count)
        ringController.set_color(color,count)
    else:
        continue