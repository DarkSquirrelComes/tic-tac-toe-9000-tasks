from typing import Callable, List
from copy import deepcopy

from .tic_tac_toe_common_lib import TicTacToeTurn, TicTacToeGameInfo, AbstractTicTacToeGame

class TicTacToeGame(AbstractTicTacToeGame):
    def __init__(self, game_id: str, first_player_id: str, second_player_id: str,
                 strategy: Callable[[TicTacToeGameInfo], TicTacToeTurn] = None) -> None:
        self.__game_id = game_id
        self.__first_player_id = first_player_id
        self.__second_player_id = second_player_id
        self.__winner_id = ""
        self.__strategy = strategy
        self.__turns: List[TicTacToeTurn] = []

    def is_turn_correct(self, turn: TicTacToeTurn) -> bool:
        x = turn.x_coordinate
        y = turn.y_coordinate
        whatreturn: False
        if (0 <= x <= 2) and (0 <= y <= 2) and (self.get_game_info().field[x][y] == " ") and (self.__winner_id == ""):
            if self.__turns == []:
                if turn.player_id == self.__first_player_id:
                    whatreturn =  True
                else:
                    whatreturn =  False
            else:
                if self.__turns[-1].player_id != turn.player_id:
                    whatreturn =  True
                else:
                    whatreturn =  False
            #whatreturn =  True
        else:
            whatreturn =  False
        return whatreturn

    def do_turn(self, turn: TicTacToeTurn) -> TicTacToeGameInfo:
        if self.is_turn_correct(turn) == True:
            self.__turns.append(turn)
            self.__winner_id = self.win(self.get_game_info())

        return self.get_game_info()

    def win(self, turn: TicTacToeGameInfo):
        xo = ["X", "O"]
        whoiswin = ""
       #horizontale
        for sym in xo:
            for i in range(3):
                combo = 0
                for j in range(3):
                    if turn.field[i][j] == sym:
                        combo += 1
                if combo == 3:
                    if sym == "X":
                        whoiswin = self.__first_player_id
                    else:
                        whoiswin = self.__second_player_id
        #verticale"""
        for sym in xo:
            for i in range(3):
                combo = 0
                for j in range(3):
                    if turn.field[j][i] == sym:
                        combo += 1
                if combo == 3:
                    if sym == "X":
                        whoiswin = self.__first_player_id
                    else:
                        whoiswin = self.__second_player_id
        #from left up to right down"""
        for sym in xo:
            if (turn.field[0][0]==sym)and(turn.field[1][1]==sym)and(turn.field[2][2]==sym):
                if sym == "X":
                    whoiswin = self.__first_player_id
                else:
                    whoiswin = self.__second_player_id
        #from right up to left down"""
        for sym in xo:
            if (turn.field[0][2] == sym)and(turn.field[1][1] == sym)and(turn.field[2][0] == sym):
                if sym == "X":
                    whoiswin = self.__first_player_id
                else:
                    whoiswin = self.__second_player_id
        return whoiswin

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
            if  turn.player_id == self.__first_player_id:
                ch = "X"      
            else:
                ch = "O"
            result.field[turn.x_coordinate][turn.y_coordinate] = ch
        return result
