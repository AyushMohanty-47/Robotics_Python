def robot_action(sensors):
    
    if sensors==[0, 0, 0, 0, 0, 0]:
        return "Stop Robot"

    elif sensors==[1, 1, 1, 1, 1, 1]:
        return "Junction Detected"

    elif sensors[2]==1 or sensors[3]==1:
        return "Move Forward"

    elif sensors[0]==1 or sensors[1]==1:
        return "Turn Left"

    elif sensors[4]==1 or sensors[5]==1:
        return "Turn Right"

    return "No Action"