from datetime import date, time
from src.medico import Medico
class Agendamento:
    agenda = {
        date(2026, 4, 30): {
            time(8,0): True,
            time(9,0): False,
            time(10,0): True,
            time(11,0): True,
        }
    }

    def _validar_data_do_agendamento(self, data):
        if data not in self.agenda:
            raise ValueError("data não encontrada para agendamento")
        
    def _validar_horario_do_agendamento(self, horario, data):
        if horario not in self.agenda[data]:
            raise ValueError("horário não existe para a data informada")

    def _verificar_se_horario_esta_disponivel(self, data, horario):
        if not self.agenda [data][horario]:
            raise ValueError("horário indisponivel para agendamento")
        

    def processar_agendamento(self, data_agendamento, horario_agendamento):
        self._validar_data_do_agendamento(data_agendamento)
        self._validar_horario_do_agendamento(horario_agendamento, data_agendamento)
        self._verificar_se_horario_esta_disponivel(data_agendamento, horario_agendamento)


        return True

    