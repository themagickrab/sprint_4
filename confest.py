import pytest
import random

@pytest.fixture()
def personal_data():
    return {'name': 'Сергей', 'last_name': 'Жуков',
            'address': 'Университетская 1', 'metro': 'Университет',
            'phone': str(random.randint(100000000000, 999999999999))}

@pytest.fixture()
def date():
    return str(random.randint(1, 28))+'.'+ str(random.randint(1, 12))+'.'+str(random.randint(2023, 2025))

@pytest.fixture()
def personal_data_two():
    return {'name': 'Мария', 'last_name': 'Кравченко',
            'address': 'Лубянка 1', 'metro': 'Лубянка',
            'phone': str(random.randint(100000000000, 999999999999))}
