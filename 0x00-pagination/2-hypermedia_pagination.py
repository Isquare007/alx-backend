#!/usr/bin/env python3
"""hypermedia function"""
import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
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

    def index_range(self, page: int, page_size: int) -> tuple:
        """return a tuple of size two containing a
        start index and an end index"""
        start_index = (page - 1) * page_size
        end_page = page * page_size
        return start_index, end_page

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """gets the page"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        start, end = self.index_range(page, page_size)
        dataset = self.dataset()

        if start > len(dataset):
            return []
        return dataset[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Dict]:
        """return a dictionary containing the data info"""
        data = {}

        data['page_size'] = page_size
        data['page'] = page

        get_page = self.get_page(page, page_size)
        data['data'] = get_page

        data_set = len(self.dataset())

        try:
            total_pages = math.ceil(data_set / page_size)
        except Exception:
            total_pages = 0

        data['next_page'] = page + 1 if page < total_pages else None

        data['prev_page'] = page - 1 if page > 1 else None

        data['total_pages'] = total_pages

        return data


if __name__ == "__main__":
    server = Server()

    print(server.get_hyper(1, 2))
    print("---")
    print(server.get_hyper(2, 2))
    print("---")
    print(server.get_hyper(100, 3))
    print("---")
    print(server.get_hyper(3000, 100))
