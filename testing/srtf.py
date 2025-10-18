from algorithms.scheduling.process import Process

# Przypadki testowe dla algorytmu szeregowania SRTF (Shortest Remaining Time First).

srtf = [
    ([Process(1, arrival_time=0, duration=7), Process(2, arrival_time=2, duration=4), Process(3, arrival_time=4, duration=1), Process(4, arrival_time=5, duration=4)],
     [Process(1, arrival_time=0, duration=2), Process(2, arrival_time=2, duration=2), Process(3, arrival_time=4, duration=1), Process(2, arrival_time=5, duration=2), Process(4, arrival_time=7, duration=4), Process(1, arrival_time=11, duration=5)]),

    # Test Case 1: All processes arrive at time 0
    ([Process(1, arrival_time=0, duration=5), Process(2, arrival_time=0, duration=3), Process(3, arrival_time=0, duration=1)],
     [Process(3, arrival_time=0, duration=1), Process(2, arrival_time=1, duration=3), Process(1, arrival_time=4, duration=5)]),

    # Test Case 2: Later shorter process preempts earlier longer one
    ([Process(1, 0, 8), Process(2, 2, 4), Process(3, 3, 2)],
     [Process(1, 0, 2), Process(2, 2, 1), Process(3, 3, 2), Process(2, 5, 3), Process(1, 8, 6)]),

    # Test Case 3: Processes arrive in reverse shortest-first order
    ([Process(1, arrival_time=0, duration=10), Process(2, arrival_time=1, duration=6), Process(3, arrival_time=2, duration=2)],
     [Process(1, arrival_time=0, duration=1), Process(2, arrival_time=1, duration=1), Process(3, arrival_time=2, duration=2), Process(2, arrival_time=4, duration=5), Process(1, arrival_time=9, duration=9)]),

    # Test Case 4: Staggered arrivals with same duration
    ([Process(1, arrival_time=0, duration=3), Process(2, arrival_time=2, duration=3), Process(3, arrival_time=4, duration=3)],
     [Process(1, arrival_time=0, duration=3), Process(2, arrival_time=3, duration=3), Process(3, arrival_time=6, duration=3)]),

    # Test Case 5: One process completely finishes before others arrive
    ([Process(1, arrival_time=0, duration=2), Process(2, arrival_time=3, duration=1), Process(3, arrival_time=4, duration=2)],
     [Process(1, arrival_time=0, duration=2), Process(2, arrival_time=3, duration=1), Process(3, arrival_time=4, duration=2)]),

    # Test Case 6: Continuous preemption as shorter jobs keep arriving
    ([Process(1, arrival_time=0, duration=10), Process(2, arrival_time=1, duration=9), Process(3, arrival_time=2, duration=8), Process(4, arrival_time=3, duration=7)],
     [Process(1, arrival_time=0, duration=10), Process(4, arrival_time=10, duration=7), Process(3, arrival_time=17, duration=8), Process(2, arrival_time=25, duration=9)]),

    # Test Case 7: Idle CPU period before any process arrives
    ([Process(1, arrival_time=3, duration=4), Process(2, arrival_time=5, duration=2)],
     [Process(1, 3, 4), Process(2, 7, 2)])
]