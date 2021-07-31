## Offside Detection System for Football


### Usage of Program:
* To detect offside in a pre-recorded video, go to the folder in which code and video are stored and type the following in terminal:

```javascript
$ python Offside_detection.py -v 'path/name of video file'
```
* To detect offside from live camera feed:
```javascript
$ python Offside_detection.py
```
* While running the program, press ***'i'*** to input and ***'q'*** to quit
	
* Input patch of jersey of any player of team A by clicking and dragging with the mouse and making sure that background does not get included. The size of patch doesn’t matter much though it is better to have a bigger patch.
* Input patch of jersey of any player of team B in similar manner. 
* Input patch of ball. 
* Input two points along each side of the field in the exact order as shown 
i.e. Top edge, Left edge, Bottom edge then Right edge.

* To run the interface :
```javascript
$ python interface.py
```








