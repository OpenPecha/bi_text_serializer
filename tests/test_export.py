from pathlib import Path

from bi_text_serializer.exporter import Exporter
from bi_text_serializer.utils import from_yaml, to_yaml


def test_export():
    opa_path = Path('./tests/data/A2062B422.opa')
    exporter = Exporter(opa_path)
    src_pecha_paths = {
        'I2AE4A92A': Path('./tests/data/I2AE4A92A.opf'),
        'I5816F981': Path('./tests/data/I5816F981.opf'),
        'IC5E658A1': Path('./tests/data/IC5E658A1.opf'),
        'IE18EE205': Path('./tests/data/IE18EE205.opf'),
        
    }
    serialized_alignments = exporter.export(src_pecha_paths)
   

    expected_alignments = from_yaml(Path('./tests/data/expected_alignment.yml'))
    assert serialized_alignments == expected_alignments
