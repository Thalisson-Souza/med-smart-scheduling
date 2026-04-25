from datetime import date, time

class Agendamento:
    
    agenda = {
        date(2026, 4, 30): {
            time(8,0): True,
            time(9,0): False,
            time(10,0): True,
            time(11,0): True,
        }
    }

    def processar_agendamento(self, data_agendamento, horario_agendamento):
    
        if data_agendamento not in self.agenda:
            raise ValueError("data não encontrada para agendamento")
        
        if horario_agendamento not in self.agenda[data_agendamento]:
            raise ValueError("horário não existe para a data informada")

        return True

    