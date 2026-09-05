import socket
import threading
from tkinter import *
from tkinter import messagebox


def send_message():
    message = message_entry.get()

    if message == "":
        return

    try:
        chat_list.insert(END, "Client: " + message)
        message_entry.delete(0, END)

        client_socket.send(message.encode("utf-8"))

        if message.lower() == "bye":
            close_chat()

    except:
        messagebox.showerror("Error", "Could not send the message")


def receive_message():
    while True:
        try:
            message = client_socket.recv(50).decode("utf-8")

            if message.lower() == "bye":
                chat_list.insert(END, "Server disconnected")
                close_chat()
                break

            chat_list.insert(END, "Server: " + message)

        except:
            break


def close_chat():
    try:
        client_socket.close()
    except:
        pass

    root.destroy()


# Creating the main window
root = Tk()
root.title("Chat Application - Client Side")
root.geometry("400x500")


# Chat area
chat_frame = Frame(root)
chat_frame.pack(fill="both", expand=True, padx=10, pady=10)

scrollbar = Scrollbar(chat_frame)
scrollbar.pack(side=RIGHT, fill=Y)

chat_list = Listbox(
    chat_frame,
    yscrollcommand=scrollbar.set,
    font=("Arial", 10)
)
chat_list.pack(side=LEFT, fill="both", expand=True)

scrollbar.config(command=chat_list.yview)

chat_list.insert(END, "------ YOUR CHAT HISTORY ------")
chat_list.itemconfig(0, fg="blue")


# Message input
message_entry = Entry(root, font=("Arial", 11))
message_entry.pack(fill="x", padx=10, pady=5)


# Send button
button_frame = Frame(root)
button_frame.pack(side=BOTTOM, fill="x", pady=10)

send_button = Button(
    button_frame,
    text="Send",
    bg="#4CAF50",
    fg="white",
    width=12,
    command=send_message
)
send_button.pack(side=LEFT, padx=20, expand=True)


# Connecting to the server
try:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    host = socket.gethostname()
    port = 12345

    client_socket.connect((host, port))

    chat_list.insert(END, "Connected to server!")

    receive_thread = threading.Thread(target=receive_message)
    receive_thread.daemon = True
    receive_thread.start()

except Exception as error:
    messagebox.showerror("Error", f"Connection failed: {error}")
    root.destroy()


# Close the application when the window is closed
root.protocol("WM_DELETE_WINDOW", close_chat)

root.mainloop()
