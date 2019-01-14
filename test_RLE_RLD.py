from RLE_RLD import rle_encoder,rle_decoder
import sys
from hypothesis import given
from hypothesis.strategies import text
#import afl

#afl.init()

"""
Start with simple testing one letter, then more letters and single combined
"""
def test_simple_encoder():
    assert rle_encoder('a') == [('a', 1)]
    assert rle_encoder('bbb') == [('b', 3)]
    assert rle_encoder('ab') == [('a', 1),('b', 1)]

"""
Testing more advanced with multiple letters combined
"""
def test_advanced_encoder():
    assert rle_encoder('zzzzzzzziiiii') == [('z', 8), ('i', 5)]
    assert rle_encoder('ttttttttttt') == [('t', 11)]

"""
Testing the decoder
"""
#  Tests for rle_decoder

def test_simple_decoder():
    assert rle_decoder('k3b3') == 'kkkbbb'
    assert rle_decoder('a11b9') == 'aaaaaaaaaaabbbbbbbbb'
    assert rle_decoder('c1d12') == 'cdddddddddddd'

@given(text())
def test_invariant(abcdefghijklmn):
    assert rle_decoder(rle_encoder('abcdefghijklmn')) == 'abcdefghijklmn'


#def test_hypo(x):
#    print(x)
#    assert rle_decoder(rle_encoder(x)) == x

if __name__ == '__main__':
    # run 'py-afl-fuzz -o ./pdf/ -i ./examples/ -- (which python) test_rle.py'
    # from commandline to use afl to fuzz the encoder.
    print(rle_encoder(sys.stdin.read()))
