import BaseGame from "../base/GameBase";
import TimerBaseGame from "../base/TimerGameBase";

export default class BombGame extends TimerBaseGame {
    constructor() {
        super({
            "name": "폭탄 돌리기 게임",
            "direction": "RIGHT",
            "description": "폭탄 돌리기! 어쩌구~, 어쩌구 하는 사람이 벌칙!",
            "intimacy": "LOW",
            "recommendedPeopleRange": [1, 5],
        });
    }

    public game(): void {
        // ㅇㄹㅁㄴㅇㄹㅁ 
    }

    public endTimer(): void {
        // sound();
    }
}