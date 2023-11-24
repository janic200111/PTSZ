import random
import sys

# Parametry
ns=list(range(50, 501, 50))
ni = int(sys.argv[1])  # Liczba zadań
max_p = int(sys.argv[2])  # Maksymalny czas trwania zadania
max_r = int(sys.argv[3])  # Maksymalny moment gotowości
max_s = int(sys.argv[4]) #max czas przez

for n in ns:

    # Generowanie danych
    tasks = [(random.randint(1, max_p)*10, random.randint(0, max_r)) for _ in range(n)]
    setup_times = [[random.randint(0, max_s) if i != j else 0 for j in range(n)] for i in range(n)]

    # Zapis danych do pliku
    with open('in_148240_' +str(n) +'.txt', 'w') as file:
        file.write(str(n) + '\n')
        for task in tasks:
            file.write(f"{task[0]} {task[1]}\n")
        for setup_time in setup_times:
            file.write(" ".join(map(str, setup_time)) + '\n')

