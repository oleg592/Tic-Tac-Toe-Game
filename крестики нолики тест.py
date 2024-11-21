def play_game():
    # создаём пустое игровое поле
    board = [[" " for _ in range(3)] for _ in range(3)]

    # функция для печати игрового поля
    def print_board(board):
        for i in range(len(board)):
            print(" | ".join(board[i]))  # печатаем строку с разделителями " | "
            if i < len(board) - 1:  # разделитель только между строками
                print("--+---+--")

    # имена игроков
    player_X = input("Введите имя игрока, который будет играть за X: ")
    player_O = input("Введите имя игрока, который будет играть за O: ")

    print_board(board)

    # функция для хода игрока
    def player_move(board, player, player_name):
        while True:
            move = input(f"{player_name} ({player}), выберите номер клетки (1-9): ")
            if move.isdigit() and 1 <= int(move) <= 9:
                move = int(move) - 1
                row, col = divmod(move, 3)
                if board[row][col] == " ":
                    board[row][col] = player  # если клетка пуста, ставим символ игрока
                    break
                else:
                    print("Эта клетка уже занята. Попробуйте другую.")
            else:
                print("Неправильный ввод. Введите число от 1 до 9.")

    # функция проверки победителя
    def check_winner(board):
        # проверка строк и столбцов
        for row in board:
            if row[0] == row[1] == row[2] != " ":
                return row[0]

        for col in range(3):
            if board[0][col] == board[1][col] == board[2][col] != " ":
                return board[0][col]

        # проверка диагоналей
        if board[0][0] == board[1][1] == board[2][2] != " ":
            return board[0][0]

        if board[0][2] == board[1][1] == board[2][0] != " ":
            return board[0][2]

        return None

    # функция для проверки ничьей
    def is_full(board):
        for row in board:
            if " " in row:
                return False
        return True

    # игровой цикл
    current_player = "X"  # начинает игрок X
    while True:
        current_player_name = player_X if current_player == "X" else player_O
        player_move(board, current_player, current_player_name)
        print_board(board)

        # проверяем на победителя
        winner = check_winner(board)
        if winner:
            print(f"Поздравляем, {player_X if winner == 'X' else player_O}! Вы выиграли!")
            break

        # проверяем на ничью
        if is_full(board):
            print("Ничья!")
            break

        # сменить игрока
        current_player = "O" if current_player == "X" else "X"

    # повтор игры
    play_again = input("Хотите сыграть еще раз? (Y/N): ").strip().lower()
    if play_again == "y":
        play_game()  # если да, запускаем новую игру
    else:
        print("Спасибо за игру!")


# начинаем игру
play_game()

