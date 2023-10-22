def cost_delivery(quantity, *args, discount=0):
    if quantity < 0:
        raise ValueError("Quantity must be a non-negative integer.")
    
    if not (0 <= discount <= 1):
        raise ValueError("Discount should be a fraction between 0 and 1.")

    if quantity == 0:
        return 0
    
    first_item_cost = 5  # ціна за перший товар
    additional_items_cost = 2  # ціна за кожен наступний товар після першого
    
    total_cost = first_item_cost + (quantity - 1) * additional_items_cost
    total_cost *= (1 - discount)  # застосування знижки
    
    return total_cost

# Тести
test1 = cost_delivery(2, 1, 2, 3)
print("Test 1:", test1)

test2 = cost_delivery(3, 3)
print("Test 2:", test2)

test3 = cost_delivery(1)
print("Test 3:", test3)

test4 = cost_delivery(2, 1, 2, 3, discount=0.5)
print("Test 4:", test4)