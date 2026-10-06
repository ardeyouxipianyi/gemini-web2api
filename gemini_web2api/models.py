"""Model definitions and mapping from Gemini frontend StreamGenerate payloads."""

# Model selection uses TWO fields in the f.req inner array (decoded from live
# browser captures, Sep 2026):
#   inner[79] = family: 1=flash, 3=pro, 4=auto, 5=dynamic-thinking, 6=flash-lite
#   inner[80] = variant: 1=standard, 2=extended/thinking
# E.g. 3.1 Pro=(3,1), 3.1 Pro Extended=(3,2), Flash Extended=(1,2),
# Flash-Lite=(6,1), Flash-Lite Extended=(6,2).
# HOWEVER: the server only honors these fields when the request also carries
# the per-model ticket header X-Goog-Ext-525001261-Jspb (minted by the browser
# per model family; embeds family/variant in plaintext). Without the ticket
# the server falls back to the account default regardless of [79]/[80].
# The ticket wins over the body fields when both are present.
# Note: no field selects the exact 3.x point version within a family; the
# server picks its current default (e.g. requesting "3.5-flash" yields 3.6 Flash).

# Model list mirrors the Gemini web UI (Sep 2026): Flash 3.6 (+Extended) /
# Flash-Lite 3.5 (+Extended) / Pro 3.1 (+Extended). The "3.x" in the name is
# just a label — routing is decided by the ticket (family, variant), so the
# server serves its current family default regardless of point version.

TICKET_HEADER = "X-Goog-Ext-525001261-Jspb"

MODELS = {
    # Gemini 3.8
    "gemini-3.8-flash": {
        "mode": 1, "think": 4, "variant": 1, "ticket": "flash",
        "desc": "Alias of the Flash family (latest served Flash)",
    },
    "gemini-3.8-flash-high": {
        "mode": 2, "think": 0,
        "desc": "Latest all-around model with high thinking depth (Gemini 3.8 Flash High, ~20k chars)",
    },
    "gemini-3.8-flash-thinking": {
        "mode": 2, "think": 0,
        "desc": "Deep thinking mode (Gemini 3.8 Flash), longest output (~20k chars)",
    },
    "gemini-3.8-flash-thinking@think=0": {
        "mode": 2, "think": 0,
        "desc": "Gemini 3.8 Flash thinking mode - deepest reasoning (~20k chars)",
    },
    "gemini-3.8-flash-thinking@think=2": {
        "mode": 2, "think": 2,
        "desc": "Gemini 3.8 Flash thinking mode - medium reasoning (~15k chars)",
    },
    "gemini-3.8-flash-thinking@think=4": {
        "mode": 2, "think": 4,
        "desc": "Gemini 3.8 Flash thinking mode - shallowest reasoning (~12k chars)",
    },
    "gemini-3.8-flash@think=0": {
        "mode": 1, "think": 0,
        "desc": "Gemini 3.8 Flash with deep thinking (think=0)",
    },

    # Gemini 3.7
    "gemini-3.7-flash": {
        "mode": 1, "think": 4, "variant": 1, "ticket": "flash",
        "desc": "Alias of the Flash family (Gemini 3.7 Flash)",
    },
    "gemini-3.7-flash-high": {
        "mode": 2, "think": 0,
        "desc": "Gemini 3.7 Flash with high thinking depth (~20k chars)",
    },
    "gemini-3.7-flash-thinking": {
        "mode": 2, "think": 0,
        "desc": "Deep thinking mode (Gemini 3.7 Flash), longest output (~20k chars)",
    },
    "gemini-3.7-flash-thinking@think=0": {
        "mode": 2, "think": 0,
        "desc": "Gemini 3.7 Flash thinking mode - deepest reasoning (~20k chars)",
    },
    "gemini-3.7-flash-thinking@think=2": {
        "mode": 2, "think": 2,
        "desc": "Gemini 3.7 Flash thinking mode - medium reasoning (~15k chars)",
    },
    "gemini-3.7-flash-thinking@think=4": {
        "mode": 2, "think": 4,
        "desc": "Gemini 3.7 Flash thinking mode - shallowest reasoning (~12k chars)",
    },
    "gemini-3.7-flash@think=0": {
        "mode": 1, "think": 0,
        "desc": "Gemini 3.7 Flash with deep thinking (think=0)",
    },

    # Gemini 3.6
    "gemini-3.6-flash": {
        "mode": 1, "think": 4, "variant": 1, "ticket": "flash",
        "desc": "All-around model (Gemini 3.6 Flash)",
    },
    "gemini-3.6-flash-thinking": {
        "mode": 1, "think": 1, "variant": 2, "ticket": "flash-thinking",
        "desc": "Extended thinking on Flash (~20k chars)",
    },
    "gemini-3.6-flash-high": {
        "mode": 1, "think": 1, "variant": 2, "ticket": "flash-thinking",
        "desc": "Alias of gemini-3.6-flash-thinking",
    },
    "gemini-3.7-flash-high": {
        "mode": 1, "think": 1, "variant": 2, "ticket": "flash-thinking",
        "desc": "Flash extended thinking (3.7 name)",
    },
    "gemini-3.7-flash-thinking": {
        "mode": 1, "think": 1, "variant": 2, "ticket": "flash-thinking",
        "desc": "Flash extended thinking (3.7 name)",
    },
    "gemini-3.8-flash-high": {
        "mode": 1, "think": 1, "variant": 2, "ticket": "flash-thinking",
        "desc": "Flash extended thinking (3.8 name)",
    },
    "gemini-3.8-flash-thinking": {
        "mode": 1, "think": 1, "variant": 2, "ticket": "flash-thinking",
        "desc": "Flash extended thinking (3.8 name)",
    },
    "gemini-3.5-flash-lite": {
        "mode": 6, "think": 4, "variant": 1, "ticket": "lite",
        "desc": "Cost-efficient high-capacity model (Gemini 3.5 Flash-Lite)",
    },
    "gemini-3.5-flash-thinking-lite": {
        "mode": 5, "think": 1, "variant": 2, "ticket": "lite-thinking",
        "desc": "Extended thinking on Flash-Lite",
    },
    "gemini-3.1-pro": {
        "mode": 3, "think": 4, "variant": 1, "ticket": "pro",
        "desc": "Pro model (requires cookie for real routing)",
    },
    "gemini-3.1-pro-thinking": {
        "mode": 3, "think": 1, "variant": 2, "ticket": "pro-thinking",
        "desc": "Extended thinking on Pro",
    },
    "gemini-auto": {
        "mode": 4, "think": 4,
        "desc": "Auto: account default model (no ticket)",
    },
}

