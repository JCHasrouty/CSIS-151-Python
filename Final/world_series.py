def main():
    ## open the file
    ## fill the dictionary
    # count number of games won etc
    world_series = {}
    file = open('WorldSeriesWinners.txt', 'r')
    lineCount = 0
    value = 0
    for line in file:
        lineCount += 1
        key = line.rstrip('\n')

        if key not in world_series.keys():
            world_series[key] = 1
        else:
            count = world_series[key]
            world_series[key] = count + 1

    file.close()
    max_value = 0
    max_key = ""
    for value in world_series:
        if world_series[value] > max_value:
            max_value = world_series[value]
            max_key = value
            
    
    print("Total number of World Series games:", lineCount)
    print("Number of World Series champions:", len(world_series.items()))
    print("The team that won most World Series games:" , max_key)
    print(max_key, "won", max_value , "times.")
    
main()
