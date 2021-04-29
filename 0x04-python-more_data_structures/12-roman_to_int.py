#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None:
        return (0)
    numerals = {
        1: ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"],
        10: ["X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"],
        100: ["C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"],
        1000: ["M", "MM", "MMM"]
    }
    numeral_vals = {}
    for r in numerals.items():
        for ix, val in enumerate(r[1]):
            numeral_vals[val] = (ix + 1) * r[0]

    def f(item):
        roman_string[:len(item[0])] == item[0]
    val = 0
    while (roman_string):
        match = sorted(
            dict(filter(
                 lambda i: roman_string[:len(i[0])] == i[0],
                 numeral_vals.items())
                 ).items(), reverse=True, key=lambda i: i[1])[0]
        val += match[1]
        roman_string = roman_string[len(match[0]):]
    return (val)
