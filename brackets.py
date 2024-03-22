class Stack:
    def __init__(self):
        self.__items = []

    def is_empty(self):
        return bool(self.__items)

    def push(self, item):
        self.__items.append(item)

    def pop(self):
        return self.__items.pop()

    def peek(self):
        return self.__items[-1]

    def size(self):
        return len(self.__items)


def is_correct_brackets(line):
    some_list = []
    brackets = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    for el in line:
        if el not in brackets:
            some_list.append(el)
        elif some_list and some_list[-1] == brackets[el]:
            some_list.pop()
        else:
            print("Несбалансированно")
            return

    if some_list:
        print("Несбалансированно")
    else:
        print("Сбалансированно")

is_correct_brackets("(((([{}]))))")
is_correct_brackets("[([])((([[[]]])))]{()}")
is_correct_brackets("{{[()]}}")
is_correct_brackets("}{}")
is_correct_brackets("{{[(])]}}")
is_correct_brackets("[[{())}]")