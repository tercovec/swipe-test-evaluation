import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.server
import base64


sample_string = "GeeksForGeeks is the best"
sample_string_bytes = sample_string.encode("ascii")
  
base64_bytes = base64.b64encode(sample_string_bytes)
base64_string = base64_bytes.decode("ascii")

def get_b64string(image):
  encoded = base64.b64encode(image)
  return encoded.decode("ascii")

