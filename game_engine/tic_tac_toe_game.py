from copy import deepcopy
from typing import Callable, List, Optional
from game_engine import TicTacToeTurn, TicTacToeGameInfo, AbstractTicTacToeGame


class TicTacToeGame(AbstractTicTacToeGame):

    def __init__(self, game_id: str, first_player_id: str, second_player_id: str,
                 strategy: Optional[Callable[[TicTacToeGameInfo], TicTacToeTurn]] = None) -> None:
        self.game_id = game_id
        self.first_player_id = first_player_id
        self.second_player_id = second_player_id
        self.field =[
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]
        self.strategy = strategy
        self.sequence_of_turns = []


    def current_player_id(self):
        if self.sequence_of_turns == []:
            self.current_player_id == self.first_player_id
        if self.sequence_of_turns[-1] == self.first_player_id:
            self.current_player_id == self.second_player_id
        else:
            self.current_player_id == self.first_player_id
        

    def set_winner_id(self, turn):
        counter = 0 #checked lines for draw
        str1 = ''
        str2 = ''
        for i in range(3):
            for j in range(3):
                str1 += self.field[i][j]
                str2 += self.field[j][i]
            if str1 == 'XXX' or str2 == 'XXX':
                self.winner_id = self.first_player_id
            elif str1 == 'OOO' or str2 == 'OOO':
                self.winner_id = self.first_player_id
            elif 'O' in str1 and 'X' in str1: #checking for draw
                counter += 1
            if 'O' in str2 and 'X' in str2:
                counter += 1

        str10 = ''
        str20 = ''
        for i in range(3):
            str10 += self.field[i][i]
            str20 += self.field[i][2-i]
        if str10 == 'XXX' or str20 == 'XXX':
            self.winner_id = self.first_player_id
        elif str10 =='OOO' or str20 == 'OOO':
            self.winner_id = self.second_player_id
        elif 'O' in str1 and 'X' in str1: #checking for draw
            counter += 1
        if 'O' in str2 and 'X' in str2:
            counter += 1
        if counter == 8:
            self.winner_id = 'draw'


    def is_turn_correct(self, turn: TicTacToeTurn) -> bool:
        if self.winner_id != '':
            return False
        if not (0 <= turn.x_coordinate <= 2 and 0 <= turn.y_coordinate <= 2):
            return False
        if turn.player_id != self.current_player_id:
            return False
        if self.field[turn.x_coordinate][turn.y_coordinate] != ' ':
            return False
        return True
        raise NotImplementedError

    def do_turn(self, turn: TicTacToeTurn) -> TicTacToeGameInfo:
        if is_turn_correct(self, turn) == False:
            print('Incorrect turn')
        else:
            if self.current_turn_player == turn.first_player_id:
                self.field[turn.x_coordinate][turn.y_coordinate] == 'X'
            else:
                self.field[turn.x_coordinate][turn.y_coordinate] == 'O'
            self.sequence_of_turns.append(deepcopy(turn))
        raise NotImplementedError

    def get_game_info(self) -> TicTacToeGameInfo:
        result = TicTacToeGameInfo(
            game_id=self.__game_id,
            field=[
                [" ", " ", " "],
                [" ", " ", " "],
                [" ", " ", " "]
            ],
            sequence_of_turns=deepcopy(self.__turns),
            first_player_id=self.__first_player_id,
            second_player_id=self.__second_player_id,
            winner_id=self.__winner_id
        )
        for turn in self.__turns:
            if turn.player_id == self.__first_player_id:
                ch = "X"
            else:
                ch = "O"
            result.field[turn.x_coordinate][turn.y_coordinate] = ch
        return result