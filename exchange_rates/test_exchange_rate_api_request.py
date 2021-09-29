import unittest

import mock
import requests
from requests.exceptions import HTTPError


def api_request(query):
    """
    Function that does a GET request against api result and returns the raw content

    """
    url = "https://api.frankfurter.app/"
    params = {'amount': query}
    resp = requests.get(url, params=params)
    resp.raise_for_status()
    return resp.content


class TestExchangeRateAPIRequest(unittest.TestCase):
    def _mock_response(
            self,
            status=200,
            content="CONTENT",
            json_data=None,
            raise_for_status=None):
        """
        Example text that mocks requests.get and returns a mock Response object
        """

        mock_resp = mock.Mock()
        mock_resp.raise_for_status = mock.Mock()
        if raise_for_status:
            mock_resp.raise_for_status.side_effect = raise_for_status

        mock_resp.status_code = status
        mock_resp.content = content

        if json_data:
            mock_resp.json = mock.Mock(
                return_value=json_data
            )
        return mock_resp

    @mock.patch('requests.get')
    def test_api_get_request(self, mock_get):
        """
        Api get request success case
        """
        mock_resp = self._mock_response(content="amount")
        mock_get.return_value = mock_resp

        result = api_request('amount')
        self.assertEqual(result, 'amount')
        self.assertTrue(mock_resp.raise_for_status.called)

    @mock.patch('requests.get')
    def test_failed_query(self, mock_get):
        """
        Api get request error case
        """
        mock_resp = self._mock_response(status=500, raise_for_status=HTTPError("api is down"))
        mock_get.return_value = mock_resp
        self.assertRaises(HTTPError, api_request, 'amount')


if __name__ == '__main__':
    unittest.main()
