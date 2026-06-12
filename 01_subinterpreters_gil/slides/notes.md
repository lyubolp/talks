# Subinterpreters and GIL-less python

## What is a process ?

A process is a unit of execution with it's own (separate) memory, file descriptors, execution state, etc.
In Python, the process will have it's own interpreter (and it's own GIL).
Creating new processes is a "heavy" operation - we need to copy everything the process has.

In Python, starting a new process is done via either `fork` (Linux) or `fork + exec` (MacOS & Windows).

This is wrapped around in the `Process` object in `multiprocessing`.

## What is a thread ?

A thread is the smalles unit of execution. It shares memory and file descriptors with other threads.

In Python, the threads run in the same interpreter, with a shared GIL.
Creating new threads is a lightweight operation.

The `Thread` object from `multithreading` is the interface we use to work with threads in Python.

## The `concurrent.futures` module

Showcase of the `concurrent.futures` module in general - talk about `ThreadPoolExecutor` and `ProcessPoolExecutor`.

Focus on the general interface:

- `submit`
- `map`

https://docs.python.org/3/library/concurrent.futures.html#module-concurrent.futures

## Examples 00, 01 and 02

## What is a subinterpreter ?

While named "subinterpreters", the subinterpreter is not a new interpreter.
An “interpreter” is effectively the execution context of the Python runtime. It contains all of the state the runtime needs to execute a program. 

The thing that actually interprets Python - the bytecode evaluation loop is one, regardles of the code running in the "main" or a "sub" interpreter. There's no duplication of the evaluation logic.

When you create a subinterpreter, what CPython allocates is a new `PyInterpreterState` — a C struct that holds all the state an interpreter needs to operate independently. Roughly speaking, each subinterpreter contains:

Its own GIL (since PEP 684 / Python 3.12)
Its own sys.modules (module registry)
Its own import state and builtins
Its own garbage collector state
Its own set of PyThreadState objects (at least one per OS thread running in that interpreter)


### Sharing objects

Subinterpreters can't efffectively share objects between themselves

### exec
Function is not shareable, when there is a dependency outside of the new interpreter => `.call` requires "pure" functions

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

### Communication between interpreters

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



## Real-life tests

### Django

### gunicorn

### numpy

### pytorch


## Summary