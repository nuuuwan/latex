import re


def escape_url(s: str) -> str:
    URL_PATTERN = r'http[s]?://[\w.?/=&]+'
    wrapped_s = re.sub(URL_PATTERN, r'\\url{\g<0>}', s)
    return wrapped_s


def escape(s: str) -> str:
    for c in ['(', ')', '%', '&']:
        s = s.replace(c, '\\' + c)

    s = escape_url(s)

    return s
