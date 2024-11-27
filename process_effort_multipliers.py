class EffortMultiplier:
    # Effort multiplier dictionaries (class constants)
    EFFORT_MULTIPLIERS = {
        # Product Factors
        # Required Software Reliability
        "RELY": {'very low': 0.82, 'low': 0.92, 'nominal': 1.00, 'high': 1.10, 'very high': 1.26, 'extra high': 0.00},
        # Data Base Size
        "DATA": {'very low': 0.00, 'low': 0.90, 'nominal': 1.00, 'high': 1.14, 'very high': 1.28, 'extra high': 0.00},
        # Product Complexity
        "CPLX": {'very low': 0.73, 'low': 0.87, 'nominal': 1.00, 'high': 1.17, 'very high': 1.34, 'extra high': 1.74},
        # Required Reusability
        "RUSE": {'very low': 0.00, 'low': 0.95, 'nominal': 1.00, 'high': 1.07, 'very high': 1.15, 'extra high': 1.24},
        # Documentation Match to Life-Cycle Needs
        "DOCU": {'very low': 0.81, 'low': 0.91, 'nominal': 1.00, 'high': 1.11, 'very high': 1.23, 'extra high': 0.00},

        # Platform Factors
        # Execution Time Constraint
        "TIME": {'very low': 0.00, 'low': 0.00, 'nominal': 1.00, 'high': 1.11, 'very high': 1.29, 'extra high': 1.63},
        # Main Storage Constraint
        "STOR": {'very low': 0.00, 'low': 0.00, 'nominal': 1.00, 'high': 1.05, 'very high': 1.17, 'extra high': 1.46},
        # Platform Volatility
        "PVOL": {'very low': 0.00, 'low': 0.87, 'nominal': 1.00, 'high': 1.15, 'very high': 1.30, 'extra high': 0.00},

        # Personnel Factors
        # Analyst Capability
        "ACAP": {'very low': 1.42, 'low': 1.19, 'nominal': 1.00, 'high': 0.85, 'very high': 0.71, 'extra high': 0.00},
        # Programmer Capability
        "PCAP": {'very low': 1.34, 'low': 1.15, 'nominal': 1.00, 'high': 0.88, 'very high': 0.76, 'extra high': 0.00},
        # Applications Experience
        "APEX": {'very low': 1.22, 'low': 1.10, 'nominal': 1.00, 'high': 0.88, 'very high': 0.81, 'extra high': 0.00},
        # Platform Experience
        "PLEX": {'very low': 1.19, 'low': 1.09, 'nominal': 1.00, 'high': 0.91, 'very high': 0.85, 'extra high': 0.00},
        # Language and Tool Experience
        "LTEX": {'very low': 1.20, 'low': 1.09, 'nominal': 1.00, 'high': 0.91, 'very high': 0.84, 'extra high': 0.00},
        # Personnel Continuity
        "PCON": {'very low': 1.29, 'low': 1.12, 'nominal': 1.00, 'high': 0.90, 'very high': 0.81, 'extra high': 0.00},

        # Project Factors
        # Usage of Software Tools
        "TOOL": {'very low': 1.17, 'low': 1.09, 'nominal': 1.00, 'high': 0.90, 'very high': 0.78, 'extra high': 0.00},
        # Multisite Development
        "SITE": {'very low': 1.22, 'low': 1.09, 'nominal': 1.00, 'high': 0.93, 'very high': 0.86, 'extra high': 0.80},
        # Required Development Schedule
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
