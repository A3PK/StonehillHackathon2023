import serial

# Open the serial port for communication with the Arduino
ser = serial.Serial('COM3', 9600)

# Define a list of authorized RFID tags
authorized_tags = ['AA:BB:CC:DD', '11:22:33:44']

while True:
    # Read the RFID tag data from the Arduino
    rfid_data = ser.readline().strip()

    # Convert the RFID data from bytes to string
    rfid_tag = rfid_data.decode('utf-8')

    # Check if the RFID tag is authorized
    if rfid_tag in authorized_tags:
        print("Access granted")
        # Send a signal to the Arduino to unlock the door
        ser.write(b'1')
    else:
        print("Access denied")
        # Send a signal to the Arduino to keep the door locked
        ser.write(b'0')
