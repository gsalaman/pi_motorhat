# pi_motorhat
To install adafruit's library:
```
sudo pip3 install adafruit-circuitpython-motorkit
```

stepper.py does a simple demo with two stpper motors.

Adafruit's guide:
https://learn.adafruit.com/adafruit-dc-and-stepper-motor-hat-for-raspberry-pi/installing-software

## Glenn Notes:
* I like the "release" funcationality
* Need to power off a 5v power.  12v was causing current limiting...that's a nice feature of doing the "big easy" board on an arduino instead
* Microstepping was touchy.  Interleave stepping was fine, but that means we're x2 the steps rather than x16 with the "big easy"
* Doing steps over I2C means you don't have as much control over when you step.  I could see differences in 5 ms....but if you are caluclating exacly "time between steps" (I'm looking at you, equatorial mount...), then going arduino is better.
