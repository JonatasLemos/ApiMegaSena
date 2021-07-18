from django.test import TestCase, Client
from django.db.models.query import QuerySet
from django.urls import reverse
from django.contrib.auth.models import User
from megasena.models import SorteioMegaSena
from megasena.tests.fake_data import instances

class MegaSenaDrawTestCase(TestCase):

    def setUp(self):
        SorteioMegaSena.objects.bulk_create([SorteioMegaSena(**instances[i]) for i in range(len(instances))])
        self.all_records = SorteioMegaSena.objects.all()

    def test_verify_items(self):
        self.assertEqual(len(self.all_records),len(instances))


