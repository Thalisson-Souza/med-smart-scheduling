from unittest import TestCase
from agendamento import Agendamento

class TestAgendamento(TestCase):

    def test_deve_agendar_com_sucesso_quando_data_e_horario_estiverem_disponiveis(self):
        agendamento = Agendamento()

        data_agendamento = "30-04-2026"
        hora_agendamento = "08:00"

        resultado = agendamento.processar_agendamento(data_agendamento, hora_agendamento)
        self.assertTrue(resultado)

    def test_nao_deve_agendar_quando_horario_nao_existir(self):
        agendamento = Agendamento()

        data_agendamento = "30-04-2026"
        hora_agendamento_inexistente = "00:00"

        self.assertRaises(ValueError, agendamento.processar_agendamento, data_agendamento, hora_agendamento_inexistente)

    def test_nao_deve_agendar_quando_data_nao_existir(self):
        agendamento = Agendamento()

        data_agendamento = "20-04-2026"
        hora_agendamento = "11:00"

        self.assertRaises(ValueError, agendamento.processar_agendamento, data_agendamento, hora_agendamento)