MODEL_ALIASES = {
    # Short names (pr-101), retargeted at the ticket-wired models above.
    "3.8-flash": "gemini-3.8-flash",
    "3.7-flash": "gemini-3.7-flash",
    "3.6-flash": "gemini-3.6-flash",
    "3.6-flash-thinking": "gemini-3.6-flash-thinking",
    "3.5-flash": "gemini-3.6-flash",
    "gemini-3.5-flash": "gemini-3.6-flash",
    "3.5-flash-lite": "gemini-3.5-flash-lite",
    "3.5-flash-thinking-lite": "gemini-3.5-flash-thinking-lite",
    "flash-lite": "gemini-3.5-flash-lite",
    "lite": "gemini-3.5-flash-lite",
    "pro": "gemini-3.1-pro",
    "pro-thinking": "gemini-3.1-pro-thinking",
    "pro-enhanced": "gemini-3.1-pro",
    "gemini-3.1-pro-enhanced": "gemini-3.1-pro",
    "auto": "gemini-auto",
    # Thinking-depth spellings from pr-101 ("-high" == extended thinking).
    "gemini-3.8-flash:high": "gemini-3.8-flash-high",
    "gemini-3.8-flash (high)": "gemini-3.8-flash-high",
    "gemini-3.8-flash-thinking-high": "gemini-3.8-flash-high",
    "gemini-3.8-flash-thinking-medium": "gemini-3.8-flash-thinking",
    "gemini-3.8-flash-thinking-low": "gemini-3.8-flash-thinking",
    "3.8-flash-high": "gemini-3.8-flash-high",
    "3.8 flash high": "gemini-3.8-flash-high",
    "3.8-flash-thinking": "gemini-3.8-flash-thinking",
    "gemini-3.7-flash:high": "gemini-3.7-flash-high",
    "gemini-3.7-flash (high)": "gemini-3.7-flash-high",
    "gemini-3.7-flash-thinking-high": "gemini-3.7-flash-high",
    "gemini-3.7-flash-thinking-medium": "gemini-3.7-flash-thinking",
    "gemini-3.7-flash-thinking-low": "gemini-3.7-flash-thinking",
    "3.7-flash-high": "gemini-3.7-flash-high",
    "3.7 flash high": "gemini-3.7-flash-high",
    "3.7-flash-thinking": "gemini-3.7-flash-thinking",
    "gemini-3.6-flash:high": "gemini-3.6-flash-high",
    "gemini-3.6-flash (high)": "gemini-3.6-flash-high",
    "gemini-3.6-flash-thinking-high": "gemini-3.6-flash-high",
    "gemini-3.6-flash-thinking-medium": "gemini-3.6-flash-thinking",
    "gemini-3.6-flash-thinking-low": "gemini-3.6-flash-thinking",
    "3.6-flash-high": "gemini-3.6-flash-high",
    "3.6 flash high": "gemini-3.6-flash-high",
    "gemini-3.5-flash-high": "gemini-3.6-flash-high",
    "gemini-3.5-flash:high": "gemini-3.6-flash-high",
    "gemini-3.5-flash-thinking": "gemini-3.6-flash-thinking",
    "gemini-3.5-flash-thinking-medium": "gemini-3.6-flash-thinking",
    "gemini-3.5-flash-thinking-low": "gemini-3.6-flash-thinking",
    "3.5-flash-thinking": "gemini-3.6-flash-thinking",
    "3.5-flash-high": "gemini-3.6-flash-high",
    "3.5 flash high": "gemini-3.6-flash-high",
}


