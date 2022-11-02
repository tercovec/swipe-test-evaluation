from ._anvil_designer import mainTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class main(mainTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  def generate_graph_click(self, **event_args):
    """This method is called when the button is clicked"""
    response = anvil.server.call('say_hi')
    self.label.content = response
    

