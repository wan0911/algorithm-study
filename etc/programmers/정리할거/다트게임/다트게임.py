import re

result = re.match('([0-9]{1,2}[SDT][*#]?)([0-9]{1,2}[SDT][*#]?)([0-9]{1,2}[SDT][*#]?)', '1S2D*3T').groups()

a = re.match('([0-9]{1,2})([SDT])([*#]?)', result[0]).groups()

int(a[0]), a[1], a[2] if a[2] is not None else None