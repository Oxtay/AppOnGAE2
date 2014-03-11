import webapp2
import validdate
import htmlhandle

form  = """
<h2>Enter some text to ROT13:</h2>
<form method="post">
      <textarea name="text"
                style="height: 100px; width: 400px;">%(text)s</textarea>
      <br>
      <input type="submit">
</form>
"""

class Rot13(webapp2.RequestHandler):
    def write_form(self, error="", text=""):
        self.response.out.write(form % {"error": error,
                                    "month": htmlhandle.escape_html(text)})
        
    def get(self):
        self.write_form()
        
    def post(self):
        user_month = self.request.get("month")
        
        month = validdate.valid_month(user_month)
        self.redirect("/rot13")
            

application = webapp2.WSGIApplication([('/rot13', Rot13)], debug=True)