def main():
    months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
    date_final = get_final_date(months)
    print(f"{date_final}")

def get_final_date(l):
    while True:
        try:
            input_date = input("Date: ").strip()
            date_list = input_date.split()
            if date_list[0] in l:
                if not date_list[1].endswith(","):
                    continue
                month = l.index(date_list[0]) + 1
                day = int(date_list[1].replace(",", ""))
                year = int(date_list[2])
                if 1 <= day <= 31:
                    date = (f"{year}-{month:02}-{day:02}")
                    return date
            else:
                m, d, y = input_date.split("/")
                m, d, y = int(m), int(d), int(y)
                if 1 <= m <= 12 and 1 <= d <= 31:
                    return f"{y}-{m:02}-{d:02}"
        except (ValueError, IndexError):
            pass
main()
