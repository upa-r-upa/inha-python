from flask import Flask, redirect, render_template, request
from urllib.parse import urlencode

from .static.model.game_provider import GameProvider
from .static.model.game_data_set import game_data_set

# main 실행 함수
def create_app():
    # flask instance 생성
    app = Flask(__name__)

    return app


app = create_app()

__game_provider = GameProvider(game_data_set.values())


@app.route("/")
def root():
    return render_template("./main.html")


@app.route("/api/redirect-game")
def redirect_random_game():
    people_min = int(request.args.get("people_min"))
    people_max = int(request.args.get("people_max"))
    intimacy = int(request.args.get("intimacy"))
    prev_game = request.args.get("prev_game")

    if people_min and people_max and intimacy:
        random_game = __game_provider.get_random_game(
            people_range=[people_min, people_max],
            intimacy=intimacy,
            prev_game=prev_game,
        )
        return redirect("/" + random_game["game_id"] + "?" + urlencode(request.args))
    else:
        return redirect("/")


# 아래에서부터는 각 게임별 route로 연결

# 폭탄 돌리기 게임
@app.route("/bomb-game")
def render_bomb_game():
    game = game_data_set["bomb-game"]

    return render_template(
        "./game/bombGame.html",
        game_title=game["name"],
        game_description=game["description"],
        game_image_url=game["main_image_url"],
    )


# 눈치 게임
@app.route("/hunch-game")
def render_hunch_game():
    game = game_data_set["hunch-game"]

    return render_template(
        "./game/hunchGame.html",
        game_title=game["name"],
        game_description=game["description"],
        game_image_url=game["main_image_url"],
    )


# 모듈로써 실행했을 때만 main 함수가 실행되도록 전처리
if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8000")
