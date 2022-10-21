from fpdf import FPDF
import os
import glob
from plotting_functions import plot_fermenter_complete
import datetime

class PDF(FPDF):
    def __init__(self):
        super().__init__()
        self.WIDTH = 210
        self.HEIGHT = 297
        
    def header(self):
        # Custom logo and positioning
        # Create an `assets` folder and put any wide and short image inside
        # Name the image `logo.png`
        self.image(os.path.join('resources', 'Biomicrosystems_logo.png'), 10, 8, 70)
        self.set_font('Arial', 'B', 11)
        self.cell(self.WIDTH - 80)
        self.cell(60, 12, 'Reporte General - '+datetime.datetime.now().strftime("%m-%d-%Y  %H:%M") , 0, 0, 'R')
        self.ln(20)
        
    def footer(self):
        # Page numbers in the footer
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.set_text_color(128)
        self.cell(0, 10, 'Pagina ' + str(self.page_no()), 0, 0, 'C')

    def save_plots(self, global_df, freq, resample):
        # Make and save plots for every fermenter in global_df
        f_number = global_df.columns.get_level_values(0).unique().str.contains('f').sum()
        for i in range(f_number):
            plot_fermenter_complete(i+1, global_df, freq, resample)
        
        # Get list of images paths
        img_paths = glob.glob(os.path.join('data', 'ferm_current_state','*'))
        img_paths = [img_paths[i:i + 2] for i in range(0, len(img_paths), 2)]
        return img_paths

    def page_body(self, images):
        # Determine how many plots there are per page and set positions
        # and margins accordingly
        if len(images) == 3:
            self.image(images[0], 15, 25, self.WIDTH - 30)
            self.image(images[1], 15, self.WIDTH / 2 + 5, self.WIDTH - 30)
            self.image(images[2], 15, self.WIDTH / 2 + 90, self.WIDTH - 30)
        elif len(images) == 2:
            self.image(images[0], 15, 25, self.WIDTH - 30)
            self.image(images[1], 15, self.HEIGHT // 2 + 7, self.WIDTH - 30)
        else:
            self.image(images[0], 15, 25, self.WIDTH - 30)
            
    def print_page(self, images):
        # Generates the report
        self.add_page()
        self.page_body(images)

# FIXME: Image generation and loadiong is really really slow right now
def make_report(global_df, freq, resample):
    pdf_doc = PDF() # Create pdf class
    img_paths = pdf_doc.save_plots(global_df, freq, resample) # Make and save plots for each fermenter
    # Iterate to print pages
    for elem in img_paths:
        print(elem)
        pdf_doc.print_page(elem)

    pdf_doc.output('Reporte_general.pdf', 'F')

