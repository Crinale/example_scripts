def solve(s):
    cap = []
    text = s.split(" ")
    for i in text:
    	cap.append(i.capitalize())
    return ' '.join(cap)


solve("hello my name is devon 1 2 3 ! @ # ")