import string
import random
digits = string.digits

pin_code = ''.join(random.choice(digits) for _ in range(6))

print(pin_code)
