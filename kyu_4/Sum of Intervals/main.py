# Sum of Intervals

# https://www.codewars.com/kata/52b7ed099cdc285c300001cd/train/python

def sum_of_intervals(intervals):
    
    intervals.sort(key=lambda x: x[0])
    
    merge = []
    
    curr_start, curr_end = intervals[0]
    
    for start, end in intervals[1:]:
        
        if start <= curr_end:
            curr_end = max(curr_end, end)
            
        else:
            merge.append((curr_start, curr_end))
            
            curr_start, curr_end = start, end
            
    merge.append((curr_start, curr_end))
    
    return sum(end - start for start, end in merge)
