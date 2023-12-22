import tkinter as tk


class Command:
    def execute(self):
        pass


class HelloCommand(Command):
    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self):
        self.receiver.say_hello()


class GoodbyeCommand(Command):
    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self):
        self.receiver.say_goodbye()


class ColorChangeCommand(Command):
    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self):
        self.receiver.change_color()


class Receiver:
    def __init__(self, canvas):
        self.canvas = canvas

    def say_hello(self):
        print("Hello!")

    def say_goodbye(self):
        print("Goodbye!")

    def change_color(self):
        print("Changing color!")
        current_color = self.canvas.cget("bg")
        new_color = "red" if current_color == "white" else "white"
        self.canvas.configure(bg=new_color)


class Invoker:
    def __init__(self):
        self.commands = []

    def add_command(self, command):
        self.commands.append(command)

    def execute_commands(self):
        for command in self.commands:
            command.execute()


class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Command Pattern Example")

        self.receiver1 = Receiver(None)
        self.receiver2 = Receiver(None)
        self.invoker = Invoker()

        # Create a label
        self.label = tk.Label(self, text="Welcome to Command Pattern Example!")
        self.label.pack(padx=10, pady=10)

        # Create a button to say hello using receiver1
        hello_button1 = tk.Button(self, text="Say Hello 1", command=self.say_hello1)
        hello_button1.pack(side=tk.LEFT, padx=10, pady=10)

        # Create a button to say goodbye using receiver1
        goodbye_button1 = tk.Button(self, text="Say Goodbye 1", command=self.say_goodbye1)
        goodbye_button1.pack(side=tk.LEFT, padx=10, pady=10)

        # Create a canvas to change color using receiver1
        canvas1 = tk.Canvas(self, width=200, height=200, bg="white")
        canvas1.pack(padx=10, pady=10)
        canvas1.bind("<Button-1>", lambda event, receiver=self.receiver1: self.change_canvas_color(event, receiver))
        self.receiver1.canvas = canvas1

        # Create a button to say hello using receiver2
        hello_button2 = tk.Button(self, text="Say Hello 2", command=self.say_hello2)
        hello_button2.pack(side=tk.LEFT, padx=10, pady=10)

        # Create a button to say goodbye using receiver2
        goodbye_button2 = tk.Button(self, text="Say Goodbye 2", command=self.say_goodbye2)
        goodbye_button2.pack(side=tk.LEFT, padx=10, pady=10)

        # Create a canvas to change color using receiver2
        canvas2 = tk.Canvas(self, width=200, height=200, bg="white")
        canvas2.pack(padx=10, pady=10)
        canvas2.bind("<Button-1>", lambda event, receiver=self.receiver2: self.change_canvas_color(event, receiver))
        self.receiver2.canvas = canvas2

        # Create a button to execute commands
        execute_button = tk.Button(self, text="Execute Commands", command=self.execute_commands)
        execute_button.pack(padx=10, pady=10)

    def say_hello1(self):
        hello_command = HelloCommand(self.receiver1)
        self.invoker.add_command(hello_command)

    def say_goodbye1(self):
        goodbye_command = GoodbyeCommand(self.receiver1)
        self.invoker.add_command(goodbye_command)

    def say_hello2(self):
        hello_command = HelloCommand(self.receiver2)
        self.invoker.add_command(hello_command)

    def say_goodbye2(self):
        goodbye_command = GoodbyeCommand(self.receiver2)
        self.invoker.add_command(goodbye_command)

    def change_canvas_color(self, event, receiver):
        color_change_command = ColorChangeCommand(receiver)
        self.invoker.add_command(color_change_command)

    def execute_commands(self):
        self.invoker.execute_commands()


if __name__ == "__main__":
    app = Application()
    app.mainloop()



# In this updated example, we have created two instances of the Receiver class, receiver1 and receiver2. Each receiver is associated with its own set of buttons and a canvas widget.

# The Application class now includes buttons for saying hello and goodbye using both receivers. Clicking the buttons adds the respective commands (HelloCommand and GoodbyeCommand) to the invoker's command list, specific to the corresponding receiver.

# Additionally, each canvas is bound to the change_canvas_color method using lambda functions. The method now receives the associated receiver as a parameter, allowing the invoker to add the ColorChangeCommand specific to that receiver.

# A new button, "Execute Commands," has been added to the application. Clicking this button triggers the execution of all the commands stored in the invoker's command list.

# Feel free to modify and enhance the example further according to your specific requirements.