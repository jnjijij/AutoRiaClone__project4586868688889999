from textblob import TextBlob

from backend.apps.core import db
from backend.autoria.price.models import ExchangeRate


class Listing(db.Model):
    # ...

    def __init__(self):
        self.description = None
        self.title = None
        self.price = None

    def get_price_in_currency(self, currency):
        exchange_rate = ExchangeRate.query.filter_by(currency=currency).first()
        if exchange_rate is None:
            return None

        return self.price * exchange_rate.rate

    def check_content(self):
        inappropriate_words = ["badword1", "badword2", "badword3"]  # Add your list of inappropriate words

        title_blob = TextBlob(self.title)
        description_blob = TextBlob(self.description)

        if any(word in title_blob.words for word in inappropriate_words):
            return False

        if any(word in description_blob.words for word in inappropriate_words):
            return False

        return True

    editing_attempts = db.Column()

    def can_edit(self):
        return self.editing_attempts < 3

    def edit(self):
        if not self.can_edit():
            return False

        # Implement your editing logic here

        self.editing_attempts += 1
        db.session.commit()

        return True