from abc import ABC, abstractmethod
from typing import List

from cvescan.scan_result import ScanResult


# Sorts a list of Scan Results in place
class AbstractStackableScanResultSorter(ABC):
    # TODO: String annotation can be removed after python 3.7
    # https://stackoverflow.com/questions/40049016/using-the-class-as-a-type-hint-for-
    # arguments-in-its-methods/50768146#50768146
    def __init__(
        self, reverse=False, subsorters: List["AbstractStackableScanResultSorter"] = []
    ):
        self.reverse = reverse
        self.subsorters = subsorters
        super().__init__()

    def sort(self, scan_results: List[ScanResult]) -> None:
        self._run_subsorters(scan_results)
        scan_results.sort(key=self._key_fn, reverse=self.reverse)

    @abstractmethod
    def _key_fn(self, scan_result: ScanResult):
        pass

    def _run_subsorters(self, scan_results: List[ScanResult]) -> None:
        for subsorter in reversed(self.subsorters):
            subsorter.sort(scan_results)
