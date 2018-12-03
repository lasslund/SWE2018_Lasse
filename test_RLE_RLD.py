from RLE_RLD import rle_encoder,rle_decoder
import sys
from hypothesis import given
from hypothesis.strategies import text
#import afl

#afl.init()

def test_simple():
    assert rle_encoder("bbbkkk") == "b3k3"
def test_advanced():
    assert rle_encoder("ffffiiiii") == "f4i5"

def test_single():
    assert rle_encoder('k') == "k1"
    assert rle_encoder('kf') == "k1f1"

#  Tests for rle_decoder

def test_simple_decoder():
    assert rle_decoder('k3b3') == 'kkkbbb'

def test_invariant():
    for x in [
        'adfdgdfgfdsg',
        'asdsassasfgsdfhgjhgfdsdfghjhgfd']:
        assert rle_decoder(rle_encoder(x)) == x

@given(text())
def test_hypo(x):
    print(x)
    assert rle_decoder(rle_encoder(x)) == x

if __name__ == '__main__':
    # run 'py-afl-fuzz -o ./pdf/ -i ./examples/ -- (which python) test_rle.py'
    # from commandline to use afl to fuzz the encoder.
    print(rle_encoder(sys.stdin.read()))
