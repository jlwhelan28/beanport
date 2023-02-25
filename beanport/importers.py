from attrs import define
from beancount.ingest import importer

@define
class BaseImporter(importer.ImporterProtocol):
    
    def name(self) -> str:
        pass

    def identify(self) -> bool:
        pass

    def extract(self):
        pass

    def file_account(self):
        pass

    def file_date(self):
        pass

    def file_name(self):
        pass


class ChaseImporter(BaseImporter):
    pass


class USAAImporter(BaseImporter):
    pass


class TradestationImporter(BaseImporter):
    pass


class VanguardImporter(BaseImporter):
    pass
