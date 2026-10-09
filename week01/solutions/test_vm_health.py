INPUT_FILE: str = 'vm_health.txt'
VALID_STATUSES: list[str] = ['running', 'stopped', 'error']
VM_PARAMETERS: list[str] = ['vm_name', 'status', 'cpu']


def get_vm_parameters_list() -> list[str]:
    vm_parameters_list: list[str] = []
    with open(INPUT_FILE, 'r') as vm_list:
        for line in vm_list.readlines():
            vm_parameters_list.append(line.strip())

    return vm_parameters_list


def get_legal_vms_preliminary_list(vm_parameters_list: list[str]) -> list[str]:
    valid_vm_preliminary_list: list[str] = []
    for vm in vm_parameters_list:
        if len(vm.split(',')) == 3 and vm.split(',')[1] in VALID_STATUSES:
            valid_vm_preliminary_list.append(vm)

    return valid_vm_preliminary_list


def get_invalid_input(vm_parameters_list: list[str], valid_list: list[str]) -> list[str]:
    invalid_input: list[str] = []
    for vm in vm_parameters_list:
        if vm not in valid_list:
            invalid_input.append(vm)

    return invalid_input


def get_vms_list(vm_preliminary_list: list[str]) -> list[dict[str, str]]:
    vms: list[dict[str, str]] = []
    for vm in vm_preliminary_list:
        vm_dict: dict[str, str] = {}
        vm = vm.split(',')
        for index, value in enumerate(VM_PARAMETERS):
            vm_dict[value] = vm[index]
        vms.append(vm_dict)

    return vms


def count_cpus(vms: list[dict[str, str]]) -> tuple[int, list[str]]:
    max_cpu: int = 0
    max_cpu_list: list[str] = []

    for vm in vms:
        vm_cpu: int = int(vm[VM_PARAMETERS[2]])
        if vm_cpu > max_cpu:
            max_cpu = vm_cpu
            max_cpu_list = [vm[VM_PARAMETERS[0]]]
        elif vm_cpu == max_cpu:
            max_cpu_list.append(vm[VM_PARAMETERS[0]])

    return max_cpu, max_cpu_list


def count_statuses(vms: list[dict[str, str]]) -> dict[str, int]:
    statuses: dict[str, int] = {}
    for status in VALID_STATUSES:
        statuses[status] = 0

    for vm in vms:
        statuses[vm['status']] += 1

    return statuses


def format_dict_to_list(dic: dict[str, int]) -> list[str]:
    output_list: list[str] = []
    for key, value in dic.items():
        output_list.append(f'{key}: {value}')

    return output_list


def format_list_to_string(lst: list[str]) -> str:
    output_str: str = ''
    for item in lst:
        output_str += f'- {item}\n'

    return output_str


def main_output() -> None:
    vm_parameters_list = get_vm_parameters_list()
    valid_vm_preliminary_list = get_legal_vms_preliminary_list(vm_parameters_list)
    invalid_input = get_invalid_input(vm_parameters_list, valid_vm_preliminary_list)
    vms = get_vms_list(valid_vm_preliminary_list)
    max_cpu, max_cpu_list = count_cpus(vms)
    statuses = count_statuses(vms)

    print(f'Valid VMs: {len(valid_vm_preliminary_list)}')
    print(f'Invalid lines: {len(invalid_input)}\n')
    print(f'By status:\n'
          f'{format_list_to_string(format_dict_to_list(statuses))}')
    print(f'Highest CPU: {max_cpu}\n'
          f'{format_list_to_string(max_cpu_list)}')
    print(f'Invalid input:\n'
          f'{format_list_to_string(invalid_input)}')


main_output()
