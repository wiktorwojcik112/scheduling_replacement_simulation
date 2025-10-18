from algorithms.replacement.step import StepState

# Przypadki testowe dla algorytmu FIFO (First In First Out) zastępowania stron.

fifo = [
    # 1. Basic case
    (([1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5], 3),
     [StepState(1, [], 1, 1), StepState(2, [1], 2, 2), StepState(3, [1, 2], 3, 3),
      StepState(4, [1, 2, 3], 4, 4), StepState(5, [2, 3, 4], 1, 1), StepState(6, [3, 4, 1], 2, 2),
      StepState(7, [4, 1, 2], 5, 5), StepState(8, [1, 2, 5], 1, None), StepState(9, [1, 2, 5], 2, None),
      StepState(10, [1, 2, 5], 3, 3), StepState(11, [2, 5, 3], 4, 4), StepState(12, [5, 3, 4], 5, None)]
    ),

    # 2. Repeating sequence fits in memory
    (([1, 2, 3, 1, 2, 3], 3),
     [StepState(1, [], 1, 1), StepState(2, [1], 2, 2), StepState(3, [1, 2], 3, 3),
      StepState(4, [1, 2, 3], 1, None), StepState(5, [1, 2, 3], 2, None), StepState(6, [1, 2, 3], 3, None)]
    ),

    # 3. One frame only
    (([1, 2, 3, 1, 2], 1),
     [StepState(1, [], 1, 1), StepState(2, [1], 2, 2), StepState(3, [2], 3, 3),
      StepState(4, [3], 1, 1), StepState(5, [1], 2, 2)]
    ),

    # 4. Empty reference string
    (([], 3), []),

    # 5. All pages same
    (([1, 1, 1, 1], 2),
     [StepState(1, [], 1, 1), StepState(2, [1], 1, None), StepState(3, [1], 1, None), StepState(4, [1], 1, None)]
    ),

    # 6. Frame count = ref length
    (([1, 2, 3], 3),
     [StepState(1, [], 1, 1), StepState(2, [1], 2, 2), StepState(3, [1, 2], 3, 3)]
    ),

    # 7. Frame count > ref length
    (([1, 2], 4),
     [StepState(1, [], 1, 1), StepState(2, [1], 2, 2)]
    ),

    # 8. Frequent eviction
    (([1, 2, 3, 4, 5], 2),
     [StepState(1, [], 1, 1), StepState(2, [1], 2, 2), StepState(3, [1, 2], 3, 3),
      StepState(4, [2, 3], 4, 4), StepState(5, [3, 4], 5, 5)]
    )
]