import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of 
    popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        start_point = (page - 1) * page_size
        end_point = page * page_size
        
        page_content = self.__dataset[start_point: end_point + 1]
        
        return page_content