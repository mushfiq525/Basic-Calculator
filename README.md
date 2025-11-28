# Basic Calculator

This is a simple console‑based calculator written in Python as an **Ostad Module 5 assignment**.  
It demonstrates both functional programming (standalone arithmetic functions) and object‑oriented programming using a `Calculator` class. [web:1][web:2]

## Features

- Basic operations: Add, Subtract, Multiply, Divide  
- Input validation using a reusable `get_number()` function  
- Protection against division by zero  
- Menu‑driven interface with a loop so the user can perform multiple calculations until choosing to exit [web:5]

## How It Works

- `add(a, b)`, `subtract(a, b)`, `multiply(a, b)`, `divide(a, b)` implement the core arithmetic logic.  
- `get_number(message)` repeatedly asks for input and only accepts valid numeric values.  
- `show_menu()` prints a simple text menu for the calculator.  
- `Calculator` class:
  - Wraps the arithmetic functions as methods
  - Uses `menu()` to display the menu
  - Uses `run()` to:
    - Show the menu
    - Take the user’s choice (1–5)
    - Ask for two numbers if needed
    - Perform the selected operation and print the result
    - Exit when the user selects option 5

## Requirements

- Python 3.x installed on your system [web:2]

## How to Run

1. Clone or download this repository.  
2. Save the calculator code in a file named, for example, `calculator.py` in the project folder.  
3. Open a terminal (or command prompt) in the project folder.  
4. Run:


