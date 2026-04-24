from unittest import TestCase
from agendamento import Agendamento

class TestAgendamento(TestCase):

    def test_deve_localizar_data_disponivel_na_agenda(self):
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