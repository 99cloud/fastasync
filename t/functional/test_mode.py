import fastasync


def test_dir():
    assert dir(fastasync)
    assert '__version__' in dir(fastasync)
