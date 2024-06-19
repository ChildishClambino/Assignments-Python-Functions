def fitness_tracker():                     #task1
    activities = []
    duration = []
    while True:
        activities_done = input("What activities have you done today? If you're done type 'done': ")
        if activities_done == "done":
            break
        duration_done = input("for how long? If you are done type 'done':  ")
        if duration_done == "done":
            break
        
        activities.append(activities_done)
        duration.append(int(duration_done))

    return activities,duration

def calories_burned(duration):                     #task 2
    total_calories_burned = sum(duration) * 3.5
    return(total_calories_burned)

def main():                                           #task 3
    activities, duration = fitness_tracker()
    total_calories =calories_burned(duration)

    print("Activities:", activities)
    print("Duration:", duration)
    print("Total Calories Burned", total_calories)

if __name__== "__main__":
    main()
   
