import machine
import time

LDR_PIN = 35
BUTTON_PIN = 27

adc = machine.ADC(machine.Pin(LDR_PIN))
adc.atten(machine.ADC.ATTN_11DB)
adc.width(machine.ADC.WIDTH_12BIT)

button = machine.Pin(
    BUTTON_PIN,
    machine.Pin.IN,
    machine.Pin.PULL_UP
)

THRESH_FREE = 1200
THRESH_BLOCKED = 1800

MICROPARADA_MS = 5000
DEBOUNCE_MS = 50
LOOP_DELAY_MS = 20

total = 0

blocked = False
blocked_since = None
microparada_reportada = False

btn_last_reading = button.value()
btn_stable_state = btn_last_reading
btn_last_change = time.ticks_ms()

print("Contador de Producao Inicializado")

while True:
    agora = time.ticks_ms()

    valor = adc.read()

    livre = valor < THRESH_FREE
    bloqueado = valor > THRESH_BLOCKED

    if bloqueado and not blocked:
        blocked = True
        blocked_since = agora
        microparada_reportada = False

    if livre and blocked:
        total += 1
        print(f"Peca detectada! Total: {total}")

        blocked = False
        blocked_since = None
        microparada_reportada = False

    if blocked and not microparada_reportada:
        if time.ticks_diff(agora, blocked_since) >= MICROPARADA_MS:
            print("Alerta: Micro-parada detectada!")
            microparada_reportada = True

    leitura = button.value()

    if leitura != btn_last_reading:
        btn_last_change = agora
        btn_last_reading = leitura

    if time.ticks_diff(agora, btn_last_change) >= DEBOUNCE_MS:
        if leitura != btn_stable_state:
            btn_stable_state = leitura

            if btn_stable_state == 1:
                total = 0
                blocked = False
                blocked_since = None
                microparada_reportada = False

                print(
                    "Turno resetado com sucesso. "
                    "Contadores zerados."
                )

    time.sleep_ms(LOOP_DELAY_MS)