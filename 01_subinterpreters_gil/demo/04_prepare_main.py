from concurrent import interpreters

interpreter = interpreters.create()

# interpreter.prepare_main({"a": 42})  # Comment this line for error

interpreter.exec("print(a)")

interpreter.close()