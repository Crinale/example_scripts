if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = raw_input()

    mark = student_marks[query_name] 
    add = mark[0]+mark[1]+mark[2]
    avg = add/3

    print format(avg,'.2f')