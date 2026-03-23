# PythonSerialReader

A Python script that reads data from an Arduino's serial port and logs it —
a workaround for macOS not supporting the DataStreamer add-in for Excel.

---

## Requirements

- Python 3 installed ([download here](https://www.python.org/downloads/))
- `pyserial` library installed
- Arduino connected via USB

---

## Setup

### 1. Install the pyserial library
Open Terminal and run:
```bash
pip install pyserial
```

### 2. Find your Arduino's port name
In Terminal, run:
```bash
ls /dev/tty.*
```
Look for something like `/dev/tty.usbmodem14101` — that's your Arduino.

### 3. Update the port name in the script
Open `SerialReader.py` and find this line:
```python
port = '/dev/tty.usbmodem14101'
```
Replace it with the port name you found in Step 2.

---

## Running the Script

1. Open Terminal
2. Navigate to the folder containing `SerialReader.py`:
```bash
cd path/to/your/folder
```
> **Tip:** You can drag the folder from Finder into Terminal to auto-fill the path.

3. Run the script:
```bash
python3 SerialReader.py
```

---

## Troubleshooting

| Problem | Fix |
|--------|-----|
| `No such file or directory` | Double-check the port name with `ls /dev/tty.*` |
| `ModuleNotFoundError: pyserial` | Run `pip install pyserial` in Terminal |
| No data showing | Make sure the Arduino is plugged in and running a sketch |
| Wrong baud rate | Match the baud rate in the script to the one in your Arduino sketch |