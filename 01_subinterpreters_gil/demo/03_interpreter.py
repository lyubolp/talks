from concurrent import interpreters

interpreter = interpreters.create()

interpreter.exec("print('Hello from a different interpreter')")

def answer(a, b) -> int:
    return a + b

result = interpreter.call(answer, 2, 3)

print(result)

interpreter.close()