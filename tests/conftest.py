import pytest

cnt = 0

@pytest.fixture(autouse=True)
def clean_txt_file():
    global cnt
    with open("tests/testfile.txt", "w"):
        pass
    print(cnt)