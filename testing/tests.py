from .fcfs import fcfs
from .sjf import sjf
from .srtf import srtf
from .fifo import fifo
from .lru import lru

def test(name, run, sets, only_results=False):
    """
    Funkcja do wykonywania testów na funkcji wykorzystując listę testów.

    Parameters
    ----------
    name : str
         Nazwa testu.
    run : function
        Funkcja która będzie testowana.
    sets : list[(A, B)]
         Zbiór przypadków testowych. A to dane wejściowe, a B to prawidłowe dane wyjściowe.
    only_results : Bool
                 Jeśli False, to informacje o sukcesie/porażce przypadku testowego zostaną wypisane. Jeśli True, wypisany będzie tylko finalny wynik.
    """


    correct = 0

    for i, (input, output) in enumerate(sets):
        input = input

        if hasattr(input, 'copy') and callable(input.copy):
            input = input.copy()

        if not only_results:
            print(f'Case {i}: ', end='')

        result = None

        if isinstance(input, tuple):
            result = run(*input)
        else:
            result = run(input)

        if result == output:
            correct += 1
            if not only_results:
                print(f'test case {i} succesful')
        elif not only_results:
            print(f'test case {i} failed')
            print(f'    Output: {result}')
            print(f'   Correct: {output}')

    print(f'Testing "{name}" finished [{correct}/{len(sets)}]')
