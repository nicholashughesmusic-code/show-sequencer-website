# Show Arts Website

The public website for Show Arts and its first product, working name Show Sequencer.

This repository holds public website assets only. Application source, internal documentation and
specifications live elsewhere and are never copied here.

## Build

```bash
python3 build.py
```

This writes the site to `_site/`. It needs only Python 3. Open `_site/index.html` through a local
server so the root-relative links work:

```bash
python3 -m http.server --directory _site 8000
```

## Change the Product Name, Links or Launch State

Everything that changes between now and launch lives in `site.json`:

- `productName` and `productIsWorkingName`: the product's name everywhere on the site
- `betaFormUrl`, `updatesFormUrl`, `feedbackUrl`, `manualUrl`, `contactEmail`: shown only once set
- `launched`: while `false`, every page carries `noindex`, `robots.txt` blocks crawlers and a
  preview banner shows
- `siteUrl`: set to the custom domain (for example `https://show-arts.com`) to write the `CNAME` file

## Deploy

Every push to `main` builds and deploys to GitHub Pages (`.github/workflows/pages.yml`).

## Assets

- `assets/fonts/Anton-Regular.ttf` is the Anton typeface, under the SIL Open Font License
  (`assets/fonts/Anton-OFL.txt`)
- Screenshots are added here only once they have been taken for the website. The slots on each page
  say which are still to come

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
