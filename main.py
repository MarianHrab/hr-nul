# Функція для створення дошки
def create_board():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    return board

# Функція для виведення дошки на екран
def print_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * 5)

# Функція для перевірки переможця
def check_winner(board):
    # Перевірка рядків
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return row[0]

    # Перевірка стовпців
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return board[0][col]

    # Перевірка діагоналей
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]

    return None

# Функція для перевірки нічиєї
def check_tie(board):
    for row in board:
        if ' ' in row:
            return False
    return True

# Головна функція гри
def play_game():
    board = create_board()
    current_player = 'X'
    winner = None
    tie = False

    while not winner and not tie:
        print_board(board)

        # Запитуємо гравця про хід
        print(f"Гравець '{current_player}', введіть рядок та стовпець (наприклад, 1 2):")
        move = input().split()
        row = int(move[0]) - 1
        col = int(move[1]) - 1

        # Перевірка чи введений хід вірний
        if row < 0 or row > 2 or col < 0 or col > 2 or board[row][col] != ' ':
            print("Неправильний хід. Спробуйте ще раз.")
            continue

        # Виконуємо хід
        board[row][col] = current_player

        # Перевірка переможця
        winner = check_winner(board)

        # Перевірка нічиєї
        tie = check_tie(board)

        # Міняємо гравця
        current_player = 'O' if current_player == 'X' else 'X'

    # Виводимо результати гри
    print_board(board)

    if winner:
        print(f"Гравець '{winner}' переміг!")
    else:
        print("Гра завершилась нічиєю.")

# Запуск гри
play_game()
