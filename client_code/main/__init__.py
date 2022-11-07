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
    try:
      anvil.server.call('server_alive')
      self.server_status.text = "server OK"
    except anvil.server.UplinkDisconnectedError:
      self.server_status.text = "server disconnected"


  def generate_graph_click(self, **event_args):
    """This method is called when the button is clicked"""
    blank = self.loader_blank.file
    samples = self.loader_sample.files
    
    self.graph_repeating_panel.items = [anvil.server.call('generate_graph', blank, sample) for sample in samples]
    # media_obj = anvil.server.call('generate_graph', blank, samples)


  def loader_blank_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    self.lbl_blank_name.text = file.name

  def loader_sample_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    file_names = str([file.name for file in self.loader_sample.files])
    self.lbl_sample_name.text = file_names


    

