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


class EffortMultiplier:
    # Effort multiplier dictionaries (class constants)
    EFFORT_MULTIPLIERS = {
        # Product Factors
        "RELY": {'very low': 0.82, 'low': 0.92, 'nominal': 1.00, 'high': 1.10, 'very high': 1.26, 'extra high': 0.00},
        "DATA": {'very low': 0.00, 'low': 0.90, 'nominal': 1.00, 'high': 1.14, 'very high': 1.28, 'extra high': 0.00},
        "CPLX": {'very low': 0.73, 'low': 0.87, 'nominal': 1.00, 'high': 1.17, 'very high': 1.34, 'extra high': 1.74},
        "RUSE": {'very low': 0.00, 'low': 0.95, 'nominal': 1.00, 'high': 1.07, 'very high': 1.15, 'extra high': 1.24},
        "DOCU": {'very low': 0.81, 'low': 0.91, 'nominal': 1.00, 'high': 1.11, 'very high': 1.23, 'extra high': 0.00},
        # Platform Factors
        "TIME": {'very low': 0.00, 'low': 0.00, 'nominal': 1.00, 'high': 1.11, 'very high': 1.29, 'extra high': 1.63},
        "STOR": {'very low': 0.00, 'low': 0.00, 'nominal': 1.00, 'high': 1.05, 'very high': 1.17, 'extra high': 1.46},
        "PVOL": {'very low': 0.00, 'low': 0.87, 'nominal': 1.00, 'high': 1.15, 'very high': 1.30, 'extra high': 0.00},
        # Personnel Factors
        "ACAP": {'very low': 1.42, 'low': 1.19, 'nominal': 1.00, 'high': 0.85, 'very high': 0.71, 'extra high': 0.00},
        "PCAP": {'very low': 1.34, 'low': 1.15, 'nominal': 1.00, 'high': 0.88, 'very high': 0.76, 'extra high': 0.00},
        # Project Factors
        "TOOL": {'very low': 1.17, 'low': 1.09, 'nominal': 1.00, 'high': 0.90, 'very high': 0.78, 'extra high': 0.00},
        "SITE": {'very low': 1.22, 'low': 1.09, 'nominal': 1.00, 'high': 0.93, 'very high': 0.86, 'extra high': 0.80},
        "SCED": {'very low': 1.43, 'low': 1.14, 'nominal': 1.00, 'high': 1.00, 'very high': 1.00, 'extra high': 0.00},
    }

    def __init__(self):
        # Initialize ratings to nominal
        self.ratings = {key: 'nominal' for key in self.EFFORT_MULTIPLIERS.keys()}

    def update_effort_multipliers(self, effort_multipliers):
        # Update ratings based on input effort multipliers
        for factor, rating in effort_multipliers.items():
            factor = factor.upper()  # Ensure case-insensitivity
            if factor in self.ratings:
                self.ratings[factor] = rating.lower()

    def calculate_effort_multiplier(self):
        # Calculate and return the overall effort multiplier (EM)
        EM = 1.0
        for factor, rating in self.ratings.items():
            EM *= self.EFFORT_MULTIPLIERS[factor].get(rating, 1)  # Default to 1 if rating is invalid
        return EM


class DiseconomyOfScale:
    # Scale factor dictionaries (class constants)
    SCALE_FACTORS = {
        "PREC": {'very low': 6.20, 'low': 4.96, 'nominal': 3.72, 'high': 2.48, 'very high': 1.24, 'extra high': 0.00},
        "FLEX": {'very low': 5.07, 'low': 4.05, 'nominal': 3.04, 'high': 2.03, 'very high': 1.01, 'extra high': 0.00},
        "RESL": {'very low': 7.07, 'low': 5.65, 'nominal': 4.24, 'high': 2.83, 'very high': 1.41, 'extra high': 0.00},
        "TEAM": {'very low': 5.48, 'low': 4.38, 'nominal': 3.29, 'high': 2.19, 'very high': 1.10, 'extra high': 0.00},
        "PMAT": {'very low': 7.80, 'low': 6.24, 'nominal': 4.68, 'high': 3.12, 'very high': 1.56, 'extra high': 0.00},
    }
    
    def __init__(self):
        # Initialize ratings to nominal
        self.ratings = {key: 'nominal' for key in self.SCALE_FACTORS.keys()}
    
    def update_scale_factors(self, scale_factors):
        # Update ratings based on input scale factors
        for factor, rating in scale_factors.items():
            factor = factor.upper()  # Ensure case-insensitivity
            if factor in self.ratings:
                self.ratings[factor] = rating.lower()
    
    def calculate_diseconomy_of_scale(self):
        # Calculate and return the diseconomy of scale (E).
        B = 0.91
        E = B
        for factor, rating in self.ratings.items():
            E += 0.01 * self.SCALE_FACTORS[factor].get(rating, 0.00)  # Default to 0 if rating is invalid
        return E


# Example Usage
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
