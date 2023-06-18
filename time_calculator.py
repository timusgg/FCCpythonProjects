
def add_time(start, duration, day=False):
    input = start.split(' ')
    time = input[0].split(':')
    add = duration.split(':')

    startHour = int(time[0])
    startMinutes = int(time[1])
    startPeriod = str(input[1])
    daysLater = 0

    hoursAdd = int(add[0])
    minutesAdd = int(add[1])

    resultHour = startHour + hoursAdd
    resultMinutes = startMinutes + minutesAdd
    resultPeriod = ''

    daysOfWeek = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    resultDay = ''


    if resultMinutes > 59:
        resultHour += 1
        resultMinutes -= 60

    if hoursAdd > 0:
        daysLater += (hoursAdd // 24)


    if resultHour >= 12 :   
        if ((resultHour // 12) % 2) != 0 :
            if startPeriod == 'AM':
                resultPeriod += 'PM'
            else:
                resultPeriod += 'AM'
                daysLater += 1
        
        
        resultHour = resultHour % 12
        
        if resultHour == 0:
            resultHour = 12

    if resultPeriod == '':
        resultPeriod += startPeriod    



    if day != False:
        currentDay = str(day).lower().capitalize()
        dayNumber = daysOfWeek.index(currentDay)

        index = (dayNumber + daysLater) % 7
        resultDay += daysOfWeek[index]
        if daysLater == 1 :
            return str(resultHour) + ':' + str(resultMinutes).zfill(2) + ' ' + resultPeriod + ', ' + resultDay + ' (next day)'
    
        if daysLater > 1 :
            return str(resultHour) + ':' + str(resultMinutes).zfill(2) + ' ' + resultPeriod + ', ' + resultDay + ' (' + str(daysLater) +' days later)'
    

        return str(resultHour) + ':' + str(resultMinutes).zfill(2) + ' ' + resultPeriod + ', ' + resultDay
 
        

    if daysLater == 1:
        return str(resultHour) + ':' + str(resultMinutes).zfill(2) + ' ' + resultPeriod +' (next day)'
        
    if daysLater > 1:
        return str(resultHour) + ':' + str(resultMinutes).zfill(2) + ' ' + resultPeriod +' (' + str(daysLater) +' days later)'

    return str(resultHour) + ':' + str(resultMinutes).zfill(2) + ' ' + resultPeriod




    
print(add_time("3:00 PM", "3:10"))

print(add_time("11:43 AM", "00:20"))

print(add_time("10:10 PM", "3:30"))

print(add_time("11:43 PM", "24:20"))


print(add_time("6:30 PM", "205:12"))

print(add_time("11:43 PM", "24:20", "Monday"))

print(add_time("11:30 AM", "2:32", "Monday"))  

print('test_high_duration_with_day  ' + add_time("8:16 PM", "466:02", "tuesday"))

print('test_twenty_four  ' + add_time("2:59 AM", "24:00"))

    

print('test_twenty_four_with_day  ' + add_time("2:59 AM", "24:00", "saturDay"))
