#!/usr/bin/env python3
''' defines a class server to paginate a database'''
from typing import List, Tuple, Dict, Union


class Pagination:
    """Server class to paginate a database of api.
    """

    def __init__(self, data: List):
        self.dataset = data

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        '''
        gets the contents of a page

        Parameter
        -page (int): the page number where the content is located
        - page_size (int): the size of a page

        Return
        list of list of row in the page
        '''
        start_index, end_index = self.index_range(page, page_size)
	
        page_rows = []
        data = self.dataset
        length = len(data)
        if start_index <= length and end_index <= length:
            for i in range(start_index, end_index):
                page_rows.append(data[i])
        return page_rows

    def index_range(self, page: int, page_size: int) -> Tuple[int, int]:
        '''
        Calculate the start and end indices for a given page
        in a paginated data set.

        Parameters:
        - page (int): The page number
        - page_size (int): The number of items per page.

        Returns:
        tuple: A tuple containing the start and end indices for the given page
        '''
        start_index = (page - 1) * page_size
        end_index = start_index + page_size

        return start_index, end_index

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[
            str, Union[int, List[List], None]]:
        '''
        calculates and find a hypermedia for a given page
        Parameters:
        -- page (int): The page number
        - page_size (int): The number of items per page.

        Returns:
        a sictionatery: containg more information about the data such as next
        and previous
        '''
        all_data = self.dataset
        total_pages = (len(all_data) + page_size - 1) // page_size

        next_page = page + 1 if page < total_pages else None

        prev_page = page - 1 if page > 1 else None

        return {
                'page_size': page_size,
                'page': page,
                'data': self.get_page(page, page_size),
                'next_page': next_page,
                'prev_page': prev_page,
                'total_pages': total_pages,
                }
