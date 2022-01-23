def conversions(cc, tc):
    if tc > cc:
        return "Test"
    elif tc < cc:
        return "Control"
    elif tc == cc:
        return "Same"
