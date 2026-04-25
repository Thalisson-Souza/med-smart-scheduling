from unittest import TestCase
from src.agendamento import Agendamento

class TestAgendamento(TestCase):
    def setUp(self):
        self.agendamento = Agendamento()


    def test_deve_agendar_com_sucesso_quando_data_e_horario_estiverem_disponiveis(self):
        data_agendamento = "30-04-2026"
        hora_agendamento = "08:00"

        resultado = self.agendamento.processar_agendamento(data_agendamento, hora_agendamento)
        self.assertTrue(resultado)

    def test_nao_deve_agendar_quando_horario_nao_existir(self):
        data_agendamento = "30-04-2026"
        hora_agendamento_inexistente = "00:00"

        self.assertRaises(ValueError, self.agendamento.processar_agendamento, data_agendamento, hora_agendamento_inexistente)

    def test_nao_deve_agendar_quando_data_nao_existir(self):
        data_agendamento = "20-04-2026"
        hora_agendamento = "11:00"

        self.assertRaises(ValueError, self.agendamento.processar_agendamento, data_agendamento, hora_agendamento)

    