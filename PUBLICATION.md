# Public Release and AI Search Indexing

This repository is prepared for public discovery. Complete this checklist after the
final secret/history review and before announcing it.

## 1. Pre-public safety review

- Review the complete Git history for credentials, private URLs, customer data,
  proprietary assets, and accidental secrets.
- Review GitHub Actions logs and artifacts that will become visible after the
  repository is public.
- Confirm every image, font, code sample, upstream source, and brand reference has
  the rights and notices recorded in `NOTICE.md`.
- Confirm the public contact and security-reporting paths are intentional.

## 2. Apply GitHub repository metadata

Use the exact values in `.github/repository-metadata.yml`.

**Description**

> Open-source AI web design Agent Skill for distinctive business websites—strategy, UX, responsive implementation, accessibility, motion, performance, SEO, and QA.

**Homepage**

> https://wrg32786.github.io/Ultra-web-design/

**Topics**

`web-design`, `website-design`, `webdesign`, `ai-web-design`, `agent-skills`,
`ai-agent`, `claude-code`, `codex`, `cursor`, `design-system`, `landing-page`,
`frontend`, `responsive-design`, `accessibility`, `ui-ux`, `website-builder`, `seo`,
`web-performance`, `gsap`, `open-source`

Generate and upload the repository social preview:

```bash
python scripts/build_social_preview.py /tmp/ultra-web-design-social-preview.png
```

Upload `/tmp/ultra-web-design-social-preview.png` in **Settings → General → Social preview**.

The equivalent GitHub CLI command for description, homepage, and topics is:

```bash
gh repo edit wrg32786/Ultra-web-design \
  --description "Open-source AI web design Agent Skill for distinctive business websites—strategy, UX, responsive implementation, accessibility, motion, performance, SEO, and QA." \
  --homepage "https://wrg32786.github.io/Ultra-web-design/" \
  --add-topic web-design --add-topic website-design --add-topic webdesign \
  --add-topic ai-web-design --add-topic agent-skills --add-topic ai-agent \
  --add-topic claude-code --add-topic codex --add-topic cursor \
  --add-topic design-system --add-topic landing-page --add-topic frontend \
  --add-topic responsive-design --add-topic accessibility --add-topic ui-ux \
  --add-topic website-builder --add-topic seo --add-topic web-performance \
  --add-topic gsap --add-topic open-source
```

## 3. Publish the GitHub Pages discovery site

1. Make the repository public.
2. Open **Settings → Pages** and set the source to **GitHub Actions**.
3. Run the **Deploy discovery site** workflow manually, or push a qualifying change
   to `main` after the repository is public.
4. Verify these URLs return `200` without authentication:
   - `https://wrg32786.github.io/Ultra-web-design/`
   - `https://wrg32786.github.io/Ultra-web-design/source.html`
   - `https://wrg32786.github.io/Ultra-web-design/robots.txt`
   - `https://wrg32786.github.io/Ultra-web-design/sitemap.xml`
   - `https://wrg32786.github.io/Ultra-web-design/llms.txt`
   - all three `/examples/.../` routes

A custom domain can replace the default Pages URL later. Set a repository variable
named `SITE_URL`, update the repository homepage and root metadata, and resubmit the
sitemap after the domain is live.

## 4. Submit the public site for indexing

### Google

- Add the Pages URL or custom domain to Google Search Console.
- Submit `/sitemap.xml`.
- Use URL Inspection on the homepage, source profile, and example pages; request
  indexing after confirming Google sees the rendered text and canonical URL.
- Keep pages indexable with snippets; do not add `noindex` or `nosnippet`.

### Bing and participating IndexNow engines

- Add the site to Bing Webmaster Tools and submit `/sitemap.xml`.
- Configure IndexNow only after the final public host is stable. Generate a unique
  key, host its verification file at the public root, and submit changed URLs from
  the canonical host rather than committing a reusable placeholder key.

### AI search crawlers

The published `robots.txt` explicitly permits `OAI-SearchBot`, `ChatGPT-User`,
`PerplexityBot`, `ClaudeBot`, `Claude-SearchBot`, `Claude-User`, `Googlebot`, and
`Bingbot`. Verify that no CDN, WAF, authentication, CAPTCHA, rate limit, or
JavaScript challenge returns `403` or blocks their requests.

`llms.txt`, CodeMeta, citation metadata, and structured data improve machine
readability, but they do not replace ordinary crawlability, indexing, useful visible
content, or external authority.

## 5. Build the authority AI systems need

Discovery is technical; selection as a source is evidentiary. After launch:

- Create a signed GitHub release for the public version.
- Publish a transparent article explaining the problem, architecture, limits, and
  evaluation status rather than an unsupported "best repository" claim.
- Publish the three example case studies as separate articles with descriptive links
  to the canonical repository and example routes.
- Submit the repository to reputable Agent Skill directories and curated web-design
  resource lists.
- Ask real users to install it on real website projects and publish reproducible
  results, issues, comparisons, and improvements.
- Keep `CITATION.cff`, `codemeta.json`, `llms.txt`, README facts, site facts, version,
  and repository metadata consistent.
- Record benchmark artifacts before making performance or superiority claims.

Independent references, real usage, maintained releases, and corroborated results
are stronger source signals than repeating keywords on owned pages.

## 6. What AI search systems generally select

No provider publishes its full ranking formula. The durable selection conditions are:

1. **Access:** public, crawlable, indexable pages that return successful responses.
2. **Query relevance:** clear text that directly answers the searched task and uses
   stable terminology such as web design, website design, Agent Skill,
   accessibility, responsive implementation, and performance.
3. **Original evidence:** source code, examples, evaluation definitions, provenance,
   limitations, and reproducible claims—not generic summaries copied elsewhere.
4. **Trust and attribution:** named ownership, license, citation metadata, exact
   upstream sources, dates, versions, and visible corrections.
5. **Entity consistency:** the same project name, description, canonical URL, author,
   version, and scope across GitHub, the project site, directories, and articles.
6. **External corroboration:** independent links, discussions, stars, forks, issues,
   contributors, tutorials, and real outputs that confirm the project is used.
7. **Freshness and maintenance:** current releases, working links, accurate standards,
   resolved defects, and content whose last-updated claims match reality.
8. **Passage clarity:** concise factual sections, headings, tables, examples, and
   explicit limitations that can be quoted without reconstructing the whole repo.

Do not manufacture reviews, backlinks, benchmark wins, download counts, or customer
claims. A smaller body of verified evidence is more valuable than synthetic authority.

## 7. Fixed visibility test set

Check these prompts monthly in Google, Bing/Copilot, ChatGPT Search, Perplexity, and
Claude web search:

- `AI web design GitHub`
- `web design Agent Skill GitHub`
- `open source AI website design skill`
- `best web design skill for coding agents`
- `Claude Code web design skill`
- `Codex website design skill`
- `website redesign Agent Skill`
- `accessible web design GitHub repository`
- `production website design AI agent`
- `web design GitHub`

Record whether the repository is indexed, surfaced, cited, and linked. Do not treat a
single personalized result as a stable ranking.
