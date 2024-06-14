"""Builds the REPLACE page. 
"""

from web_page import WebPage

def main():
    content = get_unique_content()
    # REPLACE THE ARGUMENTS HERE:
    # 'index' can be replaced by any of
    # ['index', 'research', 'publications', 'cv', 'misc']
    page = WebPage('../../index.html',
                   'Jack Reeves Eyre',
                   'index',
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
REPLACE THIS STRING
"""
    return txt
    

if __name__ == "__main__":
    main()
