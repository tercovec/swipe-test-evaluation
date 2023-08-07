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
      tag += f'''<img alt="Swipe result" style="width:95%;height:auto" src="data:image/jpeg;base64,{helpers.get_b64string(image.get_bytes())}"<br>'''
    return tag
    
  anvil.google.mail.send(
   from_address = "ELI Bis User <bisuserbt@gmail.com>",
   # to = ["petr.zimmermann@eli-beams.eu"],
   to = ["david.modransky@eli-beams.eu", "petr.pospisil@eli-beams.eu"],
   cc = ["frantisek.vanek@eli-beams.eu", "petr.zimmermann@eli-beams.eu"],
   subject = "ELI Swipe Results",
   html =
   f"""Swipe results from Eli Swipe Evaluation https://eli-swipe.anvil.app<p>Petr<p> <div style="max-width:1024px">{image_tag(images)}</div> """)
  
