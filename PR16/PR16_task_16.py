import re

ip = "192.168.1.1"
pattern = r"^((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.){3}(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)$"
result = bool(re.fullmatch(pattern, ip))
print(result)
