import time


class TimerManager:

    def __init__(self):
        self.running = False
        self.seconds = 0
        self.last_time = 0

    def start_timer(self):

        # Evita reiniciar o cronômetro
        # caso Start seja clicado novamente
        if not self.running:
            self.running = True
            self.last_time = time.perf_counter()

    def stop_timer(self):
        self.running = False

    def reset_timer(self):
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

            self.seconds += delta

            self.last_time = current_time

        return self.seconds