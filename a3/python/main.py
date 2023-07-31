def intro():
	print("Painting Emulator")


# Developer: Bailey Weiss
# Course: LIS4369
# Semester Fall 2021

def get_requirements():
	print("Program Requirements:")
	print("1. Calculate home interior paint cost (w/o primer).")
	print("2. Must use float data types.")
	print("3. Must use SQFT_PER_GALLON constant (350).")
	print("4. Must use iteration structure (aka \"loop\").")
	print("5. Format, right-align numbers, and round to two decimal places")
	print("6. Create at least five functions that are called by the program: ")
	print("\ta. main(): calls two other functions: get_requirements() and estimate_painting_cost().")
	print("\tb. get_requirements(): displays the program requirements.")
	print("\tc. estimate_painting_cost(): calculates interior home painting, and calls print functions.")
	print("\td. print_painting_estimate(): displays painting costs.")
	print("\te. print_painting_percentage(): displays painting costs percentages.")


def print_painting_estimate(total, price, hourly):
	sqft_per_gallon = 350
	num_gal = total/sqft_per_gallon

	paint_cost = price * num_gal
	labor_cost = hourly * total
	total_cost = paint_cost + labor_cost

	formatted_paint_cost = "{:.2f}".format(paint_cost)
	formatted_labor_cost = "{:.2f}".format(labor_cost)
	formatted_total_cost = "{:.2f}".format(total_cost)

	return formatted_paint_cost, formatted_labor_cost, formatted_total_cost


def print_painting_percentage(total, price, hourly):
	sqft_per_gallon = 350
	num_gal = total / sqft_per_gallon
	paint_cost = price * num_gal
	labor_cost = hourly * total
	total_cost = paint_cost + labor_cost

	totalpercent = 100
	laborpercent = ((total_cost - paint_cost) / total_cost) * 100
	paintpercent = ((total_cost - labor_cost) / total_cost) * 100

	formatted_paint_percent = "{:.2f}".format(paintpercent)
	formatted_labor_percent = "{:.2f}".format(laborpercent)
	formatted_total_percent = "{:.2f}".format(totalpercent)

	return formatted_paint_percent, formatted_labor_percent, formatted_total_percent


def estimate_painting_cost(price, labor, total):
	sqft_per_gallon = 350

	num_gal = total/sqft_per_gallon

	formatted_total = "{:.2f}".format(total)
	formatted_sqft = "{:.2f}".format(sqft_per_gallon)
	formatted_num_gal = "{:.2f}".format(num_gal)
	formatted_paint_per_gal = "{:.2f}".format(price)
	formatted_labor = "{:.2f}".format(labor)

	print("Output:")
	text1 = "Item"
	print(text1.ljust(30, ' '), "Amount")
	text2 = "Total Sq Ft: "
	print(text2.ljust(30, ' '), formatted_total)
	text3 = "Sq Ft per Gallon:"
	print(text3.ljust(30, ' '), formatted_sqft)
	text4 = "Number of Gallons: "
	print(text4.ljust(30, ' '), formatted_num_gal)
	text5 = "Paint per Gallon: "
	print(text5.ljust(30, ' '), "$", formatted_paint_per_gal)
	text6 = "Labor per Sq Ft: "
	print(text6.ljust(30, ' '), "$", formatted_labor,)


def main():
	intro()
	get_requirements()
	print("\nInput:")
	total = float(input("Enter total interior sq ft: "))
	price = float(input("Enter price per gallon paint: "))
	hourly = float(input("Enter hourly painting rate per sq ft: "))

	estimate_painting_cost(total, price, hourly)
	
	print_painting_estimate(total, price, hourly)
	formatted_paint_cost, formatted_labor_cost, formatted_total_cost = print_painting_estimate(total, price, hourly)

	print_painting_estimate(total, price, hourly)
	formatted_paint_percent, formatted_labor_percent, formatted_total_percent = print_painting_percentage(total, price, hourly)

	text7 = "Cost"
	text11 = "Amount"
	print(text7.ljust(20, ' '), text11.ljust(20, ' '), "Percentage")
	text8 = "Paint:"
	print(text8.ljust(20, ' '), formatted_paint_cost.ljust(20, ' '), formatted_paint_percent, "%")
	text9 = "Labor:"
	print(text9.ljust(20, ' '), formatted_labor_cost.ljust(20, ' '), formatted_labor_percent, "%")
	text10 = "Total:"
	print(text10.ljust(20, ' '), formatted_total_cost.ljust(20, ' '), formatted_total_percent, "%")


if __name__ == "__main__":
	main()
