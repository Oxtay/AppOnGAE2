import webapp2
import os
import validdate, htmlhandle, rot13, validsign
import jinja2

THANKS      = "Thank you! That's a valid response."
USER_ERR    = "That's not a valid username."
PASS_ERR    = "That wasn't a valid password."
VERIFY_ERR  = "Your passwords didn't match."
EMAIL_ERR   = "That's not a valid email."

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape = True)

def render_str(template, **params):
    t = jinja_env.get_template(template)
    return t.render(params)
    
class BaseHandler(webapp2.RequestHandler):
    def render(self, template, **kw):
        self.response.out.write(render_str(template, **kw))
    
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)
    

class MainPage(BaseHandler):
    def get(self):
        self.render('form_main.html')
        
    def post(self):
        section = self.request.get("section")
        
        if section == "birth":
            self.redirect("/birth")
        
        elif section == "rot13":
            self.redirect("/rot13")
        
        elif section == "signup":
            self.redirect("/signup")
                
class EnterBirthday(BaseHandler):
    def get(self):
        self.render('form_birthday.html')
        
    def post(self):
        user_month = self.request.get("month")
        user_day   = self.request.get("day")
        user_year  = self.request.get("year")
        
        month   = validdate.valid_month(user_month)
        day     = validdate.valid_day(user_day)
        year    = validdate.valid_year(user_year)
        
        if not (month and day and year):
            params = dict(month = user_month, 
                            day = user_day, 
                            year = user_year)
            params['error'] = "That doesn't seem right"
            self.render('form_birthday.html', **params)
        else:
            self.redirect("/thanks")
            
class ThanksHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write(THANKS)

class Rot13(BaseHandler):       
    def get(self):
        self.render('form_rot13.html')
        
    def post(self):
        user_text = self.request.get('text')
        text = rot13.rot13ify(user_text)
        self.render('form_rot13.html', text=text)
        
class signup(BaseHandler):
    def get(self):
        self.render('form_signup.html')
        
    def post(self):
        username = self.request.get("username")
        password = self.request.get("password")
        verify   = self.request.get("verify")
        email    = self.request.get("email")
        
        have_error = False
        params = dict(username = username, email = email)
                
        if not validsign.isValidUser(username):
            params['user_err'] = USER_ERR
            have_error = True
            
        if not validsign.isValidPass(password):
            params['pass_err'] = PASS_ERR
            have_error = True
        
        if not validsign.isValidEmail(email):
            params['email_err'] = EMAIL_ERR
            have_error = True
            
        if password != verify:
            params['verify_err'] = VERIFY_ERR
            have_error = True
            
        if have_error:
            self.render('form_signup.html', **params)
            
        else:
            #self.response.out.write("Welcome, %s" % username)
            self.redirect("/welcome?username=" + username)

class Welcome(BaseHandler):
    def get(self):
        username = self.request.get('username')
        if validsign.isValidUser(username):
            self.response.write("Welcome, " + username + '!')
        else:
            self.redirect('/signup')

application = webapp2.WSGIApplication([
                                ('/', MainPage), 
                                ('/birth', EnterBirthday), 
                                ('/thanks', ThanksHandler), 
                                ('/rot13', Rot13), 
                                ('/signup', signup), 
                                ('/welcome', Welcome)], debug=True)