from unittest import TestCase
from datetime import datetime, date, time
from src.agendamento import Agendamento
from src.medico import Medico

class TestAgendamento(TestCase):
    def setUp(self):
        self.agendamento = Agendamento()
        self.medico = Medico("Dr. House", time(8,0), time(12,0))

    def test_deve_agendar_com_sucesso_quando_data_e_horario_estiverem_disponiveis(self):
        data_agendamento = date(2026, 4, 30)
        horario_agendamento = time(8,0)

        resultado = self.agendamento.processar_agendamento(self.medico, data_agendamento, horario_agendamento)
        self.assertTrue(resultado)

    def test_nao_deve_agendar_quando_horario_nao_existir(self):
        data_agendamento = date(2026, 4, 30)
        horario_agendamento_inexistente = time(0,0)

        self.assertRaises(ValueError, self.agendamento.processar_agendamento, self.medico, data_agendamento, horario_agendamento_inexistente)

    def test_nao_deve_agendar_quando_data_nao_existir(self):
        data_agendamento_inexistente = date(2026, 4, 20)
        horario_agendamento = time(11,0)

        self.assertRaises(ValueError, self.agendamento.processar_agendamento, self.medico, data_agendamento_inexistente, horario_agendamento)

    def test_nao_deve_agendar_quando_horario_esta_indisponivel(self):
        data_agendamento = date(2026, 4, 30)
        horario_agendamento_indisponivel = time(9,0)

        self.assertRaises(ValueError, self.agendamento.processar_agendamento, self.medico, data_agendamento, horario_agendamento_indisponivel)


    def test_nao_deve_agendar_fora_do_horario_de_atendimento_do_medico(self):
        data_agendamento = date(2026, 4, 30)
        horario_agendamento_fora_do_atendimento = time(14,0)

        with self.assertRaises(ValueError):
            self.agendamento.processar_agendamento(self.medico, data_agendamento, horario_agendamento_fora_do_atendimento)


    def test_deve_cadastrar_agenda_do_medico_com_sucesso(self):
        medico = Medico(nome="Teste", hora_inicio=time(8,0), hora_fim=time(12,0))
        
        agenda_dr_teste = {
            date(2026, 4, 30): {
                time(8,0): True,
                time(9,0): False,
            }
        }

        self.agendamento.cadastrar_agenda_medico(medico, agenda_dr_teste)
        self.assertIn("Teste", self.agendamento.agenda_por_medico)
        self.assertEqual(self.agendamento.agenda_por_medico["Teste"], agenda_dr_teste)