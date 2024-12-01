class EquivalentKloc:
    su_dict = {
        'very low': 50,
        'low': 40,
        'nominal': 30,
        'high': 20,
        'very high': 10
    }

    unfm_dict = {
        'completely familiar': 0.0,
        'mostly familiar': 0.2,
        'somewhat familiar': 0.4,
        'considerably familiar': 0.6,
        'mostly unfamiliar': 0.8,
        'completely unfamiliar': 1.0
    }

    aa_dict = {
        'none': 0,
        'basic module search and documentation': 2,
        'some T&E, documentation': 4,
        'considerable T&E, documentation': 6,
        'extensive T&E, documentation': 8
    }

    def __init__(self, size, dm, cm, im, su_increment, unfm_increment, aa_increment, at):
        self.size = size
        self.dm = dm
        self.cm = cm
        self.im = im
        self.at = at
        self.su_value = self.su_dict[su_increment]
        self.unfm_value = self.unfm_dict[unfm_increment]
        self.aa_value = self.aa_dict[aa_increment]
        self.result = self.calculate()

    def calculate(self):
        aaf = (.4 * self.dm)+(.3 * self.cm)+(.3 * self.im)
        automatically_translated_code = (1 - (self.at / 100))

        if aaf > 50:
            aam = (self.aa_value + aaf + (self.su_value * self.unfm_value)) / 100
        else:
            aam = (self.aa_value + (aaf * (1 + (.02 * self.su_value * self.unfm_value)))) / 100

        return self.size * automatically_translated_code * aam
