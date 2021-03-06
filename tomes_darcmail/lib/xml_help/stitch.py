import logging
import os
from collections import OrderedDict


class Stitcher:
    def __init__(self, xml_path, gid):
        self.xml_loc = xml_path
        self.global_id = gid
        self.files = OrderedDict()
		self.logger = logging.getLogger(__name__)

    def stitch_account(self):
        fh = open(os.path.join(self.xml_loc, '{}.xml'.format(self.global_id)), 'w+', encoding='utf-8')
        fh.write(self.get_root_element_attributes())
        fh.write(self.get_id())
        res = os.listdir(self.xml_loc)
        self.files = [f for f in res if f.endswith(".xml")]
        for fn in self.files:
            self.logger.info('Stitching {}'.format(fn))
            acc_part = open(os.path.join(self.xml_loc, fn), 'r', encoding='utf-8')
            x = 0
            for line in acc_part.readlines():
                if x < 4:
                    x += 1
                    continue
                if line == '</Account>\n':
                    continue
                fh.write(line)
        fh.write('</Account>')

    @staticmethod
    def get_root_element_attributes():
        return '<?xml version="1.0" encoding="UTF-8"?>\n' \
               '<Account {}="{}" {}="{}" {}="{}">\n'. \
            format("xmlns", "https://github.com/StateArchivesOfNorthCarolina/tomes-eaxs",
                   "xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance",
                   "xsi:schemaLocation", "https://github.com/StateArchivesOfNorthCarolina/tomes-eaxs\n"
                                         "https://raw.githubusercontent.com/StateArchivesOfNorthCarolina/tomes-eaxs/master/versions/1/eaxs_schema_v1.xsd")

    def get_id(self):
        return '<GlobalId>{}</GlobalId>\n'.format(self.global_id)
