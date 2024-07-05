import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Tworzenie nowego błądzenia losowego, dopóki program pozostaje aktywny.
while True:
    # Przygotowanie błądzenia losowego.
    rw = RandomWalk(50_000)
    rw.fill_walk()

    # Wyświetlanie puntków błądzenia losowego.
    plt.style.use('classic')
    fig, ax = plt.subplots()
    # Zmienianie wielkości wykresu, aby wypełnił ekran:
    # fig, ax = plt.subplots(figsize=(15, 9))
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=1)
    ax.set_aspect('equal')

    # Podkreślenie pierwszego i ostatniego punktu błądzenia losowego.
    ax.scatter(0, 0, c='green', edgecolor='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolor='none', s=100)

    # Ukrywanie osi.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Utworzyć kolejne błądzenie losowe? (t/n): ")
    if keep_running == 'n':
        break