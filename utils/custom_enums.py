import enum
from enum import Enum


class BaseEnum(Enum):
    pass

@enum.unique
class Size(int, BaseEnum):
    SMALL = 34
    MEDIUM = 35
    LARGE = 36
    EXTRA_LARGE = 37

@enum.unique
class Color(str, BaseEnum):
    BLUE = 'Blue'
    PINK = 'Pink'
    BLACK = 'Black'
    PURPLE = 'Purple'
    ORANGE = 'Orange'

@enum.unique
class SupportedBrowsers(str, BaseEnum):
    CHROME = 'chrome'
    FIREFOX = 'firefox'

@enum.unique
class PageLoadStrategy(str, BaseEnum):
    NONE = 'none'
    EAGER = 'eager'
    NORMAL = 'normal'

@enum.unique
class ProductType(str, BaseEnum):
    DESKTOP = 'desktop'
    BOOK = 'book'
    ACCESSORY = 'accessory'
    SHOE = 'shoe'
    SOFTWARE = 'software'
    NOTEBOOK = 'notebook'
    
@enum.unique
class SortBy(str, BaseEnum):
    AZ = 'Name: A to Z'
    ZA = 'Name: Z to A'
    LOWHIGH  = 'Price: Low to High'
    HIGHLOW = 'Price: High to Low'
    CREATEDON = 'Created on'