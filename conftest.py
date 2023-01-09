import csv
import os
import pathlib
import zipfile
from io import TextIOWrapper, BytesIO
from openpyxl import load_workbook
import PyPDF2

import pytest

import tests

path_zip_arch = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'resources/files.zip')


@pytest.fixture(scope='session', autouse=True)
def zip_packer():
    """Фикстура для запаковки файлов и удаления файлов после тестов"""
    files_dir = pathlib.Path(tests.__file__).parent.parent.joinpath('resources').absolute()
    current_dir = pathlib.Path.cwd()
    with zipfile.ZipFile("files.zip", mode="w") as archive:
        for file_path in files_dir.iterdir():
            archive.write(file_path, arcname=file_path.name)
    pathlib.Path(f'{current_dir}/files.zip').rename(f'{files_dir}/files.zip')
    yield
    pathlib.Path(f'{files_dir}/files.zip').unlink()


@pytest.fixture
def get_list_filenames():
    """Фикстура для получения списка имен файлов в zip архиве"""
    with zipfile.ZipFile(f"{path_zip_arch}", mode="r") as archive:
        return sorted(archive.namelist())


@pytest.fixture
def get_csv_addresses():
    """Фикстура для получения csv reader с файлом addresses.csv"""
    with zipfile.ZipFile(f"{path_zip_arch}", mode="r") as archive:
        with archive.open('addresses.csv', 'r') as infile:
            reader = csv.reader(TextIOWrapper(infile, 'utf-8'))
            return list(reader)


@pytest.fixture
def get_pdf_reader():
    """Фикстура для получения pdf reader с файлом addresses.csv"""
    with zipfile.ZipFile(f"{path_zip_arch}", mode="r") as archive:
        filename = sorted(archive.namelist())[2]
        pdf_file = PyPDF2.PdfReader(BytesIO(archive.read(filename)))
        return pdf_file


@pytest.fixture
def get_xlsx_reader():
    """Фикстура для получения xlsx reader с файлом addresses.csv"""
    with zipfile.ZipFile(f"{path_zip_arch}", mode="r") as archive:
        filename = sorted(archive.namelist())[1]
        workbook = load_workbook(BytesIO(archive.read(filename)))
        sheet = workbook.active
        return sheet
