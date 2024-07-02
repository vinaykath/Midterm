# Python Calculator App

## Overview
This Python Calculator App is a simple command-line tool that performs basic arithmetic operations such as addition, subtraction, multiplication, and division. Additionally, it keeps a history of all calculations which can be displayed or cleared as needed.

### Demonstration video link: 
[[Demonstration Video]](https://youtu.be/_U9EveKmf9c)

### Code/ File Explanation

#### Table of Content with Documentation
1) [main.py](./mainpy_readme.md)
2) [app/__init__.py](./app/README.MD)
3) [app/command_processor.py](./app/commandprocess_readme.md)
4) [app/base_command/__init__.py](./app/base_command/Readme.md)
5) [app/plugins/history_manager.py](./app/plugins/readme.md)
6) [app/plugins/commands/__init__.py](./app/plugins/commands/readme.md)
7) [data/history.csv](./data/readme.md)
8) [tests/test_app.py](./tests/testapp_readme.md)
9) [tests/test_command_processor.py](./tests/testcommandprocessor_readme.md)
10) [tests/test_history.py](./tests/testhistory_readme.md)
11) [tests/test_plugin.py](./tests/testplugin_readme.md)

[![Demonstration Video](https://img.youtube.com/vi/_U9EveKmf9c/maxresdefault.jpg)](https://youtu.be/_U9EveKmf9c?si=PbbJ3YCjl65z6UGy)

## Features
- **Addition**: Add two numbers.
- **Subtraction**: Subtract one number from another.
- **Multiplication**: Multiply two numbers.
- **Division**: Divide one number by another.
- **History**: Display and clear the history of all calculations.

### Additional Features:
- **Command-Line Interface (REPL)**
- **Arithmetic Operations:** Supports Add, Subtract, Multiply, and Divide operations.
- **History Management:** Manage calculation history, including loading, saving, clearing, and deleting records through the REPL interface.
- **Extended Functionalities:** Access additional functionalities via dynamically loaded plugins.
- **Plugin System**
- **Flexible Integration:** Allows seamless integration of new commands or features without modifying the core application code.
- **Menu Command:** Lists all available plugin commands for user discoverability and interaction.
- **Calculation History Management with Pandas**
- **Efficient Data Handling:** Uses Pandas for robust management of calculation history.
- **Data Persistence:** Efficient reading and writing of data to CSV files.
- **Professional Logging Practices**
- **Comprehensive Logging:** Records detailed application operations, data manipulations, errors, and informational messages.
- **Severity Levels:** Differentiates log messages by severity (INFO, WARNING, ERROR) for effective monitoring.
- **Dynamic Configuration:** Logging levels and output destinations are configurable via environment variables.
- **Design Patterns for Scalable Architecture**
- **Facade Pattern:** Simplifies the interface for complex Pandas data manipulations.
- **Command Pattern:** Structures commands within the REPL for effective calculation and history management.
- **Factory Method, Singleton, and Strategy Patterns:** Enhance the application's code structure, flexibility, and scalability.


## Installation

### Prerequisites
- Python 3.x

### Steps
1. Clone the repository:
   ```sh
   git clone git@github.com:vinaykath/Midterm.git
    ```
2. Install the required packages:
    ```sh 
    pip install -r requirements.txt
    ```
3. Run the app:
    ```
    python main.py
    ```

## Usage

To start the calculator app, run the following command:

```sh
python main.py
```

### Commands

- #### Add: To add two numbers
    ```
    add <number1> <number2>
    add 1 3 
    ```

- ### Subtract: To subtract one number from another
    ```
    subtract <number1> <number2>
    subtract 5 2
    ```
- ### Multiply: To multiply two numbers
    ```
    multiply <number1> <number2>
    multiply 10 5
    ```

- ### Divide: To divide one number by another
    ```
    divide <number1> <number2>
    divide 10 2
    ```

- ### Show History: To display the history of all calculations
    ```
    show history
    ```

- ### Clear History: To clear the history of all calculations
    ```
    clear history
    ```

- ### Exit: To exit from command prompt
    ```
    exit
    ```


### Fully Running Example:
```
$ python main.py
Available commands: add, subtract, multiply, divide, menu, show history, clear history, exit
Enter command:

> add 1 3
Result: 4

> subtract 4 1
Result: 3

> multiply 2 3
Result: 6

> divide 10 2
Result: 5

> show history
    command         args  result
0       add   [1.0, 2.0]     3.0
1  subtract   [3.0, 1.0]     2.0
2       add   [1.0, 3.0]     4.0
3  subtract   [4.0, 1.0]     3.0
4  multiply   [2.0, 3.0]     6.0
5    divide  [10.0, 2.0]     5.0

> clear history
History cleared.

> show history
No history available.

```