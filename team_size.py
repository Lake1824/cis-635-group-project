class TeamSize:
    def __init__(self, effort_estimation, schedule_estimation):
        self.effort_estimation = effort_estimation
        self.schedule_estimation = schedule_estimation

    def calculate(self):
        return self.effort_estimation / self.schedule_estimation