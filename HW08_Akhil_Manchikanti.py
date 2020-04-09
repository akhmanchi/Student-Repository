""" Functions to perform some date arithmatic operations, 
    field separated file reader, 
    Scanning directories and files """

# import re
import os
from datetime import datetime, timedelta
from typing import Tuple, Iterator, List, IO, Dict
from prettytable import PrettyTable

def date_arithmetic()-> Tuple[datetime, datetime, int]:
    """ Function to calculate the dates between, after and before certain dates """
    dt1: datetime = datetime.strptime("Feb 27 2020", "%b %d %Y")
    dt2: datetime = datetime.strptime("Feb 27 2019", "%b %d %Y")
    dt3: datetime = datetime.strptime("Feb 1 2019", "%b %d %Y")
    dt4: datetime = datetime.strptime("Sep 30 2019", "%b %d %Y")
    three_days_after_02272020: datetime = dt1 + timedelta(days=3)
    three_days_after_02272019: datetime = dt2 + timedelta(days=3)
    days_passed_01012019_10312019: int = (dt4 - dt3).days

    return three_days_after_02272020, three_days_after_02272019, days_passed_01012019_10312019

    # return datetime.strptime(three_days_after_02272020.strftime("%b %d %Y"), "%b %d %Y"), datetime.strptime(three_days_after_02272019.strftime("%b %d %Y"), "%b %d %Y"), days_passed_01012019_10312019

    # three_days_after_02272020: datetime = (dt1 + timedelta(days=3)).strftime("%b %d %Y")
    # three_days_after_02272019: datetime = (dt2 + timedelta(days=3)).strftime("%b %d %Y")
    # days_passed_01012019_10312019: int = (dt4 - dt3).days

    # return three_days_after_02272020, three_days_after_02272019, days_passed_01012019_10312019

def file_reader(path:str, fields:int, sep:str, header:bool = False) -> Iterator[List[str]]:
    """ generator to return each line of a file as a tuple split on a specific string """
    try:
        input_file: IO = open(path, 'r', encoding='utf-8')
    except FileNotFoundError:
        raise FileNotFoundError(f"Can't open '{path}'")
    else:
        with input_file:
            for offset, line in enumerate(input_file):
                line = line.rstrip('\n')
                if offset == 0 and header:
                    continue
                if len(line.split(sep)) == fields:
                    yield line.split(sep)
                else:
                    # fileName: str = re.split('\\|/', path)
                    raise ValueError(f"line {offset+1} in {path} has {len(line.split(sep))} fields instead of {fields}")
        
        # with fp:
        #     for n, line in enumerate(fp, 1):
        #         fields:List[str] = line.rstrip('\n').split(sep)
        #         if len(fields) != num_fields:
        #             raise ValueError(f"'{path}' line: {n}: read {len(fields)} fields but expected {num_fields}")
        #         elif n==1 and header:
        #             continue
        #         else:
        #             yield tuple(fields)

class FileAnalyzer:
    """ analyze all the python files in a directory """
    def __init__(self, dir_path: str) -> None:
        """ stores the directory path """
        self.dir_path = dir_path
        self.files_summary: Dict[str, Dict[str, int]] = dict()
        # self.analyze_files()
    
    def analyze_files(self) -> Dict[str, Dict[str, int]]:
        """ count the number of functions, lines, characters and classes """
        try:
            files = os.listdir(self.dir_path)
        except:
            raise FileNotFoundError(f"Can't get files at '{self.dir_path}'")

        for file in files:
            if file.endswith(".py"):
                lines: int = 0
                chars: int = 0
                classes: int = 0
                functions: int = 0

                try:
                    fp: IO = open(self.dir_path+"\\"+file, 'r', encoding='utf-8')
                    # Use os.path.join instead of concatenating
                except:
                    raise FileNotFoundError(f"Can't open '{file}'")
                else:
                    with fp:
                        for line in fp:
                            
                            lines += 1
                            chars += len(line)

                            if line.strip().startswith("class "):
                                classes += 1
                            elif line.strip().startswith("def "):
                                functions += 1

                    self.files_summary[file] = {
                        'class' : classes,
                        'function' : functions,
                        'line' : lines,
                        'char' : chars
                    }
        return self.files_summary

    def pretty_print(self) -> PrettyTable:
        pt: PrettyTable = PrettyTable(field_names = ['File Name', 'Classes', 'Functions', 'Lines', 'Characters'])
        for file_name, stats in self.files_summary.items():
            pt.add_row([file_name, stats['class'], stats['function'], stats['line'], stats['char']])
        return pt