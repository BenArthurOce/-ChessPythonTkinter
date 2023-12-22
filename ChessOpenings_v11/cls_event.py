import tkinter as tk

class EventHandler:
    def __init__(self):
        # Initialize the event handler

        # Create a dictionary to store the widget instances
        self.widgets = {}

    def add_widget(self, widget_name, widget_instance):
        # Add a widget instance to the event handler
        self.widgets[widget_name] = widget_instance

    def handle_event(self, widget_name):
        print("widget name: ", widget_name)
        # Handle the click event for the specified widget
        if widget_name in self.widgets:
            widget = self.widgets[widget_name]
            # Perform specific actions or call methods on the widget instance
            # For example, widget.do_something()

            print(f"Event occurred for widget: {widget_name}")
        else:
            print(f"Widget not found: {widget_name}")