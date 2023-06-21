# Create a demo app by following the FlytBase documentation to make the drone takeoff at 5m, move in a square trajectory of side length 6.5m at a
# height of 5m, and land once the entire mission is over. Demonstrate the app and fly the drone in the FlytSIM simulator.

#!/usr/bin/env python3
import time
from flyt_python import api
drone = api.navigation(timeout=120000) # instance of flyt drone Naviigation class

# At least 2 sec sleep time for the drone interface to initialize properly
time.sleep(2)

print ('taking off')
drone.take_off(5.0)

print (' going along the setpoints')
drone.position_set(6.5,0,0,relative=True)
drone.position_set(0,6.5,0,relative=True)
drone.position_set(-6.5,0,0,relative=True)
drone.position_set(0,-6.5,0,relative=True)

print ('Landing')
drone.land(async=False)

#shutdown the instance
drone.disconnect()


# Create a demo app by following the FlytBase documentation to make the drone takeoff at 10m, move in a triangle trajectory of side length 10m at a
# height of 10m, and land once the entire mission is over. Demonstrate the app and fly the drone in the FlytSIM simulator.

#!/usr/bin/env python3
import time
from flyt_python import api
drone = api.navigation(timeout=120000) # instance of flyt drone Navigation class

# At least 2 sec sleep time for the drone interface to initialize properly
time.sleep(2)

print ('taking off')
drone.take_off(10.0)

print ('going along the setpoints')
drone.position_set(8.66,5,0,relative=True)
drone.position_set(-8.66,5,0,relative=True)
drone.position_set(0,-10,0,relative=True)

print ('Landing')
drone.land(async=False)

#shutdown the instance
drone.disconnect()