def ticket_for(model_name: str):
    """Return the upstream ticket header value for a model, or None.

    Looks up the model's ticket key in CONFIG["model_tickets"]. Tickets only
    steer routing for a signed-in session, so anonymous requests get None:
    sending a captured ticket without a cookie makes upstream try to serve a
    family the anonymous session cannot use (empty or error responses).
    """
    from .config import CONFIG
    from .gemini import load_cookie
    if not load_cookie()[0]:
        return None
    cfg = MODELS.get(model_name) or {}
    key = cfg.get("ticket")
    if not key:
        return None
    return (CONFIG.get("model_tickets") or {}).get(key)


def resolve_model(model_name: str, default: str = "gemini-3.6-flash"):
    """Resolve model name to (name, mode_id, think_mode, error, extra_fields).

    Unknown model names fall back to default rather than erroring,
    since upstream clients may request arbitrary model identifiers.
    """
    from .gemini import load_cookie

    signed_in = bool(load_cookie()[0])
    original_name = model_name
    think_override = None
    if "@think=" in model_name:
        base_name, think_str = model_name.rsplit("@think=", 1)
        try:
            think_override = int(think_str)
            model_name = base_name
        except ValueError:
            return None, None, None, f"Invalid think level: {think_str}", None

    resolved_name = model_name
    if resolved_name not in MODELS:
        resolved_name = MODEL_ALIASES.get(model_name.lower().strip(), model_name)

    cfg = MODELS.get(original_name) or MODELS.get(resolved_name)
    if not cfg:
        from .gemini import log
        log(f"Unknown model '{original_name}', falling back to '{default}'")
        resolved_name = default
        cfg = MODELS[default]

    mode_id = cfg["mode"]
    think_mode = think_override if think_override is not None else cfg["think"]
    extra = dict(cfg.get("extra") or {})
    if "variant" in cfg and 80 not in extra and signed_in:
        # Anonymous sessions cannot route a variant; claiming one without a
        # ticket makes upstream reject or stall the request.
        extra[80] = cfg["variant"]
    # Return the canonical (alias-resolved) name: callers use it for the
    # per-model ticket lookup and the response echo.
    return resolved_name, mode_id, think_mode, None, extra or None
