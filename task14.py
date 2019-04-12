def MaximumDiscount(N, prices):
    discount = 0
    col = len(prices) % 3;
    for i in range(col+1):
        prices.append(0)
    prices.sort(reverse=True)
    for idx, price in  enumerate(prices):
        if idx % 3 == 2:
            discount = discount + price
    return discount