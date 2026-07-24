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

## Comentários Adicionais (Opcional).

Durante o desenvolvimento foi necessário realizar testes para identificar os valores de leitura do sensor fotoresistor no ambiente de simulação, permitindo definir limiares adequados para diferenciar os estados de linha livre e linha bloqueada.

Também foi realizada a validação da ligação elétrica do botão utilizando o resistor interno de pull-up do ESP32, garantindo compatibilidade entre o circuito implementado e a lógica do firmware.

Como melhoria futura, seria interessante adicionar um LED para fornecer feedback visual ao operador, indicando eventos como micro-paradas ou o reset do turno. Essa alteração tornaria a interação com o sistema mais intuitiva e facilitaria o monitoramento da linha de produção sem depender exclusivamente do monitor serial.

A estrutura atual do firmware permite incorporar novos dispositivos de saída sem alterações significativas na lógica principal do sistema.
