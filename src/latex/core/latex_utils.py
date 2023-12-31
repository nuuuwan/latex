import re


def escape_url(s: str) -> str:
    wrapped_s = re.sub(
        r'http[s]?://[\w.?/=&_\-%#,]+', r'\\footnote{\\url{\g<0>}}', s
    )
    return wrapped_s


def escape_quotes(s: str) -> str:
    wrapped_s = re.sub(r'"(.*?)"', r'\\say{\1}', s)
    return wrapped_s


def escape(s: str) -> str:
    s = escape_url(s)
    s = escape_quotes(s)

    for c in ['%', '&', '#']:
        s = s.replace(c, '\\' + c)

    s = s.encode('ascii', 'ignore').decode('ascii')
    return s
