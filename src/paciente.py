class Paciente:
    def __init__(self, nome, cpf):
        if not nome:
            raise ValueError("nome do paciente é obrigatório")

        self.__nome = nome
        self.__cpf = cpf
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def cpf(self):
        return self.__cpf