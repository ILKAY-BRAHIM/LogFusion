import os
import sys
import time
import shutil
from colorama import Fore, Style

class Reader:
    def __init__(self, logger, spinner, mutex):
        self.logger = logger
        self.spinner = spinner
        self.mutex = mutex
        self.printing = False
        self.spinner_index = 0
        self.previous_spinner_symbol = self.spinner.get_first_frame()

    def clear_lines(self, num_lines):
        """
        Clears the specified number of lines from the terminal.
        Uses ANSI escape codes for cross-platform compatibility.
        """
        for _ in range(num_lines):
            sys.stdout.write("\033[F")  # Move cursor up one line
            sys.stdout.write("\033[K")  # Clear the line
        sys.stdout.flush()

    def read_output(self):
        while True:
            if self.printing:
                lines_printed = 0
                with self.mutex:
                    if self.spinner_index < len(self.logger.get_messages()):
                        spinner_symbol = f"{Fore.YELLOW}{self.spinner.next_frame()}{Style.RESET_ALL}"
                        current_message = self.logger.get_messages()[self.spinner_index]
                        if self.previous_spinner_symbol in current_message:
                            self.logger.get_messages()[self.spinner_index] = current_message.replace(self.previous_spinner_symbol, spinner_symbol)
                        else:
                            self.logger.get_messages()[self.spinner_index] = spinner_symbol + current_message
                        self.previous_spinner_symbol = spinner_symbol

                    for line in self.logger.get_messages():
                        print(line, flush=True)
                        lines_printed += 1

                time.sleep(0.1)
                self.clear_lines(lines_printed)
            else:
                time.sleep(0.05)