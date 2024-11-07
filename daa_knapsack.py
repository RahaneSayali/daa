class Item:
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight

def fractionknapsack(capacity, items):
    # Sort items by profit-to-weight ratio in descending order
    items.sort(key=lambda x: x.profit / x.weight, reverse=True)
    final_val = 0.0

    for item in items:
        if capacity >= item.weight:
            # Take the full item
            final_val += item.profit
            capacity -= item.weight	
        else:
            # Take the fraction of the item that fits
            final_val += item.profit * (capacity / item.weight)
            break

    return final_val

def main():
    n = int(input("Enter the number of items:\n"))
    
    items = []
    
    for i in range(n):
        profit = int(input(f"Enter profit of item {i+1}:\n"))
        weight = int(input(f"Enter weight of item {i+1}:\n"))
        items.append(Item(profit, weight))
    
    capacity = int(input("Enter capacity of knapsack:\n"))
    
    max_value = fractionknapsack(capacity, items)
    print("Maximum profit:", max_value)

if __name__ == "__main__":
    main()
