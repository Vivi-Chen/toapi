from collections import OrderedDict

from htmlparsing import Selector


class ItemType(type):
    def __new__(cls, what, bases=None, attrdict=None):
        __fields__ = OrderedDict()

        for name, selector in attrdict.items():
            if isinstance(selector, Selector):
                __fields__[name] = selector

        for name in __fields__.keys():
            del attrdict[name]

        instance = type.__new__(cls, what, bases, attrdict)
        instance._list = None
        instance._site = None
        instance._selector = None
        instance.__fields__ = __fields__
        return instance

    def __repr__(self):
        return 'Item<{}>'.format(self.__name__)


class Item(metaclass=ItemType):
    """"""
