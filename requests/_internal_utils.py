# -*- coding: utf-8 -*-

"""
requests._internal_utils
~~~~~~~~~~~~~~

Provides utility functions that are consumed internally by Requests
which depend on extremely few external helpers (such as compat)
"""

# 内部工具

from .compat import is_py2, builtin_str, str

# 转原生字符串
def to_native_string(string, encoding='ascii'):
    """Given a string object, regardless of type, returns a representation of
    that string in the native string type, encoding and decoding where
    necessary. This assumes ASCII unless told otherwise.
    """
    if isinstance(string, builtin_str):
        out = string
    else:
        if is_py2:
            # 转至unicode
            out = string.encode(encoding)
        else:
            # 解码utf8
            out = string.decode(encoding)

    return out

# 校验是否只是ascii 码
def unicode_is_ascii(u_string):
    """Determine if unicode string only contains ASCII characters.

    :param str u_string: unicode string to check. Must be unicode
        and not Python 2 `str`.
    :rtype: bool
    """
    assert isinstance(u_string, str)

    try:
        u_string.encode('ascii')
        return True
    except UnicodeEncodeError:
        return False
