

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



