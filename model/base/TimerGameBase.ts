import GameBase from "./GameBase";

type GameIntimacy = "HIGH" | "LOW";
type GamePlayDirection = "LEFT" | "RIGHT" ;

interface IBaseGame {
    intimacy: GameIntimacy;
    recommendedPeopleRange: [number, number];
    direction: GamePlayDirection;
    description: string;
    name: string; 
}
 
/**
 * Game의 기본적인 기능을 확장시키고, 타이머 기능이 있는 게임
 * 이걸 확장시켜서 게임을 제작함
 */
export default abstract class TimerBaseGame extends GameBase {
    timer: number;
    hideTimer: number;
    
    constructor({ ...props }: IBaseGame) {
        super({...props});
    }

    public endTimer() {
        // adfsadf
    }
    public  abstract game(): void;
    
}