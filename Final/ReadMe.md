# Gladiator
A simple game of gladiator combat. The gladiator starts in the center of the arena and can move in any direction.
The gladiator can attack in any direction.  The gladiator has 2 hit boxes.  The attack hit box which spawns and despawns
from the gladiator after the animation is complete.  This box is used to determine the collision with the enemy.  The
second hit box is the gladiator's hit box.  This is used to determine if the gladiator has been hit by the enemy.

## Movement
- Arrow Keys
  - Up - Move Up
  - Left - Move Left
  - Down - Move Down
  - Right - Move Right
- Space - Attack

OR

- W - Move Up
- A - Move Left
- S - Move Down
- D - Move Right
- Space - Attack

## Pre-requisites
- Python 3.10 +
- [SimpleGE Game Engine](https://github.com/twopiharris/simpleGE) - this was included with the project so you don't 
need to install it. but to learn more about the engine visit the link.

## Getting Started
1.) **To get started, clone the repository**
```bash
git clone https://github.com/brianbuckles1/CS120.git
```
2.) **Make sure to get the branches**
```bash
git fetch
```
3.) **Checkout the final branch**
```bash
git checkout final
```
4.) **Navigate to the CS120 directory**
```bash
cd CS120
```
5.)**navigate to the Final directory**
```bash
cd Final
```
5a.) **Optional** - Create Virtual Environment so you don't mess up your system python
[Python venv documentation](https://docs.python.org/3/library/venv.html)
```bash
python -m venv venv
```
5b.) Activate the virtual environment

**Linux**
```bash
source venv/bin/activate
```

**Windows Powershell**
```bash
venv\Scripts\activate.ps1
```
6.) **Install the requirements**
```bash
pip install -r requirements.txt
```

## Running the game
```bash
python main.py
```

## Game Design
When designing the game I tried to separate the concerns into different folder and files.
- The main.py file is responsible for looping the game until the quit command is given by the menu. by default the first
screen is the menu scene.
- The menu scene is responsible for displaying the menu screen and handling the start and quit buttons. The menu screen 
has a property for the high score that is displayed on the screen and what button command was pressed.
- The game scene is responsible for displaying the game screen and handling the game logic.
- The sprites\gladiator file contains classes thar are responsible for the different gladiator classes and their animations.  It also contains
the transparent hit boxes that are used for collision detection since they technically apply to the gladiator.
- The health file contains the heart sprite that is used to display the health of the player.

## Improvements
The game could be improved by adding different difficulties, character classes, maybe new mode that goes my time instead
of lives.
- split the assets into different folders for images and music
- create better base classes for the gladiators and hit boxes so they could be extended better later like new classes an
such.  If I put more though into the base classes it would have been alot easier to add other gladiator classes with different
hit boxes and animations.

I had to change my design alot because I didn't think about the base classes enough.  I spent too much time on trying to 
get the mechanics to work and not enough time on the code design.  It was easy to say "I would like to have different classes" 
but when it came to implementing them it would have taken alot longer to implement with the current design structure.  I would
create a base player gladiator class with all the movement and such and then inherit it in each new class like sword gladiator,
whip gladiator, archer, spear, with only needing to worry about the attack animation and hit boxes.

Staying on track was not an issue for me.  My issue was thinking too much about the mechanics and all the things I could do
instead of focusing on the base game.  I had to cut alot of features that I wanted to add because I didn't have enough time.
My mind kept adding "what if" and "this would be cool".

## Milestones
- The gladiator can take damage by the enemy sprite running into the gladiator hit box
- The gladiator can kill the enemy by pressing attack key while the enemy in the attack hit box
- The high score is saved to a file save.dat after each game if it is higher than the previous high score
- the high score is loaded when the program starts.
- 2 screens\scenes menu screen and a game screen. The menu screen is displayed when the game starts.
### Gladiator sprite
  - move in any direction using the movement keys
  - attack in any direction using the attack key
  - walking animations for each direction
  - attack animation for each direction
  - death animation
### Hit Boxes
  - Attack hit box - used to determine if the enemy is hit by the gladiator's attack
  - Hit box - used to determine if the gladiator is hit by the enemy

### Menu screen
This screen is displayed when the game starts.  It has a start button and a quit button and shows the high score.
  - has a title
  - has high score
  - has background music
  - has background image - 
  - start button starts the game
  - quit button quits the game
### Game screen 
This screen is responsible for collision detection in the hit boxes and updating the score and health of the player.
  - has a wall around the screen that the gladiator cannot pass through
  - the gladiator starting in the center of the screen
  - shows the score in the bottom right corner
  - shows the player's health in the bottom left corner as hearts
  - background music
  - game over sound
- the enemies spawn on the inside of the wall.
- the enemies move towards the gladiator

## Structure
- The folder structure is as follows:
  - **assets**: contains all the images, sounds, licences for the images or sounds used in the game or making of the game.
  - **scenes**: contains the game scenes
    - **game** - the actual game that is played 
      - inherits from simpleGE.Scene
    - **menu** - the menu screen that is displayed when the game starts.
      - inherits from simpleGE.Scene
  - sprites: contains the sprites for the game
    - **health** - the heart sprite
    - **gladiator**
      - **BaseGladiator** - the base gladiator class 
        - inherits from simpleGE.Sprite
      - **Gladiator** - the gladiator class that 
        - inherits from BaseGladiator
      - **EnemyGladiator** - the enemy gladiator class 
        - inherits from BaseGladiator
      - **PlayerAttackHitBox** - the attack box class 
        - inherits from simpleGE.Sprite
      - **PlayerHitBox** - the hit box class 
        - inherits from simpleGE.Sprite

## Credits
assets/hero.png – gladiator-credits.txt - https://sanderfrenken.github.io/Universal-LPC-Spritesheet-Character-Generator/
assets/hero-attacking.png – gladiator-credits.txt - https://sanderfrenken.github.io/Universal-LPC-Spritesheet-Character-Generator/
assets/hero-death.png – gladiator-credits.txt - https://sanderfrenken.github.io/Universal-LPC-Spritesheet-Character-Generator/
assets/hero-walking.png – gladiator-credits.txt - https://sanderfrenken.github.io/Universal-LPC-Spritesheet-Character-Generator/
assets/enemy.png – enemy-credits.txt - https://sanderfrenken.github.io/Universal-LPC-Spritesheet-Character-Generator/
assets/game_over.ogg - voiceover-license.txt - https://www.kenney.nl/assets/voiceover-pack-fighter
assets/fight.ogg - voiceover-license.txt - https://www.kenney.nl/assets/voiceover-pack-fighter
assets/intro.ogg - https://opengameart.org/content/dark-intro
assets/heart.png - https://opengameart.org/content/heart-1
assets/background.wav - https://opengameart.org/content/boss-battle-music
assets/sword_sfx.wav - https://opengameart.org/content/boss-battle-music
assets/background.png - https://designer.microsoft.com/image-creator 
assets/menu_background.png - https://designer.microsoft.com/image-creator