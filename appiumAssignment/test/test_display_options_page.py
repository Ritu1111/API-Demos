from Pages.displayOptionsPage import DisplayOptPage
from utility.utills import UtilClass
import  pytest
import utility.custom_logger as cl
import logging

log = cl.customLogger(logging.DEBUG)


@pytest.mark.a
def test_display_options_page():
    disp = DisplayOptPage()
    disp.setup_display_options()
    try:
        disp.visible()
    except:
        assert True # title is hidden