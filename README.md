# Program Structure Overview

## 1. Class Node
- Represents a book in the library.

### Constructor:
```python
__init__(self, book_id, book_name, author_name, availability_status, borrowed_by, reservation_heap)
Initializes a book node.
Methods:
python
Copy
Edit
__repr__(self)
Provides a string representation of the node.
2. Class BinaryMinHeap
Represents a binary min-heap data structure.
Constructor:
python
Copy
Edit
__init__(self)
Initializes an empty heap.
Methods:
python
Copy
Edit
insert(self, k)
Inserts an element into the heap.
python
Copy
Edit
extract_min(self)
Removes and returns the smallest element.
python
Copy
Edit
_min_heapify(self, index)
Maintains the min-heap property.
python
Copy
Edit
_bubble_up(self, index)
Internal method to adjust the heap upwards from the given index, maintaining the min-heap property.
3. Class RedBlackTree
Represents a Red-Black Tree data structure.
Constructor:
python
Copy
Edit
__init__(self)
Initializes the Red-Black Tree.
Methods:
python
Copy
Edit
minimum(self, node)
Finds the node with the minimum value.
python
Copy
Edit
transplant(self, u, v)
Replaces one subtree with another.
python
Copy
Edit
delete(self, z)
Deletes a node from the tree.
python
Copy
Edit
delete_fixup(self, x)
Adjusts the tree after deletion.
python
Copy
Edit
Flip_count(self, node)
Flip the color of the given node in the Red-Black Tree.
python
Copy
Edit
Insert(self, node)
Insert a new node into the Red-Black Tree.
python
Copy
Edit
fix_insert(self, node)
Fixes the tree after insertion.
python
Copy
Edit
left_rotate(self, x)
Performs a left rotation.
python
Copy
Edit
right_rotate(self, y)
Performs a right rotation.
python
Copy
Edit
Print_books_range(self, book_id1, book_id2)
Print the details of books in a specified range of IDs.
python
Copy
Edit
_print_books_range(self, node, book_id1, book_id2, book_details_list)
Traverse the Red-Black Tree and collect details of books within the specified book ID range.
python
Copy
Edit
Search(self, node, book_id)
Search for a book by its ID in the tree.
4. Class GatorLibrary
Represents the main library system.
Constructor:
python
Copy
Edit
__init__(self)
Initializes the library with a Red-Black Tree.
Methods:
python
Copy
Edit
insert_book(self, book_id, book_name, author_name, availability_status)
Inserts a book.
python
Copy
Edit
print_book(self, book_id)
Prints a book's details.
python
Copy
Edit
print_books(self, book_id1, book_id2)
Prints books in a range.
python
Copy
Edit
borrow_book(self, patron_id, book_id, patron_priority)
Manages borrowing a book.
python
Copy
Edit
return_book(self, patron_id, book_id)
Handles returning a book.
python
Copy
Edit
find_closest_book(self, target_id)
Finds the closest book by ID.
python
Copy
Edit
_find_closest_book(self, node, target_id, closest_books)
Helper for finding the closest book.
python
Copy
Edit
delete_book(self, book_id)
Deletes a book from the library.
python
Copy
Edit
read_commands_from_file(self, input_filename)
Reads commands from a file.
python
Copy
Edit
write_output_to_file(self, output_filename, output_lines)
Writes output to a file.
python
Copy
Edit
run_command(self, command)
Executes a given command.
Main Program Execution
Reads command-line arguments for input filename.
Creates an instance of GatorLibrary.
Processes commands from the input file.
Outputs results to a specified file.
My Approach to Calculating the Color Flip Count
Approach to calculating the Color Flip Count is straightforward and aligns with the Red-Black Tree balancing rules as the flip counts vary from the original output flip count:
Flip Color:

Whenever a color change occurs for a node (from red to black or vice versa), we increment the Color Flip Count.
This change typically happens during balancing operations such as rotations and color flips.
Tracking Operations:

We track color changes that occur within the Red-Black Tree during insertions and deletions.
Specifically, we focus on the following scenarios:
Flipping colors of nodes.
Rotations (left and right) that may lead to color changes.
Count Increment:

The Color Flip Count is incremented every time a color change is detected as per the defined rules.
This count reflects the number of balancing actions performed on the tree.
