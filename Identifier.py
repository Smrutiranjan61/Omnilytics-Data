import re


def is_integer(number):
    pattern = re.compile("[0-9]")
    if pattern.match(number):
        return True
    return False


def is_real(number):
    pattern = re.compile("([0-9]\.?[0-9]?)")
    if pattern.match(number):
        return True
    return False
    # return isinstance(number, float)


def is_alphabetical(text):
    pattern = re.compile("[a-z]")
    if pattern.match(text):
        return True
    return False


def is_alphanumeric(text):
    pattern = re.compile("[ ]{0,10}[a-z0-9][ ]{0,10}")
    if pattern.match(text):
        return True
    return False


if __name__ == '__main__':
    print(is_integer(5.4))
    print(is_real(10.0))
    print(is_alphabetical('abcdfsd'))
    print(is_alphanumeric('  ytrytr124sdf534rewr    '))
