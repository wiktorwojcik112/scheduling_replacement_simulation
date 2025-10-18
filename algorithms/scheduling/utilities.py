from .process import Process
from typing import Union

def calculate_remaining_time(current_time: int, process: Process):
    """
    Zwraca pozostały czas do wykonania procesu.

    Parameters
    ----------
    current_time : int
        Czas względem którego obliczony zostanie czas pozostały.
         process : Process

    Returns
    -------
    int
        Czas pozostały do wykonania procesu.
    """
    return process.arrival_time + process.duration - current_time


def remove_from_list(process: Union[Process, None], processes: list[Process]):
    """
    Usuwa proces z listy, jeśli taki się w liście znajduje.

    Parameters
    ----------
      process : Process|None
    processes : list[Process]
    """

    if not process:
        return

    for i, c_process in enumerate(processes):
        if c_process == process:
            processes.pop(i)
            break



def divide_at(time: int, process: Process):
    """
    Zwraca proces podzielony na dwa o określonym punkcie przecięcia.

    Parameters
    ----------
       time : int
        Punkt przecięcia procesów.
    process : Process

    Returns
    -------
    (Process, Process)
        Dwa procesy będące wynikiem podziału procesu.
    """
    
    return Process(process.id, arrival_time=process.arrival_time, duration=time), Process(process.id, arrival_time=process.arrival_time + time + 1, duration=process.duration - time)


def find_shortest(processes: list[Process]):
    """
    Znajduje najkrótszy proces w liście.

    Parameters
    ----------
    processes : list[Process]

    Returns
    -------
    None or Process
        Zwraca None jeśli lista jest pusta. W innym przypadku zwraca najkrótszy proces.
    """

    current_shortest = None

    for process in processes:
        if not current_shortest:
            current_shortest = process
            continue

        if process.duration < current_shortest.duration:
            current_shortest = process 

    return current_shortest


def find_processes_at(time: int, processes: list[Process]):
    """
    Znajduje i zwraca procesy, który przybyły o czasie time.

    Parameters
    ----------
         time : int
    processes : list[Process]

    Returns
    -------
    [Process]
    """

    arriving_processes = []

    for process in processes:
        if time == process.arrival_time:
            arriving_processes.append(process)
        
        if time < process.arrival_time:
            return arriving_processes
        
    return arriving_processes

