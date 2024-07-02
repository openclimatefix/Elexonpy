import os
import sys
import pytest
import pandas as pd
from unittest.mock import patch, MagicMock

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pyelexon.datasets import Datasets
import requests

@pytest.fixture
def mock_requests_get(mocker):
    return mocker.patch('requests.get')

def test_fetch_data_dict_response(mock_requests_get):
    # Mock response data for dict response
    mock_response = {
        'dataset': 'ABUC',
        'documentId': 'NGET-EMFIP-ABUC-00689635',
        'documentRevisionNumber': 1,
        'publishTime': '2024-06-25T08:29:53Z',
        'businessType': 'Replacement reserve',
        'psrType': 'Load',
        'marketAgreementType': 'Daily',
        'flowDirection': 'Down',
        'settlementDate': '2024-06-26',
        'quantity': 73.0
    }
    mock_requests_get.return_value.json.return_value = mock_response
    mock_requests_get.return_value.status_code = 200

    datasets = Datasets()
    data_dict = datasets.fetch_data('/datasets/ABUC', convert_to_dataframe=False)

    assert isinstance(data_dict, dict)
    assert data_dict == mock_response

def test_fetch_data_list_response(mock_requests_get):
    # Mock response data for list response
    mock_response = [
        {
            'dataset': 'ABUC',
            'documentId': 'NGET-EMFIP-ABUC-00689635',
            'documentRevisionNumber': 1,
            'publishTime': '2024-06-25T08:29:53Z',
            'businessType': 'Replacement reserve',
            'psrType': 'Load',
            'marketAgreementType': 'Daily',
            'flowDirection': 'Down',
            'settlementDate': '2024-06-26',
            'quantity': 73.0
        },
        {
            'dataset': 'ABUC',
            'documentId': 'NGET-EMFIP-ABUC-00689636',
            'documentRevisionNumber': 1,
            'publishTime': '2024-06-25T08:30:00Z',
            'businessType': 'Replacement reserve',
            'psrType': 'Generation',
            'marketAgreementType': 'Daily',
            'flowDirection': 'Up',
            'settlementDate': '2024-06-26',
            'quantity': 1136.0
        }
    ]
    mock_requests_get.return_value.json.return_value = mock_response
    mock_requests_get.return_value.status_code = 200

    datasets = Datasets()
    data_df = datasets.fetch_data('/datasets/ABUC', convert_to_dataframe=True)

    assert isinstance(data_df, pd.DataFrame)
    assert data_df.equals(pd.DataFrame(mock_response))

def test_fetch_abuc_dataframe(mock_requests_get):
    # Mock response data for fetch_abuc
    mock_response = [
        {
            'dataset': 'ABUC',
            'documentId': 'NGET-EMFIP-ABUC-00689635',
            'documentRevisionNumber': 1,
            'publishTime': '2024-06-25T08:29:53Z',
            'businessType': 'Replacement reserve',
            'psrType': 'Load',
            'marketAgreementType': 'Daily',
            'flowDirection': 'Down',
            'settlementDate': '2024-06-26',
            'quantity': 73.0
        },
        {
            'dataset': 'ABUC',
            'documentId': 'NGET-EMFIP-ABUC-00689636',
            'documentRevisionNumber': 1,
            'publishTime': '2024-06-25T08:30:00Z',
            'businessType': 'Replacement reserve',
            'psrType': 'Generation',
            'marketAgreementType': 'Daily',
            'flowDirection': 'Up',
            'settlementDate': '2024-06-26',
            'quantity': 1136.0
        }
    ]
    mock_requests_get.return_value.json.return_value = mock_response
    mock_requests_get.return_value.status_code = 200

    datasets = Datasets()
    abuc_data_df = datasets.fetch_abuc('2024-06-25T00:00:00Z', '2024-06-26T00:00:00Z', convert_to_dataframe=True)

    assert isinstance(abuc_data_df, pd.DataFrame)
    assert abuc_data_df.equals(pd.DataFrame(mock_response))

def test_fetch_abuc_stream_dataframe(mock_requests_get):
    # Mock response data for fetch_abuc_stream
    mock_response = [
        {
            'dataset': 'ABUC',
            'documentId': 'NGET-EMFIP-ABUC-00689635',
            'documentRevisionNumber': 1,
            'publishTime': '2024-06-25T08:29:53Z',
            'businessType': 'Replacement reserve',
            'psrType': 'Load',
            'marketAgreementType': 'Daily',
            'flowDirection': 'Down',
            'settlementDate': '2024-06-26',
            'quantity': 73.0
        },
        {
            'dataset': 'ABUC',
            'documentId': 'NGET-EMFIP-ABUC-00689636',
            'documentRevisionNumber': 1,
            'publishTime': '2024-06-25T08:30:00Z',
            'businessType': 'Replacement reserve',
            'psrType': 'Generation',
            'marketAgreementType': 'Daily',
            'flowDirection': 'Up',
            'settlementDate': '2024-06-26',
            'quantity': 1136.0
        }
    ]
    mock_requests_get.return_value.json.return_value = mock_response
    mock_requests_get.return_value.status_code = 200

    datasets = Datasets()
    abuc_stream_data_df = datasets.fetch_abuc_stream('2024-06-25T00:00:00Z', '2024-06-26T00:00:00Z', convert_to_dataframe=True)

    assert isinstance(abuc_stream_data_df, pd.DataFrame)
    assert abuc_stream_data_df.equals(pd.DataFrame(mock_response))