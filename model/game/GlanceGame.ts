import BaseGame from "../base/GameBase";

export default class GlanceGame extends BaseGame {
    constructor() {
        super({
            "name": "눈치게임",
            "direction": "LEFT",
            "description": "눈치게임! 숫자를 어쩌구 외칩니다. 어쩌구 하는 사람이 벌칙!",
            "intimacy": "LOW",
            "recommendedPeopleRange": [1, 50],
        });
    }

    public game(): void {
        // 
        // 눈치게임은 화면 표출 기능밖에 없으므로 화면에 눈치게임 시작! 문구만
    }
}