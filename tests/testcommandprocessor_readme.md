### tests/test_command_processor.py
This code contains unit tests for a CommandProcessor class, testing various command functionalities using pytest and unittest.mock. Here's a breakdown:

1) **Command Execution Tests:** Four tests (test_execute_command_add, test_execute_command_subtract, test_execute_command_multiply, test_execute_command_divide) verify basic arithmetic operations (add, subtract, multiply, divide) of the CommandProcessor.
2) **Error Handling Tests:** Two tests (test_command_not_found, test_execute_command_invalid_command) ensure that appropriate errors (ValueError) are raised for non-existent and invalid commands.
3) **Edge Case Tests:** test_execute_command_divide_by_zero checks that a ZeroDivisionError is raised when dividing by zero.
4) **Exit Command Tests:** test_process_command_exit and test_process_command_unknown validate that processing exit and unknown commands result in a SystemExit.
5) **Command Loading Test:** test_load_commands mocks file operations (os.listdir, module loading with importlib) to verify that commands can be loaded dynamically from files.
