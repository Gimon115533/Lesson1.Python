import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class Search(unittest.TestCase):
    def setUp(self):
        self.drv = webdriver.Chrome("chromedriver.exe")

    def test_search(self):
        self.drv.get("https://www.yandex.ru/")
        assert 'Яндекс' in self.drv.title
        elm = self.drv.find_element_by_css_selector('#text')
        elm.send_keys('selenide')
        elm.send_keys(Keys.RETURN)
        assert 'No results found' not in self.drv.page_source
        spisok = self.drv.find_element_by_css_selector('body > div.main.serp.i-bem.main_js_inited.serp_js_inited > div.main__center > div.main__content > div.content.i-bem.content_js_inited > div.content__left > ul > li:nth-child(3) > div > div.organic__subtitle.typo.typo_type_greenurl > div.path.path_show-https.organic__path > a > b')
        assert 'selenide.org' in spisok.text
        baton_more = self.drv.find_element_by_css_selector('body > div.serp-navigation.z-index-group.z-index-group_level_8 > div > div > div.navigation__item.navigation__item_service_yes.navigation__item_name_images > div > a > span')
        baton_more.click()
        time.sleep(5)
        self.drv.switch_to.window(self.drv.window_handles[1])
        assert 'инструкция когда' in self.drv.find_element_by_css_selector('body > div.serp-header.serp-header_head-auth_yes.serp-header_yaplus_yes.serp-header_filters_light.serp-header_slide-auto-hide.serp-header_slide-hidden_no.i-bem.serp-header_js_inited > div > div.serp-header__under > div.tags.tags_carousel.tags_full-scroll.tags_cluster.tags_position_header.i-bem.header__clarification-tags.tags_js_inited > div > div.carousel__content > div > div > div.tags__group.tags__group_color_0.carousel__item > a').text
        img = self.drv.find_element_by_css_selector('div > a.serp-item__link[href*= "https%3A%2F%2Ffolderit"]')
        img.click()
        time.sleep(5)
        self.drv.switch_to.window(self.drv.window_handles[1])
        elementText = self.drv.find_element_by_css_selector('body > div.page-layout.page-layout_page_search.page-layout_layout_serp.serp-controller.serp-controller_infinite_yes.serp-controller_navigation_yes.serp-controller_complain_yes.serp-controller_prefetch_yes.serp-controller_height_full.serp-controller_vertical-shadowed.navigation-controller.pane2-controller.pane2-controller_crop_yes.pane2-controller_related-scroll-autoload.pane2-controller_preload_yes.trimmer-controller.trimmer-controller_objects_yes.incut-controller.cbir-counter.serp-counter.i-bem.navigation-controller_js_inited.page-layout_js_inited.serp-controller_page_search.serp-controller_js_inited.pane2-controller_js_inited.incut-controller_js_inited.serp-counter_js_inited.trimmer-controller_js_inited > div.pane2.pane2_color-position_yes.pane2_fullscreen_no.pane2_customized.pane2_related-scroll-autoload.pane2_direct-type_stripe.pane2_market_no.pane2_ajax-direct_yes.pane2-controller__pane.pane2-api.advice-controller.blocks-grid.i-bem.pane2-api_js_inited.pane2_flexbox_yes.pane2_js_inited.pane2_visibility_visible.blocks-grid_js_inited > div.pane2__wrapper.blocks-grid__item.blocks-grid__item_static > div.pane2__column.pane2__column_type_info.pane2__column_flexbox_yes > div.pane2__info-wrapper.pane2-sidebar > div.snippet2.snippet2_query.snippet2_favicon.pane2-sidebar__section.pane2__snippet.blocks-grid__item.blocks-grid__item_dynamic.i-bem.snippet2_js_inited > div.snippet2__query > div > div > div > a:nth-child(2)')
        assert 'Selenide' in elementText.text
        self.drv.find_element_by_css_selector('body > div.page-layout.page-layout_page_search.page-layout_layout_serp.serp-controller.serp-controller_infinite_yes.serp-controller_navigation_yes.serp-controller_complain_yes.serp-controller_prefetch_yes.serp-controller_height_full.serp-controller_vertical-shadowed.navigation-controller.pane2-controller.pane2-controller_crop_yes.pane2-controller_related-scroll-autoload.pane2-controller_preload_yes.trimmer-controller.trimmer-controller_objects_yes.incut-controller.cbir-counter.serp-counter.i-bem.navigation-controller_js_inited.page-layout_js_inited.serp-controller_page_search.serp-controller_js_inited.pane2-controller_js_inited.incut-controller_js_inited.serp-counter_js_inited.trimmer-controller_js_inited > div.pane2.pane2_color-position_yes.pane2_fullscreen_no.pane2_customized.pane2_related-scroll-autoload.pane2_direct-type_stripe.pane2_market_no.pane2_ajax-direct_yes.pane2-controller__pane.pane2-api.advice-controller.blocks-grid.i-bem.pane2-api_js_inited.pane2_flexbox_yes.pane2_js_inited.pane2_visibility_visible.blocks-grid_js_inited > div.pane2__wrapper.blocks-grid__item.blocks-grid__item_static > a > div').click()
        time.sleep(5)
        self.drv.switch_to.window(self.drv.window_handles[1])
        seah = self.drv.find_element_by_css_selector('a[href*="https://yandex.ru/search/?text=selenide"]')
        seah.click()
        time.sleep(10)
        self.drv.switch_to.window(self.drv.window_handles[0])
        spisok2 = self.drv.find_element_by_css_selector('body > div.main.serp.i-bem.main_js_inited.serp_js_inited > div.main__center > div.main__content > div.content.i-bem.content_js_inited > div.content__left > ul > li:nth-child(3) > div > div.organic__subtitle.typo.typo_type_greenurl > div.path.path_show-https.organic__path > a > b')
        assert 'selenide.org' in spisok2.text

    def tearDown(self):
        self.drv.close()

if __name__ == '__main__':
    unittest.main()
