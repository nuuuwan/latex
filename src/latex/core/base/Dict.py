class Dict:
    def __init__(self, **kwargs):
        self.dict = kwargs

    def __str__(self):
        return ','.join(
            [f'{key}={value}' for key, value in self.dict.items()]
        )
