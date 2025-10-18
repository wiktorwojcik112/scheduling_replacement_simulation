"""
Symulator GUI dla algorytmów szeregowania i zamiany stron

Ten moduł udostępnia graficzny interfejs Tkinter do symulacji
algorytmów szeregowania procesora oraz zamiany stron. Użytkownik może wybrać typ algorytmu,
podać dane wejściowe i zobaczyć wyniki (diagram Gantta lub tabelę stron) wraz z metrykami wydajności.
"""
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.scrolledtext import ScrolledText

from algorithms.scheduling.fcfs import fcfs
from algorithms.scheduling.sjf import sjf
from algorithms.scheduling.srtf import srtf
from algorithms.replacement.fifo import fifo
from algorithms.replacement.lru import lru
from testing.metrics import (
    calculate_average_waiting_time,
    calculate_max_waiting_time,
    calculate_average_turnaround_time,
    calculate_average_response_time,
    calculate_throughput,
    calculate_context_switches,
    calculate_page_faults,
    calculate_hit_ratio
)
from algorithms.scheduling.process import Process

class SimulatorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Symulator algorytmów")
        self.geometry("900x600")
        self.resizable(False, False)
        self.create_widgets()

    def create_widgets(self):
        # Wybór typu algorytmu
        self.alg_type_var = tk.StringVar(value="scheduling")
        type_frame = ttk.LabelFrame(self, text="Typ algorytmu")
        type_frame.pack(fill="x", padx=10, pady=5)
        ttk.Radiobutton(type_frame, text="Szeregowanie procesów", variable=self.alg_type_var, value="scheduling", command=self.update_algorithms).pack(side="left", padx=5)
        ttk.Radiobutton(type_frame, text="Zamiana stron", variable=self.alg_type_var, value="replacement", command=self.update_algorithms).pack(side="left", padx=5)

        # Wybór algorytmu
        self.alg_var = tk.StringVar()
        self.alg_combo = ttk.Combobox(self, textvariable=self.alg_var, state="readonly")
        self.alg_combo.pack(fill="x", padx=10, pady=5)

        # Pola wejściowe
        self.input_frame = ttk.LabelFrame(self, text="Dane wejściowe")
        self.input_frame.pack(fill="x", padx=10, pady=5)
        self.create_input_fields()
        self.update_algorithms()

        # Przycisk uruchomienia
        self.run_btn = ttk.Button(self, text="Symuluj", command=self.run_simulation)
        self.run_btn.pack(pady=10)

        # Wyjście
        self.output_frame = ttk.LabelFrame(self, text="Wynik")
        self.output_frame.pack(fill="both", expand=True, padx=10, pady=5)
        self.output_text = ScrolledText(self.output_frame, height=15, font=("JetBrains Mono", 11))
        self.output_text.pack(fill="both", expand=True)

    def create_input_fields(self):
        for widget in self.input_frame.winfo_children():
            widget.destroy()
        if self.alg_type_var.get() == "scheduling":
            ttk.Label(self.input_frame, text="Czasy przybycia (spacje)").grid(row=0, column=0, sticky="w", padx=5, pady=2)
            self.arrivals_entry = ttk.Entry(self.input_frame, width=50)
            self.arrivals_entry.grid(row=0, column=1, padx=5, pady=2)
            ttk.Label(self.input_frame, text="Czasy trwania (spacje)").grid(row=1, column=0, sticky="w", padx=5, pady=2)
            self.durations_entry = ttk.Entry(self.input_frame, width=50)
            self.durations_entry.grid(row=1, column=1, padx=5, pady=2)
        else:
            ttk.Label(self.input_frame, text="Referencje do stron (spacje)").grid(row=0, column=0, sticky="w", padx=5, pady=2)
            self.pages_entry = ttk.Entry(self.input_frame, width=50)
            self.pages_entry.grid(row=0, column=1, padx=5, pady=2)
            ttk.Label(self.input_frame, text="Liczba ramek").grid(row=1, column=0, sticky="w", padx=5, pady=2)
            self.frames_entry = ttk.Entry(self.input_frame, width=10)
            self.frames_entry.grid(row=1, column=1, padx=5, pady=2, sticky="w")

    def update_algorithms(self):
        # Aktualizuje listę dostępnych algorytmów w zależności od typu
        if self.alg_type_var.get() == "scheduling":
            self.alg_combo['values'] = ("FCFS", "SJF", "SRTF")
            self.alg_combo.current(0)
        else:
            self.alg_combo['values'] = ("FIFO", "LRU")
            self.alg_combo.current(0)
        self.create_input_fields()

    def run_simulation(self):
        # Uruchamia symulację na podstawie danych wejściowych
        self.output_text.delete("1.0", tk.END)
        try:
            alg = self.alg_var.get()
            if self.alg_type_var.get() == "scheduling":
                arrivals = list(map(int, self.arrivals_entry.get().strip().split()))
                durations = list(map(int, self.durations_entry.get().strip().split()))
                if len(arrivals) != len(durations):
                    raise ValueError("Liczba czasów przybycia i trwania musi być taka sama.")
                processes = [Process(i+1, arrivals[i], durations[i]) for i in range(len(arrivals))]
                if alg == "FCFS":
                    out = fcfs([Process(p.id, p.arrival_time, p.duration) for p in processes])
                elif alg == "SJF":
                    out = sjf([Process(p.id, p.arrival_time, p.duration) for p in processes])
                elif alg == "SRTF":
                    out = srtf([Process(p.id, p.arrival_time, p.duration) for p in processes])
                else:
                    raise ValueError("Nieznany algorytm szeregowania.")
                self.output_text.insert(tk.END, f"Wybrany algorytm: {alg}\n")
                self.display_gantt_chart(out)
                self.display_scheduling_metrics(processes, out)
            else:
                pages = list(map(int, self.pages_entry.get().strip().split()))
                frames = int(self.frames_entry.get().strip())
                if alg == "FIFO":
                    steps = fifo(pages, frames)
                elif alg == "LRU":
                    steps = lru(pages, frames)
                else:
                    raise ValueError("Nieznany algorytm zamiany stron.")
                self.output_text.insert(tk.END, f"Wybrany algorytm: {alg}\n")
                self.display_page_table(steps, frames)
                self.display_replacement_metrics(pages, steps)
        except Exception as e:
            messagebox.showerror("Błąd", str(e))

    def display_gantt_chart(self, out_processes):
        # Wyświetla diagram Gantta jako pasek z etykietami procesów i znacznikami czasu
        if not out_processes:
            self.output_text.insert(tk.END, "Brak danych do wyświetlenia Gantta.\n\n")
            return
        min_time = min(proc.arrival_time for proc in out_processes)
        max_time = max(proc.arrival_time + proc.duration for proc in out_processes)
        bar = ""
        time_marks = ""
        last_end = min_time
        positions = [min_time]
        for proc in out_processes:
            # Dodaj spacje jeśli jest luka
            if proc.arrival_time > last_end:
                gap = proc.arrival_time - last_end
                bar += " " * gap * 2
                time_marks += " " * gap * 2
                positions.append(proc.arrival_time)
                last_end = proc.arrival_time
            # Każdy proces ma długość co najmniej 2 znaki
            proc_len = max(2, proc.duration * 2)
            bar += "|" + f"P{proc.id}" + " " * (proc_len - 2)
            positions.append(last_end + proc.duration)
            last_end += proc.duration
        bar += "|"
        # Buduj znaczniki czasu
        time_marks = ""
        last_pos = 0
        for idx, pos in enumerate(positions):
            # Oblicz gdzie wstawić liczbę
            if idx == 0:
                time_marks += str(pos)
                last_pos = len(str(pos))
            else:
                bar_pos = 0
                for proc in out_processes[:idx]:
                    proc_len = max(2, proc.duration * 2)
                    bar_pos += proc_len
                # Korekta o luki
                bar_pos += idx  # za znaki '|'
                spaces = bar_pos - last_pos
                time_marks += " " * spaces + str(pos)
                last_pos += spaces + len(str(pos))
        chart = bar + "\n" + time_marks.rstrip() + "\n"
        self.output_text.insert(tk.END, "Diagram Gantta:\n" + chart + "\n")

    def display_scheduling_metrics(self, in_processes, out_processes):
        # Wyświetla metryki dla algorytmów szeregowania
        avg_wait = calculate_average_waiting_time(in_processes, out_processes)
        max_wait = calculate_max_waiting_time(in_processes, out_processes)
        avg_turn = calculate_average_turnaround_time(in_processes, out_processes)
        avg_resp = calculate_average_response_time(in_processes, out_processes)
        throughput = calculate_throughput(in_processes, out_processes)
        ctx_switches = calculate_context_switches(out_processes)
        metrics = (
            f"Średni czas oczekiwania: {avg_wait:.2f}\n"
            f"Maksymalny czas oczekiwania: {max_wait:.2f}\n"
            f"Średni czas realizacji: {avg_turn:.2f}\n"
            f"Średni czas odpowiedzi: {avg_resp:.2f}\n"
            f"Przepustowość: {throughput:.2f}\n"
            f"Liczba przełączeń kontekstu: {ctx_switches}\n"
        )
        self.output_text.insert(tk.END, metrics + "\n")

    def display_page_table(self, steps, frames):
        # Wyświetla tabelę zamiany stron jako tekst (czcionka o stałej szerokości)
        header = "Krok | " + " ".join([f"F{i+1}" for i in range(frames)]) + " | Potrzebna | Błąd\n"
        table = header
        for step in steps:
            # Dopełnij ramki do pełnej liczby
            padded_frames = list(step.frames) + ["-"] * (frames - len(step.frames))
            frames_str = "  ".join(str(f) for f in padded_frames)
            table += f"{step.i:>4} | {frames_str:<{frames*3-1}} |  {step.needed:^8} | {str(step.missing) if step.missing else '-'}\n"
        self.output_text.insert(tk.END, table + "\n")

    def display_replacement_metrics(self, pages, steps):
        # Wyświetla metryki dla algorytmów zamiany stron
        faults = calculate_page_faults(steps)
        hit = calculate_hit_ratio(pages, faults)
        metrics = (
            f"Liczba błędów stron: {faults}\n"
            f"Współczynnik trafień: {hit:.2f}\n"
        )
        self.output_text.insert(tk.END, metrics + "\n")

if __name__ == "__main__":
    app = SimulatorApp()
    app.mainloop()
