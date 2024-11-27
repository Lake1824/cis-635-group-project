class EffortEstimation:
    def __init__(self, ufc, cost_drivers=None, scale_factors=None):
        self.ufc = ufc  # Unadjusted Function Points (size of the project)
        self.cost_drivers = cost_drivers if cost_drivers else {}
        self.scale_factors = scale_factors if scale_factors else {}
        self.PM = None  # Effort Estimation in Person-Months
        self.E = None   # Effort Exponent

    def calculate_effort(self):
        A = 2.94  # Default coefficient from COCOMO II
        B = 0.91  # Exponent base from COCOMO II

        # Calculate the sum of scale factors
        SF_sum = sum(self.scale_factors.values())
        # Calculate the Effort Exponent E
        self.E = B + 0.01 * SF_sum

        # Calculate the product of cost drivers
        PROD_COST_DRIVERS = 1.0
        for value in self.cost_drivers.values():
            PROD_COST_DRIVERS *= value

        # Calculate the Effort Estimation (PM)
        self.PM = A * (self.ufc) ** self.E * PROD_COST_DRIVERS
        return self.PM

class ScheduleEstimation:
    def __init__(self, pm, E, sced_percent=100):
        self.pm = pm                # Effort in Person-Months
        self.E = E                  # Effort Exponent
        self.sced_percent = sced_percent  # Schedule Compression/Expansion percentage
        self.TDEV = None            # Schedule Estimation in Months

    def calculate_schedule(self):
        C = 3.67  # Coefficient from COCOMO II
        D = 0.28  # Exponent base from COCOMO II
        B = 0.91  # Exponent base used in Effort Estimation

        # Calculate the Schedule Exponent F
        F = D + 0.2 * (self.E - B)

        # Calculate the Schedule Estimation (TDEV)
        self.TDEV = C * (self.pm) ** F

        # Adjust TDEV based on SCED percentage
        self.TDEV *= (self.sced_percent / 100.0)
        return self.TDEV

    def calculate_team_size(self):
        if self.TDEV is None:
            raise ValueError("TDEV has not been calculated yet.")
        if self.TDEV == 0:
            raise ValueError("TDEV cannot be zero.")
        # Calculate the Team Size
        team_size = self.pm / self.TDEV
        return team_size


if __name__ == "__main__":
    ufc = 150  # Size of the project in function points
    cost_drivers = {'RELY': 1.1, 'DATA': 1.0, 'CPLX': 1.2}  # Non-nominal cost drivers
    scale_factors = {'PREC': 2.0, 'FLEX': 3.0}              # Non-nominal scale factors

    # Instantiate EffortEstimation class and calculate PM
    effort_estimator = EffortEstimation(ufc, cost_drivers, scale_factors)
    PM = effort_estimator.calculate_effort()
    E = effort_estimator.E
    print(f"Effort Estimation (PM): {PM}")

    # Instantiate ScheduleEstimation class and calculate TDEV
    schedule_estimator = ScheduleEstimation(PM, E)
    TDEV = schedule_estimator.calculate_schedule()
    print(f"Schedule Estimation (TDEV): {TDEV}")

    # Calculate Team Size using the method in ScheduleEstimation
    team_size = schedule_estimator.calculate_team_size()
    print(f"Team Size: {team_size}")
