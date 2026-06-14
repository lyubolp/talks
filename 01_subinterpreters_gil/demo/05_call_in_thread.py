from concurrent import interpreters


def sleepy_print():
    print("Hello from the subinterpreter!")
    import time

    time.sleep(2)


interpreter = interpreters.create()

t = interpreter.call_in_thread(sleepy_print)

import time
time.sleep(2)

print("Hello from the main interpreter!")

t.join()

interpreter.close()