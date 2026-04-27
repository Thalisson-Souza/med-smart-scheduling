from datetime import date, time
from src.medico import Medico
class Agendamento:
    def __init__(self):
        self.agendamentos = []

        self.agenda = {
        date(2026, 4, 30): {
            time(8,0): True,
            time(9,0): False,
            time(10,0): True,
            time(11,0): True,
            time(14,0): True,
            time(15,0): True
            }
        }    

        self.agenda_por_medico = {}

    def cadastrar_agenda_medico(self, medico: Medico, agenda: dict):
        self.agenda_por_medico[medico.nome] = agenda

    def _validar_data_do_agendamento(self, data_agendamento):
        if data_agendamento not in self.agenda:
            raise ValueError("data não encontrada para agendamento")
        
    def _validar_horario_do_agendamento(self, data_agendamento, horario_agendamento):
        if horario_agendamento not in self.agenda[data_agendamento]:
            raise ValueError("horário não existe para a data informada")

    def _validar_horario_disponivel(self, data_agendamento, horario_agendamento):
        if not self.agenda [data_agendamento][horario_agendamento]:
            raise ValueError("horário indisponível para agendamento")
        
    def _validar_horario_de_atendimento_do_medico(self, medico: Medico, horario_agendamento):
        if not medico.esta_disponivel_no_horario(horario_agendamento):
            raise ValueError("médico não está disponível nesse horário")

    def processar_agendamento(self, medico: Medico, data_agendamento, horario_agendamento):
        self._validar_data_do_agendamento(data_agendamento)
        self._validar_horario_do_agendamento(data_agendamento, horario_agendamento)
        self._validar_horario_disponivel(data_agendamento, horario_agendamento)
        self._validar_horario_de_atendimento_do_medico(medico, horario_agendamento)


        self.agendamentos.append({
            "medico":medico, 
            "data":data_agendamento,
            "horario": horario_agendamento
        })

        self.agenda[data_agendamento][horario_agendamento] = False

        return True

    