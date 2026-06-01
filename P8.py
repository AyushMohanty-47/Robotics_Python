angles = [30,-15,45,200,60,90]

def validANGLE(angle):
    return 0 <= angle <= 180

def servoANGLE(angle):
    return angle*10

valid_ANGLES = list(filter(validANGLE, angles))
servo_ANGLES = list(map(servoANGLE, valid_ANGLES))

print("Angles are as follows: ")
print(f"Valid Angles: {valid_ANGLES}")
print(f"Servo Commands: {servo_ANGLES}")