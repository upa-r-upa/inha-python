class PenaltyCard:
    def __init__(
        self,
        name,
        intimacy=0,
        img_src="/static/images/penalty/beer-with-cup.png",
    ):
        self.intimacy = intimacy
        self.name = name
        self.img_src = img_src
