def intro():
	print("Payroll Calculator")


# Developer: Bailey Weiss
# Course: LIS4369
# Semester Fall 2021

def get_requirements():
	print("Program Requirements:")
	print("1. Must use float data type for user input.")
	print("2. Overtime rate: 1.5 times hourly rate (hours over 40)")
	print("3. Holiday rate: 2.0 times hourly rate (all holiday hours)")
	print("4. Must format currency with dollar sign, and round to two decimal places.")
	print("5. Create at least three functions that are called by the program:")
	print("\ta. main(): calls at least two other functions")
	print("\tb. get_requirements(): displays the program requirements.")
	print("\tc. calculate_payroll(): calculates an individual one-week paycheck.")


def calculate_payroll(work_hours, holiday_hours, hourly):
	left_over = 0
	base = 0
	if work_hours > 40:
		base = 40 * hourly
		left_over = work_hours - 40
	elif work_hours <= 40:
		base = work_hours * hourly
		left_over = 0
	overtime = left_over * hourly * 1.5

	holiday_pay = holiday_hours * hourly * 2.0
	gross = base + overtime + holiday_pay

	formatted_base = "{:.2f}".format(base)
	formatted_overtime = "{:.2f}".format(overtime)
	formatted_holiday_pay = "{:.2f}".format(holiday_pay)
	formatted_gross = "{:.2f}".format(gross)

	print("Output:")
	print("Base: ", formatted_base)
	print("Overtime: ", formatted_overtime)
	print("Holiday: ", formatted_holiday_pay)
	print("Gross: ", formatted_gross)


def main():
	intro()
	get_requirements()
	print("\nInput:")
	work_hours = float(input("Enter hours worked: "))
	holiday_hours = float(input("Enter holiday hours: "))
	hourly = float(input("Enter hourly pay rate: "))

	calculate_payroll(work_hours, holiday_hours, hourly)

	return 0


if __name__ == "__main__":
	main()
