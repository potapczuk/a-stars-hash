with open('input_file', 'r') as f:
    R, C, L, H = map(lambda x: int(x), f.readline().split())
    matrix = [[char for char in line.strip()] for line in f]


def algorithm():
    pass


def write_result(result):
    length = len(result)
    with open('result_file', 'w') as result_file:
        result_file.write(str(length) + '\n')
        for line in result:
            result_file.write(' '.join(str(elem) for elem in line) + '\n')


result = algorithm()
write_result(result)

print('')
