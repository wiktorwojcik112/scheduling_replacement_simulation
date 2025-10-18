from algorithms.scheduling.process import Process

def make_from_line(line: str):
    """
    Tworzy obiekt analizy na podstawie pojedynczej linii tekstu.

    Parameters
    ----------
    line : str
        Linia tekstu zawierająca dane do analizy.

    Returns
    -------
    list[Process] | (list[int], int)
    Jeśli lina zawiera 1 informację to zwraca listę procesów, 
    jeśli zawiera 2 informacje to zwraca krotkę z listą stron i liczbą ramek.
    """
    parts = line.strip().split(':')
    
    if len(parts) == 1:
        # Przypadek dla procesów
        return [make_process(description) for description in parts[0].strip('[]').split(',')]
    elif len(parts) == 2:
        # Przypadek dla stron
        pages = list(map(int, parts[0].strip('[]').split(',')))
        frames = int(parts[1])
        return (pages, frames)


def make_process(description: str) -> Process:
    """
    Tworzy obiekt Process na podstawie opisu. Na przykład,
    '1 0 5', gdzie 1 oznacza PID, 0 czas przybycia a 5 czas działania.

    Parameters
    ----------
    description : str
        Opis procesu w formacie 'id arrival_time duration'.

    Returns
    -------
    Process
        Obiekt procesu.
    """
    parts = description.split()
    return Process(id=int(parts[0]), arrival_time=int(parts[1]), duration=int(parts[2]))