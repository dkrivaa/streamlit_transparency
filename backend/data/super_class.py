import httpx


class SupermarketChain:
    registry = []  # holds all subclasses automatically

    def __init_subclass__(cls, **kwargs):
        """Automatically register any subclass."""
        super().__init_subclass__(**kwargs)
        if cls is not SupermarketChain and not getattr(cls, 'abstract', False):  # avoid registering the abstract base itself
            SupermarketChain.registry.append(cls)

    @classmethod
    async def stores(cls, ):
        """ This function gets latest store list for the supermarket chain. """
        raise NotImplementedError("Subclasses must implement this method.")

    @classmethod
    async def prices(cls, store_code: int | str, ):
        """ This function gets latest price and promo files for relevant store for the supermarket chain. """
        raise NotImplementedError("Subclasses must implement this method.")

    @classmethod
    async def get_code(cls):
        """ Returns the code of the supermarket chain """
        return getattr(cls, 'chain_code', None)

    @classmethod
    async def get_alias(cls):
        """ Returns the code of the supermarket chain """
        return getattr(cls, 'alias', None)

    @classmethod
    async def get_url(cls):
        """ Returns the url of the supermarket chain """
        return getattr(cls, 'url', None)

    @classmethod
    async def get_link_type(cls):
        """ Returns the link type of the supermarket chain """
        return getattr(cls, 'link_type', None)

    @classmethod
    async def get_username(cls):
        """ Returns the username of the supermarket chain """
        return getattr(cls, 'username', None)

    @classmethod
    async def get_password(cls):
        """ Returns the password of the supermarket chain """
        return getattr(cls, 'password', None)

    @classmethod
    async def as_store_dict(cls, s: dict, **extra) -> dict:
        """Utility to standardize store output."""
        return {
            "chain_code": extra.get('chain_code') or await cls.get_code(),
            "chain_name": await cls.get_alias(),
            "subchain_code": extra.get('subchain_code') or s.get("SubChainID") or s.get("SUBCHAINID") or s.get(
                "SubChainId"),
            "subchain_name": extra.get('subchain_name') or s.get("SubChainName") or s.get("SUBCHAINNAME"),
            "store_code": s.get("StoreID") or s.get("STOREID") or s.get("StoreId"),
            "store_name": s.get("StoreName") or s.get("STORENAME"),
            "store_type": s.get("StoreType") or s.get("STORETYPE"),
            "address": s.get("Address") or s.get("ADDRESS"),
            "city": s.get("City") or s.get("CITY"),
            "zipcode": s.get("ZipCode") or s.get("ZIPCODE") or s.get("ZIPCode"),
        }


