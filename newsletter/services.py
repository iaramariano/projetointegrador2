import os
import httpx
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

BASE_URL = "https://connect.mailerlite.com/api"

class MailerLiteError(Exception):
    pass

def _get_api_key() -> str:
    api_key = getattr(settings, "MAILERLITE_API_KEY", "")
    if not api_key:
        raise ImproperlyConfigured("MAILERLITE_API_KEY não configurada (.env ou ambiente).")
    return api_key

def _get_group_id() -> str | None:
    # opcional: grupo pode ser None (só cria o subscriber)
    return getattr(settings, "MAILERLITE_NEWSLETTER_GROUP_ID", None) or os.environ.get("MAILERLITE_NEWSLETTER_GROUP_ID")

def subscribe_email(email: str, name: str | None = None, ip: str | None = None) -> dict:
    api_key = _get_api_key()
    group_id = _get_group_id()
    timeout = float(getattr(settings, "MAILERLITE_TIMEOUT", os.environ.get("MAILERLITE_TIMEOUT") or 6))

    payload = {
        "email": email,
        "fields": {"name": name} if name else {},
        "groups": [group_id] if group_id else [],
        "ip_address": ip,
    }
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "Accept": "application/json",
    }

    with httpx.Client(base_url=BASE_URL, headers=headers, timeout=timeout) as client:
        resp = client.post("/subscribers", json=payload)
    if resp.status_code not in (200, 201):
        raise MailerLiteError(f"MailerLite error {resp.status_code}: {resp.text}")
    return resp.json()
