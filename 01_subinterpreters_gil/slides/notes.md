# Subinterpreters and GIL-less python

## What is a thread ?

## What is a process ?

## Examples 00, 01 and 02

## What is a subinterpreter ?

https://docs.python.org/3/library/concurrent.interpreters.html#

https://peps.python.org/pep-0734/

https://peps.python.org/pep-0684/


https://docs.python.org/3/c-api/subinterpreters.html#sub-interpreter-support, optional


Function is not shareable, when there is a dependency outside of the new interpreter => `.call` requires "pure" functions

### exec

### call

### prepare_main

```python
from concurrent import interpreters

interpreter = interpreters.create()

interpreter.prepare_main({"a": 42})  # Comment this line for error

interpreter.exec("print(a)")

interpreter.close()
```

### call_in_thread

```python
from concurrent import interpreters


def sleepy_print():
    print("Hello from the subinterpreter!")
    import time

    time.sleep(2)


interpreter = interpreters.create()

t = interpreter.call_in_thread(sleepy_print)

print("Hello from the main interpreter!")

t.join()

interpreter.close()
```

## Example 03

## What is the GIL ?

https://wiki.python.org/moin/GlobalInterpreterLock

https://softwareengineering.stackexchange.com/questions/186889/why-was-python-written-with-the-gil

https://docs.python.org/3/c-api/threads.html#threads, optional

## GIL-less (freethreaded) Python

https://docs.python.org/3/howto/free-threading-python.html (Thread safety, Immortalization, Iterators, Single-threaded performance)

https://peps.python.org/pep-0703/, optional


### Packages that don't work with freethreaded Python

Pure-Python wheels can already be used in free-threaded builds, but wheels with extensions need to be updated for free-threaded Python. 


- psycopg2-binary
- psycopg-binary
- tokenizers
- psycopg2
- opencv-python
- spacy


Source: https://hugovk.dev/free-threaded-wheels/


## Examples 00-03 with freethreaded Python

## Summary