Project Overview
This project is part of a software engineering graduate course midterm assignment. The goal is to develop an advanced Python-based calculator application that emphasizes professional software development practices. The calculator integrates clean, maintainable code, design patterns, comprehensive logging, dynamic configuration via environment variables, sophisticated data handling with Pandas, and a command-line interface (REPL) for real-time user interaction.

Features:
1. Command-Line Interface (REPL)
2. Arithmetic Operations: Supports Add, Subtract, Multiply, and Divide operations.
3. History Management: Manage calculation history, including loading, saving, clearing, and deleting records through the REPL interface.
4. Extended Functionalities: Access additional functionalities via dynamically loaded plugins.
5. Plugin System
6. Flexible Integration: Allows seamless integration of new commands or features without modifying the core application code.
7. Menu Command: Lists all available plugin commands for user discoverability and interaction.
8. Calculation History Management with Pandas
9. Efficient Data Handling: Uses Pandas for robust management of calculation history.
10. Data Persistence: Efficient reading and writing of data to CSV files.
11. Professional Logging Practices
12. Comprehensive Logging: Records detailed application operations, data manipulations, errors, and informational messages.
13. Severity Levels: Differentiates log messages by severity (INFO, WARNING, ERROR) for effective monitoring.
14. Dynamic Configuration: Logging levels and output destinations are configurable via environment variables.
15. Design Patterns for Scalable Architecture
16. Facade Pattern: Simplifies the interface for complex Pandas data manipulations.
17. Command Pattern: Structures commands within the REPL for effective calculation and history management.
18. Factory Method, Singleton, and Strategy Patterns: Enhance the application's code structure, flexibility, and scalability.