with open('d2.input', 'r') as file:
    report = [list(map(int, line.strip().split())) for line in file]


def is_safe_report(levels):

    increasing = all(1 <= levels[i + 1] - levels[i] <= 3 for i in range(len(levels) - 1))
    decreasing = all(1 <= levels[i] - levels[i + 1] <= 3 for i in range(len(levels) - 1))

    return increasing or decreasing

def count_safe_reports(reports):
    safe_count = 0
    for report_line in reports:

        if is_safe_report(report_line):
            safe_count += 1
    return safe_count


safe_reports_count = count_safe_reports(report)
print(safe_reports_count)
