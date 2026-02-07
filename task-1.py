from datetime import datetime

def get_days_from_today(date):
   try:
      target_date = datetime.strptime(date, "%Y-%m-%d")
   except ValueError:
      return "Wrong date format! YYYY-MM-DD needed"

   current_date = datetime.today()
   date_range = current_date.date() - target_date.date() 
   return date_range.days

# tests
print("I have been living for " + str(get_days_from_today("1985-12-11")) + " days") 
print("Days difference with New Year: " + str(get_days_from_today("2027-01-01")))
print("Todays date return: " + str(get_days_from_today(str(datetime.today().date())))) 
# test errors
print(get_days_from_today("some wrong text"))
print(get_days_from_today("2026-99-99"))