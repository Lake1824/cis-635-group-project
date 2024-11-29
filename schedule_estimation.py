class ScheduleEstimation:
    # The purpose of this class is to calculate TDEV
    # The formula is TDEV = C * (PM)^(D + 0.2 * (E - B)) * SCED%/100
    # C = 3.67, D = 0.28, B = 0.91, and the default for SCED% is 1
    # SCED% is the cost driver value

    # Constant Values
    C = 3.67
    D = 0.28
    B = 0.91

    def __init__(self, effort_estimation, diseconomy_of_scale, sced_multiplier = 1):
        self.effort_estimation = effort_estimation
        self.diseconomy_of_scale = diseconomy_of_scale
        self.sced_multiplier = sced_multiplier

    def calculate(self):
        effort_estimation_power = self.D + 0.2 * (self.diseconomy_of_scale - self.B)

        return self.C * pow(self.effort_estimation, effort_estimation_power) * self.sced_multiplier
