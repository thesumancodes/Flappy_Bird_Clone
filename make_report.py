from docx import Document
from docx.shared import Inches, Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.section import WD_SECTION
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_CELL_VERTICAL_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

D=Document()
sec=D.sections[0]; sec.top_margin=Inches(.75); sec.bottom_margin=Inches(.75); sec.left_margin=Inches(.85); sec.right_margin=Inches(.85)
style=D.styles['Normal']; style.font.name='Times New Roman'; style.font.size=Pt(11)
style.paragraph_format.space_after=Pt(6)

def center(text,size=14,bold=True):
 p=D.add_paragraph(); p.alignment=WD_ALIGN_PARAGRAPH.CENTER; r=p.add_run(text); r.bold=bold;r.font.size=Pt(size);r.font.name='Times New Roman';return p

def heading(t): D.add_heading(t,level=1)
def para(t): D.add_paragraph(t)
def bullet(t): D.add_paragraph(t,style='List Bullet')
def table(headers,rows):
 t=D.add_table(rows=1,cols=len(headers));t.style='Table Grid';t.alignment=WD_TABLE_ALIGNMENT.CENTER
 for c,h in zip(t.rows[0].cells,headers): c.text=h
 for row in rows:
  cells=t.add_row().cells
  for c,v in zip(cells,row):c.text=str(v)
 return t

