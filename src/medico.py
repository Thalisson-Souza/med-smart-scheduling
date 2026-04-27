from datetime import datetime, date, time

class Medico:
    def __init__(self, nome, hora_inicio, hora_fim):
        if not nome:
            raise ValueError("nome do médico é obrigatório")

        if hora_inicio >= hora_fim:
            raise ValueError("horário invalido")

        self.__nome = nome
        self.__hora_inicio = hora_inicio
        self.__hora_fim = hora_fim

    @property
    def nome(self):
        return self.__nome

    def esta_disponivel_no_horario(self, horario):
        return self.__hora_inicio <= horario < self.__hora_fim
    