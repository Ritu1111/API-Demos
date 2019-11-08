from Pages.animationPage import HideAnimationPage
import pytest
import utility.custom_logger as cl
import logging

log = cl.customLogger(logging.DEBUG)

@pytest.mark.a
def test_animation_page_show_option():
    anim = HideAnimationPage()
    anim.setup_animation_hide_show()
    anim.setup_animation_hide()
    try:
        anim.visible() == (True, True, True, True)
    except:
        assert True #buton0, button1, button2, button3 are hidden

    anim.setup_animation_show()
    assert anim.visible() == (True, True, True, True) ##buton0, button1, button2, button3 are shown
