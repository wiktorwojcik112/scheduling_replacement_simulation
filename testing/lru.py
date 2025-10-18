from algorithms.replacement.step import StepState

# Przypadki testowe dla algorytmu LRU (Least Recently Used) zastępowania stron.

lru = [
  # Test case 0
    (([1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5], 3),
     [StepState(1, [], 1, 1), StepState(2, [1], 2, 2), StepState(3, [1, 2], 3, 3),
      StepState(4, [1, 2, 3], 4, 4), StepState(5, [2, 3, 4], 1, 1), StepState(6, [3, 4, 1], 2, 2),
      StepState(7, [4, 1, 2], 5, 5), StepState(8, [1, 2, 5], 1, None), StepState(9, [2, 5, 1], 2, None),
      StepState(10, [5, 1, 2], 3, 3), StepState(11, [1, 2, 3], 4, 4), StepState(12, [2, 3, 4], 5, 5)]),

  # Test case 1
    (([1, 2, 3, 1, 2, 3], 3),
     [StepState(1, [], 1, 1), StepState(2, [1], 2, 2), StepState(3, [1, 2], 3, 3),
      StepState(4, [1, 2, 3], 1, None), StepState(5, [2, 3, 1], 2, None), StepState(6, [3, 1, 2], 3, None)]),

  # Test case 2
    (([1, 2, 3, 1, 2], 1),
     [StepState(1, [], 1, 1), StepState(2, [1], 2, 2), StepState(3, [2], 3, 3),
      StepState(4, [3], 1, 1), StepState(5, [1], 2, 2)]),

  # Test case 3
    (([], 3), []),

  # Test case 4
    (([1, 1, 1, 1], 2),
     [StepState(1, [], 1, 1), StepState(2, [1], 1, None), StepState(3, [1], 1, None), StepState(4, [1], 1, None)]),

  # Test case 5
    (([1, 2, 3], 3),
     [StepState(1, [], 1, 1), StepState(2, [1], 2, 2), StepState(3, [1, 2], 3, 3)]),

  # Test case 6
    (([1, 2], 4),
     [StepState(1, [], 1, 1), StepState(2, [1], 2, 2)]),

  # Test case 7
    (([1, 2, 3, 1, 4], 3),
     [StepState(1, [], 1, 1), StepState(2, [1], 2, 2), StepState(3, [1, 2], 3, 3),
      StepState(4, [1, 2, 3], 1, None), StepState(5, [2, 3, 1], 4, 4)])
]