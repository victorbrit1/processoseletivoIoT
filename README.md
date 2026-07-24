# Processo Seletivo – Intensivo Maker | IoT

## Etapa Prática – Sistemas Embarcados

Bem-vindo(a) à **etapa prática do processo seletivo para o Intensivo Maker | IoT**.

Esta atividade tem como objetivo avaliar suas competências em **Sistemas Embarcados**, com foco em **organização de projeto, lógica de firmware e simulação de hardware**, a partir da aplicação prática dos conhecimentos adquiridos nos cursos EAD da etapa anterior.

> **Objetivo principal**  
> Avaliar sua capacidade de **planejar, estruturar e desenvolver** uma solução funcional de sistemas embarcados, seguindo boas práticas de engenharia.

---

## Antes de Tudo

Se você **nunca utilizou Git ou GitHub**, não se preocupe.  
Siga atentamente os passos abaixo.

---

### 1 - Criação de Conta no GitHub

1. Acesse: <https://github.com>
2. Clique em **Sign up**
3. Crie sua conta gratuita seguindo as instruções da plataforma

> O GitHub será utilizado para:
>
> - Envio do seu projeto
> - Versionamento do código
> - Correção e validação automática via GitHub Actions

---

### 2 - Instalação do Git

O **Git** é a ferramenta responsável pelo controle de versões do seu código.

### Windows

Baixe e instale o **Git Bash**:  
<https://git-scm.com/downloads>

### Linux / macOS

Verifique se o Git já está instalado:

```bash
git --version
```

> Caso não esteja, instale pelo gerenciador de pacotes do seu sistema.

## Preparando o Ambiente

Para desenvolver o desafio, você deverá criar uma cópia deste repositório no seu GitHub.

### 1 - Fork do Repositório

No canto superior direito desta página, clique em Fork

<img width="219" height="45" alt="image" src="https://github.com/user-attachments/assets/5d629626-513a-445c-ba0f-e5bb3e225187" />

Uma cópia do repositório será criada no seu perfil do GitHub

> O Fork permite que você trabalhe de forma independente, sem alterar o repositório original do processo seletivo.

### 2 - Clone do Repositório

No repositório do seu Fork, clique em **<> Code**

<img width="149" height="52" alt="image" src="https://github.com/user-attachments/assets/abbd331b-a005-4633-89c6-afd16acbe828" />

Copie a URL e execute no terminal:

```bash
git clone https://github.com/SEU_USUARIO/nome-do-repositorio.git
cd nome-do-repositorio
```

> O comando git clone cria uma cópia local do repositório para desenvolvimento.

### 3 - Preparação do Ambiente de Execução

Você pode executar o projeto de duas formas. Escolha apenas uma.

#### Opção A – Ambiente Python Local

**Requisitos:**

- Python 3.10 ou 3.11
- pip

**Instale as dependências:**

```bash
pip install -r requirements.txt
```

#### Opção B – Dev Container (Recomendado)

Este repositório inclui um Dev Container, garantindo um ambiente padronizado.

**Requisitos:**

- VS Code
- Docker instalado
- Extensão Dev Containers

**Passos:**

1. Abra o repositório no VS Code
2. Clique em “Reopen in Container”
3. Aguarde a criação automática do ambiente

> Todas as dependências serão instaladas automaticamente.

## Criando sua API Key do Wokwi

A simulação do projeto será executada automaticamente via GitHub Actions, utilizando o Wokwi CLI.

Para isso, você precisa gerar uma API Key.

1. Acesse: <https://wokwi.com/dashboard/ci>
2. Faça login (Google ou GitHub)
3. Clique em Generate API Token
4. Copie a chave gerada (exemplo: wokwi-xxxxxxxx)

> Importante

- Nunca faça commit dessa chave
- Ela deve ser armazenada apenas como secret no GitHub

## Configurando a API Key no GitHub (Secrets)

**No repositório do seu Fork:**

1. Vá em Settings
2. Acesse Secrets and variables → Actions
3. Clique em New repository secret
4. Nome: WOKWI_API_KEY
5. Valor: sua chave gerada
6. Salve

> As GitHub Actions do template já estão preparadas para usar essa variável automaticamente.

## Desafio Técnico

Você deverá desenvolver um projeto de sistemas embarcados simulados, utilizando Python e Wokwi.

### Estrutura mínima esperada

```text
/project
 ├── src/
 │   └── main.py        # Código principal do projeto
 ├── wokwi.toml         # Configuração da simulação
 ├── diagram.json       # Circuito no Wokwi
 └── README.md          # Explicação do seu projeto
```

> Você pode expandir essa estrutura se desejar, desde que mantenha os arquivos essenciais.

