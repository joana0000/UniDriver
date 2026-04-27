# Sprint 0 - Projeto Prático de Sistemas Distribuídos

## 1. Formação da Equipe

Repositório criado no GitHub para organização do projeto prático da disciplina de Sistemas Distribuídos.

### Integrantes da equipe

- Joana Martins Braga
- Rhaissa Rodrigues Rocha
- Gabriela Stringasci

Projeto utilizado como base: **Panapana**.

---

## 2. Definição do Domínio

O **Panapana** é um sistema web desenvolvido como projeto de TCC, com o objetivo de auxiliar no gerenciamento e organização de informações relacionadas ao seu domínio principal, permitindo que usuários acessem, cadastrem e consultem dados de forma centralizada.

O sistema busca oferecer uma plataforma organizada, segura e acessível, facilitando o uso por diferentes usuários e garantindo que as informações sejam armazenadas corretamente.

### Arquitetura lógica pretendida

A arquitetura lógica escolhida para o Panapana é **Cliente-Servidor**.

Nessa arquitetura, o usuário acessa o sistema por meio de uma interface web, que atua como cliente. As requisições feitas pelo usuário são enviadas para o servidor backend, responsável por processar as regras de negócio, acessar o banco de dados e devolver as respostas para o cliente.

### Estrutura geral da arquitetura

- **Cliente:** interface web utilizada pelos usuários.
- **Servidor Backend:** responsável pelo processamento das requisições, validações e regras de negócio.
- **Banco de Dados:** responsável pelo armazenamento das informações do sistema.

Essa arquitetura foi escolhida por ser adequada para sistemas web, permitir maior controle sobre os dados e facilitar a aplicação de conceitos de segurança, concorrência e tolerância a falhas.

---

## 3. O Recurso Crítico

O recurso crítico identificado no Panapana é o **cadastro e atualização de dados sensíveis dos usuários no sistema**.

Essas informações não podem ser alteradas simultaneamente por dois usuários ou processos ao mesmo tempo, pois isso poderia gerar inconsistências, perda de dados ou sobrescrita indevida de informações.

### Exemplo de problema

Caso dois acessos tentem alterar o mesmo registro ao mesmo tempo, uma atualização poderia sobrescrever a outra, fazendo com que o sistema salve uma informação incorreta ou desatualizada.

### Justificativa técnica

Como o Panapana trabalha com informações importantes dos usuários, é necessário garantir que operações de criação, edição ou exclusão desses dados sejam controladas. Para isso, futuramente poderão ser aplicadas estratégias como:

- controle de concorrência;
- bloqueio de registro durante atualização;
- validações no backend;
- transações no banco de dados;
- logs de alteração;
- mecanismos de tolerância a falhas.

Dessa forma, o sistema poderá manter a integridade dos dados e evitar conflitos em acessos simultâneos.
