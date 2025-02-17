class Solution:
    def missingInfo(self, employees: List[List[str]]) -> int:
        employee_info = set()
        
        for employee in employees:
            emp_id = ''.join(filter(str.isalnum, employee[0]))
            if len(emp_id) == 8 and emp_id[:6].isdigit():
                employee_info.add(emp_id)
        
        return len(employee_info)