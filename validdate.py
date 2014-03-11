months = ['January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December']

month_abbvs = dict((m[:3].lower(), m) for m in months)

def valid_month(month):
    if month: 
        short_month = month[:3].lower()
        return month_abbvs.get(short_month)
	
def valid_day(day):
    if day.isdigit():
        day_int= int(day)
        if day_int<=31 and day_int>=1:
            return day_int
			
def valid_year(year):
    if year and year.isdigit():
        if int(year)>=1900 and int(year)<=2020:
            return int(year)