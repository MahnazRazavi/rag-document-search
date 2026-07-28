class DocumentContentRepository:
    def __init__(self, db):
        self.db = db

    def create(self, content):
        self.db.add(content)

        self.db.commit()

        self.db.refresh(content)

        return content
