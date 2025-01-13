import subprocess
import time
from colorama import Fore, Style, init
import os

class Runner:
    def __init__(self, logger, output_reader, mutex):
        self.logger = logger
        self.output_reader = output_reader
        self.mutex = mutex
        init(autoreset=True)

    def run_commands(self, commands):
        for cmd in commands:
            with self.mutex:
                self.logger.add_message(f"Running: {cmd}")
                self.output_reader.printing = True

            process = subprocess.Popen(
                cmd,
                shell=True if os.name != 'nt' else False,
                stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True
            )

            logs = []
            while True:
                output = process.stdout.readline()
                if output == "" and process.poll() is not None:
                    break
                if output:
                    logs.append(output.rstrip('\n'))
                    if len(logs) > 1:
                        with self.mutex:
                            clean_log = self.logger.sanitize(logs[-2])
                            self.logger.add_message(f" {Fore.LIGHTBLACK_EX}{clean_log}{Style.RESET_ALL}")

            exit_code = process.returncode
            total_lines_to_clear = len(logs)

            with self.mutex:
                self.logger.clear_logs(total_lines_to_clear)
                if exit_code == 0:
                    self.logger.add_message(f"{Fore.GREEN}✔ [Success] : {Style.RESET_ALL}{cmd}")
                else:
                    self.logger.add_message(f"{Fore.RED}[Failed]  : {Style.RESET_ALL}{cmd}")

            self.output_reader.spinner_index += 1

        self.output_reader.printing = False
        time.sleep(0.1)