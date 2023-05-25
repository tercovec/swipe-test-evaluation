import anvil.google.auth, anvil.google.drive, anvil.google.mail
import base64
from anvil.google.drive import app_files
import anvil.server
import anvil.pdf
from imagesmodule import imageb64

@anvil.server.callable
def create_pdf(form):
  media_object = anvil.pdf.render_form(form)
  return media_object

@anvil.server.callable
def send_mail():
  anvil.google.mail.send(
   from_address = "Bis User <bisuserbt@gmail.com>",
   to = "petr.zimmermann@eli-beams.eu",
   subject = "TestMail",
   html =
   f"""Dear all, <p>There will be a meeting today at <b>5pm</b>. <p>Best regards, <p>Petr <img alt="My Image" src="data:image/jpeg;base64,{imageb64}" /> """)
  
# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#
