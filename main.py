from src.masks import get_mask_account
from src.masks import get_mask_card_number
from src.utils import load_transactions


def main():
    load_transactions("data/operations.json")
    get_mask_card_number("1234567823495678")
    get_mask_account("12345678123567819234")


if __name__ == '__main__':
    main()
