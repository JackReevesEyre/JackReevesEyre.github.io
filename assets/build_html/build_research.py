"""Builds the research page. 
"""

from web_page import WebPage

def main():
    content = get_unique_content()
    page = WebPage('../../research.html',
                   'Research | Jack Reeves Eyre',
                   'research',
                   content)
    page.build_web_page()
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
						<div class="row">
							<section class="col-6 col-12-narrower">
								<div class="box post">
									<a href="./ocean_diurnal_cycle.html" class="image left"><img src="images/pexels-photo-2775196.jpeg" alt="" /></a>
									<div class="inner">
										<a href="./ocean_diurnal_cycle.html"><h3>Ocean Diurnal Cycle</h3></a>
										<p>Understanding the diurnal variation of the ocean and atmosphere.</p>
									</div>
								</div>
							</section>
							<section class="col-6 col-12-narrower">
								<div class="box post">
									<a href="./saildrone.html" class="image left"><img src="images/saildrone.jpg" alt="" /></a>
									<div class="inner">
										<a href="./saildrone.html"><h3>Saildrone Surface Fluxes</h3></a>
										<p>Verifying saildrones' ability to make direct covariance flux observations.</p>
									</div>
								</div>
							</section>
						</div>
						<div class="row">
							<section class="col-6 col-12-narrower">
								<div class="box post">
									<a href="./e3sm.html" class="image left"><img src="images/pexels-rafael-paul-4797130_square.jpg" alt="" /></a>
									<div class="inner">
										<a href="./e3sm.html"><h3>Ocean-Atmosphere Interactions in E3SM</h3></a>
										<p>Quantifying surface flux algorithm sensitivity and upper ocean stratification in the Energy Exascale Earth System Model.</p>
									</div>
								</div>
							</section>
							<section class="col-6 col-12-narrower">
								<div class="box post">
									<a href="#" class="image left"><img src="images/pexels-sergio-souza-6793564.jpg" alt="" /></a>
									<div class="inner">
										<a href="#"><h3>Amazon Water Cycle</h3></a>
										<p>Using water budget closure and ocean salinity to tell us about the water cycle of the Amazon River.</p>
									</div>
								</div>
							</section>
						</div>
						<div class="row">
							<section class="col-6 col-12-narrower">
								<div class="box post">
									<a href="#" class="image left"><img src="images/pexels-magic-k-6730626.jpg" alt="" /></a>
									<div class="inner">
										<a href="#"><h3>Greenland Air Temperature</h3></a>
										<p>Evaluating how reanalyses, CMIP5 models and other datasets portray patterns and trends in air temperature over the Greenland Ice Sheet.</p>
									</div>
								</div>
							</section>
						</div>
					</div>
				</section>

"""
    return txt
    

if __name__ == "__main__":
    main()
