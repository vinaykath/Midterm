import pandas as pd

# Singleton class to manage history of commands
class HistoryManager:
    _instance = None  # Class variable to hold the single instance

    def __new__(cls, *args, **kwargs):
        # Create a new instance if one doesn't exist
        if cls._instance is None:
            cls._instance = super(HistoryManager, cls).__new__(cls)
        return cls._instance

    def __init__(self, file_path='data/history.csv'):
        # Initialize only if not already initialized
        if not hasattr(self, 'initialized'):
            self.file_path = file_path  # Path to the history file
            self.history = self.load_history()  # Load history from file
            self.initialized = True  # Mark as initialized

    def load_history(self):
        try:
            # Load history from CSV file
            return pd.read_csv(self.file_path)
        except FileNotFoundError:
            # Return an empty DataFrame if file not found
            return pd.DataFrame(columns=['command', 'args', 'result'])

    def save_history(self):
        # Save the current history to the CSV file
        self.history.to_csv(self.file_path, index=False)

    def add_record(self, command, args, result):
        # Add a new record to the history
        new_record = pd.DataFrame([{'command': command, 'args': args, 'result': result}])
        self.history = pd.concat([self.history, new_record], ignore_index=True)
        self.save_history()

    def clear_history(self):
        # Clear the history
        self.history = pd.DataFrame(columns=['command', 'args', 'result'])
        self.save_history()
