def highFive(logs):
    employees = {}
    for log in logs:
        emp, score = log.split()
        emp = int(emp)
        score = int(score[:-1])
        if emp not in employees:
            employees[emp] = []
        employees[emp].append(score)
    
    result = []
    for emp in employees:
        scores = employees[emp]
        avg = sum(scores) // len(scores)
        result.append([emp, avg])
        
    return sorted(result, key=lambda x: (-x[1], x[0]))