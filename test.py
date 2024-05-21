
from datetime import datetime
import time

a = datetime.now()

time.sleep(2)

b = datetime.now()

print((b - a).total_seconds())