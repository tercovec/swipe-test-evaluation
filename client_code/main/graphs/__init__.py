from ._anvil_designer import graphsTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class graphs(graphsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.download_link.url = self.item
    self.graph_image.source = self.item
    # Any code you write here will run when the form opens.

  def download_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    pass

