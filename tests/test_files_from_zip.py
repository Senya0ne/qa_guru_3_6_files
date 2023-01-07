def test_namelist_files(get_list_filenames):
    expected_filenames = ['addresses.csv', 'file_example_XLSX_10.xlsx', 'sample.pdf']
    assert len(expected_filenames) == len(get_list_filenames)
    assert all([a == b for a, b in zip(expected_filenames, get_list_filenames)])


def test_csv(get_csv_addresses):
    list_adresses = [['John', 'Doe', '120 jefferson st.', 'Riverside', ' NJ', ' 08075'],
                     ['Jack', 'McGinnis', '220 hobo Av.', 'Phila', ' PA', '09119'],
                     ['John "Da Man"', 'Repici', '120 Jefferson St.', 'Riverside', ' NJ', '08075'],
                     ['Stephen', 'Tyler', '7452 Terrace "At the Plaza" road', 'SomeTown', 'SD', ' 91234'],
                     ['', 'Blankman', '', 'SomeTown', ' SD', ' 00298'],
                     ['Joan "the bone", Anne', 'Jet', '9th, at Terrace plc', 'Desert City', 'CO', '00123']]
    assert len(list_adresses) == len(get_csv_addresses)
    assert all([a == b for a, b in zip(list_adresses, get_csv_addresses)])


def test_pdf(get_pdf_reader):
    assert 2 == len(get_pdf_reader.pages)
    assert "This is a small demonstration .pdf file " in get_pdf_reader.pages[0].extract_text()


def test_xlsx(get_xlsx_reader):
    assert 'Mara' == get_xlsx_reader.cell(row=3, column=2).value
