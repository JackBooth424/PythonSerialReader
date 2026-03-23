import serial
import csv
from datetime import datetime
import time

PORT = '/dev/cu.usbserial-0001'
BAUD = 4800
OUTPUT_FILE = 'temperature_log.csv'

def open_port():
    ser = serial.Serial()
    ser.port = PORT
    ser.baudrate = BAUD
    ser.timeout = 3
    ser.dtr = False
    ser.rts = False
    ser.open()
    time.sleep(3)
    ser.reset_input_buffer()
    return ser

with open(OUTPUT_FILE, 'a', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['timestamp', 'temperature_c'])

    ser = open_port()
    print("Ready\n")

    while True:
        try:
            raw = ser.readline()
            line = raw.decode('utf-8').strip()
            if line:
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                writer.writerow([timestamp, line])
                csvfile.flush()
                print(f"✅ {timestamp} — {line}°C")

        except KeyboardInterrupt:
            print("\nLogging stopped.")
            ser.close()
            break

        except serial.SerialException:
            print("⚠️ Connection dropped, reconnecting...")
            try:
                ser.close()
            except:
                pass
            time.sleep(2)
            ser = open_port()

        except ValueError:
            pass
