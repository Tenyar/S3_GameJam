class Parameters:
    def __init__(self, argv : list[str]) -> None:
        self.parameters = {
            "playerSpeed": 0.45,

            "tasksDifficulty": 2,
            "tasksSpeed": 0.001,
            "tasksProgressPerSuccess": 20,
            "tasksTimeAfterError": 1000,

            "gamesDifficulty": 2,
            "litSpeed": 0.1,
            "litSpeedDifference": 3,
            "litProgress": 0.2,
            "litZoneLength": 10,
            "socialZoneLength": 10,
            "socialSpeed": 0.03,
            "socialProgress": 10,
            "socialTimeAfterError": 1000
        }
        for text in argv[1:]:
            key, value = text.split('=')
            if key in self.parameters:
                self.parameters[key] = value

        if self.parameters["tasksDifficulty"] > 5:
            self.parameters["tasksDifficulty"] = 5
        elif self.parameters["tasksDifficulty"] < 0:
            self.parameters["tasksDifficulty"] = 0
        
        self.parameters["tasksSpeed"] *= self.parameters["tasksDifficulty"]/2
        self.parameters["tasksProgressPerSuccess"] *= self.parameters["tasksDifficulty"]/2
        self.parameters["tasksTimeAfterError"] *= self.parameters["tasksDifficulty"]/2

        if self.parameters["gamesDifficulty"] > 5:
            self.parameters["gamesDifficulty"] = 5
        elif self.parameters["gamesDifficulty"] < 0:
            self.parameters["gamesDifficulty"] = 0
        
        self.parameters["litSpeed"] *= self.parameters["tasksDifficulty"]/2
        self.parameters["litSpeedDifference"] *= self.parameters["tasksDifficulty"]/2
        self.parameters["litProgress"] *= self.parameters["tasksDifficulty"]/2
        self.parameters["litZoneLength"] *= self.parameters["tasksDifficulty"]/2
        self.parameters["socialZoneLength"] *= self.parameters["tasksDifficulty"]/2
        self.parameters["socialSpeed"] *= self.parameters["tasksDifficulty"]/2
        self.parameters["socialProgress"] *= self.parameters["tasksDifficulty"]/2
        self.parameters["socialTimeAfterError"] *= self.parameters["tasksDifficulty"]/2


