from src.medico import Medico
from src.paciente import Paciente

class Consulta:
    def __init__(self, medico, paciente, data_consulta, hora_consulta):
        if not medico:
            raise ValueError("médico é obrigatório para consulta")

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
    