from copy import deepcopy
from typing import Callable, List, Optional
from game_engine import TicTacToeTurn, TicTacToeGameInfo, AbstractTicTacToeGame


class TicTacToeGame(AbstractTicTacToeGame):

    def __init__(self, game_id: str, first_player_id: str, second_player_id: str,
                 strategy: Optional[Callable[[TicTacToeGameInfo], TicTacToeTurn]] = None) -> None:
        self.__game_id = game_id
        self.__first_player_id = first_player_id
        self.__second_player_id = second_player_id
        self.__field =[
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]
        self.__strategy = strategy
        self.__turns = []
        self.__winner_id = ''
        self.__current_player_id = ''

    def set_winner_id(self, turn):
        counter = 0 #checked lines for draw
        str1 = ''
        str2 = ''
        for i in range(3):
            for j in range(3):
                str1 += self.__field[i][j]
                str2 += self.__field[j][i]
            if str1 == 'XXX' or str2 == 'XXX':
                self.__winner_id = self.__first_player_id
            elif str1 == 'OOO' or str2 == 'OOO':
                self.__winner_id = self.__first_player_id
            elif 'O' in str1 and 'X' in str1: #checking for draw
                counter += 1
            if 'O' in str2 and 'X' in str2:
                counter += 1

        str10 = ''
        str20 = ''
        for i in range(3):
            str10 += self.__field[i][i]
            str20 += self.__field[i][2-i]
        if str10 == 'XXX' or str20 == 'XXX':
            self.__winner_id = self.__first_player_id
        elif str10 =='OOO' or str20 == 'OOO':
            self.__winner_id = self.__second_player_id
        elif 'O' in str1 and 'X' in str1: #checking for draw
            counter += 1
        if 'O' in str2 and 'X' in str2:
            counter += 1
        if counter == 8:
            self.__winner_id = 'draw'


    def is_turn_correct(self, turn: TicTacToeTurn) -> bool:
        if self.__turns == []:
            self.__current_player_id = self.__first_player_id
        elif self.__turns[-1].player_id == self.__first_player_id:
            self.__current_player_id = self.__second_player_id
        else:
            self.__current_player_id = self.__first_player_id

        if self.__winner_id != '':
            return False
        if not (0 <= turn.x_coordinate <= 2 and 0 <= turn.y_coordinate <= 2):
            return False
        if turn.player_id != self.__current_player_id:
            return False
        if self.__field[turn.x_coordinate][turn.y_coordinate] != ' ':
            return False
        return True

    def do_turn(self, turn: TicTacToeTurn) -> TicTacToeGameInfo:
        if self.is_turn_correct(turn) == True:
            if turn.player_id == self.__first_player_id:
                self.__field[turn.x_coordinate][turn.y_coordinate] = 'X'
            else:
                self.__field[turn.x_coordinate][turn.y_coordinate] = 'O'
            self.__turns.append(deepcopy(turn))
            return self.get_game_info()

    def get_game_info(self) -> TicTacToeGameInfo:
        result = TicTacToeGameInfo(
            game_id = self.__game_id,
            field = self.__field,
            sequence_of_turns = deepcopy(self.__turns),
            first_player_id = self.__first_player_id,
            second_player_id = self.__second_player_id,
            winner_id = self.__winner_id
        )
        for turn in self.__turns:
            if turn.player_id == self.__first_player_id:
                ch = "X"
            else:
                ch = "O"
            result.field[turn.x_coordinate][turn.y_coordinate] = ch
        return result