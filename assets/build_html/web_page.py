import sys
import os
import _io
from build_sections import *

class WebPage:
    
    def __init__(self,
                 filename,
                 page_title,
                 header_section,
                 unique_content):
        self.filename = filename
        self.page_title = page_title
        self.header_section = header_section
        self.unique_content = unique_content

    def build_web_page(self):
        """Builds web page using boilerplate and instance variables.
        """
        
        try:
            f = open(self.filename, 'x')
        except FileExistsError:
            sys.exit(self.filename +
                     ' already exists; move it or delete it then try again.')

        add_doctype(f)
        add_comment(f)
        add_html_tag(f)
        add_page_head(f, self.page_title)
        add_html_body_tag(f)
        add_html_div_tag(f)
        add_header(f, self.header_section)
        add_banner(f)
        #
        f.write(self.unique_content)
        #
        add_footer(f)
        add_html_end_div_tag(f)
        add_scripts(f)
        add_html_end_body_tag(f)
        add_html_end_tag(f)
        
        f.close()
        
        return
