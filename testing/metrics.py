from algorithms.scheduling.process import Process
from algorithms.replacement.step import StepState
from collections import defaultdict


def calculate_average_waiting_time(in_processes: list[Process], out_processes: list[Process]) -> float:
    """
    Oblicza średni czas oczekiwania dla dowolnego algorytmu (w tym preemptive),
    zakładając, że out_processes to lista wykonanych odcinków procesów w kolejności ich wykonania.

    Parameters
    ----------
    in_processes  : list[Process]
                    Lista oryginalnych procesów z czasem przybycia i trwania.
    out_processes : list[Process]
                    Lista uruchomień procesów (każdy Process zawiera id, arrival_time = start_time, duration = długość odcinka)
    
    Returns
    -------
    float
    """

    # Mapuj process id na jego odcinki wykonania (czasy rozpoczęcia i długości)
    execution_slices = defaultdict(list)
    for run in out_processes:
        execution_slices[run.id].append((run.arrival_time, run.duration))

    waiting_times = []

    for proc in in_processes:
        pid = proc.id
        arrival = proc.arrival_time
        slices = sorted(execution_slices[pid], key=lambda x: x[0])

        # Czas oczekiwania przed pierwszym wykonaniem procesu
        first_start = slices[0][0]
        wait_time = max(0, first_start - arrival)

        # Dodajemy przerwy między kolejnymi odcinkami wykonania tego samego procesu
        for i in range(1, len(slices)):
            prev_end = slices[i - 1][0] + slices[i - 1][1]
            curr_start = slices[i][0]
            gap = curr_start - prev_end
            wait_time += gap

        waiting_times.append(wait_time)

    return sum(waiting_times) / len(waiting_times)

def calculate_page_faults(steps: list[StepState]) -> int:
    """
    Oblicza średnią liczbę błędów strony dla danego algorytmu zastępowania stron.

    Parameters
    ----------
    steps : list[StepState]
        Lista stanów kroków w trakcie działania algorytmu zastępowania stron.

    Returns
    -------
    int
    """
    return sum(1 if step.missing else 0 for step in steps)

def calculate_max_waiting_time(in_processes: list[Process], out_processes: list[Process]) -> float:
    """
    Oblicza maksymalny czas oczekiwania dla dowolnego algorytmu.
    """
    from collections import defaultdict
    execution_slices = defaultdict(list)
    for run in out_processes:
        execution_slices[run.id].append((run.arrival_time, run.duration))
    max_wait = 0
    for proc in in_processes:
        pid = proc.id
        arrival = proc.arrival_time
        slices = sorted(execution_slices[pid], key=lambda x: x[0])
        first_start = slices[0][0]
        wait_time = max(0, first_start - arrival)
        for i in range(1, len(slices)):
            prev_end = slices[i - 1][0] + slices[i - 1][1]
            curr_start = slices[i][0]
            gap = curr_start - prev_end
            wait_time += gap
        if wait_time > max_wait:
            max_wait = wait_time
    return max_wait

def calculate_average_turnaround_time(in_processes: list[Process], out_processes: list[Process]) -> float:
    """
    Oblicza średni czas realizacji (turnaround time).
    """
    from collections import defaultdict
    execution_slices = defaultdict(list)
    for run in out_processes:
        execution_slices[run.id].append((run.arrival_time, run.duration))
    turnaround_times = []
    for proc in in_processes:
        pid = proc.id
        arrival = proc.arrival_time
        slices = sorted(execution_slices[pid], key=lambda x: x[0])
        finish_time = slices[-1][0] + slices[-1][1]
        turnaround_times.append(finish_time - arrival)
    return sum(turnaround_times) / len(turnaround_times)

def calculate_average_response_time(in_processes: list[Process], out_processes: list[Process]) -> float:
    """
    Oblicza średni czas odpowiedzi (response time).
    """
    from collections import defaultdict
    execution_slices = defaultdict(list)
    for run in out_processes:
        execution_slices[run.id].append((run.arrival_time, run.duration))
    response_times = []
    for proc in in_processes:
        pid = proc.id
        arrival = proc.arrival_time
        slices = sorted(execution_slices[pid], key=lambda x: x[0])
        first_start = slices[0][0]
        response_times.append(max(0, first_start - arrival))
    return sum(response_times) / len(response_times)

def calculate_throughput(in_processes: list[Process], out_processes: list[Process]) -> float:
    """
    Oblicza przepustowość (throughput) jako liczbę zakończonych procesów na jednostkę czasu.
    """
    from collections import defaultdict
    execution_slices = defaultdict(list)
    for run in out_processes:
        execution_slices[run.id].append((run.arrival_time, run.duration))
    finish_times = []
    for proc in in_processes:
        pid = proc.id
        slices = sorted(execution_slices[pid], key=lambda x: x[0])
        finish_time = slices[-1][0] + slices[-1][1]
        finish_times.append(finish_time)
    total_time = max(finish_times) - min(proc.arrival_time for proc in in_processes)
    if total_time == 0:
        return len(in_processes)
    return len(in_processes) / total_time

def calculate_context_switches(out_processes: list[Process]) -> int:
    """
    Oblicza liczbę przełączeń kontekstu na podstawie listy uruchomień procesów.
    """
    if not out_processes:
        return 0
    switches = 0
    prev_id = out_processes[0].id
    for proc in out_processes[1:]:
        if proc.id != prev_id:
            switches += 1
            prev_id = proc.id
    return switches

def calculate_hit_ratio(page_refs: list[int], page_faults: int) -> float:
    """
    Oblicza współczynnik trafień (hit ratio) dla algorytmów zastępowania stron.
    """
    if not page_refs:
        return 0.0
    hits = len(page_refs) - page_faults
    return hits / len(page_refs)