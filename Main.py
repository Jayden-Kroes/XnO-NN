# import sys
# sys.path.append('')
from IPython.display import HTML, display
from tic_tac_toe.Board import Board, GameResult, CROSS, NAUGHT
from tic_tac_toe.Player import Player

'''
Doesn't work for VSCode
'''
def print_board(board):
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

play_random_game()

