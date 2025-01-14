
# LogFusion

## Overview
LogFusion is a Python-based command execution tool that combines live spinner animations, real-time log display, and result handling. This tool allows you to execute shell commands with a visually engaging terminal interface.

## Features
- Executes multiple shell commands sequentially.
- Displays real-time logs of command outputs.
- Shows a live spinner animation for the current running command.
- Provides color-coded messages for success and failure statuses.

## Requirements
- Python 3.7+
- Compatible with Linux, macOS, and Windows (with proper terminal support).

## Installation
Install LogFusion directly from PyPI:

```bash
pip install LogFusion
```

## Usage
Run shell commands with LogFusion as follows:

```bash
LogFusion "echo 'Hello, World!'" "ls -l"
```

LogFusion will execute each command sequentially, displaying real-time logs and animations in the terminal.

### Example
When running:

```bash
LogFusion "echo 'Hello, World!'" "ls -l"
```

The terminal output will show:
```
⠋ Running: echo 'Hello, World!'
✔ [Success] : echo 'Hello, World!'
⠋ Running: ls -l
✔ [Success] : ls -l
```

### Programmatic Usage
You can also use LogFusion in Python scripts:

```python
from LogFusion import LogFusion

commands = ["echo 'Hello, World!'", "ls -l"]
log_fusion = LogFusion()
log_fusion.start(commands)
```

## Project Structure
- **`main.py`**: Command-line entry point for the application.
- **`LogFusion/`**: Contains core modules for logging, spinning animations, command execution, and log reading.
- **`requirements.txt`**: Lists Python dependencies.

## Cross-Platform Compatibility
- ANSI escape codes are used for cursor and line control.
- The `colorama` library ensures proper handling of colored text on Windows terminals.

## License
This project is licensed under the MIT License. See `LICENSE` for more details.

## Contributions
Contributions are welcome! Feel free to open issues or submit pull requests.

## Contact
For questions or feedback, please contact [Brahim Chifour](https://www.linkedin.com/in/brahim-chifour-639652239/).