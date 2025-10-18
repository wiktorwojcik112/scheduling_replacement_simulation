from algorithms.scheduling.process import Process

# Przypadki testowe dla algorytmu szeregowania SJF (Shortest Job First).

sjf = [
    ([Process(1, arrival_time=0, duration=7), Process(2, arrival_time=2, duration=4), Process(3, arrival_time=4, duration=1), Process(4, arrival_time=5, duration=4)],
     [Process(1, arrival_time=0, duration=7), Process(3, arrival_time=7, duration=1), Process(2, arrival_time=8, duration=4), Process(4, arrival_time=12, duration=4)]),
     
    # 1. Basic ordering by shortest duration
    ([Process(1, 0, 8), Process(2, 1, 4), Process(3, 2, 2)],
     [Process(1, 0, 8), Process(3, 8, 2), Process(2, 10, 4)]),

    # 2. All processes arrive at 0
    ([Process(1, 0, 6), Process(2, 0, 3), Process(3, 0, 1)],
     [Process(3, 0, 1), Process(2, 1, 3), Process(1, 4, 6)]),

    # 3. Later shorter process waits
    ([Process(1, 0, 5), Process(2, 2, 2)],
     [Process(1, 0, 5), Process(2, 5, 2)]),

    # 4. Delayed process gets picked for short job
    ([Process(1, 0, 5), Process(2, 3, 1), Process(3, 3, 2)],
     [Process(1, 0, 5), Process(2, 5, 1), Process(3, 6, 2)]),

    # 5. Tie in duration → pick by arrival time
    ([Process(1, 0, 4), Process(2, 1, 2), Process(3, 2, 2)],
     [Process(1, 0, 4), Process(2, 4, 2), Process(3, 6, 2)]),

    # 6. Idle CPU before first process
    ([Process(1, 3, 2), Process(2, 5, 1)],
     [Process(1, 3, 2), Process(2, 5, 1)]),

    # 7. Out-of-order arrivals with shortest durations
    ([Process(1, 2, 6), Process(2, 0, 3), Process(3, 1, 1)],
     [Process(2, 0, 3), Process(3, 3, 1), Process(1, 4, 6)]),
]
