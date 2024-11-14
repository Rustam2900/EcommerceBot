from aiogram.fsm.state import State, StatesGroup


class UserStates(StatesGroup):
    name = State()
    contact = State()


class OrderState(StatesGroup):
    waiting_for_color = State()
    waiting_for_size = State()
    waiting_for_quantity = State()


class OrderAddress(StatesGroup):
    location = State()

