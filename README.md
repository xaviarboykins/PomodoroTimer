# Pomodoro Timer

A simple desktop Pomodoro timer built with Python as both a practical productivity tool and a focused Python learning project.

## About the Project

The **Pomodoro Technique** is a time-management method that divides focused work into timed intervals separated by short breaks. A typical cycle consists of:

1. **25 minutes** of focused work
2. **5-minute** short break
3. Repeat for four work sessions
4. Take a longer break after completing the cycle

This application provides a simple desktop interface for managing those sessions without unnecessary distractions.

## Purpose

This project is being built to **reinforce my Python fundamentals as I adopt Python as one of my primary programming languages**.

Rather than learning Python through disconnected exercises, the project provides a small but complete application where I can practice Python concepts in a real codebase.

The project focuses on:

* Python syntax and fundamentals
* Object-oriented programming
* Classes and application state
* Functions and modules
* Python project structure
* Packages and imports
* Type hints
* Separation of concerns
* Event-driven programming
* Desktop GUI development
* Unit testing
* Debugging and refactoring
* Git-based development workflow

The project is intentionally kept small so the emphasis remains on **learning Python and developing good Python engineering habits**.

## Practical Use

This is not only a learning exercise.

The finished application will become a productivity tool that I actively use during development, study, and other 
focused work sessions.

Using the application in my own workflow also gives me an opportunity to identify usability problems, bugs, and 
potential improvements through real-world use.

## Tech Stack

### Language

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python\&logoColor=white)

**Python 3** — Core application language.

### User Interface

![Tkinter](https://img.shields.io/badge/GUI-Tkinter-blue)

**Tkinter** — Python's standard GUI toolkit, used to create the desktop interface while keeping external dependencies 
minimal.

### Testing

![Pytest](https://img.shields.io/badge/Testing-pytest-0A9EDC?logo=pytest\&logoColor=white)

**pytest** — Automated testing for the timer and application logic.

### Development

![Git](https://img.shields.io/badge/Version_Control-Git-F05032?logo=git\&logoColor=white)
![GitHub](https://img.shields.io/badge/Repository-GitHub-181717?logo=github\&logoColor=white)

**Git + GitHub** — Version control, project history, and repository management.

## Planned Project Structure

```text
PomodoroTimer/
│
├── pyproject.toml
├── README.md
├── .gitignore
│
├── src/
│   └── app/
│       ├── __init__.py
│       ├── main.py
│       ├── timer.py
│       ├── session.py
│       ├── config.py
│       └── ui.py
│
└── tests/
    ├── test_timer.py
    └── test_session.py
```

The structure will evolve as the project progresses and as new Python concepts are introduced.

## Planned Features

* Work timer
* Short break timer
* Long break timer
* Start timer
* Pause and resume
* Reset timer
* Skip current session
* Automatic session transitions
* Completed session tracking
* Configurable session durations
* Simple desktop interface

## Learning Approach

Development is being completed progressively as part of a **12-lesson Python refresher course**.

Each lesson introduces Python concepts and applies them directly to the Pomodoro Timer. Lessons conclude with code 
review and a knowledge check before development progresses to the next stage.

The goal is not simply to finish the application, but to understand the Python concepts and engineering decisions 
behind its implementation.

## Project Status

**In Development**

The application is being built incrementally.
