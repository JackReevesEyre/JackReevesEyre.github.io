"""Builds the ocean diurnal cycle research page. 
"""

from web_page import WebPage

def main():
    content = get_unique_content()
    # REPLACE THE ARGUMENTS HERE:
    # 'index' can be replaced by any of
    # ['index', 'research', 'publications', 'cv', 'misc']
    page = WebPage('../../ocean_diurnal_cycle.html',
                   'Jack Reeves Eyre',
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
												<h2>Ocean Diurnal Cycle</h2>
												<p>Diurnal variation of the upper ocean and lower atmosphere</p>
											</header>

											<p>Coming soon.</p>

										</article>

								</div>
							</div>
							<div class="col-4 col-12-narrower">
								<div id="sidebar">

									<!-- Sidebar -->

										<section>
											<span><img src="images/sst_dtr_maps.jpg" width=400 alt=""/><figcaption>SST diurnal range.</figcaption></span><br>
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
