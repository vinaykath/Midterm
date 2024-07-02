### app/command_processor.py:
The provided code defines a CommandProcessor class that manages and executes commands. Here's a detailed explanation of its functionality:
Initialization
- Constructor (__init__): The CommandProcessor is initialized with a dictionary of basic commands: add, subtract, multiply, and divide. These are instances of respective command classes imported from the app.plugins.commands module.
### Loading Additional Commands ###
- load_commands Method: This method dynamically loads additional command classes from Python files located in the base_command directory (relative to the script's location).
- Directory and File Handling: The directory path is constructed using os.path.join, and all files in this directory are iterated over.
- File Filtering: Only files ending with _command.py are considered.
- Module Loading: For each matching file, the module name is constructed, and the module is loaded using importlib.util.spec_from_file_location and importlib.util.module_from_spec. The module is then executed.
- Class Extraction and Registration: The command class is extracted from the module, capitalizing the filename (minus _command.py) to match the class name. The command object is then instantiated and added to the commands dictionary, with its name being the filename minus _command.py.
### Executing Commands
- execute_command Method: This method retrieves a command object by its name from the commands dictionary and executes it with the provided arguments.
- Error Handling: If the command does not exist, a ValueError is raised.

### Special Command Handling
- Nested Command Class: This nested class defines two special commands: EXIT and UNKNOWN.
- process_command Method: This method processes special commands:
- - EXIT: Raises SystemExit, terminating the program.
- - UNKNOWN: Also raises SystemExit, indicating an unhandled command.
- - Other Commands: Prints a message indicating that the command was processed.
