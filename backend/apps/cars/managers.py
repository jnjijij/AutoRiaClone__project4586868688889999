from django.db import models

class CarManager(models.Manager):
    def get_only_audi(self, name):
        return self.filter(brand=name)

    def get_only_bmw(self, name):
        return self.filter(brand=name)

    def get_only_mercedes(self, name):
        return self.filter(brand=name)

    def get_only_toyota(self, name):
        return self.filter(brand=name)

    def get_only_honda(self, name):
        return self.filter(brand=name)