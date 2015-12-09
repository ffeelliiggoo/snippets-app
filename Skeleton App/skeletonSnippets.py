import logging

# Set the log output file, and the log level
logging.basicConfig(filename="snippets.log", level=logging.DEBUG)

#Creating a program Skeleton
#Let's figure out what operations you'll need, and create stubs for each main 
#function. A stub is a function that is defined but does nothing useful. 
#The most important feature is storing a snippet. 
#In your snippets.py file add the following stub:

#stub 1:
def put(first, snippet):
    """
    Store a snippet with an associated name.

    Returns the name and the snippet
    """
    logging.error("FIXME: Unimplemented - put({!r}, {!r})".format(first, snippet))
    return first, snippet
#stub 2:
def get(second):
    """Retrieve the snippet with a given name.

    If there is no such snippet...

    Returns the snippet.
    """
    logging.error("FIXME: Unimplemented - get({!r})".format(second))
    return ""