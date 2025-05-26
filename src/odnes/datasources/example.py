import asyncio
from datetime import datetime
from odnes.datasources.datasource import Datasource, DatasourceObject, DNSRecordGenerator

class Example(Datasource):
    def __init__(self, api_key: str = ''):
        super().__init__()
        self.__api_keys = self.config.get('api_keys', [])
        
    async def search(self, domain: str):
        datasource_objects = []
        self.print_info(f"Started search for domain {domain}")
        datasource_object = DatasourceObject(
            domain=subdomain,
            DNSData = [
                DNSRecordGenerator(
                    source=self.__class__.__name__, 
                    type='A', 
                    verified=False, 
                    value="203.0.113.19", 
                    ttl=None, 
                    record_last_seen=datetime.now())
            ],
        )
        datasource_objects.append(datasource_object)
        self.print_info(f"Finished search for domain {domain}")
        return datasource_objects