# Racing

How will the robot see the walls?
    * Mapping of some kind...?
        * Draw a way forward
    * Computer vision?
        * Go into "open space"

How will it know to move fast?
    * Always be moving at 1 speed
    * Never be not moving at 1 speed

How can a car avoid another?
    * The car in front has the right of way
    * Following cars need a big speed advantage over leading ones
    * Two "lanes" that are invisible
    * Robots drive in "inner" lane most of the time, if overtaking switch to outer
    *
Pit stop implementation
    * Bot pulls into stop to have its stats reset
    * Marked area apart from the track

Sub problems
    * Robot drive around a track
    * Issue commands to robot to change speed
    * ROScore running on only one bot with other stuff connected
    * Two robots driving around a track
    * Issue commands to both robots to change speed
    * "overtaking" logic
    * Commands from multiple computers (vnc abuse?)

# Dancing

Patterns
    * Robots move in concentric circles
    * Robots, from an unorganized position, form a line
    * Robots form vertices of shape (if there are enough)
    * Robots mix about in a disorganized manner but don't collide
    * Sync with some music (dance more or less in place)
    * Robots drive towards each other, stop, turn around, and drive away
    * Robot drives in circle while another one orbits it
    

Sub problems
    * Localize one robot with fiducials 
    * Get ROScore to run on only one bot and link another bot to it (and whatever computer the vnc runs on)
    * Publish tf2s from each robot with relative dist to the map coords
    * Have robots move in some simple pattern
    * Add more patterns
 