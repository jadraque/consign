import csv
import json

# https://pypi.org/project/azure-storage-blob/
from azure.storage.blob import BlobClient
# https://pypi.org/project/azure-data-tables/
from azure.data.tables import TableServiceClient



class StoreAdapter():
    '''
    '''

    def __init__(self, method):
        self.method = method


    def store(self, data, url, delimiter, overwrite, provider,
              connection_string, container_name):
        if self.method == 'CSV':
            self.to_csv(data, url, delimiter)
        elif self.method == 'JSON':
            self.to_json(data, url, overwrite)
        elif self.method in ['TXT', 'HTML']:
            self.to_text_file(data, url)
        elif self.method == ['PDF', 'IMG']:
            self.to_binary_file(data, url)
        elif self.method == 'BLOB':
            self.to_blob(provider, connection_string, container_name, data, url)
        elif self.method == 'TABLE':
            self.to_table(provider, connection_string, data, url)


    def to_csv(self, data, url, delimiter):
        with open(url, 'w', newline='', encoding='utf-8') as output_file:
            writer = csv.writer(output_file, delimiter=delimiter)
            for row in data:
                writer.writerow(row)


    def to_json(self, data, url, overwrite):
        if not overwrite:
            d = self.load_json(url)
            data.update(d)
        with open(url, 'w') as output_file:
            json.dump(data, output_file)

    
    def to_binary_file(self, data, url):
        '''
        Prints binary data into a binary file (ie. '.pdf').
        '''
        with open(url, 'wb') as output_file:
            output_file.write(data)


    def to_text_file(self, data, url):
        '''
        Prints text data into a text file (ie. '.txt', '.html').
        '''
        with open(output_path, 'w') as output_file:
            output_file.write(data)


    def to_blob(self, provider, connection_string, container_name, data, path):
        '''
        Uploads a Blob into the target container.
        '''
        if provider == 'azure':
            blob = BlobClient.from_connection_string(
                conn_str=connection_string,
                container_name=container_name,
                blob_name=path
            )
            blob.upload_blob(data)


    def to_table(self, provider, connection_string, data, url):
        '''
        '''
        if provider == 'azure':
            table = TableServiceClient.from_connection_string(
                conn_str=connection_string)
            table_client = table_service_client.get_table_client(table_name=url)
            for row in data:
                table_client.create_entity(entity=row)


    def load_json(self, url):
        with open(url, 'r') as input_file:
            d = json.load(input_file)
        return d
