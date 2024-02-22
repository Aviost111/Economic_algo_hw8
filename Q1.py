def can_something_be_sold(votes: list[set[str]], balances: list[float],
                          costs: dict[str, float]):
    for item, value in costs.items():
        sum = 0
        for i in range(len(votes)):
            if item in votes[i]:
                sum += balances[i]
                # was rounded to get the same results like in class
                if round(sum) >= value:
                    return True, item
        # sum_of_voters = sum(b for b in balances if item in votes[balances.index(b)])
    return False, "-1"


def elect_next_budget_item(votes: list[set[str]], balances: list[float], costs: dict[str, float]):
    increase_amount = 0.01
    can_something_be_bought, item = can_something_be_sold(votes, balances, costs)

    sum_added = 0
    while not can_something_be_bought:
        balances = [balance + increase_amount for balance in balances]
        sum_added += increase_amount
        can_something_be_bought, item = can_something_be_sold(votes, balances, costs)

    print(f"After adding {sum_added:.2f} to each citizen, {item} is chosen.")

    for i, vote in enumerate(votes):
        if item in vote:
            balances[i] = 0

    for i, balance in enumerate(balances):
        print(f"Citizen {i + 1} has {balance:.2f} remaining balance.")


# # Example usage
# votes = [{"Park", "Trees"}, {"Trees"}, {"Park", "Lights"}, {"Lights"}, {"Park"}]
# balances = [1.5, 2.4, 3.3, 4.2, 5.1]
# costs = {"Park": 1000, "Trees": 2000, "Lights": 3000}

# Example usage like in class
votes = [{"A", "B", "C", "D", "E"}] * 51 + [{"F", "G", "H", "I", "J"}] * 49
balances = [0.0] * 100
costs = {"A": 100, "B": 100, "C": 100, "D": 100, "E": 100, "F": 100, "G": 100, "H": 100, "I": 100, "J": 100}

# # Example usage like in class(for the same reason as above you need
# votes = [{"A", "B", "C", "D", "E"}] * 51 + [{"F", "G", "H", "I", "J"}] * 49
# balances = [0.0] * 51 + [1.96] * 49
# costs = {"A": 100, "B": 100, "C": 100, "D": 100, "E": 100, "F": 100, "G": 100, "H": 100, "I": 100, "J": 100}

elect_next_budget_item(votes, balances, costs)
