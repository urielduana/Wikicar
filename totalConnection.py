from carConnection import *
from newsConnection import *
from postConnection import *

class totalConnectionDataBase(car, news, post):
    def __init__(self):
        car.__init__(self)
        news.__init__(self)
        post.__init__(self)