class CarAdView:
    def __init__(self, car_id, timestamp):
        self.car_id = car_id
        self.timestamp = timestamp

    def to_dict(self):
        return {
            'car_id': self.car_id,
            'timestamp': self.timestamp,
        }
