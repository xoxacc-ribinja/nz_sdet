MY_FILE = 'ci_jobs.txt'
LEGAL_STATUSES = ['PASSED', 'FAILED', 'SKIPPED']
# LEGAL_STRING_FORMAT = ['job_name', 'status', 'duration']


def get_all_lines():
    all_lines = []
    with (open(MY_FILE, 'r') as my_file):
        for line in my_file.readlines():
            all_lines.append(line.strip())
    return all_lines


def get_jobs():
    jobs_list = get_all_lines()
    valid_jobs = []
    invalid_jobs = []
    for job in jobs_list:
        if len(job.split(',')) != 3:
            invalid_jobs.append(job)
        elif job.split(',')[1] not in LEGAL_STATUSES:
            invalid_jobs.append(job)
        else:
            valid_jobs.append(job)
    return valid_jobs, invalid_jobs


def statuses_count(valid_jobs):
    statuses = {}
    for index, status in enumerate(LEGAL_STATUSES):
        statuses[status] = 0
    jobs_list = valid_jobs
    for job in jobs_list:
        status = job.split(',')[1]
        statuses[status] +=1
    return statuses


def format_statuses_count():
    status = statuses_count(get_jobs()[0])
    formated_count = ''
    for key, value in status.items():
        formated_count += f'{key}: {value}\n'
    return formated_count


def format_invalid_lines():
    invalid_lines = get_jobs()[1]
    formatted_invalid_lines = ''
    for line in invalid_lines:
        formatted_invalid_lines += f'- {line}\n'
    return formatted_invalid_lines


def output():
    valid_jobs, invalid_jobs = get_jobs()
    sorted_statuses = format_statuses_count()
    invalid_lines = format_invalid_lines()

    print(f'Valid jobs: {len(valid_jobs)}\n'
          f'Invalid lines: {len(invalid_jobs)}\n\n'
          f'By status:\n'
          f'{sorted_statuses}\n\n'
          f'Invalid input:\n'
          f'{invalid_lines}')


output()
