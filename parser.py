def parse_input(filename):
    with open(filename, 'r') as f:
        R, C, L, H = map(lambda x: int(x), f.readline().split())
        matrix = [[char for char in line.strip()] for line in f]
    return R, C, L, H, matrix


def algorithm(*args):
    return 0


def write_result(result):
    length = len(result)
    with open('result_file', 'w') as result_file:
        result_file.write(str(length) + '\n')
        for line in result:
            result_file.write(' '.join(str(elem) for elem in line) + '\n')


R, C, L, H, matrix = parse_input('filename')
result = algorithm(R, C, L, H, matrix)
write_result(result)

print('')