center('Project Report',16);center('On',14);center('Flappy Bird Clone',22)
center('PS No. 60',12);center('Programming Fundamentals and Logic Building Using Python',12);center('SESSION: 2026–27',12)
D.add_paragraph('')
center('RUNGTA INTERNATIONAL SKILLS UNIVERSITY',14)
center('Submitted By',12,False);center('Name: __________________________',12);center('REF No.: ________________________',12)
center('Bachelor of Technology in Computer Science and Engineering',11)
center('Under the Guidance of',12,False);center('Faculty Name & Designation: __________________',11)
center('SCHOOL OF COMPUTER SCIENCE AND ENGINEERING',12);center('BHILAI, CG',12);center('December 2026',12)
D.add_page_break()
heading('Table of Contents')
for x in ['1. Abstract','2. Introduction','3. Scope and Objectives','4. System Requirements','5. Methodology','6. Flowchart','7. Function Design','8. Implementation','9. Testing and Interim Progress','10. Conclusion','11. References'] : bullet(x)
heading('1. Abstract')
para('Flappy Bird Clone is a small 2D game developed in Python using the Pygame library. The player controls a bird that falls due to gravity and can move upward when SPACE is pressed. The player tries to pass through gaps between pipe pairs. The game ends if the bird touches a pipe, the ceiling, or the ground. The project demonstrates loops, conditional statements, functions, variables, random generation, keyboard input, collision detection and basic game design. The code and report are prepared; execution testing requires installing Pygame on the target computer.')
heading('2. Introduction')
para('Python is a beginner-friendly programming language with readable syntax and a large ecosystem of libraries. Pygame provides tools for creating windows, handling keyboard input, drawing shapes and managing game loops. This project applies these concepts to a simple arcade-style game.')
para('Problem statement: implement a bird movement game in a 400 by 600 pixel window. Gravity continuously changes the bird’s vertical position, SPACE gives an upward impulse, pipe gaps are generated, passing pipes increases the score, and collisions end the game.')
para('Motivation: the project provides practical experience with programming fundamentals and shows how multiple logic components can work together in an interactive application.')
heading('3. Scope and Objectives')
para('Scope: bird physics, keyboard input, pipe generation and movement, score tracking, collision detection, game-over display and restarting. The project does not include online multiplayer, sound, persistent high scores, menus or advanced sprites.')
para('Main objective: create a playable Flappy Bird-style game using Python and Pygame.')
for x in ['Use a game loop to update and render the scene.','Apply gravity and a SPACE-key impulse.','Generate pipe pairs with a gap.','Detect collisions and track pipe passes.','Display score and restart controls.','Organize logic into reusable functions.']: bullet(x)
heading('4. System Requirements')
para('Hardware (recommended): dual-core processor, 2 GB RAM or more, and at least 100 MB free storage. These are modest recommended values for a small game and are not measured requirements.')
para('Software: Python 3.9 or newer; Pygame 2.5 or newer; an editor such as VS Code, IDLE or PyCharm; Windows, Linux or macOS.')
para('Install dependency: python -m pip install -r requirements.txt. Run the game: python main.py.')
heading('5. Methodology')
para('Input: keyboard events (SPACE, R and ESC). Processing: update bird velocity and position, create/move pipes, check collisions and update score. Output: draw the bird, pipes, ground, score and game-over message.')
for x in ['Analyse the required game behavior and values.','Design the game loop and helper functions.','Implement movement, pipe generation, scoring and collisions.','Run the program and check the listed test scenarios after installing Pygame.','Debug any behavior that differs from the expected cases.']: bullet(x)
heading('6. Flowchart')
para('START → Initialize Pygame and game variables → Read events → Is game active? → Apply SPACE impulse when pressed → Apply gravity and update bird position → Create/move pipes → Update score → Check collision → If collision: Game Over → Draw frame → Repeat until ESC/window close. After Game Over, R resets the state.')
para('Module flow: reset_game initializes state; create_pipe generates a gap location; pipe_rects converts pipe data to rectangles; check_collision evaluates bird contact with boundaries and pipe rectangles; main handles events, updates and drawing.')
heading('7. Function Design')
table(['Function','Purpose'],[
('create_pipe(x)','Creates a pipe pair with a randomized gap center.'),('pipe_rects(pipe)','Returns upper and lower pipe collision rectangles.'),('draw_pipe_pair(screen, pipe)','Draws both pipe sections.'),('check_collision(bird_rect, pipes)','Checks bird contact with pipes or vertical boundaries.'),('reset_game()','Returns initial bird position, velocity, pipes, score and status.'),('main()','Initializes Pygame and manages event, update and render loops.')])
para('Functions use parameters to share the current game objects and return values where useful. main() coordinates the functions in each frame.')
heading('8. Implementation')
para('Project files: main.py contains the game, requirements.txt lists Pygame, README.md describes setup and controls, and make_report.py generates this report. The game uses a dictionary for each pipe pair, a list to store pipe pairs, and a Rect for collision checks.')
para('Important logic: SPACE sets velocity to -10, gravity adds +1 each frame, and the bird position is updated by the resulting velocity. Pipes move left at 3 pixels per frame. When a pipe moves past the bird, score increases once. Collision with the top, ground or pipe rectangles sets the game-over state. R restarts after game over.')
para('Code is provided in main.py. A screenshot should be captured by the student after running the game successfully and inserted here for final submission.')
heading('9. Testing and Interim Progress')
table(['Test','Input / scenario','Expected behavior','Status'],[
('1','y=300, velocity=0, no key for 2 frames','Frame 1: velocity=1, y=301; Frame 2: velocity=2, y=303','Logic reviewed; runtime test pending'),
('2a','y=570, velocity=0, no SPACE','Ground collision and Game Over','Logic reviewed; runtime test pending'),
('2b','y=5, velocity=0, SPACE','velocity=-9, y=-4; top-boundary Game Over','Logic reviewed; runtime test pending'),
('3','y=300, velocity=0, Z pressed, 1 frame','Z ignored; velocity=1, y=301','Logic reviewed; runtime test pending'),
('4a','y=300, velocity=5, SPACE, 1 frame','velocity=-9, y=291','Logic reviewed; runtime test pending'),
('4b','pipe x=39, width=60, bird x=100, score=0','Pipe considered passed; score becomes 1','Logic reviewed; runtime test pending')])
para('Progress: source code, setup instructions and report structure are prepared. Runtime execution and screenshots remain to be completed on a machine where Pygame can be installed. The development environment used to prepare this package could not install Pygame due to network access limitations; therefore, the status above is not presented as verified runtime testing.')
para('Potential issues to check during runtime: package installation, window display, keyboard event handling, pipe gap placement, collision behavior, and score increment timing.')
heading('10. Conclusion')
para('The Flappy Bird Clone applies Python fundamentals to a graphical interactive program. It combines variables, lists, dictionaries, functions, loops, keyboard events, randomized pipe placement and rectangle collision checks. The next step is to run it locally, verify each test case, capture screenshots, and update the testing table with actual results.')
heading('11. References')
for x in ['Python documentation: https://docs.python.org/3/','Pygame documentation: https://www.pygame.org/docs/','Pygame getting started: https://www.pygame.org/wiki/GettingStarted']: bullet(x)
D.save('/mnt/data/flappy_bird_project/Project_Report.docx')
