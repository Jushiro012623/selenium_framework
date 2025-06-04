from tests.baseTest import BaseTest
from testPages import mainPage

class MainPageTest(BaseTest):
        
    def test_search_python(self):
        main_page = mainPage.MainPage(self.driver)
        assert main_page.is_title_matches()
        
        main_page.search_text_element = "pycon"
        main_page.click_go_button()
        
        search_result_page = mainPage.SearchResultsPage(self.driver)
        assert search_result_page.is_results_found()
        