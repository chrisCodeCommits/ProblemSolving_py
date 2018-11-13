##########################################################################################

TEST1 = '''
Sun 10:00-20:00
Fri 05:00-10:00
Fri 16:30-23:50
Sat 10:00-24:00
Sun 01:00-04:00
Sat 02:00-06:00
Tue 03:30-18:15
Tue 19:00-20:00
Wed 04:25-15:14
Wed 15:14-22:40
Thu 00:00-23:59
Mon 05:00-13:00
Mon 15:00-21:00
'''.strip()

TEST2 = '''
Mon 01:00-23:00
Tue 01:00-23:00
Wed 01:00-23:00
Thu 01:00-23:00
Fri 01:00-23:00
Sat 01:00-23:00
Sun 01:00-21:00
'''.strip()

TEST3 = '''
Mon 00:00-23:59
Tue 00:00-23:59
Wed 00:00-23:59
Thu 00:00-23:59
Fri 00:00-23:59
Sat 00:00-23:59
Sun 00:00-23:59
'''.strip()

#############################################################################################




DAY_TO_INDEX = dict((day, i) for (i, day) in enumerate('Mon Tue Wed Thu Fri Sat Sun'.split()))
ONE_DAY_IN_MINUTES = 24*60


# Self explainatory
def timestamp_to_mins(hour_min_timestamp):
    h, m = hour_min_timestamp.split(':')
    h, m = int(h), int(m)
    return h*60 + m

  
def solution(meetings):
    # start off with two fake meetings at the start/end of the week so we
    # calculate sleep time from start of week to end of week, e.g. if there are
    # no meetings, then we'll return 7 full days of sleep
    schedule = [(0, 0, 0), (6, ONE_DAY_IN_MINUTES, ONE_DAY_IN_MINUTES)]
    meetings = meetings.split('\n') if meetings else []

    # transform meeting strings into list of (day, start, end) data where start
    # and end are # of minutes from 00:00
    for m in meetings:
        day, duration = m.split()
        day = DAY_TO_INDEX[day]
        start, end = duration.split('-')
        start, end = timestamp_to_mins(start), timestamp_to_mins(end)
        print(m, "->", (day, start, end))
        schedule.append((day, start, end))

    # sort the schedule and calculate the # of minutes gap between each pair of
    # meetings to find the max
    schedule.sort()
    gaps = []
    for (m1, m2) in zip(schedule, schedule[1:]):
        start = m1[0]*ONE_DAY_IN_MINUTES + m1[2] # the end of the first meeting
        end = m2[0]*ONE_DAY_IN_MINUTES + m2[1] # the start of the next meeting
        gaps.append(end - start)
    return max(gaps)

  
  
  
#### TEST CASES ####################################################################################################  

if __name__ == "__main__":
    print(solution(TEST1))
    print(solution(TEST2))
    print(solution(TEST3))
    print(solution(""))
    
#####################################################################################################################
