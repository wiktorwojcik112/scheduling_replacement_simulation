from .step import StepState

def lru(references: list[int], n_frames: int) -> list[StepState]:
    """
    Implementacja algorytmu wymiany stron LRU (Least Recently Used).

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

    # A list containing frames ordered by the time since they were 
    # last used (first element is the oldest and the last is the most recent).

    for i, reference in enumerate(references):
        # We report the usage of the frame by moving/adding reference
        # to the end of frames list.

        if reference in frames:
            steps.append(StepState(i+1, frames=frames, needed=reference, missing=None))
            frames.remove(reference)
            frames.append(reference)
        else:
            steps.append(StepState(i+1, frames=frames, needed=reference, missing=reference))
            
            frames.append(reference)

            if len(frames) > n_frames:
                # Zastępujemy najdawniej używaną ramkę.
                frames.pop(0)

    return steps