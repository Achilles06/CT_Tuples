#1. Tuple Mastery in Python
#Task 1: Formatting Flight Itineraries

def format_itineraries(itineraries):
    formatted_itineraries = []
    for i, (name, origin, destination) in enumerate(itineraries, start=1):
        formatted_itineraries.append(f"Itinerary {i}: {name} - From {origin} to {destination}")
    return "\n".join(formatted_itineraries)

flight_data = [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]
formatted_output = format_itineraries(flight_data)
print(formatted_output)

#2. Python Data Structure Challenges in Real-World Scenarios
#Task 1: Library System Enhancement

def add_book(library, title, author):
    for existing_title, existing_author in library:
        if existing_title.lower() == title.lower() and existing_author.lower() == author.lower():
            return f"Book '{title}' by {author} to the library."
        
library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]
new_title = "Animal Farm"
new_author = "George Orwell"
result = add_book(library, new_title, new_author)
print(result)

#3. Python Loops and Tuples in Analytical Applications
#Task 1. Stock Market Data Analysis

def calculate_average_closing_price(stock_data, stock_symbol):
    total_closing_price = 0
    count = 0

    for symbol, _, closing_price in stock_data:
        if symbol == stock_symbol:
            total_closing_price += closing_price
            count += 1

    if count == 0:
        return f"No data found for stock symbol '{stock_symbol}'."
    
    average_closing_price = total_closing_price / count
    return average_closing_price

stock_data = [
    ("AAPL", "2021-01-01", 130.0),
    ("AAPL", "2021-01-02", 132.0),
    ("MSFT", "2021-01-01", 220.0),
    # More data...
]

specified_stock_symbol = "AAPL"
average_price = calculate_average_closing_price(stock_data, specified_stock_symbol)
print(f"Average closing price for {specified_stock_symbol}: ${average_price: .2f}")

#4. Mastering Tuple Packing and Unpacking in Python
#Task 1.  Customer Order Processing
def print_order_details(orders):
    for i, (customer_name, product, quantity) in enumerate(orders, start=1):
        print(f"Order {i}:")
        print(f" Customer: {customer_name}")
        print(f" Product: {product}")
        print(f" Quantity: {quantity}\n")

orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
]

print_order_details(orders)

#5. Advanced Tuple Techniques: Joining and Nesting in Python
#Task 1

def merge_catalogs(*catalogs):
    combined_catalog = ()
    for catalog in catalogs:
        combined_catalog += catalog

    return combined_catalog

catalog1 = (("Laptop", 1000), ("Camera", 500))
catalog2 = (("Smartphone", 800),("Tablet", 450))

combined_catalog = merge_catalogs(catalog1, catalog2)
print(combined_catalog)