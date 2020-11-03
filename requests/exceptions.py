# -*- coding: utf-8 -*-

"""
requests.exceptions
~~~~~~~~~~~~~~~~~~~

This module contains the set of Requests' exceptions.
"""
from urllib3.exceptions import HTTPError as BaseHTTPError


# 通用异常
class RequestException(IOError):
    """There was an ambiguous exception that occurred while handling your
    request.
    """

    def __init__(self, *args, **kwargs):
        """Initialize RequestException with `request` and `response` objects."""

        # 取出响应
        response = kwargs.pop('response', None)
        self.response = response

        # 取出请求
        self.request = kwargs.pop('request', None)

        # 尝试从响应里面获取请求
        if (response is not None and not self.request and
                hasattr(response, 'request')):
            self.request = self.response.request

        # 调用父类初始化
        super(RequestException, self).__init__(*args, **kwargs)



# http 错误
class HTTPError(RequestException):
    """An HTTP error occurred."""


# 连接异常
class ConnectionError(RequestException):
    """A Connection error occurred."""


# 代理错误
class ProxyError(ConnectionError):
    """A proxy error occurred."""



# 加密通道错误
class SSLError(ConnectionError):
    """An SSL error occurred."""


# 超时错误
class Timeout(RequestException):
    """The request timed out.

    Catching this error will catch both
    :exc:`~requests.exceptions.ConnectTimeout` and
    :exc:`~requests.exceptions.ReadTimeout` errors.
    """


# 连接错误
class ConnectTimeout(ConnectionError, Timeout):
    """The request timed out while trying to connect to the remote server.

    Requests that produced this error are safe to retry.
    """


# 读取错误
class ReadTimeout(Timeout):
    """The server did not send any data in the allotted amount of time."""


# 没有URL
class URLRequired(RequestException):
    """A valid URL is required to make a request."""


# 重定向次数过多
class TooManyRedirects(RequestException):
    """Too many redirects."""


# 网址缺少协议
class MissingSchema(RequestException, ValueError):
    """The URL schema (e.g. http or https) is missing."""


# 非法协议
class InvalidSchema(RequestException, ValueError):
    """See defaults.py for valid schemas."""


# 非法URL
class InvalidURL(RequestException, ValueError):
    """The URL provided was somehow invalid."""


# 非法头部
class InvalidHeader(RequestException, ValueError):
    """The header value provided was somehow invalid."""


# 非法代理网址
class InvalidProxyURL(InvalidURL):
    """The proxy URL provided is invalid."""


# 编码错误
class ChunkedEncodingError(RequestException):
    """The server declared chunked encoding but sent an invalid chunk."""


# 内容解码错误
class ContentDecodingError(RequestException, BaseHTTPError):
    """Failed to decode response content."""


# 流已消费过
class StreamConsumedError(RequestException, TypeError):
    """The content for this response was already consumed."""


# 重试次数过多
class RetryError(RequestException):
    """Custom retries logic failed"""


class UnrewindableBodyError(RequestException):
    """Requests encountered an error when trying to rewind a body."""

# Warnings


# 请求告警
class RequestsWarning(Warning):
    """Base warning for Requests."""


# 文件模式告警
class FileModeWarning(RequestsWarning, DeprecationWarning):
    """A file was opened in text mode, but Requests determined its binary length."""


# 库依赖告警
class RequestsDependencyWarning(RequestsWarning):
    """An imported dependency doesn't match the expected version range."""
