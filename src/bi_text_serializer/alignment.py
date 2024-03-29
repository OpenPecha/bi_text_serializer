
from bi_text_serializer.utils import from_yaml

from openpecha.core.pecha import OpenPechaFS
from openpecha.core.layer import LayerEnum
from openpecha.utils import download_pecha

class Seg_src_pecha:
     
    def __init__(self, pecha_id, lang, base_id, pecha_path:None):
        self.pecha_id = pecha_id
        self.lang=lang
        self.base_id = base_id
        self.pecha_path = pecha_path if pecha_path else download_pecha(pecha_id)
        self.opf = OpenPechaFS(self.pecha_path)
        self.base_text = self.opf.get_base(base_id)
        self.segment_layer = self.opf.get_layer(base_id, LayerEnum.segment)



class Alignment:

    def __init__(self, alignment_path) -> None:
         self.alignment_path = alignment_path
         self.alignment = from_yaml(self.alignment_path) if self.alignment_path else {}
         self.segment_srcs = self.alignment.get('segment_sources', {})
         self.segment_paris = self.alignment.get('segment_pairs', {})
    

    def get_segment_srcs_pechas(self, src_pecha_paths:None):
        srcs_pechas = {}
        for pecha_id, pecha_info in self.segment_srcs.items():
            pecha_lang = pecha_info.get('lang', "")
            pecha_base_id = pecha_info.get('base', '')
            pecha_path = src_pecha_paths.get(pecha_id, None)
            src_pecha = Seg_src_pecha(pecha_id, pecha_lang, pecha_base_id, pecha_path)
            srcs_pechas[pecha_id] = {
                'base_text': src_pecha.base_text,
                'segment_layer': src_pecha.segment_layer,
                'lang':src_pecha.lang
            }

        return srcs_pechas

    