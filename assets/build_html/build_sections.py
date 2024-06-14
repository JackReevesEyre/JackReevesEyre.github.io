"""Contains functions to more easily build my website.
"""
import _io
import os
import sys
import glob
import pandas as pd
import datetime


def add_doctype(file_object: _io.TextIOWrapper) -> None:
    """Adds html doc type to open file.

    Arguments:
        file_object - the file to write to.
    Returns:
        None
    """
    file_object.write('<!DOCTYPE html>\n')
    return None


def add_comment(file_object: _io.TextIOWrapper) -> None:
    """Adds html comment to open file.

    Arguments:
        file_object - the file to write to.
    Returns:
        None
    """
    txt = """
<!--
	Arcana by HTML5 UP
	html5up.net | @ajlkn
	Free for personal and commercial use under the CCA 3.0 license (html5up.net/license)
-->
"""
    file_object.write(txt)
    return None


def add_html_tag(file_object: _io.TextIOWrapper) -> None:
    """Adds html tag to open file.

    Arguments:
        file_object - the file to write to.
    Returns:
        None
    """
    file_object.write('<html>\n')
    return None


def add_html_end_tag(file_object: _io.TextIOWrapper) -> None:
    """Adds html end tag to open file.

    Arguments:
        file_object - the file to write to.
    Returns:
        None
    """
    file_object.write('</html>\n')
    return None


def add_page_head(file_object: _io.TextIOWrapper,
                  title: str) -> None:
    """Adds html doc head to open file.

    Arguments:
        file_object - the file to write to.
        title - the title of the rendered html page.
    Returns:
        None
    """
    txt=f"""
	<head>
		<title>{title}</title>
		<meta charset="utf-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no" />
		<link rel="stylesheet" href="assets/css/main.css" />
	</head>
"""
    file_object.write(txt)
    return None


def add_html_body_tag(file_object: _io.TextIOWrapper) -> None:
    """Adds html body section tag to open file.

    Arguments:
        file_object - the file to write to.
    Returns:
        None
    """
    file_object.write('        <body class="is-preload">\n')
    return None


def add_html_end_body_tag(file_object: _io.TextIOWrapper) -> None:
    """Adds html end of body section tag to open file.

    Arguments:
        file_object - the file to write to.
    Returns:
        None
    """
    file_object.write('        </body>\n')
    return None


def add_html_div_tag(file_object: _io.TextIOWrapper) -> None:
    """Adds html main section div tag to open file.

    Arguments:
        file_object - the file to write to.
    Returns:
        None
    """
    file_object.write('            <div id="page-wrapper">\n')
    return None


def add_html_end_div_tag(file_object: _io.TextIOWrapper) -> None:
    """Adds html main section end of div tag to open file.

    Arguments:
        file_object - the file to write to.
    Returns:
        None
    """
    file_object.write('            </div>\n')
    return None


def add_header(file_object: _io.TextIOWrapper,
               current_section: str) -> None:
    """Adds header to body section in open file.

    Arguments:
        file_object - the file to write to.
        current_section - the header bar section which is highlighted.
                          Must be one of:
                          ['index', 'research', 'publications', 'cv', 'misc']
    Returns:
        None
    """
    
    basic_link = '<li>'
    current_link = '<li class="current">'
    link_dict = {sect:basic_link for sect in
                 ['index', 'research', 'publications',
                  'cv', 'misc']}
    link_dict[current_section] = current_link
        
    txt = f"""

			<!-- Header -->
				<div id="header">

					<!-- Logo -->
						<h1><a href="index.html" id="logo">Jack Reeves Eyre</a></h1>

					<!-- Nav -->
						<nav id="nav">
							<ul>
								{link_dict['index']}<a href="index.html">Home</a></li>
								{link_dict['research']}<a href="research.html">Research</a></li>
								{link_dict['publications']}<a href="publications.html">Publications</a></li>
								{link_dict['cv']}<a href="CV-page.html">CV</a></li>
								{link_dict['misc']}<a href="miscellany.html">Miscellany</a></li>
							</ul>
						</nav>

				</div>

"""
    file_object.write(txt)
    return None


