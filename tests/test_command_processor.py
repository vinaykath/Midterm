"""Testing command processor"""
from unittest import mock
import pytest
from app.command_processor import CommandProcessor


def test_execute_command_add():
    """Test add command"""
    processor = CommandProcessor()
    result = processor.execute_command('add', 1, 2)  # Execute 'add' command with arguments 1 and 2
    assert result == 3  # Check if result is 3


def test_execute_command_subtract():
    """Test subtract command"""
    processor = CommandProcessor()
    result = processor.execute_command('subtract', 5, 3)
    # Execute 'subtract' command with arguments 5 and 3
    assert result == 2  # Check if result is 2


def test_execute_command_multiply():
    """Test multiply command"""
    processor = CommandProcessor()
    result = processor.execute_command('multiply', 2, 4)
    # Execute 'multiply' command with arguments 2 and 4
    assert result == 8  # Check if result is 8


def test_execute_command_divide():
    """Test divide command"""
    processor = CommandProcessor()
    result = processor.execute_command('divide', 10, 5)
    # Execute 'divide' command with arguments 10 and 5
    assert result == 2  # Check if result is 2


def test_command_not_found():
    """Test command not found"""
    processor = CommandProcessor()
    with pytest.raises(ValueError):  # Expect ValueError if command is not found
        processor.execute_command('nonexistent_command', 1, 2)  # Execute a non-existent command


def test_execute_command_invalid_command():
    """Test invalid command"""
    processor = CommandProcessor()
    with pytest.raises(ValueError):  # Expect ValueError if command is invalid
        processor.execute_command('invalid', 1, 2)  # Execute an invalid command


def test_execute_command_divide_by_zero():
    """Test divide by zero"""
    processor = CommandProcessor()
    with pytest.raises(ZeroDivisionError):  # Expect ZeroDivisionError when dividing by zero
        processor.execute_command('divide', 10, 0)
        # Execute 'divide' command with zero as an argument


def test_process_command_exit():
    """Test process command with exit"""
    processor = CommandProcessor()
    with pytest.raises(SystemExit):  # Expect SystemExit when processing 'exit' command
        processor.process_command(CommandProcessor.Command.EXIT)  # Process 'exit' command


def test_process_command_unknown():
    """Test process command with unknown"""
    processor = CommandProcessor()
    with pytest.raises(SystemExit):  # Expect SystemExit when processing 'unknown' command
        processor.process_command(CommandProcessor.Command.UNKNOWN)  # Process 'unknown' command


def test_load_commands():
    """Test loading commands from file"""
    with mock.patch('os.listdir', return_value=['add_command.py']):
        # Mock listdir to return a test file
        with mock.patch('importlib.util.spec_from_file_location') as mock_spec:
            mock_module = mock.Mock()
            mock_spec.return_value = mock.Mock(loader=mock.Mock(exec_module=lambda mod: mod))
            with mock.patch('importlib.util.module_from_spec', return_value=mock_module):
                processor = CommandProcessor()
                processor.load_commands()  # Load commands from file
                assert 'add' in processor.commands  # Check if 'add' command is loaded
