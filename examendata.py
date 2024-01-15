def decode(message_file):

    decoded_message = ""
    data_mapping = dict()

    # Open the text file for reading and the file handler is named data.
    # then with the for loop reads each line of the file, removes the leading and trailing with space
    # from the string, then split the string into key-value 
    # and store the splitted data in the data_mapping dictionary
    with open(message_file, "r") as data :
        for line in data:
            line = line.strip()
            index = line.find(' ')
            key = int(line[:index])
            value = line[index + 1:]
            data_mapping[key] = value

    #creates a list with the numbers that are keys of data_mapping
    # then sort it 
    numbers_list = data_mapping.keys()
    numbers_list = list(numbers_list)
    numbers_list.sort()
    
    # Creates the pyramid staircase using the ordered numbers_list.            
    step = 1
    pyramid = list()
    while len(numbers_list) != 0:
        if len(numbers_list) >= step:
            pyramid.append(numbers_list[0:step])
            numbers_list = numbers_list[step:]
            step += 1
        else:
            break
    
    # Generates decoded message        
    for i in range(0,len(pyramid)):
      decoded_message = decoded_message + data_mapping[pyramid[i].pop()] + " "
     
    return decoded_message


print(decode("coding_qual_input.txt"))