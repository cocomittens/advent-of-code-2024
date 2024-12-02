from day2_data import data

reports = []

def process_data():
    data_array = data.split("\n")

    for i, row in enumerate(data_array):
        levels = list(map(int, row.split(" ")))
        reports.append(levels)

# Returns if a level is safe
def is_safe(level):
    prev = level[0]
    is_decreasing = False
    is_increasing = False

    for i in range(1, len(level)):
        curr = level[i]
        diff = abs(curr - prev)
        if diff > 3 or diff < 1:
            return False

        if curr > prev:
            if is_decreasing:
                return False
            is_increasing = True

        elif curr < prev:
            if is_increasing:
                return False
            is_decreasing = True

        prev = curr

    return True

# Returns if a level is safe, allowing 1 bad row removal
# A bit messy tbh but it works
def is_safe_with_dampener(level):
    prev = level[0]
    is_decreasing = False
    is_increasing = False
    is_bad = False

    for i in range(1, len(level)):
        curr = level[i]
        diff = abs(curr - prev)
        if diff > 3 or diff < 1:
            if not is_bad:
                is_bad = True
                prev = curr
                continue
            else:
                return False

        if curr > prev:
            if is_decreasing:
                if not is_bad:
                    is_bad = True
                else:
                    return False
            else:
                is_increasing = True

        elif curr < prev:
            if is_increasing:
                if not is_bad:
                    is_bad = True
                else:
                    return False
            else:
                is_decreasing = True

        prev = curr

    return True

# Calculate total number of safe reports
def calculate_safe_reports(allow_bad=False):
    safe_reports = 0

    for report in reports:
        if allow_bad:
            if is_safe_with_dampener(report):
                safe_reports += 1
        else:
            if is_safe(report):
                safe_reports += 1

    return safe_reports

if __name__ == '__main__':
    process_data()
    # Part 1
    result_1 = calculate_safe_reports()
    print(result_1)
    # Part 2
    result_2 = calculate_safe_reports(True)
    print(result_2)