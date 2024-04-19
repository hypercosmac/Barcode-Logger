def main():
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?' 'version=v4')
    service = discovery.build('sheets', 'v4', http=http, discoveryServiceUrl=discoveryUrl)

    spreadsheet_id = '### spreadsheet ID ###'
    batch_update_spreadsheet_request_body = {
        "requests": [
            {
                "insertRange": {
                    "range": {
                        "sheetId": barcodes,
                        "startRowIndex": 0,
                        "endRowIndex": 1
                    },
                    "shiftDimension": "ROWS"
                }
            },
            {
                "pasteData": {
                    "data": "sample1, sample2, sample3",
                    "type": "PASTE_NORMAL",
                    "delimiter": ",",
                    "coordinate": {
                        "sheetId": 1234567890,
                        "rowIndex": 0
                    }
                }
            }
        ]
    }

    request = service.spreadsheets().batchUpdate(spreadsheetId=spreadsheet_id, body=batch_update_spreadsheet_request_body)
    response = request.execute()
    print(response)