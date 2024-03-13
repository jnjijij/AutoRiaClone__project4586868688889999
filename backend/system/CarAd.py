class CarAd:
    def __init__(self, car_id, region, price):
        self.car_id = car_id
        self.region = region
        self.price = price

    def to_dict(self):
        return {
            'car_id': self.car_id,
            'region': self.region,
            'price': self.price,
        }
