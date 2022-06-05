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

__game_provider = GameProvider(
    game_data_set.values(),
)


@app.route("/")
def root():
    return render_template("./main.html")


def get_user_settings(args):
    people_min = args.get("people_min")
    people_max = args.get("people_max")
    intimacy = args.get("intimacy")

    if people_min and people_max and intimacy is not None:
        return {
            "people_min": int(people_min),
            "people_max": int(people_max),
            "intimacy": int(intimacy),
        }

    else:
        return None


def render_template_boilerplate(args, html_link, game_id):
    user_settings = get_user_settings(args)

    if user_settings is None:
        return redirect("/")
    else:
        game = game_data_set[game_id]
        return render_template(
            html_link,
            game_title=game["name"],
            game_description=game["description"],
            game_image_url=game["main_image_url"],
        )


@app.route("/api/redirect-game")
def redirect_random_game():
    user_settings = get_user_settings(request.args)
    prev_game = request.args.get("prev_game")

    if user_settings is not None:
        random_game = __game_provider.get_random_game(
            people_range=[user_settings["people_min"], user_settings["people_max"]],
            prev_game=prev_game,
        )
        return redirect("/" + random_game["game_id"] + "?" + urlencode(request.args))
    else:
        return redirect("/")


# 아래에서부터는 각 게임별 route로 연결

# 폭탄 돌리기 게임
@app.route("/bomb-game")
def render_bomb_game():
    return render_template_boilerplate(
        args=request.args, html_link="./game/bombGame.html", game_id="bomb-game"
    )


# 눈치 게임
@app.route("/hunch-game")
def render_hunch_game():
    return render_template_boilerplate(
        args=request.args, html_link="./game/hunchGame.html", game_id="hunch-game"
    )


# 초성 게임
@app.route("/initial-consonant-quiz")
def render_initial_consonant_quiz():
    return render_template_boilerplate(
        args=request.args,
        html_link="./game/initialConsonantQuiz.html",
        game_id="initial-consonant-quiz",
    )


# 모듈로써 실행했을 때만 main 함수가 실행되도록 전처리
if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8000")
