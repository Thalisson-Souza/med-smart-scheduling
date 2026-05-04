from datetime import date, time
from src.domain.medico import Medico
from src.domain.consulta import Consulta

class Agendamento:
    def __init__(self, duracao_consulta_minutos=30):
        if duracao_consulta_minutos <= 0:
            raise ValueError("duração da consulta é menor que igual a zero")
        
        self.duracao_consulta_minutos = duracao_consulta_minutos
        self._agenda_por_medico = {}

    def listar_consultas_do_medico(self, medico):
        return list(self._agenda_por_medico.get(medico, []))

    def cadastrar_agenda_medico(self, medico: Medico, agenda: dict):
        self._agenda_por_medico[medico] = agenda

    def _obter_agenda_do_medico(self, medico: Medico):
        agenda_medico = self._agenda_por_medico.get(medico)

        if agenda_medico is None:
            raise ValueError("médico não tem agenda cadastrada")
        return agenda_medico
    

    def _validar_data_do_agendamento(self, agenda_medico, data_agendamento):
        if data_agendamento not in agenda_medico:
            raise ValueError("data não encontrada para agendamento")
        
    def _validar_horario_do_agendamento(self, agenda_medico, data_agendamento, horario_agendamento):
        if horario_agendamento not in agenda_medico[data_agendamento]:
            raise ValueError("horário não existe para a data informada")

    def _validar_horario_disponivel(self, agenda_medico, data_agendamento, horario_agendamento):
        if agenda_medico[data_agendamento][horario_agendamento] is not None:
            raise ValueError("horário indisponível para agendamento")
        
    def _validar_horario_de_atendimento_do_medico(self, medico: Medico, horario_agendamento):
        if not medico.esta_disponivel_no_horario(horario_agendamento):
            raise ValueError("horário fora do período de atendimento do médico")
        

    def processar_agendamento(self, medico: Medico, paciente, data_agendamento, horario_agendamento):
        agenda_medico = self._obter_agenda_do_medico(medico)

        self._validar_data_do_agendamento(agenda_medico, data_agendamento)
        self._validar_horario_do_agendamento(agenda_medico, data_agendamento, horario_agendamento)
        self._validar_horario_de_atendimento_do_medico(medico, horario_agendamento)
        self._validar_horario_disponivel(agenda_medico, data_agendamento, horario_agendamento)

        agenda_medico[data_agendamento][horario_agendamento] = Consulta(medico, paciente, data_agendamento, horario_agendamento)

        return True