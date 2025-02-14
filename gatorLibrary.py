# Import necessary libraries
# sys is used for system-specific parameters and functions
# time is used for time-related functions
import sys
import time

# Node class definition
class Node:
    def __init__(self, book_id, book_name, author_name, availability_status, borrowed_by, reservation_heap):
        # Constructor for the Node class, initializes a book's attributes in the library.
        # Each node represents a book with details like ID, name, author, availability, borrower, and reservation queue.
        self.book_id = book_id  # Unique identifier for the book
        self.book_name = book_name  # Name of the book
        self.author_name = author_name  # Author of the book
        self.availability_status = availability_status  # Availability status of the book (e.g., available, borrowed)
        self.borrowed_by = borrowed_by  # Information about who has borrowed the book
        self.reservation_heap = reservation_heap  # Priority queue (min-heap) for managing reservations
        # Red-Black Tree specific properties for the node
        self.color = 'black'  # Color attribute for Red-Black Tree balancing
        self.parent = None  # Parent node in the Red-Black Tree
        self.left = None  # Left child in the Red-Black Tree
        self.right = None  # Right child in the Red-Black Tree

    
    def __repr__(self):
        # Define the string representation for a Node instance.
        # This method is useful for debugging and logging, providing a clear description of the node's attributes.
        if self.book_id is None:
            return "NIL Node"  # Representation for a NIL node in the Red-Black Tree
        return (f"Node(book_id={self.book_id}, book_name=\'{self.book_name}\', "
                f"author_name=\'{self.author_name}\', availability_status={self.availability_status}, "
                f"borrowed_by={self.borrowed_by}, reservations={list(self.reservation_heap.heap)})")
# BinaryMinHeap class definition
class BinaryMinHeap:
    def __init__(self):
        # Constructor for the BinaryMinHeap class, initializes an empty min-heap.
        # A min-heap is a binary tree where the value of each parent node is less than or equal to the values of its children.
        self.heap = []  # Internal list to store heap elements
        

    def insert(self, k):
        # Insert a new element into the min-heap.
        # This method adds the element to the end of the heap and then adjusts its position to maintain the heap property.
        self.heap.append(k)  # Add the new element to the end of the heap
        self._bubble_up(len(self.heap) - 1)  # Adjust the heap upwards starting from the new element


    def extract_min(self):
        # Remove and return the minimum element from the min-heap.
        # This method retrieves the smallest element, replaces it with the last element, and then re-adjusts the heap.
        if not self.heap:
            raise IndexError("Extracting from an empty heap is not allowed.")
        min_val = self.heap[0]
        if len(self.heap) > 1:
            self.heap[0] = self.heap.pop()
            self._min_heapify(0)
        else:
            self.heap.pop()
        return min_val

    def _min_heapify(self, index):
       # Internal method to adjust the heap downwards from the given index, maintaining the min-heap property.
        # This method compares the current node with its children and swaps them if needed to maintain the heap order.
        smallest = index  # Assume the current index is the smallest
        left_child = 2 * index + 1  # Index of the left child
        right_child = 2 * index + 2  # Index of the right child

        # Check if left child is smaller than current smallest
        if left_child < len(self.heap) and self.heap[left_child] < self.heap[smallest]:
            smallest = left_child

        # Check if right child is smaller than current smallest
        if right_child < len(self.heap) and self.heap[right_child] < self.heap[smallest]:
            smallest = right_child

        # Swap and continue heapifying if the smallest is not the current index
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._min_heapify(smallest)

    def _bubble_up(self, index):
        # Internal method to adjust the heap upwards from the given index, maintaining the min-heap property.
        # This method ensures that each parent node in the heap is less than or equal to its children.
        parent_index = (index - 1) // 2  # Calculate the index of the parent node
        if index > 0 and self.heap[index] < self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self._bubble_up(parent_index)

