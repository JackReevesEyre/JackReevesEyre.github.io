"""Builds the Saildrone page. 
"""

from web_page import WebPage

def main():
    content = get_unique_content()
    # REPLACE THE ARGUMENTS HERE:
    # 'index' can be replaced by any of
    # ['index', 'research', 'publications', 'cv', 'misc']
    page = WebPage('../../saildrone.html',
                   'Saildrone Surface Fluxes | Jack Reeves Eyre',
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
						<div class="row gtr-200">
							<div class="col-8 col-12-narrower">
								<div id="content">

									<!-- Content -->

										<article>
											<header>
												<h2>Saildrone Surface Fluxes</h2>
												<p>Direct covariance fluxes from autonomous surface vehicles.</p>
											</header>

											<span class="image featured"><img src="images/saildrone_large.jpg" alt=""/><figcaption>Image credit: Saildrone Inc.</figcaption></span>

											<p>Saildrone autonomous surface vehicles have the potential to greatly increase the number of direct flux observations we make each year. However, the measurement method is full of technical challenges and the results need to be carefully verified.My research with saildrones focusses on verifying the quality of direct momentum flux measurements, and using them to investigate how the atmosphere responds to sharp temperature fronts in the ocean.</p>
											<p>The atmosphere and the ocean are in a constant exchange. Momentum is exchanged when winds blow over the ocean, causing surface waves and currents. Water is exchanged through evaporation and rainfall - evaporation from the ocean is actually the major source of water vapor for the atmosphere, and also cools the ocean.  Heat is exhanged too, because the ocean is usually about 1 degree Celsius warmer than the atmosphere directly above it. Many of these exchanges - or "fluxes" - are controlled by turbulence in the atmosphere, which is notoriously difficult to measure and predict. Measurements are possible, but require high frequency (faster than 10 Hz) measurements. Over the ocean, the measurements also need to be corrected for the motion of the measurement system as it moves around on the waves.</p>
											<p>In this research, we take these high frequency measurements, calculate the momentum flux, then compare them with other momentum flux estimates to verify that they are accurate. The results can be used in a variety of applications: ongoing work looks at turbulence near sharp fronts in ocean surface temperature. The hypothesis is that there's more turbulence in the case of cool air over warm water than in the case with warm air over cool water. Saildrone direct flux measurements can help us test this.</p>

											<h3>Publications</h3>
											
											<p><i class="ai ai-open-access ai-2x"></i>  Reeves Eyre, J. E. J., M. F. Cronin, D. Zhang, E. J. Thompson, C. W. Fairall, and J. B. Edson, 2023: Saildrone Direct Covariance Wind Stress in Various Wind and Current Regimes of the Tropical Pacific. J. Atmos. Oceanic Technol., 40, 503–517, <a href="https://doi.org/10.1175/JTECH-D-22-0077.1" target="_blank">https://doi.org/10.1175/JTECH-D-22-0077.1</a>.</p>
										</article>

								</div>
							</div>
							<div class="col-4 col-12-narrower">
								<div id="sidebar">

									<!-- Sidebar -->

										<section>
											<h3>Links</h3>
											<ul class="links">
												<li><a href="https://www.saildrone.com/">Saildrone Inc.</a></li>
												<li><a href="https://pmel.noaa.gov/ocs/saildrone">NOAA OCS Saildrone Missions</a></li>
											</ul>
										</section>

								</div>
							</div>
						</div>
					</div>
				</section>

"""
    return txt
    

if __name__ == "__main__":
    main()
