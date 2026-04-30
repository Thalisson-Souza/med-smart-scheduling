from unittest import TestCase
from datetime import datetime, date, time
from src.domain.paciente import Paciente

class TestPaciente(TestCase):

    def test_nao_deve_criar_paciente_sem_nome(self):
        with self.assertRaises(ValueError):
            Paciente(nome=None, cpf="00011122233")

    def test_deve_criar_paciente_com_sucesso(self):
        resultado = Paciente(nome="João", cpf="00011122233")
        
        self.assertTrue(resultado)