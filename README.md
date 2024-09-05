Authors: Kevin K Klefsås and Henrik N. Persen

## Welcome to our Mayhem interpretation

## This game is made using PYGAME arcade game creator, where most of the codes function are based on Pygame. therfore you will need to install Pygame to your computer, to run this program. Pygame can be downloaded thru the console where you can find insturctions on how thru this link https://www.pygame.org/news

## this is an attempt at recreating the 2D aracde game called Mayhem

this program does not use any precode, but consist of some inspiration from the internet, links below:

https://stackoverflow.com/questions/46697502/how-to-move-a-sprite-according-to-an-angle-in-pygame

https://stackoverflow.com/questions/48856922/pygame-how-to-make-sprite-move-in-the-direction-its-facing-with-vectors

https://www.reddit.com/r/pygame/comments/80z7bo/pygamemath_vector2rotate_ip/

https://opengameart.org/content/ship-space-0

## https://www.youtube.com/watch?v=pUEZbUAMZYA

## What to expect when opening the game:

HealtH, fuel bar:

The set of bars will spawn in the two top corners

Red bar is health (you will lose health when shot, also if you collide with obstacle)

brown bar is fuel (you will lose fuel when you move forward, so remenber to pick up fuel)

top left side corner is for Green (spaceship 1)
top right corner is for Red (spaceship 2)

---

Score:
the score of each ship is displayed under the health and fuel bar.
the score will go down if you collide with obsticle
the score will go down if you get shot

## the score will go up if you shoot the enemy spaceship.

two spaceships spawn onto the screen:

Green (spaceship 1)

## Red (spaceship 2)

asteriods:

Two random sized asteroids spawn onto the screen.
if spaceship hits the asteroid it takes damage and lose score the
asteroids will be destroyed and spawn inn from the top of the screen

---

Fuel can:

one red fuel can will spawn onto the screen, when the game start
the fuel can will spawn again, after a ship drives over it to get fuel

---

What happens if you win/lose:

nothing really happens, except it will be printed who won into the terminal.

## if you the want to play the game again, you need to close the application. Then start the program again.

The controls for spaceship 1, Green ship:

move forward: W
rotate left: A
rotate right: D
shoot: Space

---

The controls for spaceship 2, Red ship:

move forward: up_arrow
rotate left: left_arrow
rotate right: right_arrow
shoot: right_ctrl

---

## the images used for each of the objects, are licence free and can be used by everyone.

## to run this program you will have to unzip the folder and open it in console. afterwards you run the code using python3 main.py
