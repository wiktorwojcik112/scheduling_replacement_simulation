# Struktura reprezentująca proces lub jego część. Id musi być liczbą większą lub równą 1. -1 może być użyte w celu stworzenia sztucznego nie istniejącego procesu.
class Process:
    def __init__(self, id, arrival_time, duration):
        self.id = id
        self.arrival_time = arrival_time
        self.duration = duration
    
    def __repr__(self):
        # Alternatywna reprezentacja dla procesu w formie tekstowej.
        return f'P{self.id}({self.arrival_time}, {self.arrival_time + self.duration})'

    def __eq__(self, value):
        return self.id == value.id and self.arrival_time == value.arrival_time and self.duration == value.duration