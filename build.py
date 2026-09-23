#!/usr/bin/env python3
"""Builds the site into _site/ from src/ and site.json. No dependencies beyond Python 3.

Every page in src/ may use:
  {{key}}              a value from site.json (productName, companyShort, ...)
  {{> name}}           src/partials/name.html
  {{#if key}}...{{/if}}  kept only when site.json's key is true or non-empty
  {{#unless key}}...{{/unless}}  kept only when it is false or empty
A page's first line may be <!-- title: ... | description: ... -->.
A page builds to a folder named after its file, and a hyphen in that name becomes a
further folder: feedback.html builds to /feedback/, feedback-thanks.html to /feedback/thanks/.
The product name lives only in site.json, so renaming the product is a one-line change.
"""
import hashlib, json, os, re, shutil, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC, OUT = os.path.join(ROOT, "src"), os.path.join(ROOT, "_site")

def load_site():
    with open(os.path.join(ROOT, "site.json")) as f:
        site = json.load(f)
    name = site["productName"]
    site["productFirstMention"] = name + (" (working name)" if site.get("productIsWorkingName") else "")
    site["productUpper"] = name.upper()
    site["year"] = "2026"
    site.setdefault("basePath", "")
    with open(os.path.join(ROOT, "assets", "css", "site.css"), "rb") as f:
        site["cssVersion"] = hashlib.sha1(f.read()).hexdigest()[:10]
    return site

def truthy(v):
    return bool(v) and v != "false"

def render(text, site, page):
    ctx = dict(site, **page)
    def partial(m):
        with open(os.path.join(SRC, "partials", m.group(1).strip() + ".html")) as f:
            return render(f.read(), site, page)
    text = re.sub(r"\{\{>\s*([\w-]+)\s*\}\}", partial, text)
    text = re.sub(r"\{\{#if (\w+)\}\}(.*?)\{\{/if\}\}", lambda m: m.group(2) if truthy(ctx.get(m.group(1))) else "", text, flags=re.S)
    text = re.sub(r"\{\{#unless (\w+)\}\}(.*?)\{\{/unless\}\}", lambda m: "" if truthy(ctx.get(m.group(1))) else m.group(2), text, flags=re.S)
    def value(m):
        key = m.group(1)
        if key not in ctx:
            sys.exit(f"Unknown placeholder {{{{{key}}}}} in {page['path']}")
        return str(ctx[key])
    return re.sub(r"\{\{(\w+)\}\}", value, text)

def main():
    site = load_site()
    if os.path.exists(OUT):
        shutil.rmtree(OUT)
    shutil.copytree(os.path.join(ROOT, "assets"), os.path.join(OUT, "assets"))
    for name in sorted(os.listdir(SRC)):
        if not name.endswith(".html"):
            continue
        with open(os.path.join(SRC, name)) as f:
            text = f.read()
        page = {"title": site["companyShort"], "description": "", "path": name, "nav": name[:-5]}
        head = re.match(r"<!--\s*title:\s*(.*?)\s*\|\s*description:\s*(.*?)\s*-->\n", text)
        if head:
            page["title"], page["description"] = head.group(1), head.group(2)
            text = text[head.end():]
        page["title"] = render(page["title"], site, page)
        page["description"] = render(page["description"], site, page)
        html = render(text, site, page)
        target = os.path.join(OUT, "index.html" if name == "index.html" else ("404.html" if name == "404.html" else os.path.join(*name[:-5].split("-"), "index.html")))
        os.makedirs(os.path.dirname(target), exist_ok=True)
        with open(target, "w") as f:
            f.write(html)
    robots = "User-agent: *\nAllow: /\n" if site.get("launched") else "User-agent: *\nDisallow: /\n"
    with open(os.path.join(OUT, "robots.txt"), "w") as f:
        f.write(robots)
    if site.get("siteUrl"):
        with open(os.path.join(OUT, "CNAME"), "w") as f:
            f.write(site["siteUrl"].replace("https://", "").strip("/") + "\n")
    print("Built", OUT)

if __name__ == "__main__":
    main()