### Escolha do cenário

No diretório "scenarios" existem arquivos .md e pastas referentes a diferentes desafios. Selecione apenas um deles e mantenha apenas a pasta e .md referente ao desafio a ser desenvolvido, deletando os demais. Isso fará com o que o fluxo de testes automáticos selecione o fluxo de acordo com o desafio escolhido.

### Como Desenvolver seu Projeto

O desenvolvimento acontece principalmente nos arquivos abaixo:

#### src/main.py

- Código Python executado na simulação
- Implementa a lógica do sistema embarcado
- Exemplos: controle de LEDs, leitura de sensores, estados, temporizações, etc.

#### diagram.json

- Define o hardware virtual do projeto
- Componentes como:
  - LEDs
  - Botões
  - Sensores
  - Placa microcontroladora

#### wokwi.toml

- Configura a simulação:
  - Tipo de placa
  - Framework
  - Dependências adicionais

#### Rodando localmente

Para executar o seu projeto locamente, é necesário preparar a imagem docker local, e após isso
utiliza-la para gerar o arquivo que conterá o seu código para o projeto, para isso, execute os
seguintes códigos:

1. Prepara a imagem docker (Necessário rodar apenas 1 vez)

```bash
docker build -t esp32-builder -f Dockerfile .
```

2. Prepara o arquivo de memória fs.bin (Necessário a cada iteração)

```bash
docker run --rm -v "$(pwd)/src:/mnt/src" -v "$(pwd):/mnt/out" esp32-builder bash -c "mkdir -p /tmp/fs && cp -r /mnt/src/* /tmp/fs/ && /mklittlefs/mklittlefs -c /tmp/fs -b 4096 -p 256 -s 0x200000 /mnt/out/fs.bin"
```

#### Commit e Push

Após suas alterações:

```bash
git add .
git commit -m "Descrição clara do que foi feito"
git push
```

### Execução Automática (GitHub Actions)

A cada push, o GitHub Actions irá automaticamente:

- Executar o pipeline de build
- Rodar a simulação via Wokwi CLI
- Validar que o projeto executa sem erros

### Caso algo falhe

- Vá até a aba Actions
- Analise os logs da execução
- Corrija e envie novamente

## Critérios de Avaliação

Esta etapa será avaliada considerando:

- Funcionamento correto da simulação
- Código organizado e legível
- Estrutura de arquivos correta
- Uso adequado do Wokwi
- Commits claros e bem descritos
- Projeto executando sem falhas nas Actions

---

## Submissão Final

Após concluir o desenvolvimento:

1. Verifique se o projeto **executa sem erros** nas GitHub Actions
2. Confirme que todos os arquivos obrigatórios estão presentes
3. Copie o link do **seu repositório no GitHub**

Envie o link conforme as orientações do processo seletivo na plataforma do **PNAAT**.

---

## Relatório do Candidato

O arquivo **`README.md` do seu repositório** deve ser utilizado como o  
**relatório final do desafio técnico**.

Preencha todas as seções abaixo de forma **clara, objetiva e técnica**.

> **Dica importante**  
> Não é necessário um relatório extenso.  
> O principal critério é demonstrar **clareza nas decisões técnicas**, organização e entendimento do sistema embarcado desenvolvido.
> Não mantenha os demais conteúdos escritos nesse arquivo README, aqui devem ser concentradas apenas informações referentes ao projeto desenvolvido.

---

### Identificação do Candidato

- Victor Conceição de Brito
- https://github.com/victorbrit1

---

## Visão Geral da Solução

O projeto consiste em um sistema embarcado desenvolvido em MicroPython para simular o monitoramento de uma linha de produção utilizando um ESP32. O sistema realiza a contagem automática de peças por meio de um sensor fotoresistor (LDR), identifica situações de micro-parada quando o sensor permanece bloqueado por um período prolongado e permite reiniciar o turno de produção utilizando um botão.

A interação ocorre através do monitor serial, que informa os eventos detectados, e do botão físico, utilizado para reinicializar os contadores do sistema.

---

## Arquitetura do Sistema Embarcado

O firmware foi implementado em um único arquivo (main.py), conforme a estrutura proposta pelo desafio. A aplicação utiliza um laço principal (while True) responsável por executar continuamente todas as rotinas do sistema de forma sequencial, permitindo monitorar o sensor, o botão e o tempo de bloqueio sem interromper a execução do sistema.

Durante cada ciclo do programa são realizadas:

leitura do sensor LDR;
identificação dos estados de linha livre e linha bloqueada;
contagem das peças através da transição entre esses estados;
monitoramento do tempo de bloqueio para detectar micro-paradas;
leitura do botão utilizando debounce por software;
atualização das mensagens enviadas ao monitor serial.

