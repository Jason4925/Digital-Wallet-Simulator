# digital_wallet/data_store.py


from decimal import Decimal
from digital_wallet.constants import CATEGORIES as DEFAULT_CATEGORIES

# In-memory data store
data = {
    "accounts": {},
    "categories": list(DEFAULT_CATEGORIES)
}
