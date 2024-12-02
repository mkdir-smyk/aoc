def is_safe_report(levels):
    # Check if the list is increasing or decreasing
    increasing = all(1 <= levels[i + 1] - levels[i] <= 3 for i in range(len(levels) - 1))
    decreasing = all(1 <= levels[i] - levels[i + 1] <= 3 for i in range(len(levels) - 1))
    
    # A report is safe if it's either increasing or decreasing according to the rules
    return increasing or decreasing

def is_safe_report_with_one_removal(levels):
    # Try removing each element and check if the resulting report is safe
    for i in range(len(levels)):
        # Create a new list with the i-th element removed
        new_levels = levels[:i] + levels[i+1:]
        # Check if the new list is safe
        if is_safe_report(new_levels):
            return True
    return False

def count_safe_reports(reports):
    safe_count = 0
    for report_line in reports:
        # Check if the current report is safe either without removal or with one removal
        if is_safe_report(report_line) or is_safe_report_with_one_removal(report_line):
            safe_count += 1
    return safe_count

# Read the report data from the file
with open('d2.input', 'r') as file:
    report = [list(map(int, line.strip().split())) for line in file]

# Count the safe reports
safe_reports_count = count_safe_reports(report)
print(f"Total Safe Reports: {safe_reports_count}")
