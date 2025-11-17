# Stars

A small visual experiment creating drifting, pulsating star effects using Pygame.

# Description

This project renders a field of animated “stars” that slowly fall downward while pulsing in brightness.  
Each star uses concentric circles with varying alpha values to create a soft glow effect.  
The animation is lightweight, based on sprites, and completely CPU-rendered.  
The repository includes two versions:  
- The original version using handcrafted brightness falloff tables  
- The test version using a sinusoidal brightness model for smoother animation  
This was mostly a fun experiment in procedural glow effects, radial gradients, and sprite-based animation.

# Installation

- clone the repo
- install my [pygame_template](https://github.com/FINN-2005/pygame_template)
  ```bash
  pip install git+https://github.com/FINN-2005/pygame_template.git
  ```

# Usage

- run the scripts
  ```bash
  python main.py
  ```  
  ```bash
  python test.py
  ```
