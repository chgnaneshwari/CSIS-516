import unittest

def getNumber(upperCaseLetter):
    """
    Converts an uppercase letter to its corresponding telephone keypad digit.
    If the character is not in A-Z, it returns the character unchanged.
    (This function is expected to be called only with A-Z letters.)

    :param upperCaseLetter: A single character expected to be uppercase.
    :return: The telephone keypad digit as a string if the input is an uppercase
             letter from A-Z; otherwise, returns the original character.
    """
    # Mapping from letters to digits based on telephone keypad
    letter_to_digit = {
        "ABC": "2", "DEF": "3", "GHI": "4", "JKL": "5",
        "MNO": "6", "PQRS": "7", "TUV": "8", "WXYZ": "9"
    }

    # Check which group the letter belongs to and return the corresponding digit
    for group, digit in letter_to_digit.items():
        if upperCaseLetter in group:
            return digit

    # If it's not a letter, return the character itself (unchanged)
    return upperCaseLetter


def convertPhoneWord(s):
    """
    Converts a phone-word string (which may include letters, digits, and symbols)
    into its corresponding telephone number string.

    :param s: str - The phone-word string.
    :return: str - The converted telephone number string.
    :raises ValueError: if the input contains an invalid character.
    """
    result = []

    # Allowed symbols: *, #, -
    allowed_symbols = {'*', '#', '-'}

    # Iterate through each character of the string
    for char in s:
        # If it's a letter, convert it to uppercase and then to its corresponding digit
        if char.isalpha():
            result.append(getNumber(char.upper()))
        # If it's a digit or allowed symbol, keep it unchanged
        elif char.isdigit() or char in allowed_symbols:
            result.append(char)
        # If it's an invalid character, raise a ValueError
        else:
            raise ValueError(f"Invalid character: {char}")

    # Join the list into a single string and return the result
    return ''.join(result)


# ----------------------------
# Unit Tests for getNumber
# ----------------------------
class TestGetNumber(unittest.TestCase):
    def test_group_ABC(self):
        for ch in "ABC":
            with self.subTest(ch=ch):
                self.assertEqual(getNumber(ch), "2")

    def test_group_DEF(self):
        for ch in "DEF":
            with self.subTest(ch=ch):
                self.assertEqual(getNumber(ch), "3")

    def test_group_GHI(self):
        for ch in "GHI":
            with self.subTest(ch=ch):
                self.assertEqual(getNumber(ch), "4")

    def test_group_JKL(self):
        for ch in "JKL":
            with self.subTest(ch=ch):
                self.assertEqual(getNumber(ch), "5")

    def test_group_MNO(self):
        for ch in "MNO":
            with self.subTest(ch=ch):
                self.assertEqual(getNumber(ch), "6")

    def test_group_PQRS(self):
        for ch in "PQRS":
            with self.subTest(ch=ch):
                self.assertEqual(getNumber(ch), "7")

    def test_group_TUV(self):
        for ch in "TUV":
            with self.subTest(ch=ch):
                self.assertEqual(getNumber(ch), "8")

    def test_group_WXYZ(self):
        for ch in "WXYZ":
            with self.subTest(ch=ch):
                self.assertEqual(getNumber(ch), "9")

    def test_non_letter_characters(self):
        # Non-letter characters should be returned unchanged.
        for ch in ["1", "0", "#", "*", "-"]:
            with self.subTest(ch=ch):
                self.assertEqual(getNumber(ch), ch)

    def test_lowercase_letters(self):
        # For lowercase letters, getNumber returns the character unchanged.
        # (Normally, convertPhoneWord uppercases letters before calling getNumber.)
        for ch in "abcdefghijklmnopqrstuvwxyz":
            with self.subTest(ch=ch):
                self.assertEqual(getNumber(ch), ch)


