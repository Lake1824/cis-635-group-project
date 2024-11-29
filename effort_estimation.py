class EffortEstimation:
    # The purpose of this class is to calculate PM
    # The formula is PM = A * (Size)^E * EMi

    # Default value
    A = 2.94

    def __init__(self, size, diseconomy_of_scale, effort_modifier):
        self.size = size
        self.diseconomy_of_scale = diseconomy_of_scale
        self.effort_modifier = effort_modifier

    def calculate(self):
        return self.A * pow(self.size, self.diseconomy_of_scale) * self.effort_modifier
