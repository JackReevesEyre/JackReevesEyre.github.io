"""Builds the CV page. 
"""

from web_page import WebPage

def main():
    content = get_unique_content()
    page = WebPage('../../CV-page.html',
                   'CV | Jack Reeves Eyre',
                   'cv',
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

				<p align="center"><iframe src="images/CV_JReevesEyre_31Oct2024.pdf" width="80%" height="700px">
                                </iframe></p>


"""
    return txt
    

if __name__ == "__main__":
    main()