def add_banner(file_object: _io.TextIOWrapper) -> None:
    """Adds banner to body section in open file.

    Arguments:
        file_object - the file to write to.
    Returns:
        None
    """
    txt = """
				<section id="banner">
					<header>
						<!-- Icons -->
						<ul class="icons">
							<li><a href="https://scholar.google.com/citations?user=ddr5XFQAAAAJ&hl=en" class="ai ai-google-scholar ai-3x" target="_blank"><span class="label"></span></a></li>
							<li><a href="https://github.com/JackReevesEyre" class="icon brands fa-github" target="_blank"><span class="label"></span></a></li>
							<li><a href="https://bitbucket.org/jack_eyre/" class="icon brands fa-bitbucket" target="_blank"><span class="label"></span></a></li>
							<li><a href="https://orcid.org/0000-0001-8893-9810" class="ai ai-orcid ai-3x" target="_blank"><span class="label"></span></a></li>
							<li><a href="https://www.researchgate.net/profile/Jack-Reeves-Eyre" class="ai ai-researchgate ai-3x" target="_blank"><span class="label"></span></a></li>
							<li><a href="https://www.linkedin.com/in/jack-reeves-eyre/" class="icon brands fa-linkedin-in" target="_blank"><span class="label"></span></a></li>
						</ul>
					</header>
				</section>
"""
    file_object.write(txt)
    return None


def add_footer(file_object: _io.TextIOWrapper) -> None:
    """Adds header to body section in open file.

    Arguments:
        file_object - the file to write to.
    Returns:
        None
    """
    txt = """
				<div id="footer">
					<div class="container">
						<div class="row">
							<section class="col-3 col-6-narrower col-12-mobilep">
								<h3>Links</h3>
								<ul class="links">
									<li><a href="https://www.runningtide.com/" target="_blank">Running Tide</a></li>
									<li><a href="https://www.cpc.ncep.noaa.gov" target="_blank">CPC</a></li>
									<li><a href="https://www.weather.gov/" target="_blank">NWS</a></li>
								</ul>
							</section>
							<section class="col-3 col-6-narrower col-12-mobilep">
								<h3> </h3>
								<ul class="links">
								</ul>
							</section>
							<section class="col-6 col-12-narrower">
								<h3>Get In Touch</h3>
								<p>jack [dot] reeveseyre [at] gmail [dot] com
								</p>
							</section>
						</div>
					</div>

					<!-- Icons -->
						<ul class="icons">
							<li><a href="https://scholar.google.com/citations?user=ddr5XFQAAAAJ&hl=en" class="ai ai-google-scholar ai-3x" target="_blank"><span class="label"></span></a></li>
							<li><a href="https://github.com/JackReevesEyre" class="icon brands fa-github" target="_blank"><span class="label"></span></a></li>
							<li><a href="https://bitbucket.org/jack_eyre/" class="icon brands fa-bitbucket" target="_blank"><span class="label"></span></a></li>
							<li><a href="https://orcid.org/0000-0001-8893-9810" class="ai ai-orcid ai-3x" target="_blank"><span class="label"></span></a></li>
							<li><a href="https://www.researchgate.net/profile/Jack-Reeves-Eyre" class="ai ai-researchgate ai-3x" target="_blank"><span class="label"></span></a></li>
							<li><a href="https://www.linkedin.com/in/jack-reeves-eyre/" class="icon brands fa-linkedin-in" target="_blank"><span class="label"></span></a></li>
						</ul>

					<!-- Copyright -->
						<div class="copyright">
							<ul class="menu">
								<li>&copy; Jack Reeves Eyre. All rights reserved</li><li>Design: <a href="http://html5up.net">HTML5 UP</a></li>
							</ul>
						</div>

				</div>
"""
    file_object.write(txt)
    return None


def add_scripts(file_object: _io.TextIOWrapper) -> None:
    """Adds header to body section in open file.

    Arguments:
        file_object - the file to write to.
    Returns:
        None
    """
    txt = """
			<script src="assets/js/jquery.min.js"></script>
			<script src="assets/js/jquery.dropotron.min.js"></script>
			<script src="assets/js/browser.min.js"></script>
			<script src="assets/js/breakpoints.min.js"></script>
			<script src="assets/js/util.js"></script>
			<script src="assets/js/main.js"></script>
"""
    file_object.write(txt)
    return None
