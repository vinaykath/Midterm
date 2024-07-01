import logging
from app.base_command import Command

# Define AddCommand class
class AddCommand(Command):
    def execute(self, *args):
        logging.info("Addition")  # Log addition operation
        return sum(args)  # Return the sum of arguments

# Define SubtractCommand class
class SubtractCommand(Command):
    def execute(self, *args):
        result = args[0]  # Start with the first argument
        for num in args[1:]:
            result -= num  # Subtract each subsequent argument
        return result

# Define MultiplyCommand class
class MultiplyCommand(Command):
    def execute(self, *args):
        result = 1  # Start with 1
        for num in args:
            result *= num  # Multiply each argument
        return result

# Define DivideCommand class
class DivideCommand(Command):
    def execute(self, *args):
        result = args[0]  # Start with the first argument
        for num in args[1:]:
            result /= num  # Divide by each subsequent argument
        return result
