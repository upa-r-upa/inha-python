from flask import Flask, redirect, render_template, request

from random_game.model.GameProvider import GameProvider

# main 실행 함수
def create_app():
    # flask instance 생성
    app = Flask(__name__)

    return app


app = create_app()


def get_user_settings():
    people_range = request.args.get("range_people")
    intimacy = request.args.get("intimacy")

    if people_range and intimacy:
        return {"people_range": people_range, "intimacy": intimacy}
    else:
        return None


__game_provider = GameProvider()


@app.route("/")
def root():
    return render_template("./main.html")


@app.route("/api/redirect-game")
def redirect_random_game():
    settings = get_user_settings()
    prev_game = request.args.get("prev_game")

    print(settings)

    if settings != None:
        random_game = __game_provider.play_random_game(
            prev_game=prev_game,
            people_range=settings["people_range"],
            intimacy=settings["intimacy"],
        )
        return redirect("/" + random_game)
    else:
        return redirect("/")


# 아래에서부터는 각 게임별 route로 연결

# 폭탄 돌리기 게임
@app.route("/bomb-game")
def render_bomb_game():
    return "BOMB!"


# 눈치 게임
@app.route("/hunch-game")
def render_hunch_game():
    return "HUNCH!"


# 모듈로써 실행했을 때만 main 함수가 실행되도록 전처리
if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8000")
