"""Builds the Rossby numbers page. 
"""

from web_page import WebPage

def main():
    content = get_unique_content()
    page = WebPage('../../rossby_number.html',
                   'Rossby numbers | Jack Reeves Eyre',
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
												<h2>What's your Rossby number?</h2>
												<p>And what do Natalie Portman and Richard Feynman have in common?</p>
											</header>

											<span><img src="images/natalie-portman.jpg" height=400 alt=""/><img src="images/feynman_caltech.jpg" height=400 alt=""/><figcaption>Image credits: Bellazon; Caltech Archives.</figcaption></span>

											<p>As a teenage mega-nerd, I looked upon physicist Richard Feynman as a kind of rockstar, up there with the likes of Liam Gallagher. He was obviously a hugely successful researcher, but he was also a great explainer, and had an intriguing public life beyond theoretical physics (think bongo playing and Pasadena cocktail parties). In the refined social circles of undergraduate mathetmatics, some even more niche figures were just as cool. Paul Erd&#337s was one of them. The stories of this couch-surfing, problem-solving machine were legendary. (From a more middle-aged perspective, he sounds like simultaneously the best and worst house guest.) Erd&#337s was a prolific paper writer, a fact which led to the concept of the <a href="https://en.wikipedia.org/wiki/Erd%C5%91s_number">Erd&#337s number</a>.</p>
											<p>The idea of the Erd&#337s number is that anyone who wrote a paper with Erd&#337s gets a 1; anyone who collaborated with an Erd&#337s number 1 author (but not with Erd&#337s himself) gets a 2; and so on. It's a similar idea to six degrees of separation, and the related six degrees of Kevin Bacon. For anyone who has publised in the mathematical literature, you can use the <a href="https://mathscinet.ams.org/mathscinet/freetools/collab-dist">American Mathematical Society's calculator</a> to see your own Erd&#337s number. And you can use a <a href="https://www.oracleofbacon.org/">similar tool</a> to get the Bacon number of anyone who has worked on a major TV or movie production. A few special people have done both of these things, and have an Erd&#337s-Bacon number: the sum of their Erd&#337s number and their Bacon number. Membership in this special club is what Natalie Portman and Richard Feynman share. Their Erd&#337s-Bacon numbers are 7 (5+2) and 6 (3+3) respectively.</p>
											<p>As a meteorologist and oceanographer, I regularly come across quantities named after Carl-Gustaf Rossby. The American Meteorological Society (the other AMS) glossary has <a href="https://glossary.ametsoc.org/wiki/Special:Search?search=rossby&fulltext=Search+full+text">10s of results</a> for Rossby. So, naturally, I see an opportunity to create a new one by calculating the Rossby number of researchers as their collaboration distance from Rossby. Surprisingly, given how much influence he had on the field, Rossby was, in comparison to Erd&#337s, neither particularly prolific nor particularly collaborative. Erd&#337s has papers and co-authors numbered in the hundreds, while for Rossby, those numbers are in the tens.</p>
											<p>One consequence of Rossby's publication history is that it takes a bit more detective work to calculate Rossby's collaboration distances. Rossby can be linked to the main body of mathematical literature by a chain of 3 to John von Neumann (Rossby - Bolin - Charney - von Neumann). von Neumann himself has an Erd&#337s number of 3, so Rossby's Erd&#337s number is (at most) 6. For researchers in meteorology and oceanography, a shorter route to Rossby is likely to be via University of Washington professor John Wallace (Rossby - Starr - Wallace) who, like Erd&#337s, seems to have publications and collaborators numbered in the hundreds.</p>
											<p>Unfortunately, I can't find a reliable tool to quickly calculate researchers' Rossby numbers. My impression is that many of the journals that meteorologists and oceanographers publish in are not included in the American Mathematical Society's calculator. Using <a href="https://www.semanticscholar.org/">Semantic Scholar</a>, I calculated my own Rossby number to be 5 (Rossby - Starr - Wallace - Battisti - Rasch - Reeves Eyre). I also have an Erd&#337s number of 5 (Erd&#337s - Moran - Yavneh - McWilliams - Van Roekel - Reeves Eyre). Somewhat unexpectedly, my Bacon number is just 3, but the story behind that is best told over a beer.</p>
										</article>

								</div>
							</div>
							<div class="col-4 col-12-narrower">
								<div id="sidebar">

									<!-- Sidebar -->

										<section>
											<h3>Links</h3>
											<ul class="links">
												<li><a href="https://mathscinet.ams.org/mathscinet/freetools/collab-dist">Collaboration distance calculator</a></li>
												<li><a href="https://www.oracleofbacon.org/">Bacon number calculator</a></li>
												<li><a href="https://glossary.ametsoc.org/wiki/Welcome">Meteorology glossary</a></li>
												<li><a href="https://www.semanticscholar.org/">Semantic Scholar</a></li>
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
