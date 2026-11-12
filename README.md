---
title: Fatima Digital Clone
emoji: 🤖
colorFrom: blue
colorTo: purple
sdk: gradio
sdk_version: 4.44.1
app_file: app.py
pinned: false
---
# Digital Clone - Hybrid RAG (BM25 + Dense + RRF)
**This is an AI clone, not the real person.** Pipeline: chunk (250 words, 40 overlap) -> BM25 + MiniLM embeddings (saved in embeddings.npy) -> Reciprocal Rank Fusion (1/(60+rank)) -> LLM answer in first person, grounded only in retrieved chunks.

## One-page report
**1. Knowledge base and why:** [List your files, e.g. bio, cv, opinions, project write-up, FAQ - and why you chose them.]

**2. Test questions**
| Question | BM25 result | Dense result | Hybrid result | Best mode and why |
|---|---|---|---|---|
| Q1 (exact rare keyword, e.g. project name) | | | | BM25 - exact word match |
| Q2 (paraphrase, no shared words) | | | | Dense - semantic match |
| Q3 | | | | |
| Q4 | | | | |
| Q5 | | | | |

**3. Failure case:** [Question, wrong/weak answer, and why it happened.]

**4. Improvement:** [e.g. add a cross-encoder reranker.]

*Note:* The other fusion method (weighted min-max: alpha*dense + (1-alpha)*bm25) was not used; it needs score normalization and a tuned alpha, while RRF only needs ranks.
