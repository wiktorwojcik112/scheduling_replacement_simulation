from algorithms.scheduling.fcfs import fcfs
from algorithms.scheduling.srtf import srtf
from algorithms.scheduling.sjf import sjf

from algorithms.replacement.fifo import fifo
from algorithms.replacement.lru import lru

import testing.analysis as analysis
import testing.tests as tests
from testing.generate import generate_file

import sys

def dev():
    from testing.fcfs import fcfs
    from testing.srtf import srtf
    from testing.sjf import sjf

    print('FCFS average: ' + str(analysis.calculate_average_waiting_time(fcfs[0][0], fcfs[0][1])))
    print('SRTF average: ' + str(analysis.calculate_average_waiting_time(srtf[0][0], srtf[0][1])))
    print('SJF average: ' + str(analysis.calculate_average_waiting_time(sjf[0][0], sjf[0][1])))


def print_help():
    print('''Usage: main.py <command> <options>

    Commands:
        list - Prints available algorithms.
        test [--details] - Runs builtin tests for each algoritm.
        generate processes <name> <n> - Generates a file with n random process sets.
        generate pages <filepath> <n> [<k>] - Generates a file with n random page references, each with k or random (k == -1) number of frames.
        run <filepath> - Runs analysis on the given file by calculating average waiting time for scheduling algorithms or page faults for page replacement algorithms.
        belady-paradox <references> <min_frames> <max_frames> - Runs Belady's paradox test for page replacement algorithms with given references and frame range.

    Notation:
        [argument] - Means that the argument is optional.
        <argument> -Something that has to be replaced with a valid value.
          ''')

if __name__ == '__main__':
    args = sys.argv[1:]

    if len(args) == 0:
        print_help()
        sys.exit(1)

    if args[0] == 'dev':
        dev()
    elif args[0] == 'belady-paradox':
        if len(args) != 4:
            print('Usage: belady-paradox <references> <min_frames> <max_frames>')
            sys.exit(1)
        references = list(map(lambda r: int(r), args[1].split(',')))
        min_frames = int(args[2])
        max_frames = int(args[3])
        analysis.analyse_belady_paradox(references, min_frames, max_frames)
    elif args[0] == 'list':
        print('''
        Scheduling:
          FCFS - First Come First Served
          SJF - Shortest Job First (non-preemptive)
          SRTF - Shortest Remaining Time First (preemptive SJF)

        Page replacement:
          FIFO - First In First Out
          LRU - Least Recently Used
        ''')
    elif args[0] == 'generate':
        generate_file(args[1:])
    elif args[0] == 'test':
        print('Running tests for validation of algorithms...')
        only_results = len(args) == 1 or args[2] != '--details'
        tests.test('SRTF algorithm', srtf, tests.srtf, only_results=only_results)
        tests.test('SJF algorithm', sjf, tests.sjf, only_results=only_results)
        tests.test('FCFS algorithm', fcfs, tests.fcfs, only_results=only_results)
        tests.test('FIFO algorithm', fifo, tests.fifo, only_results=only_results)
        tests.test('LRU algorithm', lru, tests.lru, only_results=only_results)
    elif args[0] == 'run':
        analysis.run_analysis(args[1])
    elif args[0] == 'simulate':
        import os
        import sys
        gui_path = os.path.join(os.path.dirname(__file__), 'gui', 'simulator.py')
        if not os.path.exists(gui_path):
            print('Simulator GUI not found!')
            sys.exit(1)
        import runpy
        runpy.run_path(gui_path, run_name='__main__')
    else:
        print_help()