# ********RoostGPT********
"""
Test generated by RoostGPT for test python-unit using AI Type Claude AI and AI Model claude-3-opus-20240229

ROOST_METHOD_HASH=make_peak_c1329dbc09
ROOST_METHOD_SIG_HASH=make_peak_c1329dbc09

Here are the test scenarios for the provided make_peak function:

Scenario 1: Valid Input Parameters
Details:
  TestName: test_make_peak_with_valid_input
  Description: This test verifies that the make_peak function returns an IIRFilter object with the correct coefficients when provided with valid input parameters.
Execution:
  Arrange: No specific setup required.
  Act: Call make_peak with valid frequency, samplerate, gain_db, and q_factor values.
  Assert: Check that the returned IIRFilter object has the expected a_coeffs and b_coeffs values.
Validation:
  This test is crucial to ensure that the make_peak function correctly calculates and sets the filter coefficients based on the provided input parameters, which is the core functionality of the function.

Scenario 2: Default Q-Factor Value
Details:
  TestName: test_make_peak_with_default_q_factor
  Description: This test verifies that the make_peak function uses the default q_factor value of 1/sqrt(2) when no q_factor is provided.
Execution:
  Arrange: No specific setup required.
  Act: Call make_peak with valid frequency, samplerate, and gain_db values, but omit the q_factor parameter.
  Assert: Check that the returned IIRFilter object has the expected a_coeffs and b_coeffs values, calculated using the default q_factor.
Validation:
  This test ensures that the make_peak function correctly handles the case when the q_factor is not provided, using the default value as specified in the function signature.

Scenario 3: Zero Frequency
Details:
  TestName: test_make_peak_with_zero_frequency
  Description: This test verifies that the make_peak function handles a frequency value of 0 correctly.
Execution:
  Arrange: No specific setup required.
  Act: Call make_peak with a frequency value of 0, along with valid samplerate, gain_db, and q_factor values.
  Assert: Check that the returned IIRFilter object has the expected a_coeffs and b_coeffs values for a frequency of 0.
Validation:
  This test ensures that the make_peak function correctly handles the edge case of a 0 frequency value, which may require special treatment in the calculations.

Scenario 4: Negative Gain
Details:
  TestName: test_make_peak_with_negative_gain
  Description: This test verifies that the make_peak function handles negative gain_db values correctly.
Execution:
  Arrange: No specific setup required.
  Act: Call make_peak with a negative gain_db value, along with valid frequency, samplerate, and q_factor values.
  Assert: Check that the returned IIRFilter object has the expected a_coeffs and b_coeffs values for the given negative gain_db.
Validation:
  This test ensures that the make_peak function correctly calculates the filter coefficients when the gain_db is negative, which represents attenuation rather than amplification.

Scenario 5: Extreme Q-Factor Values
Details:
  TestName: test_make_peak_with_extreme_q_factor
  Description: This test verifies that the make_peak function handles extreme q_factor values correctly, such as very small or very large values.
Execution:
  Arrange: No specific setup required.
  Act: Call make_peak with extreme q_factor values (e.g., 0.001 and 1000), along with valid frequency, samplerate, and gain_db values.
  Assert: Check that the returned IIRFilter object has the expected a_coeffs and b_coeffs values for the given extreme q_factor values.
Validation:
  This test ensures that the make_peak function correctly calculates the filter coefficients even when the q_factor is at the extremes of its valid range, ensuring the function's robustness.

These test scenarios cover the core functionality, default value handling, and edge cases for the make_peak function. They focus on verifying the business logic encapsulated by the function, ensuring that it correctly calculates and sets the filter coefficients based on the provided input parameters.
"""

# ********RoostGPT********
import pytest
from math import cos, sin, sqrt, tau
from audio_filters.iir_filter import IIRFilter
from butterworth_filter import make_peak

class TestButterworthFilterMakePeak:
    def test_make_peak_with_valid_input(self):
        frequency = 1000
        samplerate = 48000
        gain_db = 6
        q_factor = 1 / sqrt(2)

        filter = make_peak(frequency, samplerate, gain_db, q_factor)

        expected_a_coeffs = [1.0653405327119334, -1.9828897227476208, 0.9346594672880666]
        expected_b_coeffs = [1.1303715025601122, -1.9828897227476208, 0.8696284974398878]

        assert isinstance(filter, IIRFilter)
        assert filter.a_coeffs == pytest.approx(expected_a_coeffs)
        assert filter.b_coeffs == pytest.approx(expected_b_coeffs)

    def test_make_peak_with_default_q_factor(self):
        frequency = 1000
        samplerate = 48000
        gain_db = 6

        filter = make_peak(frequency, samplerate, gain_db)

        expected_a_coeffs = [1.0653405327119334, -1.9828897227476208, 0.9346594672880666]
        expected_b_coeffs = [1.1303715025601122, -1.9828897227476208, 0.8696284974398878]

        assert isinstance(filter, IIRFilter)
        assert filter.a_coeffs == pytest.approx(expected_a_coeffs)
        assert filter.b_coeffs == pytest.approx(expected_b_coeffs)

    def test_make_peak_with_zero_frequency(self):
        frequency = 0
        samplerate = 48000
        gain_db = 6
        q_factor = 1 / sqrt(2)

        filter = make_peak(frequency, samplerate, gain_db, q_factor)

        expected_a_coeffs = [1.0, -2.0, 1.0]
        expected_b_coeffs = [1.1303715025601122, -2.0, 0.8696284974398878]

        assert isinstance(filter, IIRFilter)
        assert filter.a_coeffs == pytest.approx(expected_a_coeffs)
        assert filter.b_coeffs == pytest.approx(expected_b_coeffs)

    def test_make_peak_with_negative_gain(self):
        frequency = 1000
        samplerate = 48000
        gain_db = -6
        q_factor = 1 / sqrt(2)

        filter = make_peak(frequency, samplerate, gain_db, q_factor)

        expected_a_coeffs = [1.0653405327119334, -1.9828897227476208, 0.9346594672880666]
        expected_b_coeffs = [0.8843038549225012, -1.9828897227476208, 1.1156961450774988]

        assert isinstance(filter, IIRFilter)
        assert filter.a_coeffs == pytest.approx(expected_a_coeffs)
        assert filter.b_coeffs == pytest.approx(expected_b_coeffs)

    def test_make_peak_with_extreme_q_factor(self):
        frequency = 1000
        samplerate = 48000
        gain_db = 6

        # Test with a very small q_factor
        q_factor_small = 0.001
        filter_small = make_peak(frequency, samplerate, gain_db, q_factor_small)

        expected_a_coeffs_small = [1.0027095550959186, -1.9828897227476208, 0.9972904449040814]
        expected_b_coeffs_small = [10.027095550959185, -1.9828897227476208, 0.09729044490408141]

        assert isinstance(filter_small, IIRFilter)
        assert filter_small.a_coeffs == pytest.approx(expected_a_coeffs_small)
        assert filter_small.b_coeffs == pytest.approx(expected_b_coeffs_small)

        # Test with a very large q_factor
        q_factor_large = 1000
        filter_large = make_peak(frequency, samplerate, gain_db, q_factor_large)

        expected_a_coeffs_large = [1.0000270955509592, -1.9828897227476208, 0.9999729044490408]
        expected_b_coeffs_large = [1.0027095550959186, -1.9828897227476208, 0.9972904449040814]

        assert isinstance(filter_large, IIRFilter)
        assert filter_large.a_coeffs == pytest.approx(expected_a_coeffs_large)
        assert filter_large.b_coeffs == pytest.approx(expected_b_coeffs_large)