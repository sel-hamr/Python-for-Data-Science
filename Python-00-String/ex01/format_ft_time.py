import time
import datetime

# Current date and time -> floating-point number
current_time = time.time()
# Specific date
current_date = datetime.date.today()

print(f"Seconds since January 1, 1970: \
{current_time:.4f} or {current_time:.2e} in scientific notation")
print(f"{current_date.strftime('%b %d %Y')}")