class RBTree:
    def __init__(self):
        # Initialize the Red-Black Tree with a NIL node as the root and set its color to black.
        self.NIL = Node(None, None, None, None, None, BinaryMinHeap())
        self.NIL.color = 'black'
        self.NIL.left = self.NIL
        self.NIL.right = self.NIL
        self.NIL.parent = self.NIL
        self.root = self.NIL
        self.insert_fixup_count = 0
        
    def minimum(self, node):
        # Find the node with the minimum value in the subtree rooted at the given node.
            while node.left != self.NIL:
                node = node.left
            return node
        
    
    def transplant(self, u, v):
        if u.parent == None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent
    
    def delete(self, z):
        # Delete a node z from the Red-Black Tree and maintain its properties.
        
            if z is None or z == self.NIL:
                return  # Ensure we're not trying to delete a None or NIL node
            
            y = z
            y_original_color = y.color
            if z.left == self.NIL:
                x = z.right
                if x != self.NIL:  # Check if x is not NIL before transplant
                    self.transplant(z, z.right)
            elif z.right == self.NIL:
                x = z.left
                if x != self.NIL:  # Check if x is not NIL before transplant
                    self.transplant(z, z.left)
            else:
                y = self.minimum(z.right)
                y_original_color = y.color
                x = y.right
                if y.parent == z:
                    x.parent = y
                else:
                    self.transplant(y, y.right)
                    y.right = z.right
                    y.right.parent = y
                self.transplant(z, y)
                y.left = z.left
                y.left.parent = y
                y.color = z.color
                if x != self.NIL:  # Check if x is not NIL before setting parent
                    x.parent = y
            if y_original_color == 'black':
                self.delete_fixup(x if x != self.NIL else self.root)
        
    
    
    def delete_fixup(self, x):
        
        # Adjust the tree after deletion to maintain Red-Black Tree properties.
        while x != self.root and x.color == 'black':
            if x == x.parent.left:
                w = x.parent.right
                if w and w.color == 'red':
                    # Perform color flips and rotations to rebalance the tree.
                    self.flip_color(w)
                    self.flip_color(x.parent)
                    self.left_rotate(x.parent)
                    w = x.parent.right
                if w and w.left.color == 'black' and w.right.color == 'black':
                    self.flip_color(w)
                    x = x.parent
                else:
                    if w.right.color == 'black':
                        self.flip_color(w.left)
                        self.flip_color(w)
                        self.right_rotate(w)
                        w = x.parent.right
                    self.flip_color(w)
                    w.color = x.parent.color
                    self.flip_color(x.parent)
                    self.flip_color(w.right)
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.color == 'red':
                    self.flip_color(w)
                    self.flip_color(x.parent)
                    self.right_rotate(x.parent)
                    w = x.parent.left
                if w.right.color == 'black' and w.left.color == 'black':
                    self.flip_color(w)
                    x = x.parent
                else:
                    if w.left.color == 'black':
                        self.flip_color(w.right)
                        self.flip_color(w)
                        self.left_rotate(w)
                        w = x.parent.left
                    self.flip_color(w)
                    w.color = x.parent.color
                    self.flip_color(x.parent)
                    self.flip_color(w.left)
                    self.right_rotate(x.parent)
                    x = self.root
        if x != self.NIL:
            self.flip_color(x) 
        
    
    def flip_color(self, node):
    # Flip the color of the given node in the Red-Black Tree.
    # This method is used in balancing operations after insertions or deletions.

    # Check if the node is not None and not the NIL node
        if node is not None and node != self.NIL:
            original_color = node.color  # Store the original color of the node

            # Flip the color: if the node is red, change it to black, and vice versa
            node.color = 'black' if node.color == 'red' else 'red'

            # If the color of the node was changed, increment the insert_fixup_count
            # The insert_fixup_count may be used to track the number of balancing operations
            if original_color != node.color:
                self.insert_fixup_count += 1
        


    def insert(self, node):
        # Insert a new node into the Red-Black Tree.
        # This method places the new node in the correct position and maintains the tree's properties.
            print(f'Inserting node with book_id: {node.book_id}')
            y = None
            x = self.root
            while x != self.NIL:
                y = x
                if node.book_id < x.book_id:
                    x = x.left
                else:
                    x = x.right
            node.parent = y
            if y is None:
                self.root = node
            elif node.book_id < y.book_id:
                y.left = node
            else:
                y.right = node
            node.left = self.NIL
            node.right = self.NIL
            node.color = 'red'
            self.fix_insert(node)
            print(f'Node with book_id: {node.book_id} inserted')
        

    def fix_insert(self, node):
        # Fix the tree after insertion to maintain Red-Black Tree properties.
        print(f'Fixing insert for node with book_id: {node.book_id}')
        while node != self.root and node.parent.color == 'red':
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle.color == 'red':
                    # Flipping colors of parent, uncle, and grandparent
                    self.flip_color(node.parent)
                    self.flip_color(uncle)
                    self.flip_color(node.parent.parent)
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.left_rotate(node)
                    self.flip_color(node.parent)
                    self.flip_color(node.parent.parent)
                    self.right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle.color == 'red':
                    # Flipping colors of parent, uncle, and grandparent
                    self.flip_color(node.parent)
                    self.flip_color(uncle)
                    self.flip_color(node.parent.parent)
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotate(node)
                    self.flip_color(node.parent)
                    self.flip_color(node.parent.parent)
                    self.left_rotate(node.parent.parent)
            
    

    def left_rotate(self, x):
        # Perform a left rotation around a given node.
            if x is None or x.right is None:
                return "Error: 'None' node encountered in left_rotate"

            y = x.right
            x.right = y.left
            if y.left is not None:
                y.left.parent = x

            y.parent = x.parent
            if x.parent is None:
                self.root = y
            elif x == x.parent.left:
                x.parent.left = y
            else:
                x.parent.right = y

            y.left = x
            x.parent = y
            return "left_rotate executed successfully"
        

    def right_rotate(self, y):
        # Perform a right rotation around a given node.

            if y is None or y.left is None:
                return "Error: 'None' node encountered in right_rotate"

            x = y.left
            y.left = x.right
            if x.right is not None:
                x.right.parent = y

            x.parent = y.parent
            if y.parent is None:
                self.root = x
            elif y == y.parent.right:
                y.parent.right = x
            else:
                y.parent.left = x

            x.right = y
            y.parent = x
            return "right_rotate executed successfully"
        

    
    def print_books_range(self, book_id1, book_id2):
        # Print the details of books in a specified range of IDs.
        book_details_list = []
        self._print_books_range(self.root, book_id1, book_id2, book_details_list)
        return book_details_list
    
    def _print_books_range(self, node, book_id1, book_id2, book_details_list):
