# ShelfAnalyzer

ShelfAnalyzer is a Django-based project that provides a powerful solution for optimizing shelf space in retail stores. It enables retailers to analyze the arrangement of products on store shelves, identifying the shape and location of each brand with precision and efficiency.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [API Documentation](#api-documentation)
- [Contact Information](#contact-information)

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

ShelfAnalyzer is now up and running at http://localhost:8000.