# ----------------------------
# Unit Tests for convertPhoneWord
# ----------------------------
class TestConvertPhoneWord(unittest.TestCase):
    # Standard examples
    def test_standard_uppercase(self):
        self.assertEqual(convertPhoneWord("CALLNOW"), "2255669")

    def test_standard_lowercase(self):
        self.assertEqual(convertPhoneWord("callnow"), "2255669")

    def test_standard_mixed_case(self):
        self.assertEqual(convertPhoneWord("GoOdDaY"), "4663329")

    # Common phone-number formats
    def test_1_800_FLOWERS(self):
        self.assertEqual(convertPhoneWord("1-800-FLOWERS"), "1-800-3569377")

    def test_1_800_CALLSAM(self):
        self.assertEqual(convertPhoneWord("1-800-CALLSAM"), "1-800-2255726")

    def test_standalone_symbols_and_digits(self):
        self.assertEqual(convertPhoneWord("*228"), "*228")
        self.assertEqual(convertPhoneWord("#54652"), "#54652")
        self.assertEqual(convertPhoneWord("1-989-555-5555"), "1-989-555-5555")

    # Edge cases with single characters
    def test_single_letter(self):
        self.assertEqual(convertPhoneWord("A"), "2")
        self.assertEqual(convertPhoneWord("Z"), "9")

    def test_single_digit(self):
        self.assertEqual(convertPhoneWord("5"), "5")

    def test_single_symbol(self):
        for symbol in ["*", "#", "-"]:
            with self.subTest(symbol=symbol):
                self.assertEqual(convertPhoneWord(symbol), symbol)

    # Empty string
    def test_empty_string(self):
        self.assertEqual(convertPhoneWord(""), "")

    # Complex mix of allowed characters
    def test_complex_mix(self):
        input_str = "1-800-GET-FOOD"
        expected = "1-800-438-3663"
        self.assertEqual(convertPhoneWord(input_str), expected)

    # Edge cases: strings that are already only digits, symbols, or letters.
    def test_only_digits(self):
        self.assertEqual(convertPhoneWord("1234567890"), "1234567890")

    def test_only_symbols(self):
        self.assertEqual(convertPhoneWord("*-#-*-#"), "*-#-*-#")

    def test_only_letters(self):
        # Note: The expected output for the full alphabet conversion is computed by converting each letter.
        self.assertEqual(
            convertPhoneWord("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), "22233344455566677778889999"
        )

    # Invalid input tests
    def test_invalid_characters(self):
        # Characters such as spaces or punctuation (other than allowed symbols) are invalid.
        invalid_inputs = [
            "HELLO WORLD",  # contains a space
            "TEST!",  # contains an exclamation point
            "A@B",  # contains '@'
            "123_456",  # contains underscore
            "CALL,ME",  # contains a comma
            "FLOWERS.",  # contains a period
            "\tCALLNOW",  # contains a tab character
            "\nCALLNOW",  # contains a newline
        ]
        for inp in invalid_inputs:
            with self.subTest(inp=inp):
                with self.assertRaises(ValueError):
                    convertPhoneWord(inp)

    # Testing borderline valid strings (with dash at beginning or end)
    def test_edge_dashes(self):
        self.assertEqual(convertPhoneWord("-CALL-"), "-2255-")
        self.assertEqual(convertPhoneWord("CALL-"), "2255-")
        self.assertEqual(convertPhoneWord("-CALL"), "-2255")

    # Testing conversion consistency for multiple repeated symbols or letters
    def test_repeated_letters(self):
        self.assertEqual(convertPhoneWord("AAA"), "222")
        self.assertEqual(convertPhoneWord("ZZZ"), "999")

    # Testing conversion of long strings
    def test_long_string(self):
        # A long phoneword that mixes numbers, letters, and allowed symbols
        input_str = "1-800-SUPERCALIFRAGILISTICEXPIALIDOCIOUS"
        # We don't want to compute the expected value manually in this test;
        # instead, we just ensure that the output is of the correct length and contains no letters.
        output = convertPhoneWord(input_str)
        expected_length = len(input_str)
        self.assertEqual(len(output), expected_length)
        # Assert no alphabetical characters remain.
        for char in output:
            self.assertTrue(
                char.isdigit() or char in "*#-", f"Unexpected character: {char}"
            )


# ----------------------------
# Running the tests in Google Colab / Jupyter
# ----------------------------
if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
