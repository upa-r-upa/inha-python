import BaseGame from "../base/GameBase";

export default class BalanceGame extends BaseGame {
    balanceQuestion = ["강호동이랑 살기vs 강호동 어저구", "ㅁㅇㄹㅁㄴㅇㄹ", "ㅁㅇㄹㅁㅇㄴㄹ"]

    constructor() {
        super({
            "name": "밸런스 게임",
            "direction": "RIGHT",
            "description": "밸런스 게임! 어쩌구~, 어쩌구 하는 사람이 벌칙!",
            "intimacy": "HIGH",
            "recommendedPeopleRange": [1, 50],
        });
    }

    private randomQuestionPlay() {
        
    }

    public game(): void {
        // 밸런스 게임이므로 VS 형식으로 UI 띄우기~

        const randomQuestion = this.randomQuestionPlay();
        // asdfdsf randomQuestion.nameadfasdf;


    }
}