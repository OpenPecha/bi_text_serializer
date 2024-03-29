from pathlib import Path
from bi_text_serializer.utils import from_yaml
from bi_text_serializer.alignment import Alignment

class Exporter:

    def __init__(self, opa_path:Path):
        self.opa_path = opa_path


    def get_aligments(self):
        alignments = {}
        alignment_paths = list(self.opa_path.iterdir())
        alignment_paths.sort()
        for alignment_path in alignment_paths:
            if alignment_path.stem == "meta":
                continue
            alignments[alignment_path.stem] = Alignment(alignment_path)
        return alignments
    
    def get_seg_text(self, seg_id, src_pecha):
        src_base_text = src_pecha['base_text']
        seg_layer = src_pecha['segment_layer']
        seg_annotations = seg_layer.annotations
        seg_ann = seg_annotations[seg_id]
        seg_text = src_base_text[seg_ann['span']['start']:seg_ann['span']['end']]
        return seg_text

    
    def get_seg_texts(self, seg_infos, src_pechas):
        seg_texts = {}
        for pecha_id, seg_id in seg_infos.items():
            seg_lang = src_pechas[pecha_id]['lang']
            seg_text = self.get_seg_text(seg_id, src_pechas[pecha_id])
            seg_texts[pecha_id] = {
                'text':seg_text,
                'lang':seg_lang,
                
            }
        return seg_texts
        
    
    def get_alignment_segments(self, alignment_obj, src_pecha_paths):
        alignment_segments = {}

        src_pechas = alignment_obj.get_segment_srcs_pechas(src_pecha_paths)
        for seg_id, seg_info in alignment_obj.segment_paris.items():
            seg_texts = self.get_seg_texts(seg_info, src_pechas)
            alignment_segments[seg_id] = seg_texts
        return alignment_segments
    
    def export(self, src_pecha_paths):
        serialized_alignments = {}
        alignments = self.get_aligments()
        for aligment_id, alignment_obj in alignments.items():
            alignment_segments = self.get_alignment_segments(alignment_obj, src_pecha_paths)
            serialized_alignments[aligment_id] = alignment_segments
        return serialized_alignments



