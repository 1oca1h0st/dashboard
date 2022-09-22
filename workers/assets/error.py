class ModuleError(Exception):
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __str__(self):
        return repr(self.value)

    def __repr__(self):
        return f"{self.name} exception {self.value}"


class ModuleTimeoutError(ModuleError):
    pass
