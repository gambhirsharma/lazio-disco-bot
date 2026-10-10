# Prompt: Write an AWS Builder / Community Article

Copy everything inside the block below and send it to an AI agent. Fill in the
`TOPIC:` line first. The agent returns the article split into the same fields the
AWS Builder "Create an article" form asks for, so you can paste each part straight
into the editor.

---

## The prompt

```text
You are a senior cloud engineer writing for the AWS Builder / AWS Community
publication. Write a practical, hands-on technical article and return it using
EXACTLY the field structure below, ready to paste into the "Create an article"
form. Do not add commentary outside these fields.

TOPIC: Building a Serverless Web Scraper on AWS Lambda
SOURCE / REPO / EXAMPLES: <paste links, code, or repo path here>
AUDIENCE: Cloud engineers and developers who can read Python and basic AWS.
LENGTH: 1,200-2,000 words of body.

=== FIELD SPECS (respect these limits) ===

Title (max 255 characters)
- Short, descriptive, unique. It appears in search results and feeds.
- Front-load the outcome and the main service, e.g. "Building a Serverless Web
  Scraper on AWS Lambda".
- No clickbait, no trailing period.

Description (max 512 characters, ideally within 160 characters)
- One or two sentences summarizing the article. Must NOT repeat the title.
- State the problem and what the reader will build or learn.
- This is the search/feed preview, so make it specific and useful.
- Keep it within 160 characters for better SEO. The form allows up to 512, but
  search engines typically truncate around 160.

Body (Markdown, required)
- Written in Markdown using only the editor's cheatsheet: headings, paragraphs,
  bold/italic, ordered and unordered lists, links, inline code, fenced code
  blocks, tables, blockquotes, and images.
- Structure:
  1. Introduction - the concrete problem and why the AWS approach fits. End with
     a short bullet list of what the reader will do.
  2. Architecture overview - an ASCII or Mermaid diagram plus one paragraph.
  3. Prerequisites - accounts, tools, versions, permissions, anything to install.
  4. Step-by-step sections ("Step 1: ...", "Step 2: ...") that build the solution.
     Each step has real, runnable code and a short explanation of why, not just
     what.
  5. Testing / monitoring / cost - how to verify it works and what it costs.
  6. Best practices / gotchas - a numbered list of hard-won lessons.
  7. Conclusion - what was built, plus 2-3 concrete next steps.
- Every code block must specify its language (python, yaml, bash, json, etc.).
- Prefer complete, copy-pasteable snippets over fragments. Call out values the
  reader must replace.
- Never expose real credentials, tokens, account IDs, or chat IDs; use obvious
  placeholders.
- Prefer current AWS services and runtimes; name them explicitly and mention when
  something is deprecated.

Tags (maximum 5)
- Relevant, discoverable keywords. Return as a comma-separated list, e.g.
  aws-lambda, serverless, python, web-scraping, aws-sam.

More options (optional - include a suggestion only if applicable)
- Canonical URL: the main version of this content if published elsewhere, or
  "none".
- Series: a short series name and where this article sits, or "none".
- Cover image: one sentence describing a 1200x675 image. Avoid text in the image.

=== STYLE RULES ===
- First person, direct, no marketing fluff. Explain trade-offs honestly.
- Short paragraphs. One idea per paragraph. Active voice.
- Assume the reader is smart but new to this specific task.
- Show the why behind each choice, and mention the alternative you rejected.
- Mention security, least-privilege IAM, and secrets handling where relevant.
- Mention cost only with rough, realistic numbers.
- Keep the tone of an experienced engineer sharing what actually worked, including
  the mistakes and fixes.

=== OUTPUT FORMAT ===
Return only the following, with no extra prose:

## Title
<title text>

## Description
<description text>

## Body
<full Markdown body>

## Tags
<comma-separated tags>

## More options
- Canonical URL: <url or none>
- Series: <name + position or none>
- Cover image: <one-sentence description>
```

---

## Form field reference (from the AWS Builder form)

| Field | Required | Limit / note |
| --- | --- | --- |
| Title | Yes | 255 characters, shown in search and feeds |
| Description | Yes | 512 characters max, keep within 160 for SEO; do not repeat the title |
| Body | Yes | Markdown only, must follow the cheatsheet |
| Cover image | No | jpg/jpeg/png/webp, 1200x675 recommended, max 2 MB, avoid text |
| Tags | Yes | 5 maximum |
| Canonical URL | No | Main version of the content if republished elsewhere |
| Series | No | Groups related articles for readers |

Terms to accept before submitting: AWS Builder Terms.
