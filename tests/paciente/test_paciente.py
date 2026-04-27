from unittest import TestCase
from datetime import datetime, date, time
from src.paciente import Paciente

class TestPaciente(TestCase):

    def test_nao_deve_criar_paciente_sem_nome(self):
        with self.assertRaises(ValueError):
            Paciente(nome=None, cpf="00011122233")
