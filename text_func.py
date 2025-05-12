# Display list
def display(li, text_box):
    reset_text(text_box)
    curr = li.head
    while curr is not None:
        set_text(curr.data, text_box)
        curr = curr.next

# Reset text box function
def reset_text(text_box):
    text_box.configure(state="normal")
    text_box.delete("0.0", "end")
    text_box.configure(state="disabled")

# Set text Box function
def set_text(text, text_box):
    text_box.configure(state="normal")
    text_box.insert("end", text)
    text_box.configure(state="disabled")