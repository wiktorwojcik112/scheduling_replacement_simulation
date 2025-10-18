from .process import Process
from .utilities import find_processes_at, find_shortest, calculate_remaining_time, divide_at, remove_from_list

def srtf(processes: list[Process], debug=False):
    """
    Implementacja algorytmu szeregowania procesów SJF (Shorted Job First) w wersji wywłaszczającej. Inaczej nazywany SRTF (Shortest Remaining Time First).

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

    # Sortujemy według czasu przybycia żeby przyspieszyć późniejsze przeszukiwania
    arriving_processes = sorted(processes, key=lambda p: p.arrival_time)

    # Tworzymy listę w której będą procesy, które zostały wywłaszczone lub opóźnione i czekają
    waiting_list = []
    current_process = None
    time = 0

    while True:
        # Obliczamy pozostały czas dla aktywnego procesu. Jeśli takiego nie ma to pozostały czas to nieskończoność.
        remaining_time = float('inf') if not current_process else calculate_remaining_time(time, current_process)

        if remaining_time == 0 and current_process:
            result.append(current_process)
            current_process = None
            remaining_time = float('inf')

            if len(waiting_list) == 0 and len(arriving_processes) == 0:
                break

        # Pobieramy wszystkie procesy, które teraz przybyły i wrzucamy je do listy oczekujących w celu dalszego przetworzenia.
        now_arriving_processes = find_processes_at(time, arriving_processes)
        waiting_list += now_arriving_processes

        # Usuwamy procesy, które przybyły z listy przybywających.
        for arriving_process in now_arriving_processes:
            remove_from_list(arriving_process, arriving_processes)

        candidate_replacement_process = find_shortest(waiting_list)

        if candidate_replacement_process and candidate_replacement_process.duration < remaining_time:
            # Kandydat jest krótszy od aktualnie działającego procesu lub żaden proces nie jest aktywny.
            if current_process:
                # Pewien proces jest aktywny, więc musimy go przerwać i wrzucić jego resztę do listy oczekujących.
                process1, process2 = divide_at(time - current_process.arrival_time, current_process)
                result.append(process1)
                waiting_list.append(process2)

            # Zastępujemy aktualny proces kandydatem.
            current_process = candidate_replacement_process
            current_process.arrival_time = time

            remove_from_list(candidate_replacement_process, waiting_list)

        time += 1

    return result


