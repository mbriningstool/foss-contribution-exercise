def calc(raw):
    """
    """

    elements = raw.split()
    (num1, *operator_pieces, num2) = elements
    operator = " ".join(operator_pieces)

    operator_func = FUNCTIONS[operator]
    num1 = int(num1)
    num2 = int(num2)
    return operator_func(num1, num2)


def plus(num1, num2):

    return num1 + num2


def divided_by(num1, num2):

    return num1 / num2


FUNCTIONS = {"plus": plus, "divided by": divided_by}
