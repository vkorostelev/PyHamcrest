from . import matcher_test as mt


def test_matcher_matches(matcher, valid_value):
    mt.assert_matches(matcher, valid_value,
                      "Expect {0} to match {1}".format(matcher, valid_value))
    

def test_matcher_does_not_match(matcher, invalid_value):
    mt.assert_does_not_match(matcher, invalid_value,
                             "Expect {0} not to match {1}".format(matcher, invalid_value))
    
    
def test_matcher_description(matcher, description):
    mt.assert_description(description, matcher)

    
def test_successful_match_generates_no_description(matcher, valid_value):
    mt.assert_no_mismatch_description(matcher, valid_value)

    
def test_mismatch_description_contains_expected_value(matcher, invalid_value, mismatch_description):
    mt.assert_mismatch_description(mismatch_description, matcher, invalid_value)

    
def test_describe_mismatch(matcher, invalid_value, mismatch_description):
    mt.assert_describe_mismatch(mismatch_description, matcher, invalid_value)
