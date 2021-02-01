def bubble_sort(input_list):    
    sorted_elements = 0
    while (sorted_elements < len(input_list)):     # bubble sort need to do len(list)-1 times of sorting-cycle
        for i in range(len(input_list)-1-sorted_elements):       # within each cycle, compare numbers from the end to the front
            if input_list[-1-i] < input_list[-2-i]:
                input_list[-1-i],input_list[-2-i] = input_list[-2-i],input_list[-1-i]
        sorted_elements += 1     
    return input_list
            
