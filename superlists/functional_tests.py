from selenium import webdriver
import unittest
import time
from selenium.webdriver.common.keys import Keys

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()
    
    def test_can_start_a_list_and_retrieve_it_later(self):
        browser = self.browser  # Fix 1: Use self.browser instead of browser
        browser.get('http://localhost:8000')

        self.assertIn('To-Do', browser.title)  # Fix 2: Use self.browser instead of browser
        header_text = browser.find_element_by_tag_name('h1').text  # Fix 3: Use text instead of header_text
        self.assertIn('To-Do', header_text)

        inputbox = browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),  # Fix 4: Use get_attribute instead of get_attribte
            'Enter a to-do item'
        )
        inputbox.send_keys('Buy peacock feathers')

        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
      
        table = browser.find_element_by_id('id_lists_table')
        rows = table.find_elements_by_tag_name('tr')  # Fix 5: Use find_elements_by_tag_name instead of find_element_by_tag_name
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows),
            "New to-do item did not appear in the table"  # Fix 6: Corrected the typo in the message
        )

        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main()
