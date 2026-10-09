myfile = 'builds.txt'

PARAMETERS = ['component', 'status', 'duration']
STATUS = ['success', 'failed']


def get_builds_info():
    builds = []
    with open(myfile, 'r') as file:
        for line in file.readlines():
            info = line.strip().split(',')
            build_info = {}
            for index, elem in enumerate(PARAMETERS):
                if elem == PARAMETERS[2]:
                    build_info[elem] = int(info[index])
                else:
                    build_info[elem] = info[index]
            builds.append(build_info)

    return builds


def get_builds_count(info):
    total_count = len(info)
    success = fail = other = 0
    for i in info:
        if i['status'] == STATUS[0]:
            success += 1
        elif i['status'] == STATUS[1]:
            fail += 1
        else:
            other += 1

    return total_count, success, fail


def get_duration(info):
    total_duration = max_duration = 0
    slowest_builds = []

    for b in info:
        dura = b['duration']
        if dura > max_duration:
            max_duration = dura
            slowest_builds = [b['component']]
        elif dura == max_duration:
            slowest_builds.append(b['component'])

        total_duration += dura

    average = round(total_duration/len(info), 2)

    return total_duration, max_duration, average, slowest_builds


def get_failed_builds(info):
    failed_list = []
    for f in info:
        if f['status'] == STATUS[1]:
            failed_list.append(f['component'])

    return failed_list


def format_builds_lists(info):
    failed_list = '- '+'\n- '.join(get_failed_builds(info))
    slowest_list = '- '+'\n- '.join(get_duration(info)[3])

    return failed_list, slowest_list


def report():
    info = get_builds_info()
    total_count, success, fail = get_builds_count(info)
    total_duration, max_duration, average, slowest_builds = get_duration(info)
    failed_list, slowest_list = format_builds_lists(info)

    print(f'Total builds: {total_count}\n'
          f'Successful: {success}\n'
          f'Failed: {fail}\n\n'
          f'Total duration: {total_duration} sec\n'
          f'Average duration: {average} sec\n\n'
          f'Slowest build(s): \n'
          f'{slowest_list}\n'
          f'Duration: {max_duration} sec\n\n'
          f'Failed builds:\n'
          f'{failed_list}')


report()