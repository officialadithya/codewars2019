testCases = int(input())

for i in range (1, testCases+1):
    tax_rate = (float(input())/100)
    total = float(input())

    pretax_price = total / (1.0 + tax_rate)
    tax_amount = pretax_price * tax_rate

    print("On your $%.2f purchase, the tax amount was $%.2f"%(total, (tax_amount)))