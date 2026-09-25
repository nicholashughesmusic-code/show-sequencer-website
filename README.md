# Show Arts Website

The public website for Show Arts and its first product, working name Show Sequencer.

This repository holds public website assets only. Application source, internal documentation and
specifications live elsewhere and are never copied here.

## Build

```bash
python3 build.py
```

Each page in `src/` builds to a folder named after its file, and a hyphen in that name becomes a
further folder: `feedback.html` builds to `/feedback/`, and `feedback-thanks.html` to
`/feedback/thanks/`.

This writes the site to `_site/`. It needs only Python 3. Serve it locally with the base path
set to an empty string in `site.json`, or preview it on GitHub Pages:

```bash
python3 -m http.server --directory _site 8000
```

## Change the Product Name, Links or Launch State

Everything that changes between now and launch lives in `site.json`:

- `productName` and `productIsWorkingName`: the product's name everywhere on the site
- `betaFormUrl`, `updatesFormUrl`, `manualUrl`, `contactEmail`: shown only once set
- `launched`: while `false`, every page carries `noindex`, `robots.txt` blocks crawlers and a
  preview banner shows
- `siteUrl`: set to the custom domain (for example `https://show-arts.com`) to write the `CNAME` file
- `basePath`: `/show-sequencer-website` while the site is served from GitHub's own address; set it to
  an empty string once `siteUrl` is the custom domain
- `siteOrigin`: the origin the site is served from, used where a link has to leave the site and come
  back as a full URL (the feedback form's redirect after sending). It changes at the same time as
  `siteUrl` and `basePath`

## Custom Domain

The domain is `showarttechnologies.com`, registered through GoDaddy (nameservers
`ns05`/`ns06.domaincontrol.com`). Note the spelling: the company is Show Arts Technologies, the
domain is `showart` singular.

**DNS first, then the repository.** Committing a `CNAME` file makes GitHub Pages set the custom
domain and start redirecting the `github.io` address to it, so doing that before DNS resolves
takes the working site down rather than moving it.

In GoDaddy's DNS panel, on the apex record (`@`), replace whatever is parked there with these four
A records, all four of them:

```
185.199.108.153
185.199.109.153
185.199.110.153
185.199.111.153
```

Optionally the same four as AAAA, for IPv6:

```
2606:50c0:8000::153
2606:50c0:8001::153
2606:50c0:8002::153
2606:50c0:8003::153
```

And one CNAME so `www` works too:

```
www  ->  nicholashughesmusic-code.github.io
```

Check it has taken with `dig +short showarttechnologies.com` - the four GitHub addresses rather
than the parked ones. Then set three values in `site.json` together, as the section above
describes, and push:

```json
"siteUrl":    "https://showarttechnologies.com",
"siteOrigin": "https://showarttechnologies.com",
"basePath":   ""
```

GitHub then issues the certificate itself, which takes a few minutes. Tick "Enforce HTTPS" in the
repository's Pages settings once it offers it.

## Deploy

Every push to `main` builds and deploys to GitHub Pages (`.github/workflows/pages.yml`).

## Assets

- `assets/fonts/Anton-Regular.ttf` is the Anton typeface, under the SIL Open Font License
  (`assets/fonts/Anton-OFL.txt`)
- Screenshots are added here only once they have been taken for the website. The slots on each page
  say which are still to come

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
