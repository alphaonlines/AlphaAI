#!/usr/bin/env python3
import argparse
import datetime as dt
import json
import sys
import textwrap
import urllib.parse
import urllib.request


DEFAULT_QUERY = "(AI OR robotics OR humanoid OR BCI OR Neuralink OR battery OR \"energy storage\") sourceCountry:US"


def build_url(query: str, maxrecords: int, sort: str, mode: str, format_: str) -> str:
    params = {
        "query": query,
        "mode": mode,
        "format": format_,
        "maxrecords": str(maxrecords),
        "sort": sort,
    }
    return "https://api.gdeltproject.org/api/v2/doc/doc?" + urllib.parse.urlencode(params)


def fetch_json(url: str, timeout: int = 20):
    req = urllib.request.Request(url, headers={"User-Agent": "AlphaAI-Timeline/1.0"})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        body = resp.read().decode("utf-8")
    return json.loads(body)


def parse_args():
    ap = argparse.ArgumentParser(
        description="Fetch recent AI/robotics/battery/BCI/eVTOL news via GDELT.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent(
            """\
            Examples:
              python3 fetch_gdelt.py
              python3 fetch_gdelt.py --query "(AI OR robotics) sourceCountry:US" --max 25
              python3 fetch_gdelt.py --as-timeline --max 10
            """
        ),
    )
    ap.add_argument("--query", default=DEFAULT_QUERY, help="GDELT query string.")
    ap.add_argument("--max", type=int, default=50, dest="maxrecords", help="Max records (<=250).")
    ap.add_argument("--sort", default="HybridRel", help="Sort order (e.g., HybridRel, Date).")
    ap.add_argument("--timeout", type=int, default=20, help="HTTP timeout seconds.")
    ap.add_argument(
        "--as-timeline",
        action="store_true",
        help="Emit schema-ready timeline JSON skeletons from results.",
    )
    return ap.parse_args()


def month_short_from_date(d: dt.datetime) -> str:
    return d.strftime("%b")


def normalize_date(val: str):
    if not val:
        return None
    for fmt in ("%Y-%m-%d", "%Y-%m-%d %H:%M:%S", "%Y%m%dT%H%M%SZ"):
        try:
            return dt.datetime.strptime(val[: len(fmt)], fmt)
        except ValueError:
            continue
    return None


def main():
    args = parse_args()
    if args.maxrecords > 250:
        print("GDELT maxrecords caps at 250; clamping.", file=sys.stderr)
        args.maxrecords = 250

    url = build_url(args.query, args.maxrecords, args.sort, "ArtList", "json")
    try:
        payload = fetch_json(url, timeout=args.timeout)
    except Exception as e:
        print(f"Failed to fetch GDELT: {e}", file=sys.stderr)
        print(url, file=sys.stderr)
        sys.exit(1)

    articles = payload.get("articles") or []
    if not articles:
        print("No articles returned.", file=sys.stderr)
        sys.exit(0)

    if not args.as_timeline:
        for i, a in enumerate(articles, 1):
            title = (a.get("title") or "").strip()
            src = (a.get("sourceCommonName") or a.get("domain") or "").strip()
            url = a.get("url") or ""
            date = a.get("seendate") or a.get("date") or ""
            print(f"{i:02d}. {title}")
            if src or date:
                print(f"    {src} — {date}")
            print(f"    {url}")
        return

    # Timeline skeleton output
    out = []
    for a in articles:
        title = (a.get("title") or "").strip()
        url = a.get("url") or ""
        date_raw = a.get("seendate") or a.get("date") or ""
        d = normalize_date(date_raw) or dt.datetime.utcnow()
        out.append(
            {
                "year": d.year,
                "month": month_short_from_date(d),
                "title": title,
                "visual": "✨",
                "summary": "",
                "why": "",
                "market_analysis": "",
                "products": [],
                "wiki_url": "",
                "news_url": url,
            }
        )

    print(json.dumps(out, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()

