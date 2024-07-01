"""Testing app"""
import os
from unittest import mock
from app import App
from app.command_processor import CommandProcessor
from app.plugins.history_manager import HistoryManager

def test_app_initialization():
    """Test app initialization."""
    app_instance = App()  # Create an instance of the App
    assert isinstance(app_instance, App)  # Check if it is an instance of App

def test_configure_logging():
    """Test logging configuration."""
    app_instance = App()  # Create an instance of the App
    with mock.patch('os.path.exists', return_value=False):
        app_instance.configure_logging()  # Test logging configuration when the file does not exist
    with mock.patch('os.path.exists', return_value=True):
        with mock.patch('logging.config.fileConfig') as mock_file_config:
            app_instance.configure_logging()  # Test logging configuration when the file exists
            mock_file_config.assert_called_once()  # Check if fileConfig was called once

def test_load_environment_variables():
    """Test loading environment variables."""
    app_instance = App()  # Create an instance of the App
    with mock.patch.dict(os.environ, {'TEST_ENV_VAR': 'test_value'}):
        settings = app_instance.load_environment_variables()  # Load environment variables
        assert settings['TEST_ENV_VAR'] == 'test_value'
        # Check if the environment variable is loaded correctly

def test_get_environment_variable():
    """Test getting an environment variable."""
    app_instance = App()  # Create an instance of the App
    with mock.patch.dict(os.environ, {'ENVIRONMENT': 'TESTING'}):
        app_instance = App()  # Create an instance of the App
        assert app_instance.get_environment_variable('ENVIRONMENT') == 'TESTING'
        # Check if the environment variable is retrieved correctly

def test_load_plugins_no_directory():
    """Test plugin loading when directory does not exist."""
    app_instance = App()  # Create an instance of the App
    with mock.patch('os.path.exists', return_value=False):
        app_instance.load_plugins()  # Load plugins when the directory does not exist

def test_load_plugins_with_plugins():
    """Test plugin loading when plugins exist."""
    app_instance = App()  # Create an instance of the App
    with mock.patch('os.path.exists', return_value=True):
        with mock.patch('pkgutil.iter_modules', return_value=[(None, 'plugin', True)]):
            with mock.patch('importlib.import_module') as mock_import_module:
                mock_import_module.return_value = mock.Mock()
                app_instance.load_plugins()
                # Load plugins when plugins exist
                mock_import_module.assert_called_once_with('app.plugins.plugin')
                # Check if the plugin module was imported once

def test_app_start_exit_command(monkeypatch):
    """Test that the REPL exits correctly on 'exit' command."""
    inputs = iter(['exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app_instance = App()  # Create an instance of the App
    with mock.patch.object(app_instance, 'load_plugins'):
        with mock.patch('builtins.print'):
            app_instance.start()  # Start the app and test if it exits on 'exit' command

def test_app_start_unknown_command(monkeypatch):
    """Test how the REPL handles an unknown command before exiting."""
    inputs = iter(['unknown_command', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app_instance = App()  # Create an instance of the App
    with mock.patch.object(app_instance, 'load_plugins'):
        with mock.patch.object(CommandProcessor,'execute_command',side_effect=ValueError('Error')):
            app_instance.start()  # Start the app and test how it handles an unknown command

def test_clear_history_command(monkeypatch):
    """Test clear history command."""
    inputs = iter(['clear history', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app_instance = App()  # Create an instance of the App
    with mock.patch.object(app_instance, 'load_plugins'):
        with mock.patch.object(HistoryManager, 'clear_history') as mock_clear_history:
            app_instance.start()  # Start the app and test if clear history command works
            mock_clear_history.assert_called_once()  # Check if clear_history was called once
