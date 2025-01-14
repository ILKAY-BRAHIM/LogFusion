import re

class Logger:
    def __init__(self):
        self.messages = []
        self.ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')

    def add_message(self, message):
        self.messages.append(message)

    def clear_logs(self, num_lines):
        self.messages = self.messages[:-num_lines]

    def get_messages(self):
        return self.messages

    def sanitize(self, text):
        return self.ansi_escape.sub('', text)