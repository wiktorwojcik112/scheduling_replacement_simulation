from .step import StepState

def fifo(references: list[int], n_frames: int):
    """
    Implementacja algorytmu wymiany stron FIFO (First In First Out).

    Parameters
    ----------
    references : list[int]
                 Lista odwołań do stron.
        n_frames : int
                 Liczba ramek stron.

    Returns
    -------
    list[StepState]
        Tablica ze stanem po każdym dostępie do pamięci.
    """

    frames = []
    steps = []

    for i, reference in enumerate(references):
        if reference in frames:
            steps.append(StepState(i+1, frames=frames, needed=reference, missing=None))
        else:
            steps.append(StepState(i+1, frames=frames, needed=reference, missing=reference))

            frames.append(reference)

            if len(frames) > n_frames:
                frames.pop(0)

    return steps
        
         
