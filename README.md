# Show Arts Website

The public website for Show Arts and its first product, working name Show Sequencer.

This repository holds public website assets only. Application source, internal documentation and
specifications live elsewhere and are never copied here.

## Build

```bash
python3 build.py
```

This writes the site to `_site/`. It needs only Python 3. Serve it locally with the base path
set to an empty string in `site.json`, or preview it on GitHub Pages:

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
- `basePath`: `/show-arts-website` while the site is served from GitHub's own address; set it to
  an empty string once `siteUrl` is the custom domain

## Deploy

Every push to `main` builds and deploys to GitHub Pages (`.github/workflows/pages.yml`).

## Assets

- `assets/fonts/Anton-Regular.ttf` is the Anton typeface, under the SIL Open Font License
  (`assets/fonts/Anton-OFL.txt`)
- Screenshots are added here only once they have been taken for the website. The slots on each page
  say which are still to come

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
