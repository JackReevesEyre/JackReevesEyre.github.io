"""Builds the REPLACE page. 
"""

from web_page import WebPage

def main():
    content = get_unique_content()
    page = WebPage('../../sail_powered_science.html',
                   'Sail Powered Science | Jack Reeves Eyre',
                   'misc',
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
												<h2>Sail-Powered Science</h2>
												<p>Oceanographic and meteorological research conducted on sailboats</p>
											</header>

											<p>Even in the age of Earth Observing satellites, research in oceanography and marine meteorology is still heavily dependent on ships. Maintenance of moored buoys, detailed process studies, and sub-surface measurements have tended to require large ships, with large crews, large fuel tanks, and large budgets. But with advances in sensor and communication technology, and a focus on sustainability, other options have opened up.</p>

											<p>Amongst this broadening of oceanographic research platforms, sail-powered vehicles have emerged as capable options. Of course, the history of oceanographic research, and science more broadly, is entwined with navigation of the oceans under sail. The voyages of Humboldt, Darwin, Nansen, and the Antarctic explorers of the late 19th and early 20th centuries all relied on sail. Fossil fuel-power dominates research vessels now, but sail power still has its place. Sailboats' advantage comes from being able to operate in locations and conditions that large research vessels cannot, cheaply, and with impressive endurance. The data they collect is being used for research, environmental monitoring, mapping, and more. Below is a list of some of these sail-powered science projects, grouped by <a href="#crewed">crewed</a> and <a href="#uncrewed">uncrewed</a> vessels. I'm planning to update this periodically, so would be grateful to know of others I've missed.</p>

											<div id="crewed">

											<h3>Crewed vessels</h3>

											<p><b>Ocean Research Project:</b> Founded in 2012, ORP have conducted field research on ocean-ice sheet interactions, Gulf Stream circulation, ocean debris, and seabed mapping. Their 72-foot steel schooner, <i>R/V Marie Tharp</i>, can support sophisticaed sea-bed mapping equipment, launch and recovery of uncrewed vehicles, and onboard lab work. Founder Matt Rutherford and science director Nicole Trenholm have an impressive track record of, in their words, blending modern technology with timeless seafaring efficiency. <a href="https://www.oceanresearchproject.org/">Read more.</a></p>

											<p><b>Old Weather:</b> Log books from many working sail ships have been digitized by the <a href="https://www.oldweather.org/">Old Weather</a> project. Led by Philip Brohan and the late Kevin Wood, volunteers have focussed on whaling ships, military voyages to the Arctic, and World War II logs. This trove of data has helped improve records of sea ice and models of pre-20th century atmospheric circulation.</p>

											<p><b>Blue Observer:</b> Blue Observer, with their 26-meter (84-foot) ex-racing sailboat <i>Iris</i>, deployed 95 Argo floats during a 17500 nautical mile voyage in 2021 and 2022, while burning only 700 l (less then 200 US gallons) of diesel. They also collected samples of micro-organisms from both water and air. <a href="https://blue-observer.com/?lang=en">Read more.</a></p>

											<p><b>Fondation Tara Ocean:</b> The 36-meter (118-foot) <i>Tara</i> was designed for polar regions, but has been engaged in research from equator to poles for most of the last two decades. Data collected during multiple expedition phases have been used in scientific publications in meteorology, ecosystem science, and biogeochemistry. More recently, the foundation has built a new drifting ice station for deployment in the Arctic Ocean. <a href="https://fondationtaraocean.org/en/home/">Read more.</a></p>

											<p><b>Lady Amber:</b> Schooner <i>Lady Amber</i> was chartered to support operations during the SPURS-2 (Salinity Processes in the Upper ocean Regional Study 2) in the eastern tropoical Pacific. From 2016 to 2018, <i>Lady Amber</i> conducted eight cruises to the study's central research mooring, assisting with deployment, repositioning, and maintenance of drifting platforms, as well as collecting under-way data. Read more about <i>Lady Amber</i> and SPURS-2 in this <a href="https://tos.org/oceanography/%20article/novel-and-flexible-approach-to-access-the-open-ocean-uses-of-sailing">Oceanography journal paper</a>.</p>

											<p><b>The Ocean Race:</b> Descended from the Whitbread Race and Volvo Ocean Race, The Ocean Race runs every four years, with shorter European and trans-Atlantic events in between. Boats racing in the events make continuous underway physcial and biogeochemical measurements (available in this <a href="https://theoceanracescience.com/2023/">online viewer</a>), and collect water samples to monitor microplastics. They also deploy drifting buoys and Argo floats, which can be particularly valuable in data sparse, infrequently traveled regions like the Southern Ocean. Read more on The Ocean Race <a href="https://www.theoceanrace.com/en/racing-for-the-ocean">website</a> and this Global Ocean Observing System <a href="https://goosocean.org/news/sport-and-science-how-the-ocean-race-helps-advance-ocean-and-climate-knowledge/">article</a>.</p>

											</div>

											<div id="uncrewed">

											<h3>Uncrewed vessels</h3>

											<p><b>Oshen:</b> Oshen's <i>C-Star</i> platforms are small, relatively simple autonomous sailboats designed to be deployed in large fleets or "constellsations". This focus on simplicity, robustness, and large sample sizes could be a highly valuable approach in ocean research. They have sensor payloads focusing on basic meteorological and oceanographic physical variables, and on passive acoustic monitoring of marine mammals and fisheries. Since Oshen's inception in 2021, C-Stars have been deployed in a constellation of 50, and have collected data from a category-5 hurricane. <a href="https://www.oshendata.com/">Read more.</a></p>

											<p><b>Saildrone:</b> One of the most well-known companies in the autonomous ocean vehicle industry, Saildrone have been collecting meteorolgical, oceanographic, and fisheries data since 2015. Through a highly productive partnership with NOAA, especially at the Pacific Marine Environmental Laboratory, Saildrone have been used in regional climate studies, fisheries surveys, and routine climate monitoring. In fact, my personal experience <a href="https://journals.ametsoc.org/view/journals/atot/40/4/JTECH-D-22-0077.1.xml">demonstrating</a> that Saildrones could provide reliable direct covariance wind stress data is what initiated the idea for this Sail-Powered Science blog post. Largely gap-free, months-long datasets of 20 Hz wind measurements are a powerful demonstration of the robust endurance of sail-powered USVs. It is unclear how Saildrone's increasing focus on lethal military applications will affect their scientific use.</p>

											<p><b>Sailbuoy:</b> Available with a range of sensor packages for applications in physical and biological oceanography, Sailbuoy USVs are another example of relatively small, simple data collection platforms. Sailbuoys have crossed the Atlantic, operated at high latitudes in the Arctic, and racked up thousands of miles at sea. <a href="https://sailbuoy.no/">Read more.</a></p>

											</div>

											<h3>Notes</h3> 

											<p>In addition to the above, there are many educational and citizen science projects doing valuble work based on sailboats. In selecting the above, I have focused on projects that collect data for well-constrained research applications or that contribute to established, operational weather and climate monitoring programs. Everything in this post is my own personal opinion and does not represent the views of my employer or affiliated organizations.</p>

										</article>

								</div>
							</div>
							<div class="col-4 col-12-narrower">
								<div id="sidebar">

									<!-- Sidebar -->

										<section>
											<span><img src="images/Amundsen-Fram.jpeg" width=400 alt=""/><figcaption><i>Fram</i>, originally built for explorer Fridtjof Nansen, under sail in Antarctica. Image credits: photolib.noaa.gov via https://commons.wikimedia.org/w/index.php?curid=1871.</figcaption></span><br>
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
