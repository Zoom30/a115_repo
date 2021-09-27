import unittest
from blueprint_superhero import *
import pytest


class MyTestCase(unittest.TestCase):
    SAMPLE_DICTIONARY = {
        "Heat vision": 80,
        "super_speed": 90,
        "flight": 99,
        "invincibility": 45
    }

    SAMPLE_WALLET = {
        "Euro": 170,
        "Pounds": 40,
        "Dollars": 60,
        "Yen": 1000
    }

    # def test_evaluate_superpower_result(self):
    #     self.assertEqual(evaluate_superpower(dict_of_sp=self.SAMPLE_DICTIONARY, value=85),
    #                      second=[("super_speed", 90), ("flight", 99)])
    #     self.assertEqual(evaluate_superpower(dict_of_sp={}, value=70), second=[])
    #     self.assertEqual(evaluate_superpower(self.SAMPLE_DICTIONARY, value=100), second=[])
    #
    # def test_evaluate_money_result(self):
    #     self.assertEqual(evaluate_money(wallet_dict=self.SAMPLE_WALLET, currency="Dollars", num=20),
    #                      second={"Dollars": 20})
    #     self.assertEqual(evaluate_money(wallet_dict=self.SAMPLE_WALLET, currency="Yen", num=1500),
    #                      second={"Yen": self.SAMPLE_WALLET["Yen"]})
    #     self.assertEqual(evaluate_money(wallet_dict={}, currency="euros", num=50), second={})
    #
    # def test_evaluate_superpower_types(self):
    #     self.assertRaises(AttributeError, evaluate_superpower, "text", 20)
    #     self.assertRaises(TypeError, evaluate_superpower, self.SAMPLE_DICTIONARY, "fifty-two")
    #
    # def test_evaluate_money(self):
    #     self.assertRaises(AttributeError, evaluate_money, "text", "Yen", 30)
    #     self.assertRaises(TypeError, evaluate_money, self.SAMPLE_WALLET, 5465, "90")

    def test_evaluate_superpower_with_valid_dict_and_value(self):
        assert (evaluate_superpower(dict_of_sp=self.SAMPLE_DICTIONARY, value=85)) == [("super_speed", 90),
                                                                                      ("flight", 99)]

    def test_evaluate_superpower_with_empty_dict_and_someValue(self):
        assert (evaluate_superpower(dict_of_sp={}, value=50)) == []

    # 'oor' -> 'Out of Range'
    def test_evaluate_superpower_with_valid_dict_and_oor_value(self):
        assert (evaluate_superpower(dict_of_sp=self.SAMPLE_DICTIONARY, value=100)) == []

    def test_evaluate_money_with_valid_dict_and_num(self):
        assert (evaluate_money(wallet_dict=self.SAMPLE_WALLET, currency="Dollars", num=20)) == {"Dollars": 20}

    def test_evaluate_superpower_raising_attrib_err(self):
        with pytest.raises(AttributeError):
            evaluate_superpower(dict_of_sp="text", value=20)

    def test_evaluate_superpower_raise_type_err(self):
        with pytest.raises(TypeError):
            evaluate_superpower(dict_of_sp=self.SAMPLE_DICTIONARY, value="text")


if __name__ == '__main__':
    pytest.main()
