print("Payroll Calculator")

# Developer: Bailey Weiss
# Course: LIS4369
# Semester Fall 2021

def get_requirements() :
    print("\nProgram Requirements:")
    print("\n1. Must usefloat data type for user input.")
    print("\n2. Overtime rate: 1.5 times hourly rate (hours over 40)")
    print("\n3. Holiday rate: 2.0 times hourly rate (all holiday hours)")
    print("\n4. Must format currency with dollar sign, and round to two decimal places.")
    print("\n5. Create at least three functions that are called by the program:")
    print("\n \ta. main(): calls at least two other functions")
    print("\n \tb. get_requirements(): displays the program requirements.")
    print("\n \tc. calculate_payroll(): calculates an individual one-week paycheck.")

def get_input() :
    print("\nInput:")
    work_hours = float(input("Enter hours worked: "))
    holiday_hours = float(input("Enter holiday hours: "))
    hourly = float(input("Enter hourly pay rate: "))
    
def calculate_base_pay(work_hours, holiday_hours, hourly) :
    left_over = 0
    
    if work_hours > 40 :
        base = 40
        left_over = work_hours - 40
    elif work_hours < 40 :
        base = work_hours * hourly
        left_over = 0
    



print("\nProgram Output: ")
