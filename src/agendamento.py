from datetime import date, time
from src.medico import Medico
class Agendamento:
    def __init__(self):
        self.agendamentos = []
        self.agenda_por_medico = {}

    def cadastrar_agenda_medico(self, medico: Medico, agenda: dict):
        self.agenda_por_medico[medico.nome] = agenda

    def _obter_agenda_do_medico(self, medico: Medico):
        agenda_medico = self.agenda_por_medico.get(medico.nome)

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
        if not agenda_medico [data_agendamento][horario_agendamento]:
            raise ValueError("horário indisponível para agendamento")
        
    def _validar_horario_de_atendimento_do_medico(self, medico: Medico, horario_agendamento):
        if not medico.esta_disponivel_no_horario(horario_agendamento):
            raise ValueError("médico não está disponível nesse horário")
        

    def _validar_conflito_de_horario_na_agenda_do_medico(self, medico: Medico, data_agendamento, horario_agendamento):
        for agendamento in self.agendamentos:
            if (
                agendamento["medico"] == medico
                and agendamento["data"] == data_agendamento
                and agendamento["horario"] == horario_agendamento
            ):
                raise ValueError("conflito de horário, já tem consulta para esse horário")

    def processar_agendamento(self, medico: Medico, data_agendamento, horario_agendamento):
        agenda_medico = self._obter_agenda_do_medico(medico)

        self._validar_data_do_agendamento(agenda_medico, data_agendamento)
        self._validar_horario_do_agendamento(agenda_medico, data_agendamento, horario_agendamento)
        self._validar_horario_de_atendimento_do_medico(medico, horario_agendamento)
        self._validar_conflito_de_horario_na_agenda_do_medico(medico, data_agendamento, horario_agendamento)
        self._validar_horario_disponivel(agenda_medico, data_agendamento, horario_agendamento)

        self.agendamentos.append({
            "medico":medico, 
            "data":data_agendamento,
            "horario": horario_agendamento
        })

        agenda_medico[data_agendamento][horario_agendamento] = False

        return True

    