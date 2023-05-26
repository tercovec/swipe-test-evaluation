import anvil.google.auth, anvil.google.drive, anvil.google.mail
import base64
from anvil.google.drive import app_files
import anvil.server
import helpers

@anvil.server.callable
def send_mail(images):
  def image_tag(images):
    tag = ''
    for image in images:
      "creates a html tag containing all the images encoded in base64"
      tag += f'''<img alt="My Image" src="data:image/jpeg;base64,{helpers.get_b64string(image.get_bytes())}"<br>'''
    return tag
    
  anvil.google.mail.send(
   from_address = "ELI Bis User <bisuserbt@gmail.com>",
   to = ["petr.zimmermann@eli-beams.eu", "david.modransky@eli-beams.eu"],
   subject = "ELI Swipe Results",
   html =
   f"""Swipe results <p>Petr<p> {image_tag(images)} """)
  
