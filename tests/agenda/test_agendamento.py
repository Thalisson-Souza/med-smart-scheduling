from unittest import TestCase
from datetime import datetime, date, time
from src.agendamento import Agendamento
from src.medico import Medico

class TestAgendamento(TestCase):
    def setUp(self):
        self.agendamento = Agendamento()
        self.medico = Medico("Dr. House", time(8,0), time(12,0))

    def test_deve_agendar_com_sucesso_quando_data_e_horario_estiverem_disponiveis(self):
        data = date(2026, 4, 30)
        hora = time(8,0)

        resultado = self.agendamento.processar_agendamento(self.medico, data, hora)
        self.assertTrue(resultado)

    def test_nao_deve_agendar_quando_horario_nao_existir(self):
        data = date(2026, 4, 30)
        hora_inexistente = time(0,0)

        self.assertRaises(ValueError, self.agendamento.processar_agendamento, self.medico, data, hora_inexistente)

    def test_nao_deve_agendar_quando_data_nao_existir(self):
        data_inexistente = date(2026, 4, 20)
        hora = time(11,0)

        self.assertRaises(ValueError, self.agendamento.processar_agendamento, self.medico,data_inexistente, hora)

    def test_nao_deve_agendar_quando_horario_esta_indisponivel(self):
        data = date(2026, 4, 30)
        hora_indisponivel_na_agenda = time(9,0)

        self.assertRaises(ValueError, self.agendamento.processar_agendamento, self.medico, data, hora_indisponivel_na_agenda)


    def test_nao_deve_agendar_fora_do_horario_do_medico(self):
        data = date(2026, 4, 30)
        hora_fora_da_jornada = time(14,0)

        with self.assertRaises(ValueError):
            self.agendamento.processar_agendamento(self.medico, data, hora_fora_da_jornada)