import os
import importlib.util
# Import command classes from the commands module
from app.plugins.commands import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand


class CommandProcessor:
    def __init__(self):
        # Initialize the command processor with basic commands
        self.commands = {
            'add': AddCommand(),
            'subtract': SubtractCommand(),
            'multiply': MultiplyCommand(),
            'divide': DivideCommand()
        }
        # Load additional commands from files
        self.load_commands()

    def load_commands(self):
        # Directory where command files are stored
        commands_dir = os.path.join(os.path.dirname(__file__), 'base_command')
        for filename in os.listdir(commands_dir):
            if filename.endswith('_command.py'):  # Look for files ending with '_command.py'
                command_name = filename[:-3]  # Remove '.py' from filename
                module_name = f'commands.{command_name}'  # Create module name
                spec = importlib.util.spec_from_file_location(module_name, os.path.join(commands_dir, filename))
                module = importlib.util.module_from_spec(spec)  # Load the module
                spec.loader.exec_module(module)  # Execute the module
                command_class = getattr(module, command_name.capitalize())  # Get the command class
                self.commands[command_name[:-8]] = command_class()  # Add the command to the commands dictionary

    def execute_command(self, command_name, *args):
        # Get the command object by name
        command = self.commands.get(command_name)
        if not command:  # Check if the command exists
            raise ValueError(f"Command '{command_name}' not found.")
        return command.execute(*args)  # Execute the command with provided arguments
    
    class Command:
        EXIT = "exit"
        UNKNOWN = "unknown"

    def process_command(self, command):
        # Process special commands
        if command == self.Command.EXIT:
            raise SystemExit  # Exit the system
        elif command == self.Command.UNKNOWN:
            raise SystemExit  # Handle unknown command
        else:
            print(f"Command {command} processed")  # Process other commands
