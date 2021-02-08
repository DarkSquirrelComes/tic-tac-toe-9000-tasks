from copy import deepcopy
from typing import Callable, List, Optional
from game_engine import TicTacToeTurn, TicTacToeGameInfo, AbstractTicTacToeGame


class TicTacToeGame(AbstractTicTacToeGame):
    """Наследуемся от абстрактного класса и реализуем ручками все методы"""

    def __init__(self, game_id: str, first_player_id: str, second_player_id: str,
                 strategy: Optional[Callable[[TicTacToeGameInfo], TicTacToeTurn]] = None) -> None:
        self.__game_id = game_id
        self.__first_player_id = first_player_id
        self.__second_player_id = second_player_id
        self.__winner_id = ""
        self.__strategy = strategy
        self.__turns: List[TicTacToeTurn] = []

    def is_turn_correct(self, turn: TicTacToeTurn) -> bool:
        raise NotImplementedError

    def do_turn(self, turn: TicTacToeTurn) -> TicTacToeGameInfo:
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