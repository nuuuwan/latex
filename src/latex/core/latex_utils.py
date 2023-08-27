def escape(s: str):
    for c in [')', '%']:
        s = s.replace(c, '\\' + c)
    return s
