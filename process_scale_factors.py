def process_scale_factors(scale_factors):
    int: {PREC, FLEX, RESL, TEAM, PMAT, B, E}
    B = 0.91 #Constant derived from historical project data
    for key, value in scale_factors.items():
        if key == "PREC":
            if value.lower() == "nominal":
                PREC = 3.72
            elif value.lower() == "high":
                PREC = 2.48
            elif value.lower() == "low":
                PREC = 4.96
            elif value.lower() == "very high":
                PREC = 1.24
            elif value.lower() == "very low":
                PREC = 6.20
            else: #value == "Extra High"
                PREC = 0.00
        elif key == "FLEX":
            if value.lower() == "nominal":
                FLEX = 3.04
            elif value.lower() == "high":
                FLEX = 2.03
            elif value.lower() == "low":
                FLEX = 4.05
            elif value.lower() == "very high":
                FLEX = 1.01
            elif value.lower() == "very low":
                FLEX = 5.07
            else: #value == "Extra High"
                FLEX = 0.00
        elif key == "RESL":
            if value.lower() == "nominal":
                RESL = 4.24
            elif value.lower() == "high":
                RESL = 2.83
            elif value.lower() == "low":
                RESL = 5.65
            elif value.lower() == "very high":
                RESL = 1.41
            elif value.lower() == "very low":
                RESL = 7.07
            else: #value == "Extra High"
                RESL = 0.00
        elif key == "TEAM":
            if value.lower() == "nominal":
                TEAM = 3.29
            elif value.lower() == "high":
                TEAM = 2.19
            elif value.lower() == "low":
                TEAM = 4.38
            elif value.lower() == "very high":
                TEAM = 1.10
            elif value.lower() == "very low":
                TEAM = 5.48
            else: #value == "Extra High"
                TEAM = 0.00
        elif key == "PMAT":
            if value.lower() == "nominal":
                PMAT = 4.68
            elif value.lower() == "high":
                PMAT = 3.12
            elif value.lower() == "low":
                PMAT = 6.24
            elif value.lower() == "very high":
                PMAT = 1.56
            elif value.lower() == "very low":
                PMAT = 7.80
            else: #value == "Extra High"
                PMAT = 0.00
    E = B + 0.01 * (PREC + FLEX + RESL + TEAM + PMAT)
    return(E)
