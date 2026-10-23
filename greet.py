"""Small greeting module used for the Copilot bootcamp lab demo."""


def greet(name):
    """Return a friendly greeting.

    >>> greet('World')
    'Hello, World!'
    >>> greet('')
    'Hello, stranger!'
    """
    if not name:
        name = "stranger"
    return f"Hello, {name}!"
