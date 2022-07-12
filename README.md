# HandComandsFromVideo

## About 
This is an implementation of the hand tracking module for mouse control. There are two variations in the project: controller and direct control.
https://github.com/deathsmilestome/CVHandTrackModule
<br>
![image](https://user-images.githubusercontent.com/80523414/178558222-a294c93d-c4e0-489b-a468-3530fd1e5d0b.png)
### Direct control
This is a way of controlling the mouse with your hand, where the position of the cursor depends directly on the position of your hand in cam's FoV.<br>
- cursor - index finger MCP[5]
- freeze cursor - thumb tip[4] + index finger MCP[5] clenched
- left click - you have to freeze it first then index finger[8] + midle finger tip[12] clenched
- right click - you have to freeze it first then midle finger tip[12] + ring finger tip[16] clenched
- off - index finger[12] under thumb MCP[2]
<br>

### Controller
Is a virtual controller that changes the position of the mouse based on the difference in the center of the controller and the index finger[8], the further the finger from the center of the controller, the faster changes the position of the cursor. <br>
- cursor - index finger[8]
- freeze cursor - index finger[8] + thumb tip[4] clenched
- left click - нou have to freeze it first then index finger[8] + midlde finger tip[12]
- off - thumb tip[4] under line(check pic)
<br>

![image](https://user-images.githubusercontent.com/80523414/178564283-04d60b08-c303-49b6-8156-72989d2b9e7f.png)


