from aiogram.fsm.state import State, StatesGroup


class RegistrationStates(StatesGroup):
    name = State()
    contact = State()
    password = State()


class LoginStates(StatesGroup):
    phone = State()
    password = State()
