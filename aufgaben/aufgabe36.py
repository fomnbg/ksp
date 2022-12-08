from datetime import datetime, timedelta

now = datetime.now()

midnight = datetime(now.year, now.month, now.day, 0, 0, 0)

diff = timedelta()
diff = now - midnight

print(now.strftime('%A, %d, %B %Y %H:%m:%S'))
print(midnight.strftime('%A, %d, %B %Y %H:%m:%S'))
print(diff.total_seconds())