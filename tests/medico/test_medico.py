from unittest import TestCase
from datetime import datetime, date, time
from src.medico import Medico

class TestMedico(TestCase):

    def test_nao_deve_permitir_registrar_agendamento_fora_do_horario_de_trabalho(self):
        medico = Medico("Dr. House", time(8,0), time(12,0))

        self.assertFalse(medico.esta_disponivel_no_horario(time(14,00)))