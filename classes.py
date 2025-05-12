"""
Classes for doubly linked list
Used to store characters
"""
# Node Class
class ListNode:
    # Initialize class
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

# Doubly linked list class
class DoublyList:
    # Initialize class
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        self.cur = 0

    # Check if empty method
    def is_empty(self):
        return self.size == 0

    # Get length of list
    def __len__(self):
        return self.size

    # Check if cursor is same as size
    def is_cur_eq_siz(self):
        return self.cur == self.size

    # Update cursor function
    def update_cur(self, val):
        if 0 <= self.cur + val <= self.size:
            self.cur += val

    # Add to the tail of list
    def add_back(self, data):
        # Create a new node
        new_node = ListNode(data)

        # If blank, change head and tail
        if self.is_empty():
            self.head = new_node
            self.tail = new_node

        # Else add to the tail
        else:
            pre = self.tail
            new_node.prev = pre
            self.tail.next = new_node
            self.tail = new_node

        # Add 1 to the size of dataset and cursor
        self.size += 1
        self.cur += 1

    # Insert at cursor
    def insert_at_loc(self, data, loc=None):
        # If loc is None, set loc to the cursor value by default
        if loc is None:
            loc = self.cur

        # Create a new node
        new_node = ListNode(data)

        print(loc)

        # Check if loc is at zero
        if loc == 0:
            # Check if list is empty
            if self.is_empty():
                self.head = new_node
                self.tail = new_node

            # Else add to front
            else:
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node

            # Add 1 to the size of dataset and cursor
            self.size += 1
            self.cur += 1

        # Else if loc is at the tail, add to tail
        elif loc == self.size:
            self.add_back(data)

        # Else iterate
        else:
            # Set a counter and current
            counter = 0
            curr = self.head

            # Find index of cursor
            while counter != loc:
                print(curr.data)
                pre = curr
                curr = curr.next
                counter += 1

            # Insert node
            pre.next = new_node
            curr.prev = new_node
            new_node.next = curr
            new_node.prev = pre

            # Add 1 to the size of dataset and cursor
            self.size += 1
            self.cur += 1

    # Delete last item in dataset
    def delete_back(self):
        # Check if dataset is empty
        if self.is_empty():
            # Then return nothing
            return None

        # Elif check if the size is one
        elif self.size == 1:
            val = self.head.data # Get val to return
            self.tail = None
            self.head = None

        # Else remove the tail
        else:
            val = self.tail.data # Get val to return
            self.tail = self.tail.prev
            self.tail.next = None

        # Subtract 1 to the size of dataset and cursor
        self.size -= 1
        self.cur -= 1

        # Return removed data
        return val

    # Delete at cursor
    def del_at_loc(self, pos=None):
        # Set pos to self.cur by default
        if pos is None:
            pos = self.cur

        # Make sure pos is not at zero
        if pos == 0:
            return None

        # Check if the pos is at the end of the list
        if pos == self.size:
            return self.delete_back()

        # Check if removing from the front
        if pos == 1:
            # If there is only one ele
            if self.head == self.tail:
                # Find val and empty list
                val = self.head.data
                self.head = None
                self.tail = None

            # Else remove head
            else:
                ele = self.head
                val = ele.data
                self.head = ele.next
                self.head.prev = None

            # Subtract 1 to the size
            self.size -= 1

            # Change cursor if pos is less than cur
            if self.cur >= pos:
                self.cur -= 1

            # Return val
            return val

        # Else, iterate
        else:
            # Set a counter and current
            counter = 0
            curr = self.head

            # Find index of cursor
            while counter != pos:
                pre = curr.prev
                val = curr.data # Get value
                curr = curr.next
                counter += 1

            # Delete node
            pre.next = curr
            curr.prev = pre

            # Subtract 1 to the size
            self.size -= 1

            # Change cursor if pos is less than cur
            if self.cur >= pos:
                self.cur -= 1

            # Return removed item
            return val

    # Print method starting from front
    def __str__(self):
        # Convert the list to a string to return
        string = "| HEAD | "
        curr = self.head
        while curr is not None:
            string += f"{str(curr.data)}"
            curr = curr.next
        string += " | TAIL |"

        # Return string
        return string

"""
Classes for stack
Used for undo and redo functionality
"""
# Class for individual nodes in a stack
class StackNode:
    # Initialize node with data and next
    def __init__(self, data):
        self.data = data
        self.next = None

# Class for a whole stack
class Stack:
    # Initialize stack with its top value and size
    def __init__(self):
        self.top = None
        self.size = 0

    # Check if the stack is empty
    def is_empty(self):
        return self.size == 0

    # Push new node to stack
    def push(self, data):
        # Create new node
        new_node = StackNode(data) # Data is an index, not a char

        # Set next and push to top
        new_node.next = self.top
        self.top = new_node

        # Add to size
        self.size += 1

    # Remove last item in stack
    def pop(self):
        # Check if empty
        if self.is_empty():
            return None

        # Else remove top and reset top
        else:
            index = self.top.data # .data is an index
            self.top = self.top.next
            self.size -= 1
            return index

    # Empty a stack
    def empty(self):
        # Set top equal to none, reset size
        self.top = None
        self.size = 0


    # Length function
    def __len__(self):
        return self.size

    # Print stack
    def __str__(self):
        # Set value and curr
        value = "| TOP | "
        curr = self.top

        # Iterate and add to value
        while curr is not None:
            value += str(curr.data)
            curr = curr.next

        # Return value
        return value