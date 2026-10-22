# System Design — Scalable URL Shortener

## Requirements
Create a short code for a long URL, redirect users quickly, avoid collisions, and support high read traffic.

## Components
1. API layer validates URLs and rate-limits requests.
2. Code generator creates a random or encoded identifier.
3. Database maps `short_code -> long_url` with a unique index.
4. Cache stores popular mappings.
5. Redirect service checks cache, then database, and redirects.
6. Analytics queue processes click events asynchronously.

## Flows
**Create:** validate -> generate code -> insert mapping -> return short URL. If a collision occurs, retry with a new code.

**Redirect:** request -> cache lookup -> database fallback -> populate cache -> redirect.

## Trade-offs and risks
- Cache improves read latency but requires invalidation/expiry.
- Random codes are less predictable but may collide; unique constraints and retries help.
- A relational database provides constraints; a key-value store can suit simple high-volume lookups.
- Validate URL schemes, rate-limit creation, monitor abuse, and provide takedown/reporting.
- Track p50/p95/p99 latency, cache hit rate, redirect success rate, and database latency.
