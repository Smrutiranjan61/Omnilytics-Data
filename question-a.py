import argparse
import random

from file_resize import get_file_size
from creator import generate_string


def main():
    str_types = ['alphabetical', 'int', 'real', 'alphanumeric']
    choice = random.choice(str_types)
    generated_str = generate_string(default_type=choice)
    with open('answer-a.txt', mode='w+') as f:
        f.write(generated_str.__str__())
    while True:
        file_size = get_file_size(filename='answer-a.txt')
        if abs(file_size - 10) <= 10e-4:
            break        
        choice = random.choice(str_types)
        generated_str = generate_string(default_type=choice)
        with open('answer-a.txt', mode='a+') as f:
            f.write(', ' + generated_str.__str__())


if __name__ == '__main__':
    main()
