
class StepState:
    def __init__(self, i, frames, needed, missing):
        self.i = i
        self.frames = frames.copy()
        self.needed = needed
        self.missing = missing

    def __repr__(self):
        return f'S{self.i}(frames={self.frames}, needed={self.needed}, missing={self.missing})'
    
    def __eq__(self, value):
        return self.i == value.i and self.frames == value.frames and self.needed == value.needed and self.missing == self.missing

def print_step_table(step_states: list[StepState], n_frames: int):
    """
    Wypisuje tabelę zawierająca informację we wszystkich krokach.

    Parameters
    ----------
    step_states : list[StepState]
    n_frames : int
             Liczba ramek stron.
    """

    print(f' Step | {align("Frames", 2*n_frames - 1)} | Needed | Missing')
    for step in step_states:
        print(f' {align(step.i, 4)} | {align(" ".join([str(frame) for frame in step.frames]), 2*n_frames)} | {align(step.needed, 6)} | {step.missing or "-"}')

def align(text, n):
    return str(text) + ''.join([' ' for _ in range(max(0, n - len(str(text))))])