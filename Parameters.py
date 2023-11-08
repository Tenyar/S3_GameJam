class Parameters:
    def __init__(self, argv : list[str]) -> None:
        self.parameters = {
            "playerSpeed": 0.45,
            "socialBarSpeed": 0.005,
            "sleepBarSpeed": 0.005,
            "tasksDifficulty": 2,
            "gamesDifficulty": 2,

            "tasksSpeed": 1,
            "tasksProgressPerSuccess": 20,
            "tasksTimeAfterError": 1000,

            "litSpeed": 0.1,
            "litSpeedDifference": 3,
            "litSleepBarProgressPerSuccess": 0.2,
            "litZoneLength": 10,

            "socialZoneLength": 10,
            "socialSpeed": 0.03,
            "socialBarProgressPerSuccess": 10,
            "socialTimeAfterError": 1000
        }

        for text in argv[1:]:
            try:
                key, strvalue = text.split('=')
                value = float(strvalue)
            except:
                pass
            if key in self.parameters and value != None:
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
        
        self.parameters["litSpeed"] *= self.parameters["gamesDifficulty"]/2
        self.parameters["litSpeedDifference"] *= self.parameters["gamesDifficulty"]/2
        self.parameters["litSleepBarProgressPerSuccess"] *= self.parameters["gamesDifficulty"]/2
        self.parameters["litZoneLength"] *= self.parameters["gamesDifficulty"]/2
        self.parameters["socialZoneLength"] *= self.parameters["gamesDifficulty"]/2
        self.parameters["socialSpeed"] *= self.parameters["gamesDifficulty"]/2
        self.parameters["socialBarProgressPerSuccess"] *= self.parameters["gamesDifficulty"]/2
        self.parameters["socialTimeAfterError"] *= self.parameters["gamesDifficulty"]/2


