import time


class Cronometer:

    def __init__(self):

        self.running = False
        self.seconds = 0
        self.last_time = 0

    def start_cronometer(self, seconds=None):

        # Define um novo tempo
        if seconds is not None:
            self.seconds = seconds + 1

        # Inicia ou continua
        if not self.running and self.seconds > 0:

            self.running = True
            self.last_time = time.perf_counter()

    def pause_cronometer(self):

        self.running = False

    def reset_cronometer(self):

        self.running = False
        self.seconds = 0
        self.last_time = 0

    def update(self):

        if self.running:

            current_time = time.perf_counter()

            delta = (
                current_time
                - self.last_time
            )

            self.seconds -= delta

            self.last_time = current_time

            # Impede números negativos
            if self.seconds <= 0:

                self.seconds = 0
                self.running = False

        return self.seconds