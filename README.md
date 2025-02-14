# GatorLibrary Management System

## Overview
GatorLibrary Management System is a Python-based library management software designed to efficiently handle book records, member services, and lending activities. It utilizes **Red-Black Trees** for book storage and **Binary Min-Heaps** for managing reservations and waitlists.

## Features
- **Book Management**: Add, search, delete, and list books.
- **Borrow & Return Books**: Handles lending and returning processes.
- **Efficient Searching**: Utilizes Red-Black Trees for fast lookup.
- **Reservation System**: Manages reservations using Binary Min-Heaps.
- **Range Queries**: Supports book listing within a given ID range.
- **Command Processing**: Reads commands from a file and outputs results.

## Data Structures Used
1. **Red-Black Tree**
   - Maintains balanced book records for fast retrieval.
   - Supports operations like insertion, deletion, and range queries.

2. **Binary Min-Heap**
   - Manages book reservations efficiently.
   - Implements insert and extract-min operations.

## Project Structure
├── gator_library.py # Main implementation ├── input.txt # Sample input commands ├── output.txt # Output results ├── README.md # Project documentation └── report.pdf # Detailed project report

## How to Run
1. **Clone the repository**
   ```sh
   git clone <repo-url>
   cd GatorLibrary
2. **Run the program with an input file**
   '''sh
   python gator_library.py input.txt
3. **The output will be saved in**
   '''sh
   output.txt
   