# Traverse the Red-Black Tree and collect details of books within the specified book ID range.
    # This method performs an in-order traversal to find and format the book details.

    # Check if the node is not None and not the NIL node

            if node is not None and node != self.NIL:
                # Recursively traverse the left subtree if the range's lower bound is less than the current node's book ID
                if book_id1 < node.book_id:
                    self._print_books_range(node.left, book_id1, book_id2, book_details_list)
                    # Process the current node if its book ID is within the specified range
                if book_id1 <= node.book_id <= book_id2:
                    # Extract only the patron IDs from the reservations heap
                    reservations = [str(res[2]) for res in node.reservation_heap.heap] if node.reservation_heap.heap else []
                    # Format the book details as a multi-line string
                    book_details = (
                        f"BookID = {node.book_id}\n"
                        f"Title = \"{node.book_name}\"\n"
                        f"Author = \"{node.author_name}\"\n"
                        f"Availability = {'Yes' if node.availability_status else 'No'}\n"
                        f"BorrowedBy = {node.borrowed_by if node.borrowed_by else 'None'}\n"
                        f"Reservations = [{', '.join(reservations)}]\n"
                    )
                    book_details_list.append(book_details)
                    # Recursively traverse the right subtree if the range's upper bound is greater than the current node's book ID
                if book_id2 > node.book_id:
                    self._print_books_range(node.right, book_id1, book_id2, book_details_list)
        


    def search(self, node, book_id):
         # Search for a book by its ID in the tree.
            if node is None or node == self.NIL or book_id == node.book_id:
                return node
            if book_id < node.book_id:
                return self.search(node.left, book_id)
            else:
                return self.search(node.right, book_id)
        


