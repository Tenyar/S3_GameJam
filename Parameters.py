class Parameters:
    def __init__(self, argv : list[str]) -> None:
        self.parameters = {
            "playerSpeed": 0.45,
            "socialBarSpeed": 0.0015,
            "sleepBarSpeed": 0.0012,

            "startCounteurValue": 5,
            "counterDecreaseStep": 0.5,
            "counterClampMin": 5,
            "maxTask": 5,

            "tasksDifficulty": 2,
            "gamesDifficulty": 2,

            #"tasksSpeed": 0.1,
            "tasksProgressPerSuccessMin": 3,
            "tasksProgressPerSuccessMax": 5,
            "tasksTimeAfterError": 1,       # Cooldown en cas d'erreur

            "litSpeed": 0.03,
            "litSpeedDifference": 4,
            "litSleepBarProgressPerSuccess": 1,
            "litZoneLength": 15,

            "socialZoneLength": 10,
            "socialSpeed": 0.05,
            "socialBarProgressPerSuccess": 7,
            "socialBarMinTime": 0.3,
            "socialBarMaxTime": 1,
            "socialTimeAfterError": 1
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
        
        '''self.parameters["tasksSpeed"] *= self.parameters["tasksDifficulty"]/2
        self.parameters["tasksProgressPerSuccessMin"] *= self.parameters["tasksDifficulty"]/2
        self.parameters["tasksProgressPerSuccessMax"] *= self.parameters["tasksDifficulty"]/2
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
        self.parameters["socialTimeAfterError"] *= self.parameters["gamesDifficulty"]/2'''