history = []
memory = 0 
last = None

OPS = {
    "+":  lambda a, b: a + b,
    "-":  lambda a, b: a - b,
    "*":  lambda a, b: a * b,
    "/":  lambda a, b: a / b,
    "**": lambda a, b: a ** b,
}


def inputt(input):
  
    if input == "m":
        return memory
    try:
        return int(input)
    except ValueError:
        return float(input)


def to_int(n):
    if n != int(n):
        raise ValueError("the number should be an integer")
    return int(n)

