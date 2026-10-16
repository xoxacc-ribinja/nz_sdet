VALID_COMMANDS = ['START', 'PAUSE', 'RESUME', 'FINISH']
# На всё ушло не более часа. Продумывание алгоритма заняло бОльшую часть.
# Пытался найти более простое и изящное решение, но забил, решив, что быстрее будет написать решение-крипич -
# простое, но надёжное и работоспособное.

def next_state(state: str, command: str) -> str | None:

    if command not in VALID_COMMANDS:
        return None
    elif state == 'IDLE' and command != 'START':
        return None
    elif state == 'ACTIVE' and command not in ('PAUSE', 'FINISH'): # Это решение я погуглил :(
        # Просто, чтобы сократить время на отладку при поимке багов.
        # На этапе написания кода понял, что здесь будут ошибки
        return None
    elif state == 'PAUSED' and command != 'RESUME':
        return None
    elif state == 'DONE' and command:
        return None
    elif command == 'START':
        return 'ACTIVE'
    elif command == 'PAUSE':
        return 'PAUSED'
    elif command == 'RESUME':
        return 'ACTIVE'
    else:
        return 'DONE'


def check_scenario(commands: list[str]) -> tuple[str, int | None]:
    current_state: str = 'IDLE'
    for index, command in enumerate(commands):
        previous_state = current_state
        current_state = next_state(current_state, command)
        if command not in VALID_COMMANDS:
            return previous_state, index
        elif not current_state: # изначально написал elif current_state == None, идешка подсветила, что это некрасиво.
            return previous_state, index

    return current_state, None

