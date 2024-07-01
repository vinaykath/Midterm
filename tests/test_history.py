"""Test history"""
import os
from app.plugins.history_manager import HistoryManager

def test_add_record():
    """Test add record"""
    history = HistoryManager('test_history.csv')  # Create a HistoryManager instance with test file
    history.add_record('add', [1, 2], 3)  # Add a record to history
    assert history.history.iloc[-1]['command'] == 'add'  # Check if the last command is 'add'
    assert history.history.iloc[-1]['result'] == 3  # Check if the last result is 3

def test_clear_history():
    """Test clear history"""
    history = HistoryManager('test_history.csv')  # Create a HistoryManager instance with test file
    history.clear_history()  # Clear history
    assert history.history.empty  # Check if history is empty

def teardown_module():
    """Remove test file"""
    if os.path.exists('test_history.csv'):  # Check if test file exists
        os.remove('test_history.csv')  # Remove the test file
