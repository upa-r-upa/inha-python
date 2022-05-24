import BalanceGame from "./game/BalanceGame";
import BombGame from "./game/BombGame";
import GlanceGame from "./game/GlanceGame";

export default class GameManger {
    playGame: string;
    gameList=[ new BalanceGame(), new BombGame(), new GlanceGame()]

    constructor() {
        
    }

    public startRandomGame() {
        // gh
    }

    public nextRandomGame() {
        // dd
    }

    public playRandomPenalty() {
        // dd
        
    }
}