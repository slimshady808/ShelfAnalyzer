# ShelfAnalyzer

ShelfAnalyzer is a Django-based project that provides a powerful solution for optimizing shelf space in retail stores. It enables retailers to analyze the arrangement of products on store shelves, identifying the shape and location of each brand with precision and efficiency.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Test Cases and Results](#test-cases-and-results)

## Introduction

ShelfAnalyzer Mini-Project is a simple Django-based application that provides a single API call to analyze the arrangement of products on store shelves. It identifies the shape and location of each brand, offering a basic solution for optimizing shelf space in retail stores.

With ShelfAnalyzer, you can:

- Accurately identify and analyze the arrangement of products on shelves.
- Determine the shape and location of each brand, whether it's a horizontal rectangle, vertical rectangle, square, or irregular polygon.



## Features

List the key features and functionality of your ShelfAnalyzer project.

- Analyze the arrangement of products on store shelves.
- Identify the shape and location of each brand.

## Installation

Explain how to set up and run your ShelfAnalyzer project. Include information about dependencies, database setup, and any other necessary steps.

```bash
# Clone the repository
git clone https://github.com/slimshady808/ShelfAnalyzer.git
cd ShelfAnalyzer

# Create and activate a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start the development server
python manage.py runserver

# ShelfAnalyzer is now up and running at 
http://localhost:8000.

```



## Test Cases and Results

## Test Case 1: Vertical Rectangles

```bash
# Test Case 1: Vertical Rectangles
curl -X POST -H "Content-Type: application/json" -d '[
  ["G", "M", "N", "B"],
  ["G", "M", "N", "B"],
  ["G", "M", "N", "B"],
  ["G", "M", "N", "B"]
]' http://localhost:8000/analyze-shelf/
```
## Expected Result

{
  "G": {"shape": "vertical rectangle", "location": "left"},
  "M": {"shape": "vertical rectangle", "location": "left"},
  "B": {"shape": "vertical rectangle", "location": "right"},
  "N": {"shape": "vertical rectangle", "location": "right"}
}

## Test Case 2: Squares

```bash
curl -X POST -H "Content-Type: application/json" -d '
[
  ["A", "A", "B", "B"],
  ["A", "A", "B", "B"],
  ["C", "C", "D", "D"],
  ["C", "C", "D", "D"]
]
' http://localhost:8000/analyze-shelf/

```
## Expected Result

{
  "A": {"shape": "square", "location": ["top left"]},
  "B": {"shape": "square", "location": ["top right"]},
  "C": {"shape": "square", "location": ["bottom left"]},
  "D": {"shape": "square", "location": ["bottom right"]}
}



