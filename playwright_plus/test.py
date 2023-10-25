import unittest
from unittest.mock import MagicMock
from web_intercept import (
    json_detect_error,
    json_parse_result,
    intercept_json_playwright,
    request_json_playwright,
)


class TestRequestJsonPlaywright(unittest.TestCase):
    def test_request_json_playwright_success(self):
        # Mock the Page object
        mock_page = MagicMock()
        intercepted_json_response = request_json_playwright(
            json_url="https://api.apis.guru/v2/list.json",
            timeout=5000,
            page=mock_page,
            json_detect_error=json_detect_error,
            json_parse_result=json_parse_result,
        )
        self.assertEqual(intercepted_json_response.get("status_code"), 200)

    def test_request_json_playwright_error(self):
        # Mock the Page object
        mock_page = MagicMock()
        intercepted_json_response = intercept_json_playwright(
            page_url="https://api.apis.guru/v2/error.json",
            json_url_subpart="/nonexistent",
            page=mock_page,
            json_detect_error=json_detect_error,
            json_parse_result=json_parse_result,
        )

        # Perform assertions
        self.assertEqual(
            intercepted_json_response,
            {   
                'error': 'PlaywrightInterceptError', 
                'error_code': '1', 
                'error_message': 'An empty json was collected after calling the hidden API.'
            }
        )

if __name__ == "__main__":
    unittest.main()
