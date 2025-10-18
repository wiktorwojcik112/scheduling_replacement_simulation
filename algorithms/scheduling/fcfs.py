from .process import Process

def fcfs(processes: list[Process]):
    """
    Implementacja algorytmu szeregowania procesów FCFS (First Come First Serve).

    Parameters
    ----------
    processes : list[Process]
                List procesów przychodzących.

    Returns
    -------
    list[Process]
        Lista procesów uporządkowana według czasu ich wywołania według algorytmu szeregowania. W tym kontekście, arrival_time oznacza czas wywołania procesu.
    """

    # Na początku sortujemy procesy według ich czasu przybycia.
    result = sorted(processes, key=lambda p: p.arrival_time)

    # Następnie musimy zmienić czasy przybycia, który jest interpretowany jako czas faktycznego wykonania, 
    # by uwzględnić, że procesy nie muszą się uruchomić od razu po przybyciu.
    for i in range(1, len(result)):
        result[i].arrival_time = result[i-1].arrival_time + result[i-1].duration

    return result