class Config:
    DEBUG = True


class Development(Config):
    pass


class Testing(Config):
    pass


class Production(Config):
    DEBUG = False
