# gets current time from user
time_now = int(input('Current Time: \n'))
alarm_delay = int(input('Hours until alarm sounds: \n'))

# determines time that the alarm will go off
temp_val = alarm_delay % 24
alarm_time = time_now + temp_val

# determines time of alarm in 12-hour time
twelve_time = alarm_time - 12
if (alarm_time == 0 or alarm_time < 12):
    am_pm = 'am'
else:
    am_pm = 'pm'

# print time that alarm goes off
print()
print('Alarm will sound at:', str(alarm_time) + ':00 hours (' + str(twelve_time) + str(am_pm) + ')')