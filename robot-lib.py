
def keyword_add(n1, n2):
    print("Math - addition of {} + {}".format(n1, n2))
    print("Result {}".format(int(n1) + int(n2)))
    return n1 + n2


def keyword_sub(n1, n2):
    print("Math - subtraction of {} - {}".format(n1, n2))
    print("Result {}".format(int(n1) - int(n2)))
    return int(n1) - int(n2)


def keyword_mult(n1, n2):
    print("Math - multiplication of {} * {}".format(n1, n2))
    print("Result {}".format(int(n1) * int(n2)))
    return int(n1) * int(n2)


def keyword_div(n1, n2):
    if int(n2) == 0:
        raise Exception("Division by 0! (Not Possible)")
    print("Math - division of {} / {}".format(n1, n2))
    print("Result {}".format(int(n1) / int(n2)))
    return int(n1) / int(n2)


def run_test_case_1():
    print("Running Test Case 1")
    print("OK")


def turn_off_system():
    print("Turning Off the system")
    print("OK")
