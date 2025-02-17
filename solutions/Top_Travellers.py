def topTravellers(travelers):
    return sorted([(name, sum(flights.values())) for name, flights in travelers.items()], key=lambda x: -x[1])