# Homebrew games controllers
I've been playing with home-made games controllers for a while now. Probably too much. 
Mostly because I think that the 'joypad' style design is uninspired and there are much better options possible. This is my attempt to find a more fun way of playing games.

I haven't done any schematics because I free-hand the circuits and make them up as I go along. That said, there're very simple and you should be able to infer them from the code.

I got a bunch of protoboard in the shape of gamepads made up. This includes a spot to solder a Pico. Version 1 also had space for two stemma QT connectos , 
but these proved to be more complex than they're worth so I haven't actually used them. If I make a version 2, I'll drop these.

## Hardware
In the hardware folder you'll find easyEDA design files and Gerbers (for fabrication) for version 1 of the controller. There are a bunch of things I'm unhappy with on this, but it works!

## Experiment 1
Slide potentiometers!
The slides used have a 'stick point' in the middle. This makes it easy to use, but takes a bit of a push to get over this lump. It makes it a bit janky to play.

I'm particularly enjoying the micro switches on the sholders though. This is definately a feature I'd like to continue.

[![youtube vid of the controller in action](https://img.youtube.com/vi/RL6uFd8PuKk/0.jpg)](https://www.youtube.com/watch?v=RL6uFd8PuKk)

(click to open YouTube video)

## Experiment 2
IMU -- this contains a vastly overkill nine-axis IMU that can be used as an analogue input. In the initial version, it's only used to control the X axis (a bit like a steering wheel). There's also a slider becuase I enjoyed the slider for throttle control. This time, I've gone with a smooth slider (no 'bump' in the middle, but added some LEDs to indicate position (so it's easy to get 0). In hindsight, a colour scale on thes LEDs would have been nice.

Overall, I think I prefer this pot without the sticking point in the middle. IT does need a big dead-zone, and the LEDs help as well.

[![youtube vid of the controller in action](https://img.youtube.com/vi/P0G-hcmtkKg/0.jpg)](https://www.youtube.com/watch?v=P0G-hcmtkKg) 

(click to open YouTube video)



