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
        #Update ratings based on input scale factors
        for factor, rating in scale_factors.items():
            factor = factor.upper()  # Ensure case-insensitivity
            if factor in self.ratings:
                self.ratings[factor] = rating.lower()
    
    def calculate_diseconomy_of_scale(self):
        #Calculate and return the diseconomy of scale (E).
        B = 0.91
        E = B
        for factor, rating in self.ratings.items():
            E += 0.01 * self.SCALE_FACTORS[factor].get(rating, 0.00)  # Default to 0 if rating is invalid
        return E
