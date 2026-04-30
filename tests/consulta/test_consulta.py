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

    def test_nao_deve_criar_uma_consulta_sem_paciente(self):
        medico = Medico(nome="Dr. House", hora_inicio=time(8,0), hora_fim=time(12,0))

        with self.assertRaises(ValueError) as context:
            Consulta("Dr. House", None, date(2026,4,30), time(9,00))

        self.assertEqual(str(context.exception), "paciente é obrigatório para consulta")

    def test_nao_deve_criar_uma_consulta_sem_data(self):
        medico = Medico(nome="Dr. House", hora_inicio=time(8,0), hora_fim=time(12,0))
        paciente = Paciente(nome="Romário", cpf="000111222333")

        with self.assertRaises(ValueError) as context:
            Consulta(medico, paciente, None, time(9,00))

    def test_nao_deve_criar_uma_consulta_sem_horario(self):
        medico = Medico(nome="Dr. House", hora_inicio=time(8,0), hora_fim=time(12,0))
        paciente = Paciente(nome="Romário", cpf="000111222333")

        with self.assertRaises(ValueError) as context:
            Consulta(medico, paciente, date(2026,4,30), None)

        self.assertEqual(str(context.exception), "horário da consulta é obrigatório")