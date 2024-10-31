"""Builds the brackets page. 
"""

from web_page import WebPage

def main():
    content = get_unique_content()
    # REPLACE THE ARGUMENTS HERE:
    # 'index' can be replaced by any of
    # ['index', 'research', 'publications', 'cv', 'misc']
    page = WebPage('../../brackets.html',
                   'Brackets | Jack Reeves Eyre',
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
												<h2>Parenthetic (antithetic) brackets are good (bad) - discuss.</h2>
												<p>And does your opinion depend on how you read?</p>
											</header>

											<span><img src="images/dickens.png" height=400 alt=""/><img src="images/dickens_flip.png" height=400 alt=""/><figcaption><span class="caption">Robert Hindry Mason, photograph of Charles Dickens (1860s).</span><br>
              <span class="attribution"><a class="source" href="https://commons.wikimedia.org/wiki/File:Charles_Dickens_portrait_c1860s_restore.png">wikimedia/nationalmediamusuem</a>, <a class="license" href="http://creativecommons.org/licenses/by/4.0/">CC BY</a></figcaption></span><br>

											<p>I have a confession to make. I've kept it buried deep inside for a long time. It sometimes fills me with shame, especially as someone whose career involves quickly assimilating complex, technical information. I don't know how to skim read.</p>

											<p>Reading, for me, involves my internal monologue focusing on each and every word, in sequence. Like reading out loud, but silently (and without moving my lips... especially when on public transport). The Internet provides an almost infinite number of resources on how to skim and scan text. These all seem to involve some combination of: 
											        <ol>
											                <li>Just reading a subset of the text, e.g., the first paragraph of the introduction.
											                <li>Just looking at, but not really reading, a random scattering of words across a page.
											        </ol>
											There are some some peddlers of snake oil that promise you can, say, understand macroeconomics in 15 minutes by using their speed-reading strategy. But often, the goal seems to be to answer the question <i>Should I bother to properly read all of this?</i> I suppose I do actually do some of that. (As an undergraduate, with maths textbooks, the answer was almost always <i>No</i>.) And I sometimes just look at the abstract and figures in a scientific paper. However, when it comes to really understanding something, I always come back to my internal monologue reading out loud. Which brings me onto one of my pet hates in scientific writing.</p>

											<p>It is quite common, in Earth sciences at least, to see sentences like this: <i>In El Ni&ntilde;o (La Ni&ntilde;a) years, the equatorial eastern Pacific is warmer (colder) than average.</i> I call this use of brackets <i>antithetic</i>, because the contents of the brackets are the antithesis of the preceding idea. El Ni&ntilde;o is opposite to La Ni&ntilde;a, and warm is opposite to cold. (The other, presumably more common, use of brackets is parenthetic, providing supporting information, like this.)</p>

											<p>How is an internal monologue-reader supposed to read this? In the simple example given above, it might be possible to simply read the words in the order given and still parse the meaning on the first pass. But what about more complicated variations? Are we meant to mentally split it into separate sentences? Read once without the brackets, then again with the bracketed words but without the words just in front of the brackets? That's a lot of mental gymnastics. And why write like this? Is it to save a few words, or do some writers really think this construction is clearer? My hunch is that people who like this kind of sentence construction either read differently (skim or scan?) or write differently (without reading their own sentences back to themselves, repeatedly, ad nauseam - just me?). But I'd love to hear what other readers and writers think and do.</p>

											<p>To illustrate just how absurd this style can become, here is the famous opening to Dickens' <i>A Tale of Two Cities</i> rewritten by a well-meaning geoscientist:</p>
											<blockquote>"It was the best (worst) of times, it was the age of wisdom (foolishness), it was the epoch of belief (incredulity), it was the season of Light (Darkness), it was the spring (winter) of hope (despair), we had everything (nothing) before us, we were all going direct to Heaven (the other way)..."</blockquote>

											<p>I think it's just confusing. And ugly. As for mixing parenthetic and antithetic brackets in the same paragraph or sentence... the age of foolishness indeed.</p>
										</article>

								</div>
							</div>
						</div>
					</div>
				</section>

"""
    return txt
    

if __name__ == "__main__":
    main()
