data_box = [7,8,1,2,4,5,9,0] # A list of unsorted number.

def sorted (databox):
    for loop1 in range(len(data_box)):

        for loop2 in range(len(data_box)-1):

            if data_box[loop1] < data_box[loop2]:

                spare = data_box[loop1]
                data_box[loop1] = data_box[loop2]
                data_box[loop2] = spare

                # print("Swap posiotion of number.")  >> This is check
            else:
                # print("Not in condition.") >> This is Check
                pass

    print(data_box) # when loops end then print output.
sorted(data_box)

