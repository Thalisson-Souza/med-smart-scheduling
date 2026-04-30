from unittest import TestCase
from datetime import datetime, date, time
from src.consulta import Consulta
from src.medico import Medico
from src.paciente import Paciente

class TestConsulta(TestCase):

    def test_nao_deve_criar_uma_consulta_sem_medico(self):
        paciente = Paciente(nome="Romário", cpf="000111222333")

        with self.assertRaises(ValueError) as context:
            Consulta(None, paciente, date(2026,4,30), time(9,00))
        
        self.assertEqual(str(context.exception), "médico é obrigatório para consulta")