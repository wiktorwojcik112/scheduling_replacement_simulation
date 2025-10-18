from .process import Process
from .utilities import find_processes_at, find_shortest, calculate_remaining_time, remove_from_list

def sjf(processes: list[Process]):
    """
    Implementacja algorytmu szeregowania procesów SJF (Shorted Job First) w wersji niewywłaszczającej.

    Parameters
    ----------
    processes : list[Process]
                List procesów przychodzących.

    Returns
    -------
    list[Process]
        Lista procesów uporządkowana według czasu ich wywołania według algorytmu szeregowania. W tym kontekście, arrival_time oznacza czas wywołania procesu.
    """

    result = []

    
    # Sortujemy według czasu przybycia żeby przyspieszyć późniejsze przeszukiwania.
    arriving_processes = sorted(processes, key=lambda p: p.arrival_time)

    waiting_list = []
    current_process = None
    time = 0
    
    while True:
        if current_process and calculate_remaining_time(time, current_process) <= 0:
            result.append(current_process)
            current_process = None

            if len(arriving_processes) == 0 and len(waiting_list) == 0:
                break

        now_arriving_processes = find_processes_at(time, arriving_processes)
        waiting_list += now_arriving_processes

        for arriving_process in now_arriving_processes:
            remove_from_list(arriving_process, arriving_processes)

        candidate_process = find_shortest(waiting_list)
        
        if not current_process and candidate_process:
            remove_from_list(candidate_process, waiting_list)
            current_process = candidate_process
            current_process.arrival_time = time

        time += 1

    return result


    