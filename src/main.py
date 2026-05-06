from datetime import date, datetime, timedelta
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.application.agendamento import Agendamento
from src.domain.medico import Medico
from src.domain.paciente import Paciente


def titulo(texto):
    print()
    print(texto)
    print()


def pausar():
    input("\nPressione Enter para continuar...")


def ler_horario(texto):
    while True:
        valor = input(f"{texto} (HH:MM): ").strip()
        print()

        try:
            return datetime.strptime(valor, "%H:%M").time()
        except ValueError:
            print("Horario invalido. Exemplo: 09:00")
            print()


def formatar_data(data_consulta):
    return data_consulta.strftime("%d/%m/%Y")


def calcular_fim_consulta(horario_inicio, duracao_minutos):
    inicio = datetime.combine(date.today(), horario_inicio)
    return (inicio + timedelta(minutes=duracao_minutos)).time()


def criar_horarios(hora_inicio, hora_fim, duracao_minutos):
    horarios = {}
    atual = datetime.combine(date.today(), hora_inicio)
    fim = datetime.combine(date.today(), hora_fim)
    passo = timedelta(minutes=duracao_minutos)

    while atual < fim:
        horarios[atual.time()] = None
        atual += passo

    return horarios


def criar_contexto(consulta_10_ocupada=False):
    agendamento = Agendamento()
    medico = Medico(
        "Dr. House",
        datetime.strptime("08:00", "%H:%M").time(),
        datetime.strptime("12:00", "%H:%M").time(),
    )
    paciente = Paciente("Paciente Exemplo", "00011122233")
    data_consulta = date(2026, 4, 30)
    hora_inicio = datetime.strptime("08:00", "%H:%M").time()
    hora_fim = datetime.strptime("12:00", "%H:%M").time()

    agenda_medico = {
        data_consulta: criar_horarios(
            hora_inicio,
            hora_fim,
            agendamento.duracao_consulta_minutos,
        )
    }
    agendamento.cadastrar_agenda_medico(medico, agenda_medico)

    if consulta_10_ocupada:
        agendamento.processar_agendamento(
            medico,
            paciente,
            data_consulta,
            datetime.strptime("10:00", "%H:%M").time(),
        )

    return agendamento, medico, paciente, data_consulta


def mostrar_contexto(medico, data_consulta, agendamento):
    print(f'Medico criado: "{medico.nome}"')
    print("Jornada de atendimento: 08:00 as 12:00")
    print(f"Data da agenda: {formatar_data(data_consulta)}")
    print(f"Duracao fixa da consulta: {agendamento.duracao_consulta_minutos} minutos")
    print()


def mostrar_resultado_sucesso(data_consulta, horario, agendamento):
    horario_fim = calcular_fim_consulta(
        horario,
        agendamento.duracao_consulta_minutos,
    )
    print("Entao:")
    print("Agendamento confirmado com sucesso.")
    print(f"Consulta: {formatar_data(data_consulta)} {horario:%H:%M} as {horario_fim:%H:%M}")


def cenario_agendamento_com_sucesso():
    titulo("Cenario 1: Agendamento com sucesso")
    agendamento, medico, paciente, data_consulta = criar_contexto()

    print("Dado:")
    mostrar_contexto(medico, data_consulta, agendamento)
    print("E nao existe nenhum agendamento para as 09:00.")
    print()

    print("Quando:")
    horario = ler_horario("Tentar agendar consulta para")

    try:
        agendamento.processar_agendamento(medico, paciente, data_consulta, horario)
        mostrar_resultado_sucesso(data_consulta, horario, agendamento)
    except ValueError as erro:
        print("Entao:")
        print(f"Agendamento rejeitado: {erro}")


def cenario_fora_do_horario():
    titulo("Cenario 2: Erro por fora do horario de atendimento")
    agendamento, medico, paciente, data_consulta = criar_contexto()

    print("Dado:")
    mostrar_contexto(medico, data_consulta, agendamento)

    print("Quando:")
    horario = ler_horario("Tentar agendar consulta para")

    print("Entao:")
    if not medico.esta_disponivel_no_horario(horario):
        print("Agendamento rejeitado: medico nao esta disponivel nesse horario.")
        return

    try:
        agendamento.processar_agendamento(medico, paciente, data_consulta, horario)
        print("Agendamento confirmado com sucesso.")
    except ValueError as erro:
        print(f"Agendamento rejeitado: {erro}")


def cenario_conflito_de_horario():
    titulo("Cenario 3: Erro por conflito de horario")
    agendamento, medico, paciente, data_consulta = criar_contexto(
        consulta_10_ocupada=True
    )

    print("Dado:")
    mostrar_contexto(medico, data_consulta, agendamento)
    print("E o medico ja possui uma consulta marcada para as 10:00.")
    print()

    print("Quando:")
    horario = ler_horario("Tentar agendar nova consulta para")

    print("Entao:")
    try:
        agendamento.processar_agendamento(medico, paciente, data_consulta, horario)
        print("Agendamento confirmado com sucesso.")
    except ValueError as erro:
        if str(erro) == "horário indisponível para agendamento":
            print("Agendamento rejeitado: Conflito de Horario.")
        else:
            print(f"Agendamento rejeitado: {erro}")


def menu():
    opcoes = {
        "1": cenario_agendamento_com_sucesso,
        "2": cenario_fora_do_horario,
        "3": cenario_conflito_de_horario,
    }

    while True:
        titulo("Med Smart Scheduling - Criterios de Aceitacao")
        print("1. Cenario 1: Agendamento com sucesso")
        print("2. Cenario 2: Fora do horario de atendimento")
        print("3. Cenario 3: Conflito de horario")
        print("0. Sair")
        print()

        escolha = input("Escolha um cenario: ").strip()
        print()

        if escolha == "0":
            print("Encerrando...")
            break

        acao = opcoes.get(escolha)

        if acao is None:
            print("Opcao invalida.")
        else:
            acao()

        pausar()


if __name__ == "__main__":
    menu()
