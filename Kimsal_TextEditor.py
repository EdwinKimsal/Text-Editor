# Import(s)
import tkinter as tk
from pynput.keyboard import Key, Listener
import classes
import text_func

# Run when key is pressed
def on_press(key):
    # Remove cursor
    li.del_at_loc(li.cur)

    # Add key if the key is a single char
    if len(str(key)) == 3:
        if li.is_cur_eq_siz():
            li.add_back(str(key)[1]) # 0: ', 1: char, 2: '
        else:
            li.insert_at_loc(str(key)[1]) # 0: ', 1: char, 2: '
        undo.push(li.cur) # Update undo stack
        redo.empty() # Empty redo stack

    # Add space to list
    elif str(key) == "Key.space":
        if li.is_cur_eq_siz():
            li.add_back(" ")
        else:
            li.insert_at_loc(" ")
        undo.push(li.cur) # Update undo stack
        redo.empty()  # Empty redo stack

    # Del ele from list
    elif str(key) == "Key.backspace":
        if li.is_cur_eq_siz():
            val = li.delete_back()
        else:
            val = li.del_at_loc()
        if val is not None:
            undo.push((li.cur, val))  # Update undo stack, (insert, value)
            redo.empty()  # Empty redo stack

    # Undo
    elif str(key) == r"'\x1a'": # Real string due to slash
        action = undo.pop() # Get action to do that is on top of stack

        # If action is an int, it needs to be removed
        if type(action) == int:
            li.cur = action
            result = (action-1, li.del_at_loc(action)) # Make change, set result to redo stack
            redo.push(result) # Add result to redo stack

        # Else if action is not None, it is a tuple, it needs to be put back
        elif action is not None:
            li.insert_at_loc(action[1], action[0]) # (value, insert)
            result = action[0]+1  # Set result to redo  stack
            redo.push(result) # Add result to redo stack

    # Redo
    elif str(key) == r"'\x19'":
        action = redo.pop()  # Get action to do that is on top of stack

        print(action)

        # If action is an int, it needs to be removed
        if type(action) == int:
            li.cur = action
            result = (action-1, li.del_at_loc(action))  # Make change, set result to undo stack
            undo.push(result)  # Add result to redo stack

        # Else if action is not None, it is a tuple, it needs to be put back
        elif action is not None:
            li.insert_at_loc(action[1], action[0])  # (value, insert)
            result = action[0]+1  # Set result to undo stack
            undo.push(result)  # Add result to redo stack

    # Update cursor value
    elif str(key) == "Key.left":
        li.update_cur(-1)
    elif str(key) == "Key.right":
        li.update_cur(1)

    li.insert_at_loc("|", li.cur)  # Add cursor
    text_func.display(li, text_box)  # Update display

    # TEST
    print("==========")
    print(undo)
    print(redo)
    print("==========")

# FIXME
# BAD, VERY BAD
""" Global vars """
# Create doubly list
li = classes.DoublyList()
# Create undo stack
undo = classes.Stack()
# Create redo stack
redo = classes.Stack()

# Root
root = tk.Tk()
# Creating a Text Box for multi-line text input
text_box = tk.Text(root, width=10, height=4, font=("Courier", 90), state="disabled")
text_box.pack()

# Main function
def main():
    # Set display
    li.insert_at_loc("|", li.cur)  # Add cursor
    text_func.display(li, text_box)  # Update display

    # Start listener
    listener = Listener(on_press=on_press)
    listener.start()
    text_box.mainloop()

    print(li)
    print(len(li))
    print()
    print(undo)
    print(len(undo))


# Call main function
main()