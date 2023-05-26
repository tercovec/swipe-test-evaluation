import anvil.google.auth, anvil.google.drive, anvil.google.mail
import base64
from anvil.google.drive import app_files
import anvil.server
import anvil.pdf
from imagesmodule import imageb64
import helpers

@anvil.server.callable
def create_pdf(form):
  media_object = anvil.pdf.render_form(form)
  return media_object

@anvil.server.callable
def send_mail(images):
  def image_tag(images):
    tag = ''
    for image in images:
      tag += f'<img alt="My Image" src="data:image/jpeg;base64,{helpers.get_b64string(image.get_bytes())}" /></br>'
    return tag
    
  anvil.google.mail.send(
   from_address = "Bis User <bisuserbt@gmail.com>",
   to = "petr.zimmermann@eli-beams.eu",
   subject = "TestMail",
   html =
   f"""Best regards, <p>Petr<p> {image_tag(images)}" /> """)
  
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
