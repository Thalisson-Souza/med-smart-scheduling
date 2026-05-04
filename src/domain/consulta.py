from src.domain.medico import Medico
from src.domain.paciente import Paciente

class Consulta:
    def __init__(self, medico: Medico, paciente: Paciente, data_consulta, hora_consulta):
        if not medico:
            raise ValueError("médico é obrigatório para consulta")
        
        if not paciente:
            raise ValueError("paciente é obrigatório para consulta")
        
        if not isinstance(medico, Medico):
            raise ValueError("médico recebido não é uma instância de médico válida")
        
        if not data_consulta:   
            raise ValueError("data da consulta é obrigatória")
        
        if hora_consulta is None:
            raise ValueError("horário da consulta é obrigatório")

        self._medico = medico
        self._paciente = paciente
        self._data_consulta = data_consulta
        self._hora_consulta = hora_consulta

    @property
    def medico(self):
        return self._medico
    
    @property
    def paciente(self):
        return self._paciente
    
    @property
    def data(self):
        return self._data_consulta
    
    @property
    def horario(self):
        return self._hora_consulta
    