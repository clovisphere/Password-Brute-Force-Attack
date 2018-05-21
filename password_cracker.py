# A simple password cracker script

from itertools import product
import string
import time


def cracker(password):
    """How long it will take to crack a given a password

    Keyword arguments:
        password: the password to crack
    Returns: a list
    """
    number_of_attempt = 0
    characters = string.printable
    # to time the script
    start = time.time()

    for i in range(1, 10):
        temp = product(characters, repeat=i)
        for guess in temp:
            number_of_attempt += 1
            # The magic happens below
            guess = ''.join(guess)
            if guess == password:
                end = time.time()
                return {
                    'number_of_attempts': number_of_attempt,
                    'time_taken': (end - start)
                }


if __name__ == '__main__':
    try:
        print('\n{:<20} {:>25} {:>30}'.format('Password', 'Attempts', 'Time'))
        with open('sample_password', 'r') as f:
            for entry in f:
                t = cracker(entry.strip('\n'))
                print('{0:<20}\t{1:>22,}\t{2:>31.4f} sec'.format(
                    entry.strip('\n'),
                    t['number_of_attempts'],
                    t['time_taken']
                ))
    except KeyboardInterrupt as e:
        pass
