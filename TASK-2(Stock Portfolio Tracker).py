stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 320
}


def show_stocks():
    print("\nAvailable Stocks:")
    for stock, price in stock_prices.items():
        print(f"{stock} : ₹{price}")


def calculate_portfolio():
    total_value = 0
    portfolio = {}

    while True:
        stock = input(
            "\nEnter stock name (or type 'done' to finish): "
        ).upper()

        if stock == "DONE":
            break

        if stock in stock_prices:
            try:
                quantity = int(input("Enter quantity: "))

                investment = stock_prices[stock] * quantity
                total_value += investment

                portfolio[stock] = {
                    "quantity": quantity,
                    "investment": investment
                }

                print(f"{stock} Investment Value = ₹{investment}")

            except ValueError:
                print("Please enter a valid number.")

        else:
            print("Stock not found!")

    return portfolio, total_value


def save_to_file(portfolio, total_value):
    with open("portfolio.txt", "w",encoding="utf-8") as file:
        file.write("STOCK PORTFOLIO REPORT\n")
        file.write("=======================\n\n")

        for stock, details in portfolio.items():
            file.write(
                f"{stock} - Quantity: {details['quantity']} "
                f"| Investment: ₹{details['investment']}\n"
            )

        file.write("\n=======================\n")
        file.write(f"Total Portfolio Value = ₹{total_value}")

    print("\nPortfolio report saved to portfolio.txt")


print("===== STOCK PORTFOLIO TRACKER =====")

show_stocks()

portfolio, total = calculate_portfolio()

print("\nTotal Portfolio Value = ₹", total)

save_to_file(portfolio, total)

print("\nThank You for using Stock Portfolio Tracker!")