# import sys
# sys.path.append('')
from IPython.display import HTML, display
from tic_tac_toe.Board import Board, GameResult, CROSS, NAUGHT
from tic_tac_toe.Player import Player
from tic_tac_toe.RandomPlayer import RandomPlayer
from tic_tac_toe.MinMaxAgent import MinMaxAgent
from tic_tac_toe.RndMinMaxAgent import RndMinMaxAgent

def print_board(board):
    '''
    Doesn't work for VSCode
    '''
    board.print_board()
    return
    # display(HTML("""
    # <style>
    # .rendered_html table, .rendered_html th, .rendered_html tr, .rendered_html td {
    #   border: 1px  black solid !important;
    #   color: black !important;
    # }
    # </style>
    # """+board.html_str()))

def play_random_game():
    board = Board()
    finished = False
    last_play = NAUGHT
    next_play = CROSS
    while not finished:
        _, result, finished = board.move(board.random_empty_spot(), next_play)
        print_board(board) 
        last_play, next_play = next_play, last_play
    if result == GameResult.DRAW:
        print("Game is a draw")
    elif last_play == CROSS:
        print("Cross won!")
    else:
        print("Naught won!")

def play_game(board: Board, player1: Player, player2: Player):
    player1.new_game(CROSS)
    player2.new_game(NAUGHT)
    board.reset()
    
    finished = False
    while not finished:
        result, finished = player1.move(board)
        if finished:
            if result == GameResult.DRAW:
                final_result = GameResult.DRAW
            else:
                final_result =  GameResult.CROSS_WIN
        else:
            result, finished = player2.move(board)
            if finished:
                if result == GameResult.DRAW:
                    final_result =  GameResult.DRAW
                else:
                    final_result =  GameResult.NAUGHT_WIN
        
    player1.final_result(final_result)
    player2.final_result(final_result)
    return final_result

def battle(player1: Player = RandomPlayer(), player2: Player = RandomPlayer(), num_games: int = 100000):
    board = Board()
    draw_count = 0
    cross_count = 0
    naught_count = 0
    for _ in range(num_games):
        result = play_game(board, player1, player2)
        if result == GameResult.CROSS_WIN:
            cross_count += 1
        elif result == GameResult.NAUGHT_WIN:
            naught_count += 1
        else:
            draw_count += 1

    print("After {} game we have draws: {}, Player 1 wins: {}, and Player 2 wins: {}.".format(
        num_games, draw_count, cross_count, naught_count))
    print("Which gives percentages of draws: {:.2%}, Player 1 wins: {:.2%}, and Player 2 wins:  {:.2%}".format(
        draw_count / num_games, cross_count / num_games, naught_count / num_games))


player1 = RndMinMaxAgent()
player2 = RndMinMaxAgent()
board = Board()

game_count = 100000
battle(player1, player2)
