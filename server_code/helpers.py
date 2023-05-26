import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.server
import base64

def get_b64string(file):
  """this function provides a base64 encoded file and prints it as ASCII characters. It is used for embedding an image directlo the mail content"""
  encoded = base64.b64encode(file)
  return encoded.decode("ascii")

