#!/usr/bin/python3

from sorters.sort_base import sort_base
from sort_video.data_tools import data_store


class quick_sort(sort_base):
    def __init__(self) -> None:
        super().__init__()
        self.draw_counter = 0

    def name(self) -> str:
        return 'Quick'

    def _do_sort(self, data: data_store) -> None:
        self.__quick_sort(data, 0, data.size() - 1)

    def __quick_sort(self, data: data_store, low: int, high: int) -> None:
        if low < high:
            pivot = self.__partition(data, low, high)

            self.__quick_sort(data, low, pivot - 1)
            self.__quick_sort(data, pivot + 1, high)

    def __partition(self, data: data_store, low: int, high: int) -> None:
        pivot_val = data[high]

        i = (low - 1)

        for j in range(low, high):
            if data.is_less_than(j, high):
                i += 1
                data.swap(i, j)

                self.draw_counter += 1
                if self.draw_counter % 10 == 0:
                    data.draw(self.name())
        data.swap(i + 1, high)
        data.draw(self.name())
        return i + 1