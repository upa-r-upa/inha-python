class ImageCard:
    def __init__(self, *, label, img_url):
        self.label = label
        self.img_url = f"/static/images/{img_url}"
