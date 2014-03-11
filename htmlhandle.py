import cgi

# replacing <, >, &, " in html code with escape
def escape_html2(s):
    for (i,o) in (("&", "&amp;"),
                  (">", "&gt;"),
                  ("<", "&lt;"),
                  ('"', "&quot;")):
        s = s.replace(i,o)  
    return s
    
# alternative method of doing it using cgi
def escape_html(s):
    return cgi.escape(s, quote = True)