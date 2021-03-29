from flask import Flask, request, abort

from game_app import TicTacToeApp, TicTacToeGameNotFoundException


app = Flask(__name__)
t_app = TicTacToeApp()
t_app.start_game('1', '2')

@app.route('/')
def hello_world():
    return list(t_app._games.keys())[0]

@app.route('/game_info', methods=['GET'])
def get_game_info():
    game_id = request.args.get('game_id')
    if game_id:
        try:
            game_info = t_app.get_game_by_id(game_id).to_json()
        except TicTacToeGameNotFoundException:
            abort(404)
        return game_info
    abort(400)
