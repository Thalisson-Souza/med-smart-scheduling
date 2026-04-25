from datetime import datetime, date, time

class Medico:
    def __init__(self, nome, hora_inicio, hora_fim):
        if not nome:
            raise ValueError("nome do médico é obrigatório")


        self.__nome = nome
        self.__hora_inicio = hora_inicio
        self.__hora_fim = hora_fim


    def esta_disponivel_no_horario(self, horario):
        return self.__hora_inicio <= horario < self.__hora_fim
    