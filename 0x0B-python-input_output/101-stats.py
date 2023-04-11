#!/usr/bin/python3

import sys
from collections import defaultdict

total_size = 0
status_code_count = defaultdict(int)
line_count = 0

try:
    for line in sys.stdin:
        line_count += 1
        _, _, _, status_code, size = line.split()
        total_size += int(size)
        status_code_count[status_code] += 1
        if line_count % 10 == 0:
            print(f'Total file size: {total_size}')
            for code in sorted(status_code_count.keys()):
                print(f'{code}: {status_code_count[code]}')
            print('\n')
except KeyboardInterrupt:
    print(f'Total file size: {total_size}')
    for code in sorted(status_code_count.keys()):
        print(f'{code}: {status_code_count[code]}')
    print('\n')
