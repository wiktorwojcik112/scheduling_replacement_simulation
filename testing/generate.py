import random

def generate_file(args):
    try:
        if args[0] == 'processes':
          generate_processes_file(args[1], int(args[2]))
        elif args[0] == 'pages':
          if len(args) == 3:
              generate_pages_file(args[1], int(args[2]), -1)
          elif len(args) == 4:
              generate_pages_file(args[1], int(args[2]), int(args[3]))
        else:
          print('Unknown generation type:', args[0])
          print('Available types: processes, pages')
    except IndexError:
        print('Usage: generate <type> <name> <n> [<k>]')
        print('Type can be "processes" or "pages".')
        print('For processes: <name> is the file name, <n> is the number of cases.')
        print('For pages: <name> is the file name, <n> is the number of references, <k> is the number of pages.')
    

def generate_processes_file(name, n):
    """
    Towrzy plik filename z n przypadkami, każdy z losową ilością procesów i losowymi czasami przybycia i trwania.

    Na przykład:
    generate_processes_file('processes')
    Może wygenerować taki plik 'processes.scheduling' z 10 przypadkami.
    
    processes.scheduling
    Zawartość pliku może wyglądać tak:
    [1 0 5, 2 1 3, 3 2 2, 4 3 1, 5 4 4]
    [2 5 6, 3 6 2, 4 7 3, 5 8 1]
    [1 0 4, 5 6 3]
    [1 0 3, 2 1 2, 3 2 1, 4 3 4, 5 4 5]
    [1 0 2, 2 1 1, 3 2 3, 5 4 5]

    """

    filename = f'{name}.scheduling'

    with open(filename, 'w') as f:
        for _ in range(n):
            num_processes = random.randint(1, 10)  # Losowa liczba procesów
            processes = []
            for i in range(num_processes):
                arrival_time = random.randint(0, 10)
                duration = random.randint(1, 10)
                processes.append(f'{i + 1} {arrival_time} {duration}')
            f.write('[' + ', '.join(processes) + ']\n')

def generate_pages_file(name, n, k):
    """
    Tworzy plik filename z n przypadkami, każdy z losową ilością stron i losowymi odwołaniami do stron. Ilość ramek jest określona przez k (k > 0) lub losowo (k == -1).

    Na przykład:
    generate_pages_file('pages', 10)
    Może wygenerować taki plik 'pages.replacement' z 10 przypadkami.

    pages.replacement
    Zawartość pliku może wyglądać tak:
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]:3
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:5
    [1, 2, 3, 4, 5]:2
    [1, 2, 3]:1
    [1, 2]:1
    ...
    """

    filename = f'{name}.replacement'

    with open(filename, 'w') as f:
        for _ in range(n):
            num_references = random.randint(5, 20)
            references = [random.randint(1, 20) for _ in range(num_references)]
            # Teraz określamy liczbę ramek. Jeśli k jest równe -1, to losujemy liczbę ramek.
            frames = k if k > 0 else random.randint(1, 5)
            f.write(f'[{", ".join(map(str, references))}]:{frames}\n')