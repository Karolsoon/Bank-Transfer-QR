import pytest

from bank_transfer_qr import QR


# @pytest.fixture(scope='function')
# def qr_instance():
#     return QR()


def test_transformation_raises_type_error_when_input_is_not_a_list():
    pass


def test_transformation_raises_value_error_when_first_item_is_not_callable():
    pass


def test_transformation_raises_transformationerror_upon_failure():
    pass


def test_transformation_raises_type_error_when_transformation_item_is_not_tuple():
    pass


def test_transformation_executes_all_transformation_steps():
    pass
    # value = [1]
    # steps = [
    #     (list.extend, ([1],)),
    #     (list.extend, ([1],)),
    #     (list.extend, ([1],)),
    #     (list.extend, ([1],)),
    #     (sum, tuple())
    # ]
    # # for step in steps:
    # #     step[0](value, *step[1])

    # assert value == 5
