import time
from adafruit_motorkit import MotorKit
from adafruit_motor import stepper

kit = MotorKit()

# our steppers have 200 steps per rotation
steps_per_rotation = 200

# In our loop, I'm going to rotate the steppers in opposite directions, but
# each time through this loop, I want the steppers to reverse.  I'll use the 
# following variables to make that happen.
s1_dir = stepper.FORWARD
s2_dir = stepper.BACKWARD

try:
  while True:
    
    # stepper1 will be doing interleave...that doubles the number of steps,
    # therefore we'll be doing two steps every time through the loop.
    # stepper2 is going to be using "double"...which is a full step powering
    # both coils (so more torque)
    for steps in range(steps_per_rotation):
      kit.stepper1.onestep(direction = s1_dir, style=stepper.INTERLEAVE)
      kit.stepper1.onestep(direction = s1_dir, style=stepper.INTERLEAVE)
      kit.stepper2.onestep(direction = s2_dir, style=stepper.DOUBLE)
      
    # doing a "release" removes power from the coils...meaning the 
    # motor can spin.  We're going to  release stepper 2 but NOT stepper 1
    # so that you can feel the torque difference
    kit.stepper2.release()
    time.sleep(5)
    
    # reverse the direction of both steppers
    if (s1_dir == stepper.FORWARD):
      s1_dir = stepper.BACKWARD
      s2_dir = stepper.FORWARD
    else:
      s1_dir = stepper.FORWARD
      s2_dir = stepper.BACKWARD

except KeyboardInterrupt:
  pass

# release the stepper on exit
print("Exiting...releasing stepper")
kit.stepper1.release()
kit.stepper2.release()