class GatorLibrary:

    def __init__(self):
        # Initialize the library with a Red-Black Tree to store book data and a counter for color flips.
        self.rb_tree = RBTree()
        self.color_flip_count = 0  # To keep track of color flip counts during insertions
    
        
    def read_commands_from_file(self, input_filename):
         # Read and return a list of commands from the specified input file.
            with open(input_filename, 'r') as file:
                commands = file.readlines()
            return commands


    def write_output_to_file(self, output_filename, output_lines):
        # Write given output lines to the specified output file.
        with open(output_filename, 'w') as file:
            for line in output_lines:
                file.write(line + '\n')

    def insert_book(self, book_id, book_name, author_name, availability_status):
        
            # Insert book into the Red-Black Tree
            new_book = Node(book_id, book_name, author_name, availability_status, None, BinaryMinHeap())
            self.rb_tree.insert(new_book)
            self.color_flip_count += self.rb_tree.insert_fixup_count  # Update color flip count
            self.rb_tree.insert_fixup_count = 0  # Reset the fix-up count after the operation
            return ""
        
    

    def print_book(self, book_id):
            # Print details of the book with the given book_id
            node = self.rb_tree.search(self.rb_tree.root, book_id)
            if node and node != self.rb_tree.NIL:
                reservations = [str(reservation[2]) for reservation in node.reservation_heap.heap]  # Extract patron IDs
                formatted_reservations = f"[{', '.join(reservations)}]" if reservations else "[]"
                book_details = [
                    f"BookID = {node.book_id}",
                    f"Title = \"{node.book_name}\"",
                    f"Author = \"{node.author_name}\"",
                    f"Availability = {'Yes' if node.availability_status else 'No'}",
                    f"BorrowedBy = {node.borrowed_by if node.borrowed_by else 'None'}",
                    f"Reservations = {formatted_reservations}\n"  # Use the adjusted reservations list
                ]
                return '\n'.join(book_details)
            else:
                return "BookID not found in the Library\n"
       
        
    def print_books(self, book_id1, book_id2):
        # This method will call a method on the RBTree to print the details
        # of all books within the given range.
        if book_id1 > book_id2:
            return "Invalid range: Starting ID is greater than ending ID.\n"

        # Call the helper function on the RBTree with the provided range
        book_details_list = self.rb_tree.print_books_range(book_id1, book_id2)

        # Convert the list of book details into a formatted string
        output_str = "\n".join(book_details_list)
        print(output_str)
        return output_str


    def borrow_book(self, patron_id, book_id, patron_priority):
        node = self.rb_tree.search(self.rb_tree.root, book_id)
        if not node:
            return "BookID not found in the Library\n"

        # Check if the book is already borrowed by the same patron
        if node.borrowed_by == patron_id:
            self.color_flip_count += self.rb_tree.insert_fixup_count  # Update color flip count
            self.rb_tree.insert_fixup_count = 0
            return f"Book {book_id} Already Borrowed by Patron {patron_id}\n"

        # Check if the book is available for borrowing
        if node.availability_status:
            node.availability_status = False
            node.borrowed_by = patron_id
            self.color_flip_count += self.rb_tree.insert_fixup_count
            self.rb_tree.insert_fixup_count = 0 
            return f"Book {book_id} Borrowed by Patron {patron_id}\n"

        # Check reservation limit
        if len(node.reservation_heap.heap) >= 20:
            return f"Unable to reserve book {book_id} for Patron {patron_id}; reservation limit reached.\n"

        # Add patron to the reservation heap
        timestamp = time.time()  # Use timestamp for FIFO order among same-priority reservations
        node.reservation_heap.insert((patron_priority, timestamp, patron_id))
        self.color_flip_count += self.rb_tree.insert_fixup_count  # Update color flip count
        self.rb_tree.insert_fixup_count = 0
        return f"Book {book_id} Reserved by Patron {patron_id}\n"
        

    def return_book(self, patron_id, book_id):
        node = self.rb_tree.search(self.rb_tree.root, book_id)
        if not node or node == self.rb_tree.NIL:
            return "BookID not found in the Library\n"

        # Check if the book is currently borrowed by the given patron
        if not node.availability_status and node.borrowed_by == patron_id:
            # Process the next reservation, if any
            if node.reservation_heap.heap:
                next_patron_info = node.reservation_heap.extract_min()
                next_patron = next_patron_info[2]
                node.borrowed_by = next_patron
                return f"Book {book_id} returned by Patron {patron_id}\nBook {book_id} allotted to Patron {next_patron}\n"
            else:
                # Make the book available if there are no reservations
                node.availability_status = True
                node.borrowed_by = None
                self.color_flip_count += self.rb_tree.insert_fixup_count  # Update color flip count
                self.rb_tree.insert_fixup_count = 0
                return f"Book {book_id} returned by Patron {patron_id}\n"
        else:
            return "Return operation failed. Either the book is not borrowed or it is borrowed by another patron.\n"
        

            
    def find_closest_book(self, target_id):
        closest_books = self._find_closest_book(self.rb_tree.root, target_id, [])
        if closest_books:
            closest_books.sort(key=lambda book: book.book_id)
            return "\n".join([self.print_book(book.book_id) for book in closest_books])
        else:
            return "No books available in the library\n"
        

    def _find_closest_book(self, node, target_id, closest_books):
        
        if node is None or node == self.rb_tree.NIL:
            return closest_books

        if not closest_books:
            closest_books.append(node)
        else:
            current_distance = abs(target_id - node.book_id)
            closest_distance = abs(target_id - closest_books[0].book_id)

            if current_distance < closest_distance:
                closest_books = [node]
            elif current_distance == closest_distance:
                closest_books.append(node)

        if node.book_id < target_id:
            # Check right subtree
            closest_books = self._find_closest_book(node.right, target_id, closest_books)
        else:
            # Check left subtree
            closest_books = self._find_closest_book(node.left, target_id, closest_books)

        return closest_books

    
    
    def delete_book(self, book_id):
        node = self.rb_tree.search(self.rb_tree.root, book_id)
        if node is not None and node != self.rb_tree.NIL:
            # Notify patrons if there are active reservations
            if node.reservation_heap.heap:
                patrons_to_notify = [str(heap_node[2]) for heap_node in node.reservation_heap.heap]
                node.reservation_heap.heap = []  # Clear reservations
                self.rb_tree.delete(node)
                self.color_flip_count += self.rb_tree.insert_fixup_count
                self.rb_tree.insert_fixup_count = 0  # Reset the fix-up count
                return f"Book {book_id} is no longer available. Reservations made by Patrons {','.join(patrons_to_notify)} have been cancelled!\n"
            
            else:
                # Delete the book if there are no reservations
                self.rb_tree.delete(node)
                self.color_flip_count += self.rb_tree.insert_fixup_count
                self.rb_tree.insert_fixup_count = 0 
                return f"Book {book_id} is no longer available.\n"
        else:
            return "BookID not found in the Library.\n"

    def run_command(self, command):
         # Parse and execute a given command string, handling various library operations.
        
        try:
            parts = command.strip().replace(')', '(').split('(')
            cmd_type = parts[0].strip()
            args = [arg.strip().strip('"') for arg in parts[1].split(',') if arg]

            if cmd_type == 'InsertBook':
                args = parts[1].split(',', 3) 
                args = [arg.strip().strip('"') for arg in args]
                try:
                    book_id = int(args[0])
                    book_name = args[1]
                    author_name = args[2]
                    availability_status = args[3] == 'Yes'
                except (ValueError, IndexError) as e:
                    return f"Error in InsertBook arguments: {e}", True
                return self.insert_book(book_id, book_name, author_name, availability_status), True

            elif cmd_type == 'PrintBook':
                book_id = int(args[0])
                return self.print_book(book_id), True
            
            elif cmd_type == 'BorrowBook':
                patron_id = int(args[0])
                book_id = int(args[1])
                patron_priority = int(args[2])
                return self.borrow_book(patron_id, book_id, patron_priority), True
            
            elif cmd_type == 'PrintBooks':
                # Assuming parts[0] is something like 'PrintBooks(1'
                # and parts[1] is something like ' 2)'
                book_id1 = int(args[0].strip())
                book_id2 = int(args[1].strip())
                return self.print_books(book_id1, book_id2), True

            elif cmd_type == 'ReturnBook':
                # Ensure the command is split correctly
                args = [arg.strip().strip('"') for arg in parts[1].split(',')]
                if len(args) < 2:
                    return "Error: Not enough arguments for ReturnBook", True
                try:
                    patron_id = int(args[0].strip())
                    book_id = int(args[1].strip())
                except ValueError as e:
                    return f"Error in ReturnBook arguments: {e}", True
                return self.return_book(patron_id, book_id), True
                
            elif cmd_type == 'FindClosestBook':
                target_id_str = command.split('(')[1].split(')')[0].strip()
                # Check if the '(' and ')' are present and properly formatted
                try:
                    # Extract the number within the parentheses
                    target_id = int(target_id_str)
                    # Attempt to convert the string to an integer
                    target_id = int(target_id_str)
                except (ValueError, IndexError) as e:
                    return f"Error parsing target ID for FindClosestBook: {e}", True

                return self.find_closest_book(target_id), True
                
            elif cmd_type == 'DeleteBook':
                book_id = int(args[0])
                # return book_id
                return self.delete_book(book_id), True
                
            elif cmd_type == 'ColorFlipCount':
                return f"Colour Flip Count: {self.color_flip_count}", True
                
            elif cmd_type == 'Quit':
                return "Program Terminated!!", False  # Signal to stop command execution
            else:
                return f"Unknown command: {cmd_type}", True  # Continue command execution with result
        
        except Exception as e:
            return f"", True  # Continue command execution with error message
    


    # File I/O Handling
    def read_commands_from_file(self, input_filename):
        try:
            with open(input_filename, 'r', encoding='utf-8') as file:
                commands = file.readlines()
            return commands
        except IOError as e:
            print(f"Failed to read file {input_filename}: {e}")
            return []

    def write_output_to_file(self, output_filename, output_lines):
        with open(output_filename, 'w') as file:
            for line in output_lines:
                file.write(line + '\n')


# Example usage of the classes to create a library system
if __name__ == "__main__":
    import sys

    # Check if the correct number of arguments is given
    if len(sys.argv) != 2:
        print("Usage: python gator_library.py <input_filename>")
        sys.exit(1)

    # Get the input filename from command line argument
    input_filename = sys.argv[1]
    # Determine the output filename based on the input filename
    output_filename = input_filename.split('.')[0] + "_output_file.txt"
    
    # Instantiate the library system
    library_system = GatorLibrary()

    # Read commands from the input file
    commands = library_system.read_commands_from_file(input_filename)
    output_lines = []

    # Execute each command and collect the results
    for command in commands:
        result, continue_execution = library_system.run_command(command.strip())
        if not continue_execution:
            output_lines.append(result)
            break
        output_lines.append(result)

    # Write the results to the output file
    library_system.write_output_to_file(output_filename, output_lines)
    print(f"Output written to {output_filename}")
