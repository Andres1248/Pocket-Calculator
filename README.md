# Pocket-Calculator
Pocket Calculator (Python + Pygame)

A graphical pocket calculator built in Python using Pygame, including a clean user interface, support for basic and extended mathematical operations, and full asset handling (images and audio).
Originally developed as part of the Programming Workshop (IC-1803) at the Costa Rica Institute of Technology.

Features
✔ Basic Operations

Addition

Subtraction

Multiplication

Division (with zero-division protection)

✔ Extended Operations

Power (x^y)

Square root (√x)

Inverse (1/x)

Change sign (+/-)

Logarithm (user enters value and base)

✔ User Interface

Built entirely with Pygame

Background image support (Fondo.jpg)

Sound effects (explosion.mp3)

Clear button layout

Floating point input using “.”

Error handling for invalid operations

✔ Clean Project Structure

Modular Python code (src/)

Images and audio located under assets/

Cross-platform asset loader ensures all file paths work

IMPORTANT: to calculate the logarithm, press the log button. Once you do this, it will prompt you for an x value, this is the number you want to get the logarithm of.
Once you enter x, press the log button again; it will prompt you for a y value; this will be the base of the logarithm. Once you entered the base, to get the result simply press the log button a third time.


Installation
1. Clone the repository
git clone https://github.com/Andres1248/Pocket-Calculator
cd Pocket-Calculator

2. Install dependencies
pip install -r requirements.txt

3. Run the calculator
python src/main.py



Authors

Andrés Morales Salas

Carlos Isaac Hidalgo

Costa Rica Institute of Technology
IC-1803 Programming Workshop


