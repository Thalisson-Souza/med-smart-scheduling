from unittest import TestCase
from datetime import datetime, date, time
from src.medico import Medico

class TestMedico(TestCase):

    def test_nao_deve_permitir_registrar_agendamento_fora_do_horario_de_atendimento(self):
        medico = Medico("Dr. House", time(8,0), time(12,0))

        self.assertFalse(medico.esta_disponivel_no_horario(time(14,00)))

    def test_deve_permitir_registrar_agendamento_dentro_do_horario_de_atendimento(self):
        medico = Medico("Dr. House", time(8,0), time(12,0))

        self.assertTrue(medico.esta_disponivel_no_horario(time(9,00)))

    def test_deve_permitir_registrar_agendamento_no_limite_inferior_do_horario_de_atendimento(self):
        medico = Medico("Dr. House", time(8,0), time(12,0))

        self.assertTrue(medico.esta_disponivel_no_horario(time(8,0)))

    def test_nao_deve_permitir_registrar_agendamento_no_limite_superior_do_horario_de_atendimento(self):
        medico = Medico("Dr. House", time(8,0), time(12,0))

        self.assertFalse(medico.esta_disponivel_no_horario(time(12,0)))

    def test_nao_deve_criar_de_medico_sem_nome(self):
        with self.assertRaises(ValueError):
            Medico(None, time(8,0), time(12,0))     

    def test_nao_deve_criar_medico_com_hora_inicio_maior_que_hora_fim(self):
        with self.assertRaises(ValueError) as context:
            Medico("Dr. House", time(12,0), time(8,0))

        self.assertEqual(str(context.exception), "horário invalido")