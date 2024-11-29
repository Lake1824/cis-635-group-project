class TeamSize:
    # The purpose of this class is to calculate Team Size
    # The formula is Team Size = PM / TDEV

    def __init__(self, effort_estimation, schedule_estimation):
        self.effort_estimation = effort_estimation
        self.schedule_estimation = schedule_estimation

    def calculate(self):
        return self.effort_estimation / self.schedule_estimation