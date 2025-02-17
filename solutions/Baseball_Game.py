def calculate_score(cash, cookies):
    return cash + (cookies // 2) if cookies >= 12 else cash + cookies