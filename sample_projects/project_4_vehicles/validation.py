from vehicle_management import MAIN_MENU_OPTIONS


def is_user_main_menu_input_valid(user_input: str) -> bool:
    if not user_input.isdigit():
        return False
    user_input_num = int(user_input)
    if user_input_num < 1 or user_input_num >= len(MAIN_MENU_OPTIONS) + 1:
        return False
    return True
