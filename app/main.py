"""Модуль приветсвия."""


def greeting(name: str) -> str:
    """Возвращает приветсвие.

    Args:
        name (str): Имя человека

    Returns:
        str: Привествие
    """
    return 'Привет, {0}'.format(name.title())
