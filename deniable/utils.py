"""Utils module to manipulate strings and bytes"""

from time import asctime, localtime, time
from logging import debug

def slice_n(string, size):
    """Given a 'string', returns a slice array of int such that each element has size 'size'."""
    start = time()

    i = 0
    aux = ""
    result = list()
    for char in string:
        aux += char
        i += 1
        if i == size:
            result.append(int(aux))
            i = 0
            aux = ""

    if i > 0:
        result.append(int(aux))

    debug("%s: utils: _slice: %s [s]", asctime(localtime(time())), time() - start)
    return result

def get_bytes(string):
    """Returns a integer list that represents
    the bytes sliced in 9 of a given string"""
    start = time()

    str_bytes = list(str.encode(string))

    i = 0
    aux = ""
    result = list()
    for byte in str_bytes:
        aux += "%03d" % (byte,)
        i += 1
        if i == 3:
            result.append(int(aux))
            i = 0
            aux = ""

    if i > 0:
        result.append(int(aux))

    debug("%s: utils: _get_bytes: %s [s]", asctime(localtime(time())), time() - start)
    return result

def get_string(bytes_string):
    """Resturns a string representation of a given bytes array in string format"""
    start = time()

    i = 0
    aux = ""
    bytes_list = list()
    for char in bytes_string:
        aux += char
        i += 1
        if i == 3:
            bytes_list.append(int(aux))
            i = 0
            aux = ""
    string = "".join(map(chr, bytes_list))

    debug("%s: utils: _get_string: %s [s]", asctime(localtime(time())), time() - start)
    return string

def trim(num):
    """Trim the given number (with zeros in left) in sizes 3, 6 or 9"""
    start = time()

    string = str(num)
    res = 0
    if len(string) <= 3:
        res = "%03d" % (num,)
    elif len(string) <= 6:
        res = "%06d" % (num,)
    else:
        res = "%09d" % (num,)

    debug("%s: utils: trim: %s [s]", asctime(localtime(time())), time() - start)
    return res
