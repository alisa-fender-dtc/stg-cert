import os



def create_log_dir(directory):
    if not os.path.exists(directory):
        print("Creating directory for logs: {}".format(directory))
        os.makedirs(directory)


def create_data_files(log_dir, base_url):
    queue = log_dir + 'queue.txt'
    crawled = log_dir + 'crawled.txt'

    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile((crawled)):
        write_file(crawled, '')

def create_files_from_list(file_list):
    for file_name in file_list:
        if not os.path.isfile(file_name):
            write_file(file_name, '')


def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()

def append_to_file(path, data):
    with open(path, 'a') as f:
        f.write((data + '\n'))

def delete_file_contents(path):
    with open(path, 'w'):
        pass


def file_to_set(path):
    results = set()
    with open(path, 'rt') as f:
        for line in f:
            results.add(line.replace('\n', ''))
    return results

def set_to_file(data, path):
    delete_file_contents(path)
    for item in sorted(data):
        append_to_file(path, item)

# create_data_files('sling', 'https://sling.com')