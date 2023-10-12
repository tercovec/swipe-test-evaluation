import anvil.google.auth, anvil.google.drive, anvil.google.mail
import base64
from anvil.google.drive import app_files
import anvil.server
import helpers

@anvil.server.callable
def send_mail(graphs, project_description):
  def figure_tags(graphs):
    tag = ''
    for graph, graph_description in graphs:
      "creates a html tag containing all the images encoded in base64"
      tag += f'''<figure><img alt="Swipe result" style="width:95%;height:auto" src="data:image/jpeg;base64,{helpers.get_b64string(graph.get_bytes())}"><br><figcaption style="background-color:#222;color:#fff;padding:3px;text-align:center;">{graph_description or ''}</figcaption></figure><br>'''
    return tag
    
  anvil.google.mail.send(
   from_address = "ELI Bis User <bisuserbt@gmail.com>",
   # to = ["petr.zimmermann@eli-beams.eu"],
   to = ["david.modransky@eli-beams.eu", "petr.pospisil@eli-beams.eu", "milan.maly@eli-beams.eu"],
   cc = ["frantisek.vanek@eli-beams.eu", "petr.zimmermann@eli-beams.eu"],
   subject = "ELI Swipe Results",
   html =
   f"""Swipe results from Eli Swipe Evaluation https://eli-swipe.anvil.app<p>Petr<p><h3>{project_description or ''}</h3><div style="max-width:1024px">{figure_tags(graphs)}</div> """)
  
