#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Unit Tests for MBI API endpoints

    Note: Ideally, there would be tests for each character in the MBI to make
    sure all edge cases are taken into account. 

"""

import json

from flask import url_for

def test_request_contexts(app, client):
    # Make sure the API endpoints are valid
    """Activate the request context temporarily and make sure the API endpoints are correct"""
    with app.test_request_context():
        assert url_for('generate') == '/generate'
        assert url_for('verify') == '/verify'

def test_generate(app, client):
    # Make sure the generated MBI matches the rules
    res = client.get('/generate')

    mbiString = json.loads(res.get_data(as_text=True))['value']

    invalidLetters = ['S', 'L', 'O', 'I', 'B', 'Z']

    mbiList = list(mbiString)

    assert len(mbiList) == 11
    assert mbiList[0].isnumeric() and mbiList[0] is not '0'
    assert mbiList[1].isalpha() and mbiList[1] not in invalidLetters
    assert mbiList[2].isnumeric() or (mbiList[2].isalpha() and mbiList[2] not in invalidLetters)
    assert mbiList[3].isnumeric()
    assert mbiList[4].isalpha() and mbiList[4] not in invalidLetters
    assert mbiList[5].isnumeric() or (mbiList[5].isalpha() and mbiList[5] not in invalidLetters)
    assert mbiList[6].isnumeric()
    assert mbiList[7].isalpha() and mbiList[7] not in invalidLetters
    assert mbiList[8].isalpha() and mbiList[8] not in invalidLetters
    assert mbiList[9].isnumeric()
    assert mbiList[10].isnumeric()


def test_verify(app, client):
    # Test a working MBI
    mbiString = '1A00-A00-AA00'

    mimetype = 'application/json'
    params = {
        'mbi' : mbiString
    }
    res = client.post('/verify', data=params)

    assert json.loads(res.get_data())

def test_verify_fail_zero_in_pos1(app, client):
    # First character cannot be zero
    mbiString = '0A00-A00-AA00'

    mimetype = 'application/json'
    params = {
        'mbi' : mbiString
    }
    res = client.post('/verify', data=params)

    assert not json.loads(res.get_data())

def test_verify_fail_alpha_in_pos1(app, client):
    # First character cannot be alphabetic
    mbiString = 'AA00-A00-AA00'

    mimetype = 'application/json'
    params = {
        'mbi' : mbiString
    }
    res = client.post('/verify', data=params)

    assert not json.loads(res.get_data())

def test_verify_fail_invalid_alpha_in_pos2(app, client):
    # No alphabetic characters can be S, L, O, I, B, or Z
    mbiString = '0S00-A00-AA00'

    mimetype = 'application/json'
    params = {
        'mbi' : mbiString
    }
    res = client.post('/verify', data=params)

    assert not json.loads(res.get_data())

def test_verify_fail_wrong_num_chars(app, client):
    # Must be 11 characters
    # The dashes don't matter (they're stripped out for verification)
    mbiString = '0A00-A00-AA0'

    mimetype = 'application/json'
    params = {
        'mbi' : mbiString
    }
    res = client.post('/verify', data=params)

    assert not json.loads(res.get_data())

def test_generate_and_verify(app, client):
    # Generate returns a random MBI. Then we verify it is valid
    res_gen = client.get('/generate')

    mbiString = json.loads(res_gen.get_data(as_text=True))['value']

    print(mbiString)

    mimetype = 'application/json'
    params = {
        'mbi' : mbiString
    }
    res_verify = client.post('/verify', data=params)

    assert json.loads(res_verify.get_data())