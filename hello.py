import webapp2
import validdate

form  = """
<form method="post">
    What is your birthday
    <br>
    <label>
        Month 
        <input type="text" name="month" value="%(month)s">
    </label>
    <label>
        Day 
        <input type="text" name="day" value="%(day)s">
    </label>
    <label>
        Year 
        <input type="text" name="year" value="%(year)s">
    </label>
    <div style="color: red">%(error)s</div>
    <br>
    <br>
	<input type="submit">
</form>
"""

class MainPage(webapp2.RequestHandler):
    def write_form(self, error="", month="", day="", year=""):
        self.response.write(form % {"error": error,
                                    "month": month,
                                    "day": day,
                                    "year": year})
        
    def get(self):
        self.write_form()
        
    def post(self):
        user_month = self.request.get("month")
        user_day = self.request.get("day")
        user_year = self.request.get("year")
        
        month = validdate.valid_month(user_month)
        day = validdate.valid_day(user_day)
        year = validdate.valid_year(user_year)
        
        if not (month and day and year):
            self.write_form("That doesn't seem right",
                            user_month, user_day, user_year)
        else:
            self.response.write("Thank you! That's a valid responce.")

application = webapp2.WSGIApplication([
    ('/', MainPage)], debug=True)