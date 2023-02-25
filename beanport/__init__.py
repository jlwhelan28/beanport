from .importers import ChaseImporter, USAAImporter, TradestationImporter, VanguardImporter

CONFIG = [
    ChaseImporter.Importer(),
    USAAImporter.Importer(),
    TradestationImporter.Importer(),
    VanguardImporter.Importer(),
]