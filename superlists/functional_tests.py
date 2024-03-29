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
        browser = self.browser 
        browser.get('http://localhost:8000')

        self.assertIn('To-Do', browser.title)  
        header_text = browser.find_element_by_tag_name('h1').text  
        self.assertIn('To-Do', header_text)

        inputbox = browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )
        inputbox.send_keys('Buy peacock feathers')

        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
      
        table = self.browser.find_element_by_id('id_lists_table')

        rows = table.find_elements_by_tag_name('tr')  
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows),
            "New to-do item did not appear in the table" 
        )


        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main()
