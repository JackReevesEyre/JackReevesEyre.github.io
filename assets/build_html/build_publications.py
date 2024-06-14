"""Builds the publications page. 
"""

from web_page import WebPage

def main():
    content = get_unique_content()
    page = WebPage('../../publications.html',
                   'Publications | Jack Reeves Eyre',
                   'publications',
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
												<h2>Publications</h2>
											</header>
											
											<p><i class="ai ai-open-access ai-2x"></i>  Reeves Eyre, J. E. J., M. F. Cronin, D. Zhang, E. J. Thompson, C. W. Fairall, and J. B. Edson, 2023: Saildrone Direct Covariance Wind Stress in Various Wind and Current Regimes of the Tropical Pacific. J. Atmos. Oceanic Technol., 40, 503–517, <a href="https://doi.org/10.1175/JTECH-D-22-0077.1" target="_blank">https://doi.org/10.1175/JTECH-D-22-0077.1</a>.</p>
											
											<p><i class="ai ai-open-access ai-2x"></i>  Hsu, C.-W., C. A. DeMott, M. D. Branson, J. E. J. Reeves Eyre, & X. Zeng, 2022: Ocean surface flux algorithm effects on tropical Indo-Pacific intraseasonal precipitation. Geophysical Research Letters, 49, e2021GL096968, <a href="https://doi.org/10.1029/2021GL096968" target="_blank">https://doi.org/10.1029/2021GL096968</a>.</p>

											<p>Zeng, X., J. E. J. Reeves Eyre, R. D. Dixon, and J. Arevalo, 2021: Quantifying the Occurrence of Record Hot Years Through Normalized Warming Trends. Geophysical Research Letters, 48, e2020GL091626, <a href="https://doi.org/10.1029/2020GL091626" target="_blank">https://doi.org/10.1029/2020GL091626</a>.</p>

											<p><i class="ai ai-open-access ai-2x"></i>  Reeves Eyre, J. E. J., X. Zeng, and K. Zhang, 2021: Ocean Surface Flux Algorithm Effects on Earth System Model Energy and Water Cycles. Front. Mar. Sci., 8, <a href="https://doi.org/10.3389/fmars.2021.642804" target="_blank">https://doi.org/10.3389/fmars.2021.642804</a>.</p>

											<p>Reeves Eyre, J. E. J. R., and X. Zeng, 2021: The Amazon Water Cycle: Perspectives from Water Budget Closure and Ocean Salinity. Journal of Climate, 34, 1439–1451, <a href="https://doi.org/10.1175/JCLI-D-20-0309.1" target="_blank">https://doi.org/10.1175/JCLI-D-20-0309.1</a>.</p>


											<p>Brunke, M. A., P.-L. Ma, J. E. J. Reeves Eyre, P. J. Rasch, A. Sorooshian, and X. Zeng, 2019: Subtropical Marine Low Stratiform Cloud Deck Spatial Errors in the E3SMv1 Atmosphere Model. Geophysical Research Letters, 46, 12598–12607, <a href="https://doi.org/10.1029/2019GL084747" target="_blank">https://doi.org/10.1029/2019GL084747</a>. <br>[see also <a href="https://repository.arizona.edu/handle/10150/636264" target="_blank">https://repository.arizona.edu/handle/10150/636264</a>]</p>

											<p>Reeves Eyre, J. E. J., L. V. Roekel, X. Zeng, M. A. Brunke, and J.-C. Golaz, 2019: Ocean Barrier Layers in the Energy Exascale Earth System Model. Geophysical Research Letters, 46, 8234–8243, <a href="https://doi.org/10.1029/2019GL083591" target="_blank">https://doi.org/10.1029/2019GL083591</a>. <br>[see also <a href="https://repository.arizona.edu/handle/10150/634600" target="_blank">https://repository.arizona.edu/handle/10150/634600</a>]</p>

											<p><i class="ai ai-open-access ai-2x"></i>  Golaz, J.-C., and Coauthors, 2019: The DOE E3SM Coupled Model Version 1: Overview and Evaluation at Standard Resolution. Journal of Advances in Modeling Earth Systems, 11, 2089–2129, <a href="https://doi.org/10.1029/2018MS001603" target="_blank">https://doi.org/10.1029/2018MS001603</a>.</p>

											<p><i class="ai ai-open-access ai-2x"></i>  Brunke, M. A., and Coauthors, 2018: Evaluation of the atmosphere–land–ocean–sea ice interface processes in the Regional Arctic System Model version 1 (RASM1) using local and globally gridded observations. Geoscientific Model Development, 11, 4817–4841, <a href="https://doi.org/10.5194/gmd-11-4817-2018" target="_blank">https://doi.org/10.5194/gmd-11-4817-2018</a>.</p>

											<p><i class="ai ai-open-access ai-2x"></i>  Reeves Eyre, J. E. J., and X. Zeng, 2017: Evaluation of Greenland near surface air temperature datasets. The Cryosphere, 11, 1591–1605, <a href="https://doi.org/10.5194/tc-11-1591-2017" target="_blank">https://doi.org/10.5194/tc-11-1591-2017</a>.</p>

											<p>Kendon, M., J. Eyre, and J. Penman, 2015: Absence of cold spells during the UK’s stormy winter of 2013/2014. Weather, 70, 51–52, <a href="https://doi.org/10.1002/wea.2348" target="_blank">https://doi.org/10.1002/wea.2348</a>.</p>
											
											<p>Boutle, I. A., J. E. J. Eyre, and A. P. Lock, 2014: Seamless Stratocumulus Simulation across the Turbulent Gray Zone. Mon. Wea. Rev., 142, 1655–1668, <a href="https://doi.org/10.1175/MWR-D-13-00229.1" target="_blank">https://doi.org/10.1175/MWR-D-13-00229.1</a>.</p>
											
										</article>

								</div>
							</div>
							<div class="col-4 col-12-narrower">
								<div id="sidebar">

									<!-- Sidebar -->

										<section>
											<p>There may be a more up to date list:</p>
											<footer>
												<a href="https://scholar.google.com/citations?user=ddr5XFQAAAAJ&hl=en" target="_blank" class="button">Google Scholar</a>
											</footer>
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
