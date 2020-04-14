import os
import logging
from scrapy.extensions.feedexport import FileFeedStorage

class CustomFileFeedStorage(FileFeedStorage):
    """
    A file feed storage extension that overwrites existing files
    """
    
    def open(self, spider):
        logging.info(f'custom file feed storage => {self.path}')
        dirname = os.path.dirname(self.path)
        if dirname and not os.path.exists(dirname):
            os.makedirs(dirname)
        return open(self.path, "wb")