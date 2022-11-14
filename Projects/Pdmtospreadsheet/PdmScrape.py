'''Pseudocode time
We need to take a list of numbers from a spreadsheet or list,
put them in the pdm cost of quality
Grab all the relevant data and put it back into the spreadsheet on the right cells
Probably save the fixed model numbers on the spreadsheet as well for ease later.
'''
#https://docs.google.com/spreadsheets/d/1JCWLC0T4ZfMCjEf_r7lzsVcOVrh1RANVeu6TrQQTS2s/edit?usp=sharing
if __name__ == '__main__':
    def implicit():
        from google.cloud import storage

        # If you don't specify credentials when constructing the client, the
        # client library will look for credentials in the environment.
        storage_client = storage.Client()

        # Make an authenticated API request
        buckets = list(storage_client.list_buckets())
        print(buckets)
    implicit()
    #import os
    #os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="C:\Projects\Pdmtospreadsheet\Serviceaccountkey.json"
    #set GOOGLE_APPLICATION_CREDENTIALS='C:\Projects\Pdm to spreadsheet\credentials.json'
    '''
    from googleapiclient import discovery
    #import credentials.json
    credentials = None
    service = discovery.build('sheets', 'v4', credentials=credentials)
    #value_render_option = ''
    #date_time_render_option = ''
    spreadsheet_id = '1JCWLC0T4ZfMCjEf_r7lzsVcOVrh1RANVeu6TrQQTS2s'
    sheet_id = 1854171512
    range_ = 'A1'
    request = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range=range_)
    response = request.execute()

    print(response)'''