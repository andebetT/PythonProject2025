#given a string that consists of left and right parenthesis "(" and ")" balance the parenthesis by inserting new if needed return the minimum number of parenthesis needed to balance

def minimum_insertions_required(s):
    open_count=0
    close_count=0

    for i in s:
        if i=="(":
            open_count+=1
        else:
            if open_count>0:
                open_count-=1
            else:
                close_count+=1
    return close_count+open_count


s="((()))"
print(minimum_insertions_required(s))
