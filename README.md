# Command Executor

## Overview
This project is a Python-based command execution tool with live spinner animations, real-time log display, and result handling. It is designed to execute a series of shell commands and provide an interactive and visually appealing terminal interface.

## Features
- Executes multiple shell commands sequentially.
- Displays real-time logs of command outputs.
- Shows a live spinner animation for the current running command.
- Color-coded messages for success and failure statuses.

## Requirements
- Python 3.7+
- Compatible with Linux, macOS, and Windows (with proper terminal support).

## Dependencies
The project requires the following Python libraries:

```plaintext
colorama==0.4.6
```



## Installation
1. Clone this repository:

   ```bash
   git clone https://github.com/ILKAY-BRAHIM/LogFusion.git
   cd LogFusion
   ```

2. Install the required Python dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Edit the `commands` list in `main.py` to include the shell commands you want to execute.

   Example:
   ```python
   commands = [
       "curl -s https://example.com/script.sh | bash",
       "echo 'Hello, World!'",
   ]
   ```

2. Run the script:

   ```bash
   python main.py
   ```

3. The terminal will display real-time logs and spinner animations for each command.

## Project Structure
- **`main.py`**: Entry point of the application, orchestrates the execution.
- **`command_executor.py`**: Contains all the core classes (`Spinner`, `Logger`, `OutputReader`, `CommandRunner`, `CommandExecutor`).
- **`requirements.txt`**: Lists Python dependencies.

## Example Output
When running, the terminal will show:
- A spinner animation for the active command.
- Logs of each command's output in real-time.
- Color-coded success or failure messages.

Example:
```
⠋ Running: echo 'Hello, World!'
✔ [Success] : echo 'Hello, World!'
```

## Cross-Platform Compatibility
- ANSI escape codes are used for cursor and line control.
- The `colorama` library ensures proper handling of colored text on Windows terminals.

## License
This project is licensed under the MIT License. See `LICENSE` for more details.

## Contributions
Contributions are welcome! Feel free to open issues or submit pull requests.

## Contact
For questions or feedback, please contact [Brahim Chifour](https://www.linkedin.com/in/brahim-chifour-639652239/).

