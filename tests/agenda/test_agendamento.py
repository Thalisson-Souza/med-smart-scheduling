from unittest import TestCase
from datetime import datetime, date, time
from src.application.agendamento import Agendamento
from src.domain.medico import Medico
from src.domain.paciente import Paciente
from src.domain.consulta import Consulta

class TestAgendamento(TestCase):
    def setUp(self):
        self.agendamento = Agendamento()
        self.medico = Medico("Dr. House", time(8,0), time(12,0))
        self.paciente = Paciente(nome="Paciente Teste", cpf="00011122233")

        agenda_dr_house = {
        date(2026, 4, 30): {
            time(8,0): None,
            time(9,0): Consulta(self.medico, self.paciente, date(2026,4,30), time(9,0)),
            time(10,0): None,
            time(11,0): None,
            time(14,0): None,
            time(15,0): None
            }
        }   
        self.agendamento.cadastrar_agenda_medico(self.medico, agenda_dr_house)

    def test_deve_agendar_com_sucesso_quando_data_e_horario_estiverem_disponiveis(self):
        data_agendamento = date(2026, 4, 30)
        horario_agendamento = time(8,0)

        resultado = self.agendamento.processar_agendamento(self.medico, self.paciente, data_agendamento, horario_agendamento)
        self.assertTrue(resultado)

    def test_nao_deve_agendar_quando_horario_nao_existir(self):
        data_agendamento = date(2026, 4, 30)
        horario_agendamento_inexistente = time(0,0)

        self.assertRaises(ValueError, self.agendamento.processar_agendamento, self.medico, self.paciente, data_agendamento, horario_agendamento_inexistente)

    def test_nao_deve_agendar_quando_data_nao_existir(self):
        data_agendamento_inexistente = date(2026, 4, 20)
        horario_agendamento = time(11,0)

        self.assertRaises(ValueError, self.agendamento.processar_agendamento, self.medico, self.paciente, data_agendamento_inexistente, horario_agendamento)

    def test_nao_deve_agendar_quando_horario_esta_indisponivel(self):
        data_agendamento = date(2026, 4, 30)
        horario_agendamento_indisponivel = time(9,0)

        self.assertRaises(ValueError, self.agendamento.processar_agendamento, self.medico, self.paciente, data_agendamento, horario_agendamento_indisponivel)


    def test_nao_deve_agendar_fora_do_horario_de_atendimento_do_medico(self):
        data_agendamento = date(2026, 4, 30)
        horario_agendamento_fora_do_atendimento = time(14,0)

        with self.assertRaises(ValueError):
            self.agendamento.processar_agendamento(self.medico, self.paciente, data_agendamento, horario_agendamento_fora_do_atendimento)


    def test_deve_cadastrar_agenda_do_medico_com_sucesso(self):
        medico = Medico(nome="Teste", hora_inicio=time(8,0), hora_fim=time(12,0))
        
        agenda_dr_teste = {
            date(2026, 4, 30): {
                time(8,0): None,
                time(9,0): None,
            }
        }

        self.agendamento.cadastrar_agenda_medico(medico, agenda_dr_teste)
        self.assertIn(medico, self.agendamento._agenda_por_medico)
        self.assertEqual(self.agendamento._agenda_por_medico[medico], agenda_dr_teste)


    def test_nao_deve_agendar_quando_medico_ja_possui_consulta_no_mesmo_horario(self):
        data_agendamento = date(2026, 4, 30)
        horario_agendamento = time(10,0)

        self.agendamento.processar_agendamento(self.medico, self.paciente, data_agendamento, horario_agendamento)

        with self.assertRaises(ValueError) as context:
            self.agendamento.processar_agendamento(self.medico, self.paciente, data_agendamento, horario_agendamento)

        self.assertEqual(str(context.exception), "horário indisponível para agendamento")


    def test_nao_deve_criar_agendamento_com_duracao_zerada_ou_negativa(self):
        with self.assertRaises(ValueError):
            Agendamento(0)

        with self.assertRaises(ValueError):
            Agendamento(-100)


    def test_deve_listar_agenda_do_medico_se_existir_agendamento(self):
        medico = Medico(nome="Teste", hora_inicio=time(8,0), hora_fim=time(12,0))
        
        agenda_dr_teste_listagem = {
            date(2026, 4, 30): {
                time(8,0): None,
                time(9,0): None,
            }
        }
        self.agendamento.cadastrar_agenda_medico(medico, agenda_dr_teste_listagem)

        paciente_1 = Paciente(nome="Paciente 1", cpf="00011122233")
        paciente_2 = Paciente(nome="Paciente 2", cpf="11122233344")

        self.agendamento.processar_agendamento(medico, paciente_1, date(2026,4,30), time(8,0))
        self.agendamento.processar_agendamento(medico, paciente_2, date(2026,4,30), time(9,0))

        consultas = self.agendamento.listar_consultas_do_medico(medico)

        horarios = [consulta.horario for consulta in consultas]
        self.assertEqual(len(consultas), 2)
        self.assertIn(time(8,0), horarios)
        self.assertIn(time(9,0), horarios)


    def test_nao_deve_agendar_quando_horario_nao_respeita_duracao_padrao_de_consulta(self):
        agendamento = Agendamento(30)
        medico = Medico("Dr. House", time(8,0), time(12,0))
        paciente = Paciente("Paciente Teste", "00011122233")

        agenda_medico = {
            date(2026, 4, 30): {
                time(8,0): None,
                time(8,30): None,
                time(9,0): None,
            }
        }

        agendamento.cadastrar_agenda_medico(medico, agenda_medico)

        with self.assertRaises(ValueError) as context:
            agendamento.processar_agendamento(medico, paciente, date(2026,4,30), time(8,15))

        self.assertEqual(str(context.exception), "horário inválido para duração padrão da consulta")

    def test_deve_agendar_quando_horario_respeita_duracao_padrao_de_consulta(self):
        agendamento = Agendamento(30)
        medico = Medico("Dr. House", time(8,0), time(12,0))
        paciente = Paciente("Paciente Teste", "00011122233")

        agenda_medico_atende_em_30 = {
            date(2026, 4, 30): {
                time(8,0): None,
                time(8,30): None,
                time(9,0): None,
            }
        }
        
        self.agendamento.cadastrar_agenda_medico(medico, agenda_medico_atende_em_30)

        resultado = self.agendamento.processar_agendamento(medico, paciente, date(2026,4,30), time(8,30))
        self.assertTrue(resultado)