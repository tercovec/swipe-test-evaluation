from ._anvil_designer import mainTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from datetime import date
import anvil.media

class main(mainTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.sample_OK, self.blank_OK = False, False
    try:
      anvil.server.call('server_alive')
      self.server_status.text = "backend: OK"
    except: # anvil.server.UplinkDisconnectedError or anvil.server.NoServerFunctionError:
      self.server_status.text = "backend uplink: DOWN"
      self.server_status.background = 'red'
    self.item['area'] = float(self.sample_size.placeholder)
    self.item['date'] = date.today()

  def generate_graph_click(self, **event_args):
    """This method is called when the button is clicked"""
    blank = self.loader_blank.file
    samples = self.loader_sample.files
    
    self.graph_repeating_panel.items = [anvil.server.call('generate_graph', blank, sample, area = self.item['area'], datum = str(self.item['date'])) for sample in samples]
    # media_obj = anvil.server.call('generate_graph', blank, samples)


  def loader_blank_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    if self.loader_blank.file is not None:
      self.loader_blank.role = 'tonal-button'
      self.lbl_blank_name.text = self.loader_blank.file.name
      self.blank_OK = True
      if self.sample_OK and self.blank_OK:
        self.generate_graph.enabled = True
    else:
      self.loader_blank.role = 'elevated-button'
      self.lbl_blank_name.text = 'no blank file selected'
      self.blank_OK = False
      self.generate_graph.enabled = False

  def loader_sample_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    if self.loader_sample.file is not None:
      self.loader_sample.role = 'tonal-button'
      def generate_filename_markdown(files):
        md = ''
        for _ , file in enumerate(files):
          md += str(_) +'. ' + str(file.name) + '\n'
        return md
            
        
      self.lbl_sample_name.content = generate_filename_markdown(self.loader_sample.files)
      self.sample_OK = True
      if self.sample_OK and self.blank_OK:
        self.generate_graph.enabled = True
    else:
      self.loader_sample.role = 'elevated-button'
      self.lbl_sample_name.text = 'no SAMPLE files selected'
      self.sample_OK = False
      self.generate_graph.enabled = False

  def file_loader_1_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    pass

      

    

