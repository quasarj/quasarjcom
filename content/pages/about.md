Title: About Me

There really isn't much to know about me. At least, not much important.

Testing a code block:

    :::python
    import csv
    
    print "some stuff"

    class Dict(dict):
        """A dict where keys can be accessed as attributes"""
        def __init__(self, *args, **kwargs):
            super(Dict, self).__init__(*args, **kwargs) # or super().__init__ in py3
            self.__dict__ = self



    dict = Dict

    d = dict(a=4,b=3)

    d.c = 8
    d.d = 5
    d.e = dict()
    d.e.a = 9



    print d




## Setup
And how to set it up:

    :::bash
    ./import.sh
    rm bob.txt
    cp a b/

