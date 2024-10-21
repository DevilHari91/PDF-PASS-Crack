# Importing required module for handling dates
import calendar

# Specify the output file path
file_path = r"C:\Users\ADMIN\OneDrive\Desktop\Crack\all_dates.txt"


# Open the file in write mode
with open(file_path, "w") as file:
    # Loop through each month (1 to 12 for January to December)
    for month in range(1, 13):
        # Get the number of days in the current month
        # The calendar.monthrange function returns a tuple, where the second value is the number of days
        num_days = calendar.monthrange(2024, month)[1]  # Change year if needed

        # Loop through each day in the month
        for day in range(1, num_days + 1):
            # Format the day and month as DDMM (e.g., 0101 for January 1st)
            day_str = f"{day:02d}"   # Format day as two digits
            month_str = f"{month:02d}"  # Format month as two digits

            # Construct the line "RAGADDMM" format
            line = f"RAGA{day_str}{month_str}\n"

            # Write the line to the text file
            file.write(line)

print("All dates generated and saved to all_dates.txt successfully!")
