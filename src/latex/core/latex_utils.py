import re


def escape_url(s: str) -> str:
    wrapped_s = re.sub(r'http[s]?://[\w.?/=&_-]+', r'\\url{\g<0>}', s)
    return wrapped_s


def escape_quotes(s: str) -> str:
    wrapped_s = re.sub(r'"[\w\s]+"', r'\\say{\g<0>}', s)
    return wrapped_s


def escape(s: str) -> str:
    for c in ['%', '&']:
        s = s.replace(c, '\\' + c)

    s = escape_url(s)
    s = s.encode('ascii', 'ignore').decode('ascii')
    return s
