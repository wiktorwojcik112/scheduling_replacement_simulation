from algorithms.scheduling.process import Process

# Przypadki testowe dla algorytmu szeregowania FCFS (First Come First Served).

fcfs = [
    ([Process(1, arrival_time=0, duration=24), Process(2, arrival_time=1, duration=3), Process(3, arrival_time=3, duration=3)], 
     [Process(1, arrival_time=0, duration=24), Process(2, arrival_time=24, duration=3), Process(3, arrival_time=27, duration=3)]),

    # 1. Strict arrival order
    ([Process(1, 0, 4), Process(2, 2, 3), Process(3, 4, 1)],
     [Process(1, 0, 4), Process(2, 4, 3), Process(3, 7, 1)]),

    # 2. All processes arrive at time 0
    ([Process(1, 0, 5), Process(2, 0, 2), Process(3, 0, 1)],
     [Process(1, 0, 5), Process(2, 5, 2), Process(3, 7, 1)]),

    # 3. Idle time before first process
    ([Process(1, 3, 2), Process(2, 5, 4)],
     [Process(1, 3, 2), Process(2, 5, 4)]),

    # 4. Overlapping arrivals
    ([Process(1, 0, 3), Process(2, 1, 2), Process(3, 1, 1)],
     [Process(1, 0, 3), Process(2, 3, 2), Process(3, 5, 1)]),

    # 5. Back-to-back arrivals
    ([Process(1, 0, 2), Process(2, 2, 2), Process(3, 4, 2)],
     [Process(1, 0, 2), Process(2, 2, 2), Process(3, 4, 2)]),

    # 6. Long duration first delays all others
    ([Process(1, 0, 10), Process(2, 1, 1), Process(3, 2, 1)],
     [Process(1, 0, 10), Process(2, 10, 1), Process(3, 11, 1)]),

    # 7. Simultaneous arrivals with different durations
    ([Process(1, 0, 5), Process(2, 0, 3), Process(3, 0, 1)],
     [Process(1, 0, 5), Process(2, 5, 3), Process(3, 8, 1)]),
]
