"""
module => python file
package => directory having __init__.py module. Without __init__.py, a package is just a normal directory
"""


def foo():
    print("Foo")


def bar():
    print("Bar")


class Test:
    pass


if __name__ == "__main__":
    print("This is libs module")
