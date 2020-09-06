
<<<<<<< HEAD

def add_time(time1,time2,*days):
   MerdiumHours = 0
   quotes = '\''
   daysFixIntoLower = days
   daysOfTheWeek = {
      'monday' : '1',
      'tuesday' : '2',
      'wednesday' : '3',
      'thursday' : '4',
      'friday' : '5',
      'saturday' : '6',
      'sunday' : '7'
   }
   if ':' in time2:
      time2NumForColonPlace = time2.find(':')
      TIME2firstPartColonPlaceNum = time2NumForColonPlace
      TIME2secondPartColonPlaceNum = time2NumForColonPlace + 1
      time2FirstNum = time2[:TIME2firstPartColonPlaceNum]
      time2SecondNum = time2[TIME2secondPartColonPlaceNum:]
      
   if ":" in time1:
      time1NumForColonPlace = time1.find(':')
      TIME1firstPartColonPlaceNum = time1NumForColonPlace
      TIME1secondPartColonPlaceNum = time1NumForColonPlace + 1
      endBeforeMerdium = TIME1secondPartColonPlaceNum + 3
      time1FirstNum = time1[:TIME1firstPartColonPlaceNum]
      time1SecondNum = time1[TIME1secondPartColonPlaceNum:endBeforeMerdium]
      time1Merdium = time1[endBeforeMerdium:]
      timeAddedHours = int(time1FirstNum) + int(time2FirstNum)
      timeAddedMins = int(time1SecondNum) + int(time2SecondNum)
      if time1Merdium == 'PM':
         MerdiumHours += 1
      if len(days) >= 1:
         
         daysFix = str(days)
         daysFixIntoLower = daysFix.lower()
         res = [i for i in range(len(daysFixIntoLower)) if daysFixIntoLower.startswith(quotes, i)] 
         firstRes = res[0] + 1
         secondRes = res[1]
         theDayWord = daysFixIntoLower[firstRes:secondRes]
         monday = daysOfTheWeek['monday']
         tuesday = daysOfTheWeek['tuesday']
         wednesday = daysOfTheWeek['wednesday']
         thursday = daysOfTheWeek['thursday']
         friday = daysOfTheWeek['friday']
         saturday = daysOfTheWeek['saturday']
         sunday = daysOfTheWeek['sunday']
         print(theDayWord)


   while timeAddedHours >= 12:
      MerdiumHours += 1
      timeAddedHours -= 12
   print('')
   

    



add_time("3:00 PM", "3:10")
# Returns: 6:10 PM

add_time("11:30 AM", "2:32", "Monday")
# Returns: 2:02 PM, Monday

add_time("11:43 AM", "00:20")
# Returns: 12:03 PM

add_time("10:10 PM", "3:30")
# Returns: 1:40 AM (next day)

add_time("11:43 PM", "24:20", "tueSday")
# Returns: 12:03 AM, Thursday (2 days later)

add_time("6:30 PM", "205:12")
# Returns: 7:42 AM (9 days later)

=======
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
    for hoursInADay in full_time_answer_hour:
        print('PROCESSING HOURS IN DAYS...')






    print(full_time_answer_hour,colon,full_time_answer_mins)

add_time(input('STARTING TIME : '),input('HOW MUCH TIME YOU WANT TO ADD ON IN 00:00 FORMAT : '))
add_time(input('STARTING TIME : '),input('HOW MUCH TIME YOU WANT TO ADD ON IN 00:00 FORMAT : '))
add_time(input('STARTING TIME : '),input('HOW MUCH TIME YOU WANT TO ADD ON IN 00:00 FORMAT : '))
>>>>>>> a5e056bf57a82bcafe26f82ccc793dc31ffc1c30


