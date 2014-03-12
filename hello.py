import webapp2
import validdate, htmlhandle, rot13, validsign

form_main = """
<form method="post">
	<select name="section">
		<option value="birth">Enter Birthday</option>
		<option value="rot13">Convert to ROT13</option>
		<option value="signup">Signup Form</option>
	<br>
	<input type="submit">
</form>
"""
form_birthday  = """
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

form_rot13  = """
<h2>Enter some text to ROT13:</h2>
<form method="post">
      <textarea name="text"
                style="height: 100px; width: 400px;">%(text)s</textarea>
      <br>
      <input type="submit">
</form>
"""

form_singup = """
<h2>Signup</h2>
    <form method="post">
      <table>
        <tr>
          <td class="label">
            Username
          </td>
          <td>
            <input type="text" name="username" value="%(username)s">
          </td>
          <td class="error">
            %(user_err)s
          </td>
        </tr>

        <tr>
          <td class="label">
            Password
          </td>
          <td>
            <input type="password" name="password" value="%(password)s">
          </td>
          <td class="error">
            %(pass_err)s
          </td>
        </tr>

        <tr>
          <td class="label">
            Verify Password
          </td>
          <td>
            <input type="password" name="verify" value="%(verify)s">
          </td>
          <td class="error">
            %(verify_err)s
          </td>
        </tr>

        <tr>
          <td class="label">
            Email (optional)
          </td>
          <td>
            <input type="text" name="email" value="%(email)s">
          </td>
          <td class="error">
            %(email_err)s
          </td>
        </tr>
      </table>

      <input type="submit">
    </form>
"""

class MainPage(webapp2.RequestHandler):
    def write_form(self):
        self.response.out.write(form_main)
    
    def get(self):
        self.write_form()
        
    def post(self):
        section = self.request.get("section")
        
        if section == "birth":
            self.redirect("/birth")
        
        elif section == "rot13":
            self.redirect("/rot13")
        
        elif section == "signup":
            self.redirect("/signup")
                
class EnterBirthday(webapp2.RequestHandler):
    def write_form(self, error="", month="", day="", year=""):
        self.response.out.write(form_birthday % {"error": error,
                                    "month": htmlhandle.escape_html(month),
                                    "day": htmlhandle.escape_html(day),
                                    "year": htmlhandle.escape_html(year)})
        
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
            self.redirect("/thanks")
            
class ThanksHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write("Thank you! That's a valid responce.")

class Rot13(webapp2.RequestHandler):
    def write_form(self, text=""):
        self.response.out.write(form_rot13 % {"text": htmlhandle.escape_html(text)})
        
    def get(self):
        self.write_form()
        
    def post(self):
        user_text = self.request.get("text")
        text = rot13.rot13ify(user_text)
        self.write_form(text)
        
class signup(webapp2.RequestHandler):
    def write_form(self, username="", password="", 
                    verify="", email="", 
                    user_err="", pass_err="", 
                    verify_err="", email_err=""):
        self.response.out.write(form_signup % {"username":username,
                                        "password":password,
                                        "verify":verify,
                                        "email":email})
        
    def post(self):
        user_name = validsign.valid_username(username)
        pass_word = validsign.valid_password(password)
        e_mail = validsign.valid_email(email)
        
        self.response.out.write()

application = webapp2.WSGIApplication([
    ('/', MainPage), ('/birth', EnterBirthday), ('/thanks', ThanksHandler), ('/rot13', Rot13)], debug=True)