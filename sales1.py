# Priser för varje produkt
prices = {
    "Hamburgare": 50,
    "Pommes frites": 25,
    "Läsk": 20,
    "Milkshake": 30,
    "Sallader": 45,
    "McNuggets": 35
}

# Försäljningsdata för 10 dagar
sales_data = [
    {"Hamburgare": 150, "Pommes frites": 200, "Läsk": 180, "Milkshake": 40, "Sallader": 30, "McNuggets": 100},
    {"Hamburgare": 170, "Pommes frites": 220, "Läsk": 190, "Milkshake": 50, "Sallader": 35, "McNuggets": 105},
    {"Hamburgare": 160, "Pommes frites": 210, "Läsk": 185, "Milkshake": 45, "Sallader": 33, "McNuggets": 110},
    {"Hamburgare": 180, "Pommes frites": 230, "Läsk": 200, "Milkshake": 55, "Sallader": 40, "McNuggets": 115},
    {"Hamburgare": 170, "Pommes frites": 220, "Läsk": 195, "Milkshake": 50, "Sallader": 38, "McNuggets": 120},
    {"Hamburgare": 190, "Pommes frites": 240, "Läsk": 210, "Milkshake": 60, "Sallader": 42, "McNuggets": 125},
    {"Hamburgare": 185, "Pommes frites": 235, "Läsk": 205, "Milkshake": 58, "Sallader": 40, "McNuggets": 130},
    {"Hamburgare": 175, "Pommes frites": 225, "Läsk": 190, "Milkshake": 52, "Sallader": 36, "McNuggets": 120},
    {"Hamburgare": 165, "Pommes frites": 215, "Läsk": 185, "Milkshake": 48, "Sallader": 34, "McNuggets": 110},
    {"Hamburgare": 180, "Pommes frites": 230, "Läsk": 200, "Milkshake": 55, "Sallader": 39, "McNuggets": 115}
]

def calculate_daily_revenue(sales_data, prices):
    daily_revenues = []
    
    # Gå igenom varje dags försäljningsdata
    for daily_sales in sales_data:
        total_revenue = 0
        
        # Gå igenom varje produkt och multiplicera med antalet sålda enheter
        for product, quantity in daily_sales.items():
            total_revenue += prices[product] * quantity
        
        daily_revenues.append(total_revenue)
    
    return daily_revenues

# Beräkna och skriv ut resultatet
daily_revenues = calculate_daily_revenue(sales_data, prices)
print(daily_revenues)
