class AnimeItem:
    def __init__(self, id, title, release_date, image=None, rating=None, link=None):
        self.id = id
        self.title = title
        self.release_date = release_date
        self.image = image
        self.rating= float(rating) if rating else 0
        self.link = link