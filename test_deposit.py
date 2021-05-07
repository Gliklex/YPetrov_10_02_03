import pytest
from deposit import *

deposits_data = dict(interest_rate=5, period_limit=(6, 18),
                     sum_limit=(1000, 100000))


def test_TimeDeposit_str():
    assert TimeDeposit("Сохраняй", **deposits_data).__str__() == \
           f"Наименование:      Сохраняй\n" \
           f"Валюта:            руб.\n" \
           f"Процентная ставка: 5.0\n" \
           f"Срок (мес.):       [6, 18)\n" \
           f"Сумма:             [1000, 100000)"


def test_BonusTimeDeposit_str():
    assert BonusTimeDeposit("Бонусный 2", **deposits_data, bonus=dict(percent=5, sum=2000)).__str__() == \
           f"Наименование:      Бонусный 2\n" \
           f"Валюта:            руб.\n" \
           f"Процентная ставка: 5.0\n" \
           f"Срок (мес.):       [6, 18)\n" \
           f"Сумма:             [1000, 100000)\n" \
           f"Бонус (%):         5\n" \
           f"Бонус (мин. сумма):2000"


def test_CompoundTimeDeposit_str():
    assert CompoundTimeDeposit("С капитализацией", **deposits_data).__str__() == \
           f"Наименование:      С капитализацией\n" \
           f"Валюта:            руб.\n" \
           f"Процентная ставка: 5.0\n" \
           f"Срок (мес.):       [6, 18)\n" \
           f"Сумма:             [1000, 100000)\n" \
           f"Капитализация %   : Да"
