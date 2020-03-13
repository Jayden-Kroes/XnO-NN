# import sys
# sys.path.append('')
from IPython.display import HTML, display
from Board import Board, GameResult, CROSS, NAUGHT

'''
Doesn't work for VSCode
'''
def print_board(board):
    display(HTML("""
    <style>
    .rendered_html table, .rendered_html th, .rendered_html tr, .rendered_html td {
      border: 1px  black solid !important;
      color: black !important;
    }
    </style>
    """+board.html_str()))

board = Board()
# print_board(board)
board.print_board()

