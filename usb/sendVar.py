import serial
from sys import argv

## python sendVar.py COM4 red 12
## argv[1] : com port that device connects through
## argv[2] : color for LEDs (red/green/blue/yellow/pink/cyan/purple/white/orange/blank)
## argv[3] : number of LEDs to light

def main():
    s = serial.Serial(port=argv[1], parity=serial.PARITY_EVEN, stopbits=serial.STOPBITS_ONE, timeout=1)
    s.flush()
    
    s.write(f'{argv[2]}#{argv[3]}\r'.encode())
    mes = s.read_until().strip()

if __name__ == "__main__":
    main()