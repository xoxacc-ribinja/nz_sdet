import os
# vm_name,os,status,memory


keys = ['vm_name','os','status','memory']
STATUSES = ['running', 'stopped']

files_list = os.listdir('/Users/mac/Desktop/Project_NZ/nz_sdet/week01')
def check_file_input():
    file_name = input('Enter file name:\n')
    if file_name not in files_list:
        print('No such file!')
        exit()
    else:
        return file_name


def get_vm_info(filename:str):
    vms_info = []
    with open(filename, 'r') as vm_list:
        for line in vm_list.readlines():
            elements = line.strip().split(',')
            vm = {}
            for index, key in enumerate(keys):
                    vm[key] = elements[index]
            vms_info.append(vm)
    return vms_info


def status_info(vm_info):
    total_vms = len(vm_info)
    running = stopped = unknown_status = 0
    running_vm_names = []
    for vm in vm_info:
        if vm['status'].lower() == STATUSES[0]:
            running += 1
            running_vm_names.append(vm['vm_name'])
        elif vm['status'] == STATUSES[1]:
            stopped += 1
        else:
            unknown_status += 1

    return total_vms, running_vm_names, running, stopped, unknown_status


def memory_info(vm_info):
    total_memory = 0
    running_vms_memory = 0
    for vm in vm_info:
        if vm['status'] == STATUSES[0]:
            total_memory += int(vm['memory'])
            running_vms_memory += int(vm['memory'])
        else: total_memory += int(vm['memory'])

    return total_memory, running_vms_memory

def os_info(vm_info):
    oses = {}
    for vm in vm_info:
        if vm['os'] not in oses:
            oses[vm['os']] = 1
        else:
            oses[vm['os']] += 1
    return oses


def show_results():
    vm_info = get_vm_info(check_file_input())
    total_vms, running_vm_names, running, stopped, unknown_status = status_info(vm_info)
    total_memory, running_vms_memory = memory_info(vm_info)
    oses = os_info(vm_info)

    running_vms_list = ''
    for rvm in running_vm_names:
        running_vms_list += f'- {rvm}\n'

    vms_by_os = ''
    for key, value in oses.items():
        vms_by_os += f'- {key}: {value}\n'

    print(f'Total VMs: {total_vms}\n'
          f'Running: {running}\n'
          f'Stopped: {stopped}\n\n'
          f'Memory:\n'
          f'Total: {total_memory}\n'
          f'Running VMs: {running_vms_memory}\n\n'
          f'VMs by OS:\n'
          f'{vms_by_os}\n'
          f'Running VMs:\n'
          f'{running_vms_list}')

show_results()

