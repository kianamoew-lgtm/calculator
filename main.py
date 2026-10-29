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

def show_help():
    print("""

h    show calculation history
b    convert the last number to binary
o    convert the last number to octal
x    convert the last number to hexadecimal
m+   add the last number to memory
m-   subtract the last number from memory
m    show memory (and set it as the last number)
mc   clear memory
q    quit

""")


show_help()

while True:
    line = input(">>> ").strip().lower()

    if line == "q":
        break

    elif line == "h":
        if not history:
            print("History is empty")
        for i, item in enumerate(history, 1):
            print(f"{i}. {item}")

    elif line in ("b", "o", "x"):
        if last is None:
            print("No number yet")
            continue
        try:
            n = to_int(last)
        except ValueError as e:
            print("Error:", e)
            continue
        if line == "b":
            print(bin(n))
        elif line == "o":
            print(oct(n))
        else:
            print(hex(n))

    elif line == "m+":
        if last is None:
            print("No number yet")
        else:
            memory += last
            print("Memory:", memory)

    elif line == "m-":
        if last is None:
            print("No number yet")
        else:
            memory -= last
            print("Memory:", memory)

    elif line == "m":
        last = memory
        print("Memory:", memory)

    elif line == "mc":
        memory = 0
        print("Memory cleared")

    else:
        tokens = line.split()
        try:
            if len(tokens) == 3:
                a, op, b = tokens
                a = inputt(a)
            elif len(tokens) == 2 and last is not None:
                op, b = tokens
                a = last
            else:
                print("Invalid format (example: 3 + 4)")
                continue

            if op not in OPS:
                print("Invalid operator")
                continue

            b = inputt(b)
            result = OPS[op](a, b)

            last = result
            history.append(f"{a} {op} {b} = {result}")
            print("=", result)

        except ZeroDivisionError:
            print("Error: division by zero")
        except ValueError:
            print("Error: invalid number")
        except OverflowError:
            print("Error: number too large")