Para evitar contagens incorretas, foram utilizados dois limiares de leitura do sensor, criando uma histerese entre os estados de bloqueio e linha livre.

## Componentes Utilizados na Simulação

ESP32 Simulation:
Responsável pela execução do firmware e leitura dos dispositivos conectados.

Wokwi-photoresistor-sensor(LDR):
Utilizado para detectar a passagem das peças através da variação da luminosidade incidente.

Wokwi-pushbutton:
Responsável por reiniciar a contagem do turno.

Monitor Serial

Utilizado para apresentar todas as mensagens exigidas pela especificação do projeto.

## Decisões Técnicas Relevantes

Durante o desenvolvimento foram adotadas algumas decisões para garantir estabilidade durante a simulação, facilitar a manutenção do código e garantir compatibilidade com os testes automatizados.

- Utilização de constantes para configuração dos limiares do sensor e tempos de controle, evitando números fixos espalhados pelo código e facilitando futuros ajustes.

- Implementação de debounce por software utilizando `time.ticks_ms()`, eliminando leituras falsas provocadas pelo acionamento mecânico do botão e garantindo apenas um reset por acionamento.

- Utilização de temporização não bloqueante para detectar micro-paradas sem interromper a leitura contínua do sensor e do botão.

- Definição de dois limiares distintos para o sensor (`THRESH_FREE` e `THRESH_BLOCKED`), implementando uma histerese simples para evitar oscilações próximas ao ponto de leitura e impedir múltiplas contagens durante a passagem de uma única peça.

- Implementação da variável `microparada_reportada` para impedir que o mesmo alerta fosse exibido repetidamente enquanto o sensor permanecesse bloqueado.

- Utilização do resistor interno de pull-up do ESP32 (`Pin.PULL_UP`), eliminando a necessidade de componentes externos e simplificando o circuito.

- Ajuste experimental dos limiares do sensor após testes realizados no simulador Wokwi, buscando maior estabilidade na identificação da passagem das peças.

## Resultados Obtidos

Após os testes realizados na simulação, o sistema apresentou o comportamento esperado.

- Inicialização correta do firmware.
- Contagem das peças apenas após a passagem completa pelo sensor.
- Detecção automática de micro-paradas após cinco segundos de bloqueio contínuo.
- Funcionamento correto do botão de reset com tratamento de debounce.
- Exibição correta das mensagens exigidas pela especificação do desafio.
- Aprovação nos três cenários automatizados do Wokwi CI: contagem de peças, detecção de micro-parada e reset de turno.

## Comentários Adicionais (Opcional)

Durante o desenvolvimento foi necessário realizar testes para identificar os valores de leitura do sensor fotoresistor no ambiente de simulação, permitindo definir limiares adequados para diferenciar os estados de linha livre e linha bloqueada.

Também foi realizada a validação da ligação elétrica do botão utilizando o resistor interno de pull-up do ESP32, garantindo compatibilidade entre o circuito implementado e a lógica do firmware.

Como melhoria futura, seria interessante adicionar um LED para fornecer feedback visual ao operador, indicando eventos como micro-paradas ou o reset do turno. Essa alteração tornaria a interação com o sistema mais intuitiva e facilitaria o monitoramento da linha de produção sem depender exclusivamente do monitor serial.

A estrutura atual do firmware permite incorporar novos dispositivos de saída sem alterações significativas na lógica principal do sistema.

> Este relatório faz parte da avaliação técnica.  
> Clareza, objetividade e organização são tão importantes quanto o funcionamento do código.

---

## Especificação dos Testes Automatizados (Wokwi CI)

Para que o projeto seja validado com sucesso na esteira de integração contínua (CI), o firmware escrito em MicroPython deve interagir corretamente com as leituras dos sensores descritos em cada cenário e enviar as mensagens de status exatas.

### Requisitos Críticos de Implementação

1. **Casamento Exato de Strings:** O Wokwi CI faz uma verificação estrita caractere por caractere. Se houver divergência em maiúsculas/minúsculas, acentuação ou falta de pontuação, o teste irá falhar.
2. **Arquitetura Não-Bloqueante:** Evite o uso de funções bloqueantes. Elas podem fazer com que o firmware perca a janela de tempo em que o simulador altera o peso, quebrando a sincronia do teste automatizado.

---

## Suporte

Em caso de dúvidas:

- Consulte o material dos cursos EAD
- Leia atentamente este README
- Analise os logs das GitHub Actions
- Utilize os canais oficiais para contato com os instrutores
