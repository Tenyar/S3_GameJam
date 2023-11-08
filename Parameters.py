class Parameters:
    def __init__(self, argv : list[str]) -> None:
        self.parameters = {
            "taskSpeed": 0.001,
            "playerSpeed": 0.45
        }
        for text in argv[1:]:
            key, value = text.split('=')
            if key in self.parameters:
                self.parameters[key] = value



