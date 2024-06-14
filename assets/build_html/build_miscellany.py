"""Builds the miscellany page. 
"""

from web_page import WebPage

def main():
    content = get_unique_content()
    page = WebPage('../../miscellany.html',
                   'Miscellany | Jack Reeves Eyre',
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
						<div class="row">
							<section class="col-6 col-12-narrower">
								<div class="box post">
									<a href="./rossby_number.html" class="image left"><img src="images/Rossby_LCCN2016875745.jpeg" alt="" /></a>
									<div class="inner">
										<a href="./rossby_number.html"><h3>What's your Rossby number?</h3></a>
										<p>Defining yet another Rossby number, with a nod to Paul Erd&#337s and Kevin Bacon.</p>
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
