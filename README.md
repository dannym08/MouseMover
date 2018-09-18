# MouseMover
A library that will mimic human-like mouse movement. Uses Bresenham's line algroithm to get the points between where the
mouse is and its destination.

## Dependencies
You will need pyobjc-core and pyobjc to run it. It is recommded to install them in the given order to avoid a installation
problems. After those are installed you will also need pytweening.

## Usage
The majority of of the library is the moveTo function. The moveTo function is defined at 
moveTo(targetX, targetY, duration, tween). It needs the target x and y coordinate, the ammount of time you want to add
to the travel of the mouse and the tween you would like to add. The tween is a certain trait you add to the travel of the mouse
such as starting slow and gradually speed up till the end. The tweens are defined in pytweening and supplied as commentes in this
library as well.
