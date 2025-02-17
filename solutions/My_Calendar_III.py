class MyCalendarThree:

    def __init__(self):
        self.events = []

    def book(self, start: int, end: int) -> int:
        self.events.append((start, 1))
        self.events.append((end - 1, -1))
        events = sorted(self.events)
        count = 0
        max_count = 0
        curr_count = 0
        for event in events:
            if event[1] == 1:
                curr_count += 1
            else:
                curr_count -= 1
            if curr_count > max_count:
                max_count = curr_count
            if curr_count < 0:
                curr_count = 0
        return max_count + 1