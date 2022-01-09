title: Deep dive: Python
date: 2022-01-07
description: An ant's eye view of Python 3
draft: true

I want to master the tools I use every day, so I decided to read through the
[official Python 3.11 documentation][pydoc] and write down everything that
stood out to me.

My focus here is on the core language and some of the high-level features of
the standard CPython interpreter. In a follow-up post, I'll focus more
specifically on CPython's lower-level details.

[pydoc]: https://docs.python.org/3.11/


## The bird's eye view

<dfn>Python</dfn> is a simple programming language that is fast and easy to
write, read, and change. Its clean and elegant high-level design makes it a joy
to work with. Most importantly, Python solves real problems in basically any
domain: general scripting, web serving, scientific computing, [game
development][pygame], and even [frontend work][anvil].

Python has a [comprehensive standard library][pylib] for working with files,
databases, internet resources, and rich media types like audio and image data.
And its deep ecosystem of third-party libraries fills in the gaps that the
standard library leaves behind.

The core grammar of Python is so expressive and appealing that it has caught in
other contexts, too: [Cython][cython] for C-like extensions, [Jython][jython]
for JVM usage, [RustPython][rustpython] for interop with Rust, and
[Starlark][starlark] as the default config language for Bazel.

[anvil]: https://anvil.works/
[cython]: https://cython.org/
[jython]: https://www.jython.org/
[pygame]: https://www.pygame.org
[pylib]: https://docs.python.org/3.11/library/index.html
[rustpython]: https://rustpython.github.io/
[starlark]: https://docs.bazel.build/versions/main/skylark/language.html

Python's main weaknesses are around performance, concurrency, and managing
large programs. These all have the same root cause, which is that Python is
interpreted and dynamically typed.

**Performance** -- For everyday programming, Python is fast enough, as the
major bottlenecks in a typical program are usually due to algorithm or data
structure issues rather than the fundamental limitations of the language.

Thankfully, Python is extensible and can easily wrap libraries written in
more performant languages like C, C++, [and even Rust][pyo3]. With this hybrid
approach, we get Python's ease of use without a performance penalty.

**Concurrency** -- I've rarely used it in my day-to-day work and can't say
anything interesting here.

**Large programs** -- Python's dynamic typing can make it hard to refactor at
scale or understand the data flow through a deep call stack. Guido van Rossum,
who created Python, puts it well:

> I learned a painful lesson: that for small programs dynamic typing is great,
> for large programs you have to have a more disciplined approach and it helps
> if the language actually gives you that discipline, rather than telling you,
> "Well, you can do whatever you want."
> 
> -- Guido van Rossum ([PuPPY, 2019][puppy])

To help address this problem, Python now supports type annotations, which have
some support in IDEs like PyCharm. These have been a lifesaver for me,
especially when combined with features like the new `dataclass` decorator.

[pyo3]: https://github.com/PyO3/PyO3
[puppy]: https://youtu.be/csL8DLXGNlU?t=5526


## Primitive data types

<dfn>Numeric types</dfn> include `int`, `float`, and `complex`:

    #!python
    i = 3
    f = 3.14
    c = 3 + 5i

longobject.c

[longobject]: https://github.com/python/cpython/blob/main/Objects/longobject.c

<dfn>Booleans</dfn> represent true or false values. Python's `bool` subclasses
`int`:

    #!python
    assert issubclass(bool, int)
    assert False == 0
    assert True == 1

<dfn>Strings</dfn> are immutable.

    # Strings
    s = 'This is a string.'

**Bytes**

- bytes, mutable: bytearray

    f.as_integer_ratio
    f.is_intereg

    s.removeprefix
    s.removesuffix
    


[stdtypes]: https://docs.python.org/3.11/library/stdtypes.html

## Compound data types

- lists
- sets
- dicts
    ordereddict useful in python3?
    https://www.python.org/dev/peps/pep-0584/
    https://docs.python.org/3.11/library/types.html#types.MappingProxyType
    iter(d).mapping
- counter
- tuples
    - namedtuples, dataclasses
- queues (collections.deque)
- array
- bisect
- heapq
- decimal

## Comprehensions

- list, set, dict

## Control flow

if, for, while, iter
break, continue, for-else, pass
match

[pep-636]: https://www.python.org/dev/peps/pep-0636/


## Functions

- def, lambda

- any, all, sum, zip
- sorted, reversed
- enumerate, range
- getattr, hasattr
- staticmethod, classmethod, property
- bool, int, dict

[builtin-fs]: https://docs.python.org/3.11/library/functions.html




## Decorators

- without arguments
- with arguments


## Type annotations

[pep-3107]: https://www.python.org/dev/peps/pep-3107/
[pep-484]: https://www.python.org/dev/peps/pep-0484/


## Modules

__name__
code run once per module import
module search path: sys.path
    - cur directory
    - PYTHONPATH
    - defaults

dir()


## Packages

__all__
__path__


## String formatting

- f-strings

## File I/O

- pickle, json, xml, csv


## Exceptions

- exception chaining
- user-defined
- try-finally
- with
- ExceptionGroup


## Namespaces

https://docs.python.org/3.11/tutorial/classes.html

## Classes



## Python object model

- pass by tag?


## CPython and .pyc files?


## Fundamentals of the standard library

os
sys
glob
re
datetime
requests
timeit
profiling
pprint
textwrap
threading
    I/O or CPU bound?
logging
random


## Environments

venv, pip


## Extending Python


## The global interpreter lock


## Package management in 2022


## Interpreters in 2022

ipython, bpython


## Scripts


