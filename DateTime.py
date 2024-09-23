# -*- coding: utf8 -*-
from datetime import datetime

# Взять текущее время и дату
now = datetime.now()

# Получить дату, время и день недели
dt = now.strftime('%Y-%m-%d %H:%M:%S')
dw = now.strftime('%A')

# Получить номер недели
nw = now.isocalendar()

print("Current date and time:", dt)
print("Day of the week:", dw)
print("Week number:", nw.week)
