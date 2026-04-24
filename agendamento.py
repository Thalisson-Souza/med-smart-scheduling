class Agendamento:
    
    agenda = {
        "30-04-2026": {
            "08:00": True,
            "09:00": False,
            "10:00": True,
            "14:00": True,
        }
    }

    def processar_agendamento(self, data_agendamento, horario_agendamento):
    
        if data_agendamento not in self.agenda:
            raise ValueError("data não encontrada")
        
        if horario_agendamento == "00:00":
            raise ValueError("Horario invalido")

        return True

    