# Med Smart Scheduling

Módulo de Agendamento Inteligente desenvolvido como MVP para validar automaticamente horários médicos, evitando agendamentos fora da jornada de trabalho e conflitos de agenda.


## Visão geral

O projeto implementa um módulo de agendamento inteligente para validar automaticamente horários médicos e evitar conflitos de agenda durante o processo de marcação de consultas.

## Problema

Em clínicas médicas, parte do tempo operacional é gasto resolvendo conflitos de agenda ou corrigindo horários marcados fora do turno de atendimento dos médicos.

Processos manuais de agendamento podem gerar inconsistências como:

- agendamentos fora do horário de trabalho do médico;
- sobreposição de consultas para o mesmo médico;
- horários aparentemente disponíveis, mas inválidos;
- retrabalho manual para corrigir conflitos de agenda.

Segundo o cenário definido no PRD do projeto, cerca de 22% do tempo das secretárias é consumido por esse tipo de correção, enquanto 15% dos agendamentos apresentam risco de conflito de horário.

## Objetivo

Automatizar a validação de disponibilidade médica para reduzir erros de agendamento, evitar conflitos de horário e tornar o processo de marcação de consultas mais confiável.

A proposta do MVP é reduzir o tempo gasto com correções manuais e minimizar conflitos de agenda durante o processo de agendamento.

O sistema deve garantir que:

- o médico possua uma grade de atendimento configurada;
- consultas sejam agendadas apenas dentro do horário de trabalho;
- não existam dois agendamentos no mesmo horário para o mesmo médico;
- cada consulta siga uma duração padrão definida para o MVP.


## Requisitos Funcionais (RF)

- **RF01 - Configuração de Grade:**  
  O sistema deve permitir definir o horário de início e fim da jornada de um médico.

- **RF02 - Validação de Horário:**  
  Não deve ser possível agendar um paciente fora do horário de trabalho do médico.

- **RF03 - Prevenção de Sobreposição:**  
  O sistema deve impedir dois agendamentos no mesmo horário para o mesmo médico.

- **RF04 - Duração Fixa:**  
  Cada consulta possui uma duração padrão (ex: 30 minutos) definida para o MVP.


## Desenvolvimento com Test-Driven Development

O projeto foi desenvolvido utilizando a abordagem de Programação Orientada a Testes (TDD), usando os testes como guia para implementar e validar as regras de negócio do MVP.

Essa abordagem ajudou a validar os comportamentos esperados do sistema, garantir maior segurança durante as implementações e verificar que novas funcionalidades não afetassem regras já existentes, utilizando cenários de sucesso e falha durante o desenvolvimento.

## Tecnologias

- Python 3.12.3
- `unittest`

## Conceitos aplicados

- Programação Orientada a Objetos (POO)
- Test-Driven Development (TDD)

## Como executar

Clone o repositório:

```bash
git clone https://github.com/Thalisson-Souza/med-smart-scheduling
```
Entre na pasta do projeto:
```bash
cd med-smart-scheduling
```

Execute os testes:

```bash
python3 -m unittest -v
```

## Demonstração dos Critérios de Aceitação

O projeto possui um fluxo simples no terminal para demonstrar os cenários definidos no PRD do MVP.

Execute:

```bash
python3 -m src.main
```

O fluxo apresenta três cenários:

- **Cenário 1 - Agendamento com sucesso:**  
  O médico **Dr. House** atende das **08:00 às 12:00**.  
  Ao tentar agendar uma consulta para **09:00**, sem conflito prévio, o sistema confirma o agendamento com sucesso.

- **Cenário 2 - Erro por fora do horário de atendimento:**  
  O médico **Dr. House** atende das **08:00 às 12:00**.  
  Ao tentar agendar uma consulta para **14:00**, o sistema rejeita o agendamento informando que o médico não está disponível nesse horário.

- **Cenário 3 - Erro por conflito de horário:**  
  O médico **Dr. House** já possui uma consulta marcada às **10:00**.  
  Ao tentar agendar uma nova consulta às **10:00**, o sistema rejeita o agendamento por conflito de horário.

Em todos os cenários, a consulta possui duração fixa de **30 minutos**.
