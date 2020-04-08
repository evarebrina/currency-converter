from logger import get_logger
from util import get_usd_currency

logger = get_logger()


def convert(content: dict) -> dict:
    logger.info("covert method called")
    currency = get_usd_currency()
    logger.info(f"currency is {currency}")
    value = int(content.get("value"))
    if value is None:
        logger.warn("Value is empty")
        raise ValueError("Requested value must be int, float or numeric str, not None")
    resulting_value = value * currency
    logger.info(f"value is {value}, currency is {currency}, resulting value is {resulting_value}")
    return {
        "currency": currency,
        "requested_value": value,
        "resulting_value": resulting_value
    }
