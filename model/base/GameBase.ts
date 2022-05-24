import Penalty from "../Penalty";

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
 * Game의 기본적인 기능을 구현하는 Base model
 * 이걸 확장시켜서 게임을 제작함
 */
export default abstract class GameBase {
    // 친밀도
    intimacy: GameIntimacy;
    // 권장 인원
    recommendedPeopleRange: [number, number];
    // 방향
    direction: GamePlayDirection;
    // 설명
    description: string;
    // 게임 이름
    name: string; 
    
    constructor({ intimacy, recommendedPeopleRange, direction, description, name }: IBaseGame) {
        this.intimacy = intimacy;
        this.recommendedPeopleRange = recommendedPeopleRange;
        this.direction = direction;
        this.description = description;
        this.name = name;
    }

    public abstract game(): void;

    public playPenalty() {
        new Penalty().randomPlayPenalty(this.intimacy);
    }

    public gameStart() {
        this.game();
    }

    public gameEnd() {
        
    }
    
}