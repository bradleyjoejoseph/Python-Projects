
colon = ':'
def add_time(time1,time2):
    minutesInAnHour = 60
    hoursInADay = 24
    daysInminutes = minutesInAnHour * hoursInADay
    time1_counted_str = len(str(time1))
    time2_counted_str = len(str(time2))
    if time1_counted_str == 8:
        print('PROCCESSING STR VALUES...')
        time1_hours = time1[0:2]
        time1_mintutes = time1[3:5]
        time1_Meridum_Value = time1[6:8]
        if time1_Meridum_Value == 'PM':
            print('PROCESSING MIDNIGHT REQUEST...')
            time1_hours_int = int(time1_hours)
            time1_fixed_hours_int = time1_hours_int + 12
            time1_hours_half_result_hour = time1_fixed_hours_int
            time1_mintutes_half_result_mins = int(time1_mintutes)
        elif time1_Meridum_Value == "AM":
            print('PROCESSING MIDDAY REQUEST...')
            time1_hours_int = int(time1_hours)
            time1_hours_half_result_hour = time1_hours_int
            time1_mintutes_half_result_mins = int(time1_mintutes)

        else:
            print('ERROR : YOU HAVE ENTERED THE WRONG INFORMATION')
            print('YOU MIGHT BE MISSING A SPACE BETWEEN THE NUMBERS AND AM/PM')
            print('YOU MIGHT BE ADDING WRONG CHARACTERS')
            print('YOU MIGHT HAVE PUT IN AN INVALID TIME')


    else:
        print('PROCCESSING STR VALUES...')
        print('ERROR : YOU HAVE ENTERED THE WRONG INFORMATION')
        print('YOU MIGHT BE MISSING A SPACE BETWEEN THE NUMBERS AND AM/PM')
        print('YOU MIGHT BE ADDING WRONG CHARACTERS')
        print('YOU MIGHT HAVE PUT IN AN INVALID TIME')
        exit()
    time2_str = str(time2)
    time2_int_1 = time2_str[0:2]
    time2_int_2 = time2_str[3:5]
    full_time_answer_hour = time1_hours_half_result_hour + int(time2_int_1)
    full_time_answer_mins = time1_mintutes_half_result_mins + int(time2_int_2)
    





    print(full_time_answer_hour,colon,full_time_answer_mins)

add_time(input('STARTING TIME : '),input('HOW MUCH TIME YOU WANT TO ADD ON IN 00:00 FORMAT : '))
add_time(input('STARTING TIME : '),input('HOW MUCH TIME YOU WANT TO ADD ON IN 00:00 FORMAT : '))
add_time(input('STARTING TIME : '),input('HOW MUCH TIME YOU WANT TO ADD ON IN 00:00 FORMAT : '))


