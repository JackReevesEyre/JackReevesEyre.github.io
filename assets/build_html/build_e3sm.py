"""Builds the E3SM research page. 
"""

from web_page import WebPage

def main():
    content = get_unique_content()
    page = WebPage('../../e3sm.html',
                   'E3SM Ocean-Atmosphere Interactions | Jack Reeves Eyre',
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
												<h2>Ocean-Atmopshere Interactions in E3SM</h2>
												<p>Turbulence in the atmosphere; stratification in the ocean</p>
											</header>

											<span class="image featured"><img src="images/DiffComparison_RegionMap_LHFLX_DJF_conserve.png" alt=""/><figcaption>The difference, between two E3SM runs, of wintertime latent heat flux (a measure of evaporation) over the Gulf Stream. One model run uses the UA surface flux algorithm; the other uses the E3SM default. The run with UA results in less evaporation.</figcaption></span>

											<p>I spent a large part of my PhD working with the Department of Energy's Energy Exascale Earth System Model (E3SM). Before the first official release of E3SM I looked into ocean density stratification in tropical Pacific, helping to understand and improve the model's representation of El Ni&ntilde;o. This led an investigation of barrier layers in E3SM and other coupled models. Barrier layers exist where a layer of relatively warm, salty water sits vertically between warm, fresh surface waters and the thermocline, insulating the surface from cooling effects of the colder thermocline waters. The concept was first recognized around 1990, having been observed in the tropical western Pacific in several investigations in the 1980s. Since that time, they have been observed in many other parts of the world's oceans. While the formation mechanisms vary among regions, rainfall (and rainfall gradients) are often involved. The goals of our study (published in Geophysical Research Letters) were to provide the first global view of model barrier layer represntation, and to investigate links between model precipitation biases and barrier layers. We found that E3SM generally had barrier layers in the right places, but not necessarily with the correct thickness. The thickness biases were related both to atmosphere model biases (e.g., precipitation) and ocean model biases, depending on the region.</p>
											<p>As a parallel contribution to the development of E3SM, we implemented and tested two alternative bulk flux algorithms in E3SM. Bulk flux algorithms are used to calculate the exchange of heat, mass and momentum between the atmosphere and ocean. It is common to use a "set and forget" approach to this part of a climate model, but we compared two alternatives - "UA" and "COARE" - with the default algorithm used in E3SM version 1. We found the effects to be far reaching - from the top of the atmosphere right down to the ocean interior. We published our results in Frontiers in Marine Science, and we also contributed to an <a href="https://e3sm.org/e3sm-probes-uncertainties-in-ocean-surface-flux-algorithms/">E3SM Newsletter story</a> on the research.</p>

											<h3>Publications</h3>
											
											<p><i class="ai ai-open-access ai-2x"></i>  Hsu, C.-W., C. A. DeMott, M. D. Branson, J. E. J. Reeves Eyre, & X. Zeng, 2022: Ocean surface flux algorithm effects on tropical Indo-Pacific intraseasonal precipitation. Geophysical Research Letters, 49, e2021GL096968, <a href="https://doi.org/10.1029/2021GL096968" target="_blank">https://doi.org/10.1029/2021GL096968</a>.</p>
											
											<p><i class="ai ai-open-access ai-2x"></i>  Reeves Eyre, J. E. J., X. Zeng, and K. Zhang, 2021: Ocean Surface Flux Algorithm Effects on Earth System Model Energy and Water Cycles. Front. Mar. Sci., 8, <a href="https://doi.org/10.3389/fmars.2021.642804" target="_blank">https://doi.org/10.3389/fmars.2021.642804</a>.</p>

											<p>Reeves Eyre, J. E. J., L. V. Roekel, X. Zeng, M. A. Brunke, and J.-C. Golaz, 2019: Ocean Barrier Layers in the Energy Exascale Earth System Model. Geophysical Research Letters, 46, 8234–8243, <a href="https://doi.org/10.1029/2019GL083591" target="_blank">https://doi.org/10.1029/2019GL083591</a>. <br>[see also <a href="https://repository.arizona.edu/handle/10150/634600" target="_blank">https://repository.arizona.edu/handle/10150/634600</a>]</p>

										</article>

								</div>
							</div>
							<div class="col-4 col-12-narrower">
								<div id="sidebar">

									<!-- Sidebar -->

										<section>
											<h3>Links</h3>
											<ul class="links">
											  <li><a href="https://e3sm.org/">E3SM</a></li>
											  <li><a href="https://agupubs.onlinelibrary.wiley.com/doi/toc/10.1002/(ISSN)2169-8996.ENERGY1">AGU Special Collection</a></li>
											  <li><a href="https://www.frontiersin.org/research-topics/12257/energy-water-and-carbon-dioxide-fluxes-at-the-earths-surface#articles"><i>Frontiers</i> research topic</a></li>
											  
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
