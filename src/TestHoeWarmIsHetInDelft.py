import unittest
from unittest.mock import patch
from requests.exceptions import ConnectionError
from HoeWarmIsHetInDelft import *


class SAMPLE():
    
    VALID_DATA = [
        "12345 0.0 0.0 19 33.6 11 1013.8 0.0 0.0 6.3 0.00 0.00 28.3 15 100.0 5 0.0 0 0 0.0 -100.0 255.0 -100.0 -100.0 -100.0 -100.0 -100 -100 -100 11 47 17 Namib_Desert_Lodge-11:47:17_AM 0 0 18 4 0.00 0.00 100 100 100 100 100 33.6 31.2 33.6 14.4 5 Dry -0.4 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 11.3 -0.9 14228.1 18/4/2024 31.2 10.4 33.6 14.4 0.0 0 2 0 1 0 1 0 0 0 0 32.6 32.7 32.7 32.8 32.9 33.1 33.2 33.5 33.6 33.6 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 31.1 14.4 31.1 6.4 0 --- --- 23 0 0 -100.0 -100.0 -100 -100 -100 -100 -100 749.0 28.3 24.4 33.4 1014.6 1012.8 11 10:56_AM 10:56_AM 33.4 12.9 -0.2 -11.5 0 2024 -17.8 1 0 1 9 8 327 347 9 18 72 51 340 19 0.0 255.0 0.8 16.8 -24.10000 -15.90000 0.0 19 9 0.0 2:55_AM 0.0 0.0 0.0 0.0 0.0 0.0 1.1 11:39_AM 2:55_AM 15 !!C10.37S143!!",
        "12345 0.0 0.0 0 12.6 74 1013.0 0.0 0.0 0.0 277.43 0.00 17.3 51 100.0 1 0.0 0 0 0.0 -100.0 255.0 -100.0 -100.0 -100.0 -100.0 -100 -100 -100 00 27 09 weerindelft_-00:27:09 0 0 18 4 0.00 0.00 100 100 100 100 100 12.6 13.0 12.6 12.6 1 Night_time/Dry/mostly_cloudy_- 0.7 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.0 8.1 1860.0 18/4/2024 13.0 13.0 12.6 12.6 0.0 0 0 0 0 0 0 0 0 0 0 12.6 12.6 12.6 12.6 12.6 12.6 12.6 12.6 12.6 12.6 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 12.6 12.6 12.6 0.0 0 --- --- 6 0 0 -100.0 -100.0 -100 -100 -100 -100 -100 0.0 17.3 17.1 12.6 1013.0 1012.7 0 00:00 18:12:26 12.6 12.6 8.1 8.1 0 2024 -11.4 -1 0 0 32407 32407 32407 32407 32407 32407 32407 32407 32407 32407 0.0 255.0 0.0 10.4 51.97944 -4.34611 0.0 74 74 0.0 00:00 0.0 0.0 0.0 0.0 0.0 0.0 0.0 00:00 00:00 7 !!C10.37S143!!"
    ]

    INVALID_DATA = [
        "12345 0.0 0.0", # Incomplete
        "12345 0.0 0.0 19 33.6 11 1013.8 0.0 0.0", # missing values
        "12345 0.0 0.0 A B C D E F G H I J K L M N O P Q R S T U V W X Y Z",  # Incorrect format
    ]

    VALID_URL = [
        'https://weerindelft.nl/clientraw.txt',
        'https://weather.namsearch.com/namibdesert/clientraw.txt'
    ]

    INVALID_URL = [
        '',
        1,
        True,
        'not url',
        'http//noColon.com/',
        'https:noDashes.com/',
        'ttps//:#somedthing/?notright'
    ]

class TestRequestWdData(unittest.TestCase):

    @patch('HoeWarmIsHetInDelft.get')
    def test_request_wd_data_valid_url(self, mock_get):
        # Mock response
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = "Mock response text"

        wd_url = "https://example.com/weather"
        result = request_wd_data(wd_url)

        mock_get.assert_called_once_with(wd_url, headers={'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'})
        self.assertEqual(result, "Mock response text")

    @patch('HoeWarmIsHetInDelft.get')
    def test_request_wd_data_invalid_url(self, mock_get):
        wd_url = "invalid_url"
        with self.assertRaises(ValueError):
            request_wd_data(wd_url)

    @patch('HoeWarmIsHetInDelft.get')
    def test_request_wd_data_connection_error(self, mock_get):
        mock_get.return_value.status_code = 404

        wd_url = "https://example.com/weather"
        with self.assertRaises(ConnectionError):
            request_wd_data(wd_url)




class TestValidateWdData(unittest.TestCase):

    def test_validate_wd_data(self):
        for sample in SAMPLE.VALID_DATA: 
            self.assertTrue(validate_wd_data(sample))


    def test_validate_wd_data_invalid_sample(self):
        for sample in SAMPLE.INVALID_DATA: 
            self.assertFalse(validate_wd_data(sample))
    
if __name__ == '__main__':
    unittest.main()
