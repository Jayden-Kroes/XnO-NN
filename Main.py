# from IPython.display import HTML, display
from tic_tac_toe.Board import Board, GameResult, CROSS, NAUGHT, EMPTY
from tic_tac_toe.Player import Player
from tic_tac_toe.RandomPlayer import RandomPlayer
from tic_tac_toe.MinMaxAgent import MinMaxAgent
from tic_tac_toe.RndMinMaxAgent import RndMinMaxAgent
from tic_tac_toe.TabularQPlayer import TQPlayer
from tic_tac_toe.SimpleNNQPlayer import NNQPlayer
# from tic_tac_toe.TFSessionManager import TFSessionManager
import tensorflow as tf
import matplotlib
import numpy as np
import matplotlib.pyplot as plt

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

def battle(player1: Player = RandomPlayer(), player2: Player = RandomPlayer(), num_games: int = 100000, silent: bool = False):
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

    if not silent:
        print("After {} game we have draws: {}, Player 1 wins: {}, and Player 2 wins: {}.".format(
            num_games, draw_count, cross_count, naught_count))
        print("Which gives percentages of draws: {:.2%}, Player 1 wins: {:.2%}, and Player 2 wins:  {:.2%}".format(
            draw_count / num_games, cross_count / num_games, naught_count / num_games))

    return cross_count, naught_count, draw_count


def eval_players(p1 : Player, p2 : Player, num_battles : int = 100, games_per_battle : int = 100, loc='best'):
    p1_wins = []
    p2_wins = []
    draws = []
    game_number = []
    counter = 0
    
    # TFSessionManager.set_session(tf.Session())
    # TFSessionManager.get_session().run(tf.global_variables_initializer())

    for i in range(num_battles):
        p1win, p2win, draw = battle(p1, p2, num_games=games_per_battle, silent=True)
        p1_wins.append(p1win*100.0/games_per_battle)
        p2_wins.append(p2win*100.0/games_per_battle)
        draws.append(draw*100.0/games_per_battle)
        counter +=1
        game_number.append(counter)

    plt.ylabel('Game outcomes in %')
    plt.xlabel('Game number')

    plt.plot(game_number, draws, 'r-', label='Draw')
    plt.plot(game_number, p1_wins, 'g-', label='Player 1 wins')
    plt.plot(game_number, p2_wins, 'b-', label='Player 2 wins')
    plt.legend(loc=loc, shadow=True, fancybox=True, framealpha =0.7)
    plt.show()

    # TFSessionManager.set_session(None)
    return game_number, p1_wins, p2_wins, draws


# tf.reset_default_graph()    

nnplayer = NNQPlayer("QLearner1")
rndplayer = RandomPlayer()

game_number, p1_wins, p2_wins, draws = eval_players(nnplayer, rndplayer)

p = plt.plot(game_number, draws, 'r-', game_number, p1_wins, 'g-', game_number, p2_wins, 'b-')