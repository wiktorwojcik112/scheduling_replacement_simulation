from algorithms.scheduling.process import Process

from algorithms.replacement.fifo import fifo
from algorithms.replacement.lru import lru
from algorithms.scheduling.fcfs import fcfs
from algorithms.scheduling.srtf import srtf
from algorithms.scheduling.sjf import sjf

from testing.decoding import make_from_line
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
import copy
import random

def run_analysis(filepath: str):
    """
    Wykonuje analizę na podstawie pliku wejściowego.

    Parameters
    ----------
    filepath : str
        Ścieżka do pliku wejściowego z danymi procesów lub stron.
    """

    data = []

    with open(filepath, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if line.strip():
                data.append(make_from_line(line.strip()))

    if filepath.endswith('.scheduling'):
        analyse_scheduling(data)
    elif filepath.endswith('.replacement'):
        analyse_replacement(data)

def analyse_scheduling(data: list[list[Process]]):
    """
    Wykonuje wszystkie algorytmy planowania dla wszystkich przypadków testowych.
    Tworzy nowy plik results_scheduling.csv z numerem przypadku testowego, nazwą algorytmu i średnim czasem
    oczekiwania dla określonego algorytmu.

    Parameters
    ----------
    data : list[list[Process]]
    """

    results = []
    count = len(data)
    print(f'Running scheduling algorithms for {count} test cases...')
    print('This may take a while, please wait...')

    for i, processes in enumerate(data):
        print(f'Test case [{i + 1}/{count}] with {len(processes)} processes')

        if not processes:
            continue

        alg_results = {}
        for alg_name, alg_func in [('FCFS', fcfs), ('SJF', sjf), ('SRTF', srtf)]:
            # Use deepcopy to avoid in-place mutation of process objects
            in_procs = copy.deepcopy(processes)
            out = alg_func(in_procs)
            avg_wait = calculate_average_waiting_time(processes, out)
            max_wait = calculate_max_waiting_time(processes, out)
            avg_turn = calculate_average_turnaround_time(processes, out)
            avg_resp = calculate_average_response_time(processes, out)
            throughput = calculate_throughput(processes, out)
            ctx_switches = calculate_context_switches(out)
            alg_results[alg_name] = (avg_wait, max_wait, avg_turn, avg_resp, throughput, ctx_switches)

        for alg_name, (avg_wait, max_wait, avg_turn, avg_resp, throughput, ctx_switches) in alg_results.items():
            results.append((i + 1, alg_name, avg_wait, max_wait, avg_turn, avg_resp, throughput, ctx_switches))

    with open('results_scheduling.csv', 'w') as file:
        file.write('Test Case,Algorithm,Average Waiting Time,Max Waiting Time,Average Turnaround Time,Average Response Time,Throughput,Context Switches\n')
        for row in results:
            file.write(','.join(map(str, row)) + '\n')

    print('Analysis complete. Results saved to results_scheduling.csv')

def analyse_replacement(data: list[tuple[list[int], int]]):
    """
    Wykonuje wszystkie algorytmy zastępowania stron dla wszystkich przypadków testowych.
    Tworzy nowy plik results_replacement.csv z numerem przypadku testowego, nazwą algorytmu i liczbą błędów strony.

    Parameters
    ----------
    data : list[tuple[list[int], int]]
        Lista przypadków testowych, gdzie każdy przypadek to krotka zawierająca listę stron i liczbę ramek.
    """

    results = []
    count = len(data)
    print(f'Running page replacement algorithms for {count} test cases...')
    print(f'Frame count set to {data[0][1]} for all cases.')
    print('This may take a while, please wait...')

    for i, (pages, frames) in enumerate(data):
        print(f'Test case [{i + 1}/{count}] with {len(pages)} pages')

        fifo_steps = fifo(pages, frames)
        fifo_faults = calculate_page_faults(fifo_steps)
        fifo_hit = calculate_hit_ratio(pages, fifo_faults)

        lru_steps = lru(pages, frames)
        lru_faults = calculate_page_faults(lru_steps)
        lru_hit = calculate_hit_ratio(pages, lru_faults)

        results.append((i + 1, 'FIFO', fifo_faults, fifo_hit))
        results.append((i + 1, 'LRU', lru_faults, lru_hit))

    with open('results_replacement.csv', 'w') as file:
        file.write('Test Case,Algorithm,Page Faults,Hit Ratio\n')
        for row in results:
            file.write(','.join(map(str, row)) + '\n')

    print('Analysis complete. Results saved to results_replacement.csv')

def analyse_belady_paradox(reference: list[int], min_frames: int, max_frames: int):
    """
    Analizuje paradoks Belady'ego dla podanego ciągu odwołań stron.
    Tworzy plik CSV z liczbą błędów stron dla różnych liczby ramek (FIFO i LRU).

    Parameters
    ----------
    reference : list[int]
        Ciąg odwołań do stron.
    min_frames : int
        Minimalna liczba ramek.
    max_frames : int
        Maksymalna liczba ramek.
    """
    results = []
    print(f'Analysing Belady\'s paradox for frame counts {min_frames} to {max_frames}...')
    for frames in range(min_frames, max_frames + 1):
        fifo_steps = fifo(reference, frames)
        fifo_faults = calculate_page_faults(fifo_steps)
        lru_steps = lru(reference, frames)
        lru_faults = calculate_page_faults(lru_steps)
        results.append((frames, fifo_faults, lru_faults))
        print(f'Frames: {frames}, FIFO faults: {fifo_faults}, LRU faults: {lru_faults}')
    with open('results_belady.csv', 'w') as file:
        file.write('Frame Count,FIFO Page Faults,LRU Page Faults\n')
        for row in results:
            file.write(','.join(map(str, row)) + '\n')
    print('Belady analysis complete. Results saved to results_belady.csv')
