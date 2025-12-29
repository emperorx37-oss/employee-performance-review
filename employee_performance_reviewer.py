# Employee performance review

employees = [
    ["Sarah", 45000],
    ["Marcus", 28000],
    ["Jen", 62000],
    ["Kyle", 15000],
    ["Derek", 8000],
    ["Lisa", 72000],
    ["Tom", 33000],
]


def employee_segmentation(sales):
    if sales >= 50000:
        return "Top Performing"
    elif sales >= 20000:
        return "Solid Performing"
    else:
        return "Needs coaching"


# employee total
top_count = 0
solid_count = 0
needs_coaching_count = 0

# Sales total
top_sales = 0
solid_sales = 0
needs_coaching_sales = 0

# Bonus total
top_bonus = 0
solid_bonus = 0
needs_coaching_bonus = 0

for employee in employees:
    sales_segmentation = employee_segmentation(employee[1])
    if sales_segmentation == "Top Performing":
        top_count = top_count + 1
        top_sales = top_sales + employee[1]
        top_bonus = top_bonus + employee[1] * 0.1
    elif sales_segmentation == "Solid Performing":
        solid_count = solid_count + 1
        solid_sales = solid_sales + employee[1]
        solid_bonus = solid_bonus + employee[1] * 0.05
    else:
        needs_coaching_count = needs_coaching_count + 1
        needs_coaching_sales = needs_coaching_sales + employee[1]
        needs_coaching_bonus = needs_coaching_bonus + employee[1] * 0.02
total_employees = 8
total_sales = top_sales + solid_sales + needs_coaching_sales
total_bonus_payouts = top_bonus + solid_bonus + needs_coaching_bonus
top_average = top_sales / top_count
solid_average = solid_sales / solid_count
needs_coaching_average = needs_coaching_sales / needs_coaching_count
print("EMPLOYEE PERFORMANCE REPORT: ")
print(f"Top performing employees: {top_count}")
print(f"Top performing sales total: {top_sales}")
print(f"Top performing bonus total: {top_bonus}")
print("__________________________________________")
print("__________________________________________")
print(f"Solid performing employees: {solid_count}")
print(f"Solid performing sales: {solid_sales}")
print(f"Solid performing bonus total: {solid_bonus}")
print("__________________________________________")
print("__________________________________________")
print(f"Needs coaching employees: {needs_coaching_count}")
print(f"Needs coaching sales: {needs_coaching_sales}")
print(f"Needs coaching bonus total: {needs_coaching_bonus}")
print("__________________________________________")
print("__________________________________________")
print(f"Top performing average sales: {top_average}")
print(f"Solid performing average sales: {solid_average}")
print(f"Needs coaching average sales: {needs_coaching_average}")
print("__________________________________________")
print("__________________________________________")
print(f"TOTAL EMPLOYEES: {total_employees}")
print(f"TOTAL SALES: {total_sales}")
