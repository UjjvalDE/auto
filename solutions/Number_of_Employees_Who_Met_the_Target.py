def numOfEmployees(logs):
    employees = {}
    for log in logs:
        employee, amount = log.split()
        amount = int(amount)
        if employee not in employees:
            employees[employee] = 0
        employees[employee] += amount

    return sum(1 for value in employees.values() if value >= target)