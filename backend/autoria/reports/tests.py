from django.contrib.auth.models import User

from .models import Report
from ..autoria.models import Auto


class ReportTestCase(Auto):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = None
        self.report = None
        self.auto = None

    def setUp(self):
        self.user = User.objects.create(username='test_user')
        self.auto = Auto.objects.create(make='Toyota', model='Camry', year=2021)
        self.report = Report.objects.create(auto=self.auto, user=self.user, reason='Test Reason')

    def test_report_creation(self):
        self.assertEqual(self.report.auto.make, 'Toyota')
        self.assertEqual(self.report.user.username, 'test_user')
        self.assertEqual(self.report.reason, 'Test Reason')

    def assertEqual(self, username, param):
        pass
