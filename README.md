# Flappy Bird Clone (Python + Pygame)

A simple Flappy Bird-style game created for the Python Programming Fundamentals project.

## Requirements
- Python 3 or newer
- Pygame

## Install and run
```bash
python -m pip install -r requirements.txt
python main.py
```

## Controls
- **SPACE**: flap / move upward
- **R**: restart after Game Over
- **ESC**: quit

## Game rules
The bird falls under gravity. SPACE sets its vertical velocity to -10, after which gravity is applied during the frame update. Move through the pipe gaps to earn points. Contact with a pipe, ceiling, or ground ends the game.

## Files
- `main.py`: game loop, physics, pipe generation, scoring and collision logic
- `requirements.txt`: dependency list

## Project test cases
The project's supplied test cases are represented in the report. The live game uses frame-by-frame updates; the expected values in the brief are illustrative checks of the physics and collision/scoring logic.

## License
Educational use. Add your preferred license if publishing beyond coursework.
