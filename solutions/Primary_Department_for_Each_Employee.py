def mostCommonDepartment(departments):
    from collections import Counter
    department_counts = Counter({department: 0 for department in set(departments)})
    for department in departments:
        department_counts[department] += 1
    return max(department_counts, key=department_counts.get)