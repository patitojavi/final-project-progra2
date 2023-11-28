class Logger:
    def __init__(self, filename="logMovimiento.txt"):
        self.filename = filename

    def log_event(self, event):
        with open(self.filename, "a") as log_file:
            log_file.write(f"{event}\n")

logger = Logger()