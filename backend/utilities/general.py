import httpx
import asyncio

from backend.data.super_class import SupermarketChain


def run_async(coro, *args, **kwargs):
    """ Run an async coroutine in a synchronous context. """
    try:
        loop = asyncio.get_event_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

    # Always create the coroutine object first
    coro_obj = coro(*args, **kwargs)

    if loop.is_running():
        return asyncio.create_task(coro_obj)
    else:
        return loop.run_until_complete(coro_obj)


async def url_request(
    url: str = None,
    cookies: dict[str, str] | None = None,
    method: str = "GET",
    payload: dict | None = None,
    headers: dict[str, str] | None = None,
    client: httpx.AsyncClient | None = None,
) -> dict:
    """
    Use client provided or create a new client and make an async HTTP request (GET or POST)
    and safely return content or an error message.

    :param url: The URL to request.
    :param cookies: Optional cookies dictionary.
    :param method: "GET" (default) or "POST".
    :param payload: Data to send in POST body.
    :param headers: Optional request headers.
    :param client: Optional pre-configured httpx.AsyncClient.
    :return: {'response': content} or {'Error': message}.
    """
    # Reuse existing client if provided, otherwise create a new one
    owns_client = client is None

    if owns_client:
        client = httpx.AsyncClient(
            verify=False,
            cookies=cookies,
            timeout=httpx.Timeout(15.0),
        )

    else:
        # shared client → do NOT modify cookie jar if cookies is None
        if cookies:
            client.cookies.update(cookies)

    try:
        if method.upper() == "POST":
            response = await client.post(url, data=payload, headers=headers, )
        else:
            response = await client.get(url, headers=headers, )

        response.raise_for_status()
        return {"response": response.content}

    except httpx.HTTPStatusError as e:
        return {"Error": f"HTTP error: {e.response.status_code} - {e.response.text}"}
    except httpx.RequestError as e:
        return {"Error": f"Request error: {str(e)}"}

    finally:
        if owns_client:
            await client.aclose()


def get_chain_class_by_alias(alias: str):
    alias = alias.lower()
    for cls in SupermarketChain.registry:
        if getattr(cls, "alias", "").lower() == alias:
            return cls
    return None


def all_classes():
    return SupermarketChain.registry


