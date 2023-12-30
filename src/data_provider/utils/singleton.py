def singleton(cls):  # type: ignore
    instances = {}

    def getinstance(*args, **kwargs):  # type: ignore
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return getinstance
