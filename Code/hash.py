class Book:

    def __init__(self,
                 title,
                 authors,
                 year,
                 ISBN,
                 pages,
                 publisher, 
                 tags):
        self.title = title
        self.authors = authors
        self.year = year
        self.ISBN = ISBN
        self.pages = pages
        self.publisher = publisher
        self.tags = tags
        self.price = {}

    def add_tag(self, tag):
        if tag not in self.tags:
            self.tags.append(tag)
            return True
        else:
            return False
