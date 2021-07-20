from django.test import TestCase
from django.contrib.auth.models import User
from megasena.models import SorteioMegaSena,NovoJogo
from megasena.tests.fake_data import instances,additional_values

class MegaSenaDrawTestCase(TestCase):
    """Testar modelo SorteioMegaSena"""
    def setUp(self):
        """setUp do modelo SorteioMegaSena"""
        SorteioMegaSena.objects.bulk_create([SorteioMegaSena(**instances[i])
                                             for i in range(len(instances))])
        self.all_records = SorteioMegaSena.objects.all()
    def test_verify_items(self):
        """verificar se todos os itens foram inseridos"""
        self.assertEqual(len(self.all_records),len(instances))

class NovoJogoTestCase(TestCase):
    """Testar modelo NovoJogo"""
    def setUp(self):
        """setUp do modelo NovoJogo"""
        self.user = User.objects.create_user(username="abc", email="abc@abc.com", password="123")
        self.user.save()
        self.user2 = User.objects.create_user(username="cba", email="cba@cba.com", password="321")
        self.user2.save()
        NovoJogo.objects.bulk_create([NovoJogo(**instances[i], user=self.user,**additional_values)
                                if i < len(instances) - 1 else
             NovoJogo(**instances[i],user=self.user2,**additional_values)
             for i in range(len(instances))])
        self.all_records = NovoJogo.objects.all()
    def test_verify_items(self):
        """verificar se todos os itens foram inseridos"""
        self.assertEqual(len(self.all_records),len(instances))
    def test_multiple_users(self):
        """Ver se tabela tem multiplos usuarios"""
        self.assertNotEqual(self.all_records[0].user_id, self.all_records[2].user_id)