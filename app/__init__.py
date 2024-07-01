import os
import pkgutil
import importlib
# Import necessary modules and classes
from .command_processor import CommandProcessor
from dotenv import load_dotenv
import logging
import logging.config
import importlib.util
from app.plugins.history_manager import HistoryManager

class App:
    def __init__(self):
        # Create logs directory if it doesn't exist
        os.makedirs('logs', exist_ok=True)
        self.configure_logging()  # Set up logging
        load_dotenv()  # Load environment variables from .env file
        self.settings = self.load_environment_variables()  # Load environment variables into settings
        self.settings.setdefault('ENVIRONMENT', 'PRODUCTION')  # Default to 'PRODUCTION' if not set
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)  # Create a logger

    def configure_logging(self):
        # Configure logging from file if available, otherwise use basic config
        logging_conf_path = 'logging.conf'
        if os.path.exists(logging_conf_path):
            logging.config.fileConfig(logging_conf_path, disable_existing_loggers=False)
        else:
            logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        logging.info("Logging configured.")

    def load_environment_variables(self):
        # Load environment variables into a dictionary
        settings = {key: value for key, value in os.environ.items()}
        logging.info("Environment variables loaded.")
        return settings

    def get_environment_variable(self, env_var: str = 'ENVIRONMENT'):
        # Get a specific environment variable
        return self.settings.get(env_var, None)

    def load_plugins(self):
        # Load plugins from the specified directory
        plugins_package = 'app.plugins'
        plugins_path = plugins_package.replace('.', '/')
        if not os.path.exists(plugins_path):
            logging.warning(f"Plugins directory '{plugins_path}' not found.")
            return
        for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_path]):
            if is_pkg:
                try:
                    # Import the plugin module
                    plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
                    self.register_plugin_commands(plugin_module, plugin_name)  # Register plugin commands
                except ImportError as e:
                    logging.error(f"Error importing plugin {plugin_name}: {e}")

    def register_plugin_commands(self, plugin_module, plugin_name):
        # Register commands from the plugin module
        for item_name in dir(plugin_module):
            item = getattr(plugin_module, item_name)
            if isinstance(item, type) and issubclass(item, CommandProcessor.Command) and item is not CommandProcessor.Command:
                self.command_handler.register_command(plugin_name, item())  # Register the command
                logging.info(f"Command '{plugin_name}' from plugin '{plugin_name}' registered.")

    def start(self):
        # Start the application
        self.load_plugins()  # Load plugins
        processor = CommandProcessor()  # Create a command processor
        history_manager = HistoryManager()  # Create a history manager
        logging.info("Application started. Type 'exit' to exit.")
        environment = os.getenv("ENVIRONMENT", "development")  # Get the environment
        self.logger.info(f"Running in {environment} environment")

        print("Available commands: add, subtract, multiply, divide, menu, show history, clear history, exit")
        
        while True:
            user_input = input("Enter command: ")  # Get user input
            if user_input.lower() in ['exit', 'quit']:
                break
            if user_input.lower() == 'menu':
                print("Available commands: add, subtract, multiply, divide, menu, show history, clear history, exit")
                continue
            if user_input.lower() == 'show history':
                print(history_manager.history)  # Show command history
                continue
            if user_input.lower() == 'clear history':
                history_manager.clear_history()  # Clear command history
                print(history_manager.history)
                continue
            parts = user_input.split()
            command_name = parts[0]  # Get command name
            args = []
            for part in parts[1:]:
                try:
                    args.append(float(part))  # Convert arguments to float
                except ValueError as e:
                    raise ValueError(f"Could not convert string to float: '{part}'") from e
            try:
                result = processor.execute_command(command_name, *args)  # Execute the command
                self.logger.info(f"Executed command: {command_name} with arguments {args}. Result: {result}")
                history_manager.add_record(command_name, args, result)  # Add command to history
                print(f"Result: {result}")
            except ValueError as e:  # Handle invalid command
                self.logger.error(f"ValueError: {e}")
                print(e)
            except Exception as e:  # Handle other errors
                self.logger.error(f"Exception: {e}")
                print(f"An error occurred: {e}")
            finally:
                logging.info("Application shutdown.")  # Log shutdown message

if __name__ == "__main__":
    app = App()
    app.start()
