# 1)

def abbrev_name(name):
    words = name.split()
    first = words[0][0].upper()
    second  = words[1][0].upper()
    return first + "." + second

# 2)

def past(h, m, s):
    return(s + m * 60 + h * 3600)*1000

# 3)

def make_upper_case(s):
    return s.upper()

# 4)

def areYouPlayingBanjo(name):
    return '{} {}'.format(name, 'plays banjo' if name.startswith('R') or name.startswith('r') else 'does not play banjo')

# 5)

def paperwork(n, m):
    return n * m if n > 0 and m > 0 else 0