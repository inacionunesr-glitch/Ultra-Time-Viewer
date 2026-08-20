import customtkinter as ctk

from TimeManager import Time
from TimerManager import TimerManager
from CronometerManager import Cronometer


class App:

    def __init__(self):

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.root = ctk.CTk()

        self.root.title("Ultra Time View")
        self.root.geometry("500x400")
        self.root.resizable(False, False)

        # =========================
        # MANAGERS
        # =========================

        self.timer = TimerManager()
        self.cronometer = Cronometer()

        # =========================
        # TÍTULO
        # =========================

        self.title_label = ctk.CTkLabel(
            self.root,
            text="ULTRA TIME VIEW",
            font=("Arial", 26, "bold")
        )

        self.title_label.pack(pady=(20, 5))

        self.subtitle_label = ctk.CTkLabel(
            self.root,
            text="Precise time and date viewer",
            font=("Arial", 13),
            text_color="gray"
        )

        self.subtitle_label.pack(pady=(0, 15))

        # =========================
        # ABAS
        # =========================

        self.tab = ctk.CTkTabview(
            self.root,
            width=440,
            height=280,
            corner_radius=15
        )

        self.tab.add("Precise Time")
        self.tab.add("Current Date")
        self.tab.add("Timer")
        self.tab.add("Cronometer")

        self.tab.set("Precise Time")

        self.tab.pack(
            padx=20,
            pady=10,
            fill="both",
            expand=True
        )

        # =========================
        # PRECISE TIME
        # =========================

        self.time_label = ctk.CTkLabel(
            self.tab.tab("Precise Time"),
            text="00:00:00",
            font=("Consolas", 55, "bold")
        )

        self.time_label.pack(pady=(40, 10))

        self.time_info = ctk.CTkLabel(
            self.tab.tab("Precise Time"),
            text="Current local time",
            font=("Arial", 14),
            text_color="gray"
        )

        self.time_info.pack()

        # =========================
        # CURRENT DATE
        # =========================

        self.date_label = ctk.CTkLabel(
            self.tab.tab("Current Date"),
            text="00/00/0000",
            font=("Arial", 40, "bold")
        )

        self.date_label.pack(pady=(35, 10))

        self.day_label = ctk.CTkLabel(
            self.tab.tab("Current Date"),
            text="Loading...",
            font=("Arial", 20)
        )

        self.day_label.pack()

        # =========================
        # TIMER
        # =========================

        self.timer_label = ctk.CTkLabel(
            self.tab.tab("Timer"),
            text="00:00.00",
            font=("Consolas", 45, "bold")
        )

        self.timer_label.pack(pady=(20, 10))

        self.timer_buttons = ctk.CTkFrame(
            self.tab.tab("Timer"),
            fg_color="transparent"
        )

        self.timer_buttons.pack(pady=10)

        self.start_button = ctk.CTkButton(
            self.timer_buttons,
            text="Start",
            width=110,
            height=40,
            corner_radius=12,
            command=self.start_timer
        )

        self.start_button.grid(
            row=0,
            column=0,
            padx=5
        )

        self.stop_button = ctk.CTkButton(
            self.timer_buttons,
            text="Stop",
            width=110,
            height=40,
            corner_radius=12,
            command=self.stop_timer
        )

        self.stop_button.grid(
            row=0,
            column=1,
            padx=5
        )

        self.reset_button = ctk.CTkButton(
            self.timer_buttons,
            text="Reset",
            width=110,
            height=40,
            corner_radius=12,
            command=self.reset_timer
        )

        self.reset_button.grid(
            row=0,
            column=2,
            padx=5
        )

        # =========================
        # CRONOMETER
        # =========================

        self.cronometer_label = ctk.CTkLabel(
            self.tab.tab("Cronometer"),
            text="00:00:00",
            font=("Consolas", 45, "bold")
        )

        self.cronometer_label.pack(pady=(20, 10))

        self.cronometer_entry = ctk.CTkEntry(
            self.tab.tab("Cronometer"),
            placeholder_text="Seconds",
            width=200,
            height=40,
            justify="center"
        )

        self.cronometer_entry.pack(pady=5)

        self.cronometer_buttons = ctk.CTkFrame(
            self.tab.tab("Cronometer"),
            fg_color="transparent"
        )

        self.cronometer_buttons.pack(pady=10)

        self.start_cronometer_button = ctk.CTkButton(
            self.cronometer_buttons,
            text="Start",
            width=100,
            command=self.start_cronometer
        )

        self.start_cronometer_button.grid(
            row=0,
            column=0,
            padx=5
        )

        self.pause_cronometer_button = ctk.CTkButton(
            self.cronometer_buttons,
            text="Pause",
            width=100,
            command=self.pause_cronometer
        )

        self.pause_cronometer_button.grid(
            row=0,
            column=1,
            padx=5
        )

        self.reset_cronometer_button = ctk.CTkButton(
            self.cronometer_buttons,
            text="Reset",
            width=100,
            command=self.reset_cronometer
        )

        self.reset_cronometer_button.grid(
            row=0,
            column=2,
            padx=5
        )

        # =========================
        # ATUALIZAÇÕES
        # =========================

        self.update_time()
        self.update_timer()
        self.update_cronometer()

    # =========================
    # RELÓGIO E DATA
    # =========================

    def update_time(self):

        self.time_label.configure(
            text=Time.get_time()
        )

        self.date_label.configure(
            text=Time.get_date()
        )

        self.day_label.configure(
            text=Time.get_weekday()
        )

        self.root.after(
            1000,
            self.update_time
        )

    # =========================
    # TIMER
    # =========================

    def start_timer(self):
        self.timer.start_timer()

    def stop_timer(self):
        self.timer.stop_timer()

    def reset_timer(self):

        self.timer.reset_timer()

        self.timer_label.configure(
            text="00:00.00"
        )

    def update_timer(self):

        seconds = self.timer.update()

        minutes = int(seconds // 60)

        remaining_seconds = int(seconds % 60)

        milliseconds = int(
            (seconds % 1) * 100
        )

        self.timer_label.configure(
            text=f"{minutes:02}:{remaining_seconds:02}.{milliseconds:02}"
        )

        self.root.after(
            10,
            self.update_timer
        )

    # =========================
    # CRONOMETER
    # =========================

    def start_cronometer(self):

        try:

            # Se foi digitado um novo tempo
            if self.cronometer_entry.get():

                seconds = int(
                    self.cronometer_entry.get()
                )

                self.cronometer.start_cronometer(
                    seconds
                )

            else:

                # Continua de onde parou
                self.cronometer.start_cronometer()

        except ValueError:
            print("Digite um número válido!")

    def pause_cronometer(self):

        self.cronometer.pause_cronometer()

    def reset_cronometer(self):

        self.cronometer.reset_cronometer()

        self.cronometer_label.configure(
            text="00:00:00"
        )

        self.cronometer_entry.delete(
            0,
            "end"
        )

    def update_cronometer(self):

        seconds = self.cronometer.update()

        hours = int(seconds // 3600)

        minutes = int(
            (seconds % 3600) // 60
        )

        remaining_seconds = int(
            seconds % 60
        )

        self.cronometer_label.configure(
            text=f"{hours:02}:{minutes:02}:{remaining_seconds:02}"
        )

        self.root.after(
            10,
            self.update_cronometer
        )

    def run(self):
        self.root.mainloop()

    def set_icon(self, icon_path):
        self.root.iconbitmap(icon_path)


if __name__ == "__main__":

    app = App()
    app.run()