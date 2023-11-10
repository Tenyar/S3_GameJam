class Parameters:
    def __init__(self, argv : list[str]) -> None:
        self.parameters = {
            "playerSpeed": 0.45,
            "socialBarSpeed": 0.0015,
            "sleepBarSpeed": 0.0012,

            "globalDifficulty": 2,
            "tasksDifficulty": 2,
            "gamesDifficulty": 2,

            "tasksProgressPerSuccessMin": 3,
            "tasksProgressPerSuccessMax": 5,
            "tasksTimeAfterError": 0.5,       # Cooldown en cas d'erreur
            "startCounterValue": 18,
            "counterDecreaseStep": 0.25,
            "counterClampMin": 10,
            "maxTask": 4,

            "sleepSpeed": 0.035,       # vitesse de descente de la bar
            "sleepSpeedDifference": 3,    # vitesse à laquelle sa monte en fonction de lit speed
            "sleepBarProgressPerSuccess": 10,
            "sleepZoneLength": 15,

            "socialSpeed": 0.09,
            "socialBarProgressPerSuccess": 5,
            "socialBarMinTime": 0.3,
            "socialBarMaxTime": 1,
            "socialTimeAfterError": 0.5,
            "socialZoneLength": 10,

            "isDebug" : 0
        }

        for text in argv[1:]:
            try:
                key, strvalue = text.split('=')
                value = float(strvalue)
                if key in self.parameters and value != None:
                    self.parameters[key] = value
            except:
                pass

        if self.parameters["globalDifficulty"] > 4:
            self.parameters["globalDifficulty"] = 4
        elif self.parameters["globalDifficulty"] < 1:
            self.parameters["globalDifficulty"] = 1
        
        self.parameters["tasksDifficulty"] = self.parameters["globalDifficulty"]
        self.parameters["gamesDifficulty"] = self.parameters["globalDifficulty"]

        #self.parameters["playerSpeed"] /= self.parameters["globalDifficulty"]/2
        self.parameters["socialBarSpeed"] *= self.parameters["globalDifficulty"]/2
        self.parameters["sleepBarSpeed"] *= self.parameters["globalDifficulty"]/2



        if self.parameters["tasksDifficulty"] > 4:
            self.parameters["tasksDifficulty"] = 4
        elif self.parameters["tasksDifficulty"] < 1:
            self.parameters["tasksDifficulty"] = 1
        
        self.parameters["tasksProgressPerSuccessMin"] /= self.parameters["tasksDifficulty"]/2
        self.parameters["tasksProgressPerSuccessMax"] /= self.parameters["tasksDifficulty"]/2
        self.parameters["tasksTimeAfterError"] *= self.parameters["tasksDifficulty"]/2
        self.parameters["startCounterValue"] /= self.parameters["tasksDifficulty"]/2
        self.parameters["counterDecreaseStep"] *= self.parameters["tasksDifficulty"]/2
        self.parameters["counterClampMin"] /= self.parameters["tasksDifficulty"]/2
        self.parameters["maxTask"] *= self.parameters["tasksDifficulty"]/2



        if self.parameters["gamesDifficulty"] > 4:
            self.parameters["gamesDifficulty"] = 4
        elif self.parameters["gamesDifficulty"] < 1:
            self.parameters["gamesDifficulty"] = 1
        
        self.parameters["sleepSpeed"] *= self.parameters["gamesDifficulty"]/2
        self.parameters["sleepSpeedDifference"] *= self.parameters["gamesDifficulty"]/2
        self.parameters["sleepBarProgressPerSuccess"] *= self.parameters["gamesDifficulty"]/2
        self.parameters["sleepZoneLength"] *= self.parameters["gamesDifficulty"]/2

        self.parameters["socialZoneLength"] *= self.parameters["gamesDifficulty"]/2
        self.parameters["socialSpeed"] *= self.parameters["gamesDifficulty"]/2
        self.parameters["socialBarProgressPerSuccess"] *= self.parameters["gamesDifficulty"]/2
        self.parameters["socialBarMinTime"] *= self.parameters["gamesDifficulty"]/2
        self.parameters["socialBarMaxTime"] *= self.parameters["gamesDifficulty"]/2
        self.parameters["socialTimeAfterError"] *= self.parameters["gamesDifficulty"]/2
