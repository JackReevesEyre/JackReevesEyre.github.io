"""Builds the website main (index) page. 
"""

from web_page import WebPage

def main():
    content = get_unique_content()
    index = WebPage('../../index.html',
                    'Jack Reeves Eyre',
                    'index',
                    content)
    index.build_web_page()
    return


def get_unique_content() -> str:
    """Gets this page's unique content.

    Arguments:
        None
    Returns:
        The content in a single string.
    """
    txt = """

				<section class="wrapper style1">
					<div class="container">
						<div class="row gtr-200">
							<section class="col-3 col-12-narrower">
								<div class="box highlight">
									<i class="icon solid major fa-graduation-cap"></i>
									<h3>Education</h3>
									<p>I hold a PhD in hydrometeorology from the University of Arizona and a BA in astrophysics from the University of Cambridge</p>
								</div>
							</section>
							<section class="col-3 col-12-narrower">
								<div class="box highlight">
									<i class="icon solid major fa-university"></i>
									<h3>Position</h3>
									<p>I'm a meteorologist/oceanographer specializing in air-sea interactions</p>
								</div>
							</section>
							<section class="col-3 col-12-narrower">
								<div class="box highlight">
									<i class="icon solid major fa-signature"></i>
									<h3>Name</h3>
									<p>My name is kinda complicated: "Jack" is my first/given name and "Reeves Eyre" is my family name</p>
								</div>
							</section>
							<section class="col-3 col-12-narrower">
								<div class="box highlight">
									<i class="icon solid major fa-moon"></i>
									<h3>Stats</h3>
									<p>gemini<br>INFP<br>Erd&#337s #: 5<br>Bacon #: 3<br>Rossby #: 5</p>
								</div>
							</section>
						</div>
					</div>
				</section>

			<!-- Gigantic Heading -->
				<section class="wrapper style2">
					<div class="container">
						<header class="major">
							<h2>About</h2>
						</header>
						<p>I am a meteorologist and oceanographer interested in air-sea interactions. I am currently looking for my next role, and would love to find a position at the interface between scientific research and software. Until recently, I worked for Running Tide, where I developed tools to plan and quantify ocean-based carbon dioxide removal. My research areas included movement of material in the ocean, macroalgae growth, and ocean alkalinity enhancement.</p>
						<p>Before this, I was a research scientist with ERT, based at NOAA's Climate Prediction Center. I was involved in projects on ocean monitoring, and simulation experiments using Earth system models and data assimilation systems. Previously, I was a postdoctoral scholar at the Cooperative Institute for Climate Ocean and Ecosystem Studies (University of Washington) and NOAA Pacific Marine Environmental Laboratory. I worked with Meghan Cronin and Dongxiao Zhang on direct covariance fluxes from Saildrone uncrewed vehicles. From 2015 to 2020 I was a graduate student in Xubin Zeng's research group at the University of Arizona. From 2009 to 2014, I worked at the Met Office (Exeter, UK), first as a weather forecaster then as a climate scientist.</p>
						<p>I am a fan of open science and try to make my research output as accesible as possible --- papers, data and code. A lot of that is linked through this website, but if you can't see something, please ask. I like learning about and trying out new tools and techniques. When not hunched over my laptop, I enjoy cooking, eating, reading, and complaining about my bad back. Given the opportunity, I also like spending time outdoors. </p>
					</div>
				</section>

"""
    return txt
    

if __name__ == "__main__":
    main()
