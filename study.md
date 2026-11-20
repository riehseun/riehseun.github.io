# Schedule 2027

- Winter: 1/4, 1/11, 1/18, 1/25, 2/1, 2/8, 2/15, 2/22, ~3/1~, ~3/8~, ~3/15~, ~3/22~, ~3/29~ (7 weeks to work, 5 weeks vacation)
- Spring: 4/5, 4/12, 4/19, 4/26, 5/3, 5/10, 5/17, ~5/24~, 5/31, 6/7, 6/14, 6/21, ~6/28~ (11 weeks to work, 2 weeks vacation)
- Summer: 7/5, 7/12, 7/19, 7/26, ~8/2~, 8/9, 8/16, 8/23, 8/30, ~9/6~, 9/13, 9/20, 9/27 (11 weeks to work, 2 weeks vacation)
- Fall: 10/4, ~10/11~, 10/18, 10/25, 11/1, 11/8, 11/15, 11/22, 11/29, 12/6, 12/13, ~12/20~, ~12/27~ (10 weeks to work, 3 week vacation)

## Rules
- Quarterly iteration
- Vacations, weeks with holidays, year ends are excluded


# DATA STRUCTURE AND ALGORITHM (50%)

| Day | Time | Plan |
|---|---|---|
| MTWRF | 7AM - 9AM | pick 3 Type Ⅰ + 1 Type II per day |

## Rules
- If failed problems are in the backlog and due on that day, do them first
- For new problems, pick a topic first (weighted by tier - 50/35/15/0), then randomly pick unsolved problem inside that row
- Failed problems are backlogged and retried exactly a week later
- Failed if the problem does not pass Leetcode submit or overtime (15 mins for easy/medium, 30 mins for hard)

## Type Ⅰ
| Topic | Problems |
|---|---:|
| Arrays & Hashing (Prefix Sum, String) | Tier 1 - Neet 250 |
| Two Pointers | Tier 1 - Neet 250 |
| Stack | Tier 2 - Neet 150 |
| Binary Search | Tier 1 - Neet 250 |
| Sliding Window | Tier 1 - Neet 250 |
| Linked List | Tier 2 - Neet 150 |
| Tree (DFS, BFS) | Tier 1 - Neet 250 |
| Heap | Tier 1 - Neet 250 |
| Graph (DFS, BFS, Topological Sort, Union Find) | Tier 1 - Neet 250 |
| 1D DP | Tier 2 - Neet 150 |
| Interval | Tier 1 - Neet 250 |
| Greedy | Tier 2 - Neet 150 |
| Advanced Graph (Dijkstra, Bellman-Ford, Prim, Hierholzer) | Tier 3 - Neet 150 |
| 2D DP | Tier 3 - Neet 150 |
| Trie | Tier 3 - Neet 150 |
| Backtracking | Tier 3 - Neet 150 |
| Math & Geometry | Tier 4 / Out of Scope |
| Bit Manipulation | Tier 4 / Out of Scope |

## Type II
| Topic | Problems |
|---|---:|
| Rate limiter | Tier 1 - 359, 362, 933, 346, 1797 |
| LRU cache with TTL, thread-safe | Tier 1 - 146, 460 |
| Micro-batching collector | Tier 2 |
| DAG task executor | Tier 1 - 207, 210, 1136, 2050, 2115, 269 |
| Worker pool / bounded queue | Tier 1 - 1188, 1114, 1115, 1116, 1195, 1226, 1242 |
| KV store with transactions | Tier 2 - 588, 1166, 2043, 380, 1146 |
| Time-versioned KV store | Tier 2 - 981, 2034 |
| Retry, backoff, circuit breaker | Tier 2 |
| Request router / load balancer | Tier 2 - 1882, 1606, 528, 2402 |
| Log / metrics aggregator | Tier 2 - 347, 692, 295, 480, 239, 1396, 636, 635 |
| Job scheduler with priorities and resources | Tier 1 - 621, 1834, 253, 1235, 2365, 2502, 3408 |
| Debug a broken codebase | Tier 2 |


# BEHAVIORAL (10%)

| Day | Time | Plan |
|---|---|---|
| M | 5PM - 7PM | practice 4 themes per day |

## Rules
- Pick a topic (weighted by tier - 60/40)
- Use max 10 stories to cover all topics
- Use stories in different angle for different topics
- Use recent stories only Autodesk (2026.10-Presnet), TD Securities (2025.08-2026.09), Layer6 AI (2021.01-2025.07)

## Theme
| Theme |
|---|
| Ownership - Tier 1 |
| Conflict - Tier 1 |
| Leadership / Influence without authority - Tier 2 |
| Mentorship - Tier 2 |
| Ambiguity - Tier 1 |
| Challenge - Tier 1 |
| Impact - Tier 1 |
| Failure - Tier 2 |
| Risk - Tier 2 | 
| Trade-off - Tier 2 |
| Production Incident - Tier 2 |
| Project Deepdive - Tier 1 |


# SYSTEM DESIGN (20%)

| Day | Time | Plan |
|---|---|---|
| WF | 5PM - 7PM | practice 1 problem per day |

## Rules
- Each problem gets 1 review day before practice begins
- If failed problems are in the backlog and due on that day, do them first
- For new problems, pick a topic by tier weight - 60/40
- Failed problems are backlogged and retried exactly a week later
- Failed if the problem gets below 9/10 when graded by Claude targeting Senior Bar or gets below 9/10 on 10 follow up questions 

## Table of Contents

1. [Distributed Job Scheduler & Message Queue - Tier 2](#1-distributed-job-scheduler)
2. [Distributed Cache & KV Store - Tier 2](#2-distributed-cache)
3. [Distributed Rate Limiter & API Gateway - Tier 1](#3-distributed-rate-limiter)
4. [Metrics, Logging, and Monitoring Platform - Tier 1](#4-metrics-logging-and-monitoring-platform)
5. [Cross-Cutting Themes](#5-cross-cutting-themes)

---

## 1. Distributed Job Scheduler

**Core model:** A job API (create/cancel/pause/status) writes a job definition plus runs to durable storage. A scheduler decides when runs become eligible, a queue holds ready work, and workers execute it.

| Topic | Details |
|---|---|
| Job API | Separate *job definition* (cron expression, payload, retry policy) from *job run* (one execution instance). Use idempotency keys on submission. |
| DAG dependencies | Store edges and track per-node state (pending, ready, running, succeeded, failed, skipped). A node is ready when all upstream nodes succeed. Detect cycles at submit time. Define failure semantics (fail-fast, continue independent branches, trigger rules). |
| Queueing | Separate queues or priority lanes. The durable store (DB or log) is the source of truth; the queue is an optimization. |
| Worker leasing | Workers claim a job with a time-bound lease and renew it via heartbeat. Expired leases are reclaimed. Use **fencing tokens** so a zombie worker cannot commit results after losing its lease. |
| Retries | Exponential backoff with jitter, max attempts, error classification (retryable vs. permanent), then a dead-letter state. |
| Priorities | Priority queues risk starvation. Use aging or weighted fair queuing. |
| Multi-tenant fairness | Per-tenant concurrency quotas, weighted or deficit round robin across tenants, and noisy-neighbor isolation (separate pools for large tenants). |
| Delivery semantics | True exactly-once execution is impossible in general. Use **at-least-once delivery + idempotent handlers** (or transactional outbox / dedupe tables) for effectively-once. |
| Duplicate execution | Causes: lease expiry during a slow job, network partition, scheduler failover double-firing. Mitigate with fencing tokens, a unique constraint on `(job_id, scheduled_time)`, and idempotency keys. |
| Stuck leases | Heartbeat timeouts, a reaper process, max-runtime limits, and distinguishing "slow" from "dead". |
| Thundering herd (cron boundaries) | Everyone schedules at `:00`. Use jittered start times, spread-out scheduling windows, rate-limited dispatch, and pre-enqueueing with staggered release. |
| Backfills | Run in a separate low-priority lane with their own concurrency cap. Partition by time window, keep them idempotent and resumable, and don't let them starve live jobs. |

**Scheduler HA:** Leader election (etcd/ZooKeeper) or schedulers partitioned by hash of job ID. Dedupe still matters during failover.

---

## 1. Distributed Message Queue

| Topic | Details |
|---|---|
| Partitioning | A topic is split into partitions for parallelism. The partition key (hash) determines placement. |
| Ordering | Guaranteed only *within a partition*. Same key maps to the same partition. Global ordering means one partition, which kills throughput. |
| Consumer groups | Each partition is consumed by exactly one consumer per group, so max parallelism equals partition count. Different groups read independently. |
| Offsets | Per-partition position committed by consumers. Commit after processing = at-least-once. Commit before = at-most-once. Exactly-once needs transactions or idempotent sinks. |
| Replication | Leader/follower per partition, an ISR (in-sync replica) set, and `acks` (0/1/all) with `min.insync.replicas` trading durability vs. latency. Leader failover via controller or consensus. |
| Retention | Time- or size-based (or log compaction by key). Retention enables replay. |
| DLQ | Messages failing after N retries go to a dead-letter queue for inspection and reprocessing. Keep error metadata with them. |
| Backpressure | Pull-based consumption is naturally self-throttling. Use bounded buffers, producer quotas, and lag monitoring. Pause consumption when downstream is slow. |
| Rebalancing | Consumers joining or leaving triggers partition reassignment and pauses. Mitigate with cooperative/incremental rebalancing, static membership, and sensible session timeouts. |
| Ordering vs. throughput | Retries can break ordering (B succeeds while A retries). Options: block the partition, use retry topics (loses order), or check sequence numbers. |
| Replay | Reset offsets to a timestamp or position. Requires idempotent consumers. |
| Poison messages | One bad message can block a partition. Detect via retry count, skip to DLQ, and validate schemas up front. |

---

## 2. Distributed Cache

| Topic | Details |
|---|---|
| Consistent hashing | Minimizes key movement when nodes join or leave. Virtual nodes smooth distribution and handle heterogeneous capacity. |
| Replication | Primary/replica for read scaling and availability. Async replication means possible stale reads and loss on failover. |
| Quorum | With N replicas, `R + W > N` gives strong-ish consistency. Lower values favor latency and availability. |
| Eviction | LRU, LFU, FIFO, random, or TTL-based. LFU resists scan pollution. Memory limit and eviction policy interact with TTLs. |
| TTL | Add jitter to avoid synchronized expiry. |
| Invalidation | The hard problem. Options: TTL only, write-through, write-behind, cache-aside with delete-on-write, event-driven (CDC). Delete-on-write races (stale value re-populated after delete) can be handled with versioning or a short delayed double-delete. |
| Hot-key mitigation | Replicate hot keys across nodes, add a local in-process (L1) cache, split keys with suffixes, use request coalescing. |
| Stampedes (dogpile) | Many requests miss at once. Use single-flight / request coalescing, mutex or lease on regeneration, probabilistic early refresh, stale-while-revalidate, TTL jitter. |
| Leader election & split brain | Needed for primary selection (Raft, Sentinel, ZooKeeper). Prevent split brain with quorum-based election, fencing, and epoch numbers. Minority partitions should stop accepting writes if consistency matters. |
| Consistency model choice | Caches are usually eventually consistent. Choose by cost of staleness: strong for inventory and balances (or bypass the cache), eventual for feeds and profiles. |

**Also consider:** negative caching (cache "not found" briefly), cache warming, and cold-start protection.

---

## 2. Distributed KV Store (Dynamo-style)

**Core model:** Keys are partitioned across nodes with consistent hashing. Each key is replicated to N nodes. Reads and writes use tunable quorums. Conflicts are resolved with versioning. This is the AP-leaning design, and it contrasts with a Raft-based CP store (below).

| Topic | Details |
|---|---|
| Partitioning | Consistent hashing with virtual nodes for even load and easy rebalancing. A coordinator (any node or a client library) routes by key. |
| Replication | Each key lives on N successive nodes (the preference list), ideally across failure domains (racks, zones). |
| Tunable quorums | W acknowledgements for writes, R for reads. `R + W > N` gives overlap (strong-ish). `W = 1` is fast and risks loss, `R = 1` is fast and risks staleness. |
| Failure handling | **Sloppy quorum and hinted handoff:** if a replica is down, another node accepts the write and hands it back later. Improves availability, weakens consistency. |
| Conflict resolution | Last-write-wins (simple, can lose writes, needs good clocks) vs. vector clocks (detect concurrent writes, push reconciliation to the app) vs. CRDTs (merge automatically). |
| Anti-entropy | **Read repair** fixes stale replicas on reads. **Merkle trees** compare replicas efficiently in the background. |
| Membership and failure detection | Gossip protocol for membership. Accrual failure detectors (e.g. phi accrual) avoid hard timeouts. |
| Storage engine | **LSM tree:** write-ahead log, memtable, immutable SSTables, compaction, bloom filters to skip files. Good for writes. B-tree engines favor reads and in-place updates. |
| Compaction and tombstones | Deletes write tombstones that must live long enough to reach all replicas, or deleted data reappears. Watch write and space amplification. |
| TTL | Store expiry with the value, clean up in compaction. |
| Hot keys and hot partitions | Split hot ranges, replicate more, add a front-line cache, salt keys. |
| Rebalancing | Move virtual nodes gradually, throttle streaming to protect foreground traffic. |
| Multi-region | Local quorums per region with async cross-region replication, or a globally consistent store (higher latency). Decide per dataset. |
| Operations | Rolling upgrades, backups and snapshots, capacity monitoring, repair schedules. |

**CP alternative (etcd / Spanner-style):** data is range-partitioned, each range is a Raft group with a leader, writes go through the leader and commit by majority, ranges split when large, and cross-range transactions need two-phase commit. Stronger consistency, higher write latency, and a minority partition becomes unavailable. State clearly which you choose and why.

---

## 3. Distributed Rate Limiter

### Algorithms

| Algorithm | Pros | Cons |
|---|---|---|
| Token bucket | Allows bursts, simple, cheap state | Burst can briefly exceed steady rate |
| Leaky bucket | Smooth output | No burst tolerance |
| Fixed window | Simplest | Boundary spikes (up to 2x at window edges) |
| Sliding window log | Exact | High memory per key |
| Sliding window counter | Good approximation, low memory | Approximate |

### Key Details

| Topic | Details |
|---|---|
| Central vs. local counters | Central (Redis) is accurate but adds latency and a dependency. Local is fast but can over-admit by roughly N times across N nodes. Hybrid: local token leases from a central store, synced periodically, trading bounded error for speed. |
| Per-tenant / per-key limits | Hierarchical limits (global, tenant, user, endpoint, IP). Key design: `limit:{tenant}:{route}:{window}`. Return `429` with `Retry-After` and rate-limit headers. |
| Atomicity | Use Redis Lua scripts (or `INCR` + `EXPIRE` carefully) to avoid races. |
| Fail-open vs. fail-closed | Fail-open preserves availability (typical for general APIs). Fail-closed protects the backend (auth, payments, expensive ops). Decide per endpoint, with a local fallback limiter as a safety net. |
| Clock skew | Don't rely on client or node clocks. Use Redis server time or monotonic logic, and keep windows loose enough that skew doesn't matter. |
| Hot keys | One abusive key can overload a Redis shard. Mitigate with local pre-aggregation, key sharding with split counters, or edge-level blocking. |
| Redis failover | Async replication can lose recent counts, causing brief over-admission (usually acceptable). Plan for reconnect storms; use Redis Cluster for scale. |
| Burst handling | Tune bucket capacity vs. refill rate. Consider separate burst and sustained limits. Add queueing or load shedding for overflow. |

---

## 3. API Gateway

**Core model:** A **data plane** (stateless proxies at the edge) handles every request. A **control plane** stores routes, policies, and keys and pushes configuration to the proxies. Keep them separate so a control-plane outage doesn't stop traffic.

| Topic | Details |
|---|---|
| Routing | Match by host, path, method, headers. Version routing and weighted routing for canary and blue/green. |
| Authentication | Validate JWTs locally (cached keys), API keys (hashed, looked up in a cache), mTLS for service-to-service. Check expiry, audience, and scopes. |
| Authorization | Coarse checks at the gateway (scopes, tenant), fine-grained checks in the service. |
| Rate limiting and quotas | Local counters plus a central store for global limits (see the rate limiter notes). Return `429` with `Retry-After`. |
| TLS termination | Terminate at the edge, re-encrypt to backends if required. Automate certificate rotation. |
| Load balancing and health checks | Round robin, least requests, consistent hashing. Active and passive health checks, outlier ejection. |
| Retries and timeouts | Retry only idempotent calls, with a retry budget and jitter. Set per-route timeouts and propagate deadlines. Avoid retry amplification. |
| Circuit breaking | Trip on error rate or latency, fail fast, probe to recover. |
| Request and response transformation | Header rewrites, payload limits, protocol translation (REST to gRPC). Keep heavy logic out of the hot path. |
| Caching | Cache idempotent GETs with correct keys, `Vary`, and TTL. Invalidate on writes where needed. |
| Config distribution | Push updates (xDS-style) or poll. Roll out gradually, validate before applying, and support rollback. Proxies keep serving with last-known-good config if the control plane is down. |
| Observability | Access logs, metrics (RED: rate, errors, duration), distributed tracing with propagated trace IDs. Sample logs at high volume. |
| Security | WAF rules, DDoS protection at the edge, payload size limits, bot detection, secret handling. |
| Multi-tenancy | Per-tenant limits, isolation of noisy tenants, per-tenant metrics and billing. |
| Extensibility | Plugins or filters (Lua, WASM), sandboxed and time-limited so a bad plugin can't break the proxy. |
| High availability | Stateless proxies across zones, health-checked by a load balancer or anycast/DNS, rolling updates with connection draining. |
| Latency budget | The gateway should add a few milliseconds. Avoid synchronous calls to remote services on the hot path. |

---

## 4. Metrics, Logging, and Monitoring Platform

### Push vs. Pull

| | Pull (Prometheus-style) | Push (StatsD / OTLP / agent) |
|---|---|---|
| Health detection | Failed scrape = target down | Needs separate heartbeat |
| Short-lived jobs | Poor fit (needs a gateway) | Good fit |
| Firewall / NAT | Harder | Easier |
| Control | Central controls scrape rate | Clients control rate |
| Service discovery | Required | Not needed |

### Key Details

| Topic | Details |
|---|---|
| Agent-based collection | A local agent or sidecar (Fluent Bit, OTel Collector, Telegraf) tails logs, scrapes local endpoints, enriches with metadata (host, pod, tenant), and forwards. Decouples apps from backends and centralizes retries and config. |
| Batching and buffering | Batch by size and time for throughput and compression. Use in-memory buffers with optional disk spooling for durability across restarts and outages. Tradeoff: bigger batches mean higher latency and more loss on crash. |
| Backpressure and ingestion throttling | Bounded queues at every hop. When full: drop (oldest, newest, or low-priority), block, or sample. Apply per-tenant ingestion quotas, return `429` with retry hints, and use exponential backoff with jitter on clients. Prioritize critical signals (errors, SLO metrics) over debug logs. |
| Pipeline shape | Agent → Kafka-like buffer → stream processors (aggregation, downsampling) → storage (TSDB for metrics, columnar or inverted-index store for logs, trace store). The queue absorbs spikes and decouples ingest from storage. |
| Cardinality control | High-cardinality labels (user ID, request ID) can blow up a TSDB. Enforce label limits and guards. |
| Retention and downsampling | Hot/warm/cold tiers, with rollups for older metrics. |
| Alerting | Evaluate rules on a separate, highly available path. Dedupe, group, and silence alerts. Monitor the monitor with a dead-man's-switch alert. |
| Reliability | Telemetry must not take down production. Use non-blocking client libraries and drop rather than block the app. |

---

## 5. Cross-Cutting Themes

- **Idempotency + at-least-once** beats chasing exactly-once (scheduler, queue, cache invalidation).
- **Leases, fencing tokens, and epochs** solve zombie and split-brain problems (scheduler, cache, queue leaders).
- **Jitter** prevents synchronization (cron herds, TTL expiry, retry storms, rate-limit resets).
- **Hot keys and noisy neighbors** require per-key and per-tenant isolation everywhere.
- **Backpressure and load shedding** need explicit, bounded policies at every boundary.
- **Fail-open vs. fail-closed** should be decided per component by the cost of failure.



# MACHINE LEARNING SYSTEM DESIGN (20%)

| Day | Time | Plan |
|---|---|---|
| TR | practice 1 problem per day |

## Rules
- Each problem gets 1 review day before practice begins
- If failed problems are in the backlog and due on that day, do them first
- For new problems, pick a topic by tier weight - 60/40
- Failed problems are backlogged and retried exactly a week later
- Failed if the problem gets below 9/10 when graded by Claude targeting Senior Bar or gets below 9/10 on 10 follow up questions 

## Table of Contents

1. [Model Serving - Tier 1](#1-model-serving)
2. [LLM Serving - Tier 1](#2-llm-serving)
3. [Agentic Platform - Tier 1](#3-agentic-platform)
4. [Model Training - Tier 2](#4-model-training)
5. [Feature Store - Tier 2](#5-feature-store)
6. [Chatbot & RAG & Knowledge Base - Tier 2]
7. [Cross-Cutting Themes](#7-cross-cutting-themes)

---

## 1. Model Serving

**Core model:** A control plane manages models, versions, deployments, and routing. A data plane (gateway, queues, serving nodes) handles inference traffic. Keep them separate so a control-plane outage never stops inference.

### Deployment and Lifecycle

| Topic | Details |
|---|---|
| Artifact distribution | Store versioned artifacts in object storage and pull to nodes through a local cache or P2P/CDN layer. Verify checksums, and pre-stage artifacts before traffic shifts. |
| Cold starts and warm-up | Cold start = download + load weights + init runtime + compile/JIT. Mitigate with pre-pulled images, warm pools, snapshotting, and synthetic warm-up requests that exercise common shapes and kernels. |
| Readiness management | Separate **liveness** (process alive) from **readiness** (model loaded and warmed). Only route traffic after readiness passes. Use startup probes for slow loads. |
| Model versioning and compatibility | Immutable versions, pinned input/output schemas, and explicit compatibility checks (feature schema, tokenizer, preprocessing). Support multiple versions side by side. |
| Canary, rollback, traffic shifting | Shift traffic gradually (1% → 10% → 50% → 100%). Automated canary analysis compares latency, errors, and quality metrics against baseline, with automatic rollback on regression. |
| Shadow and A/B | Shadow = mirror traffic, discard responses, compare offline (no user risk, but doubles load). A/B = split real traffic with statistical rigor and sticky assignment by user or key. |

### Request Path and Overload

| Topic | Details |
|---|---|
| Admission control and prioritization | Reject or defer work early when capacity is exceeded. Priority classes (interactive > batch), per-tenant quotas, and weighted fair queuing. |
| Queue management and backpressure | Bounded queues sized by latency budget (Little's Law), not memory. Prefer LIFO or drop-oldest under overload so stale requests don't waste capacity. Propagate backpressure upstream. |
| Overload protection and load shedding | Shed low-priority or doomed requests first. Return `429`/`503` with `Retry-After`. Adaptive concurrency limits based on observed latency. |
| Deadlines, timeouts, cancellation | Propagate a deadline end to end. Drop requests whose deadline has passed before running them. Cancel in-flight work when the client disconnects. |
| Circuit breakers and fallbacks | Trip on error rate or latency. Fall back to a smaller or distilled model, cached results, or a rules-based default. Degrade gracefully and expose the degraded state. |
| Health checks | Deep checks (run a tiny inference) vs. shallow checks (port open). Avoid health checks that cascade failures or take nodes out all at once. |

### Performance

| Topic | Details |
|---|---|
| Latency metrics | Track P50, P95, P99 separately. Tail latency comes from queueing, GC pauses, batching delay, noisy neighbors, and stragglers. |
| Tail-latency optimization | Hedged requests (carefully, with budgets), right-sized batches, request isolation, pinned CPU/GPU resources, and avoiding head-of-line blocking. |
| Throughput vs. latency | Bigger batches raise throughput and GPU utilization but add wait time. Pick the batch size and max-wait from the latency SLO. |
| Dynamic batching | Collect requests until max batch size or max delay. Group by shape/length to reduce padding. Separate queues for latency-sensitive traffic. |
| GPU/CPU utilization and memory | Watch GPU utilization, memory bandwidth, host-to-device copies, and pre/post-processing on CPU (often the real bottleneck). Use multi-model packing, MIG/MPS, and pinned memory. |

### Scaling and Multi-Tenancy

| Topic | Details |
|---|---|
| Autoscaling | Scale on queue depth, concurrency, or GPU utilization, not CPU alone. Account for slow scale-up (cold starts) with headroom or predictive scaling. |
| Scale-to-zero trade-offs | Saves cost for rarely used models but adds cold-start latency on first request. Fine for batch and internal tools, risky for latency-sensitive paths. Use min replicas or warm pools for critical models. |
| Quotas, isolation, fairness | Per-tenant rate and concurrency quotas, dedicated pools for large tenants, weighted fair scheduling, and per-tenant metrics. |
| Noisy-neighbor mitigation | Resource limits, separate queues, GPU partitioning, and eviction of abusive tenants' work first under pressure. |

---

## 2. LLM Serving

**Key framing:** Prefill is **compute-bound** (processes the whole prompt in parallel). Decode is **memory-bandwidth-bound** (one token at a time, reading all weights and the KV cache each step).

### Hardware and Memory

| Topic | Details |
|---|---|
| Compute vs. bandwidth bottlenecks | Decode throughput ≈ memory bandwidth ÷ bytes read per token. Batching amortizes weight reads across requests, which is why batching matters so much for decode. |
| GPU memory hierarchy | Registers → shared memory/SRAM → L2 → HBM → host RAM → NVMe. Performance depends on keeping data in fast tiers. |
| KV cache estimation | `2 × layers × kv_heads × head_dim × bytes_per_elem × tokens` per sequence. Grouped-query attention (fewer KV heads) shrinks this significantly. Total KV memory = per-token size × tokens in flight. |
| KV allocation, paging, eviction, fragmentation | Contiguous allocation wastes memory through internal and external fragmentation. **PagedAttention** uses fixed-size blocks with a block table, enabling near-zero waste, sharing across requests, and flexible eviction or swap. |

### Scheduling and Batching

| Topic | Details |
|---|---|
| Continuous batching | Add and remove sequences at every decode step instead of waiting for a whole batch to finish. Greatly improves utilization over static batching. |
| Prefix caching | Reuse KV blocks for shared prefixes (system prompts, few-shot examples, multi-turn history). Hash blocks by token content. Cuts TTFT and compute. |
| Chunked prefill | Split long prompts into chunks interleaved with decode steps so long prefills don't stall other users' token generation. |
| Prefill/decode disaggregation | Run prefill and decode on separate GPU pools tuned for their bottleneck. Cost: KV cache transfer between pools, so it needs fast interconnect. |
| Scheduling, admission, priority, preemption | Admit based on available KV blocks and token budget. Priority classes and fairness. Preempt by swapping KV to host memory or recomputing later. |
| Context limits and token budgeting | Enforce max input + output tokens per request and per tenant. Reserve KV capacity based on `max_tokens` or use optimistic allocation with preemption. |

### Model-Level Optimizations

| Topic | Details |
|---|---|
| FlashAttention | Tiles attention computation to keep data in SRAM and avoid materializing the full N×N matrix in HBM. Same exact result, far less memory traffic. |
| Quantization | INT8, INT4 (weight-only, e.g. GPTQ/AWQ), and FP8 reduce memory and bandwidth. Weight-only helps decode; FP8 helps compute on supported hardware. KV cache quantization stretches capacity. Validate quality loss. |
| Speculative decoding | A small draft model proposes several tokens and the large model verifies them in one pass. Preserves output distribution, with speedup depending on acceptance rate. Works best at low batch sizes. |
| Multi-GPU inference | **Tensor parallelism** splits layers across GPUs (needs fast NVLink, adds all-reduce per layer). **Pipeline parallelism** splits layers into stages (adds bubbles, tolerates slower links). |
| CUDA graphs | Capture the decode step to cut kernel-launch overhead, important for small batches. |
| Expert parallelism (MoE) | Experts are sharded across GPUs with all-to-all routing. Name-drop level: load imbalance and communication are the main concerns. |
| Multi-LoRA / adapter serving | One base model with many small adapters swapped or batched per request. Needs adapter caching, paging, and batched kernels (e.g. punica-style). |
| Routing and fallback | Route by task difficulty, cost, or latency to different models. Fall back on overload or failure to a smaller model. |

### Metrics

| Metric | Meaning |
|---|---|
| **TTFT** | Time to first token. Dominated by queueing + prefill. |
| **TPOT / ITL** | Time per output token. Dominated by decode speed and batch contention. |
| **End-to-end latency** | TTFT + (output tokens × TPOT). |
| **Tokens per second** | Per-request speed and system-wide throughput (track separately). |
| **GPU and KV cache utilization** | Low KV utilization wastes capacity. Near 100% triggers preemption and tail-latency spikes. |

**Trade-offs:** Larger batches raise throughput but raise TPOT. Long-prompt workloads stress prefill and TTFT, while long-generation workloads stress decode and KV capacity. Tune differently for chat (latency-sensitive), batch (throughput-sensitive), and RAG (long prompts, prefix reuse).

---

## 2. LLM Gateway (variant)

Same as the API gateway, plus LLM-specific concerns.

| Topic | Details |
|---|---|
| Token-based limits | Estimate input tokens before the call and reserve budget, then reconcile with actual usage afterward. Limits per tenant, key, and model, plus concurrency limits. |
| Streaming | Pass through server-sent events without buffering. Handle client disconnects by cancelling upstream generation. |
| Routing and failover | Route by model alias, cost, latency, or capacity. Fail over across providers or regions, with attention to output differences. |
| Model aliases and versioning | Stable names that map to versions, with canary rollout and pinned versions for customers who need them. |
| Caching | Exact-match response cache, prompt-prefix cache, optional semantic cache (with correctness caveats). Never cache across tenants unless safe. |
| Budgets and cost attribution | Per-team and per-key spend caps, alerts, and usage reporting by model and feature. |
| Logging | Log metadata always. Log prompts and responses only with consent, retention limits, and PII redaction. |
| Safety | Input and output filters, provider-side moderation, abuse detection. |
| Overload | Queue with priorities, shed low-priority traffic first, `429` with `Retry-After`, protect providers' rate limits. |

---

## 3. Agentic Platform

**Core model:** An agent loop (plan → call model → choose tool → execute → observe → repeat) runs inside a durable orchestration layer with tools, memory, evaluation, and guardrails around it.

### Execution

| Topic | Details |
|---|---|
| DAG vs. state machine | DAGs suit predictable pipelines. State machines handle loops, branching, and dynamic control flow, which fit agents better. |
| Sequential and parallel tools | Run independent tool calls in parallel to cut latency. Enforce concurrency limits and merge results deterministically. |
| Durable execution | Persist every step (event-sourced history or checkpoints) so a run can resume after crashes. Workflow engines (Temporal-style) replay history, so steps must be deterministic or recorded. |
| Checkpointing and recovery | Checkpoint after each model or tool call. On recovery, skip completed steps and retry the in-flight one. |
| Workflow versioning | Running executions must finish on the version they started with, or be migrated safely. Version prompts, tools, and graph definitions together. |
| Lifecycle | States such as queued, running, waiting (tool/human), succeeded, failed, cancelled, timed out. Enforce max steps, max time, and max cost per run. |
| Stateful vs. stateless | Stateless workers with state in a store scale and fail over easily. Stateful sessions are faster but need affinity and recovery. Prefer stateless compute with externalized state. |
| Multi-agent coordination | Patterns: orchestrator/worker, handoffs, shared blackboard, message passing. Needs clear contracts, loop and deadlock limits, and attribution of cost and errors per agent. |

### Tools, Security, and Safety

| Topic | Details |
|---|---|
| Tool authN/authZ | Act on behalf of the user with scoped, short-lived credentials. Least privilege per tool and per task. Never let the model hold raw secrets. |
| Permissions and access control | Policy checks outside the model. Allowlists per agent, separate read and write tools, and audit logs for every action. |
| Sandboxing and isolation | Run code and untrusted tools in containers or microVMs (gVisor/Firecracker style) with CPU, memory, time, network, and filesystem limits. |
| Timeouts, cancellation, idempotency, retries | Per-tool timeouts and cancellation propagation. Idempotency keys for side-effecting calls. Retry only safe errors, with backoff and jitter. |
| Prompt injection and trust boundaries | Treat tool output and retrieved content as **untrusted data**, never instructions. Validate and sanitize outputs, restrict capabilities after reading untrusted content, and require approval for high-risk actions. |
| Human approval and escalation | Approval gates for irreversible or costly actions, with durable waiting state and timeouts. Escalate on low confidence, repeated failure, or policy triggers. |

### Context and Memory

| Topic | Details |
|---|---|
| Context-window management | Budget tokens across system prompt, history, tool results, and retrieval. Truncate, summarize, or drop old content. Trim large tool outputs. |
| Short-term vs. long-term memory | Short-term = current context and working state. Long-term = external store (vector, key-value, structured) with write policies, retrieval, expiry, and privacy controls. |
| State persistence | Store conversation and run state durably, keyed by session. Support resume, branching, and deletion. |
| Retrieval and compression | Retrieve selectively, rerank, and compress via summarization or extraction. Watch for stale or conflicting memories. |

### Evaluation and Operations

| Topic | Details |
|---|---|
| Offline and online evaluation | Offline: curated datasets, replayed trajectories, LLM or human graders. Online: production sampling, user feedback, guardrail metrics. |
| Regression testing and datasets | Run evals on every prompt, model, or tool change. Build datasets from real failures. Pin versions for reproducibility. |
| Trajectory evaluation | Track end-to-end task success, tool-call success rate, tool-selection errors, hallucinations, step count, and cost per task. Evaluate the path, not only the final answer. |
| Failure detection and recovery | Detect loops, repeated tool errors, stalled runs, and budget overruns. Recover with retries, replanning, a fallback model, or escalation. |
| Token budgets and cost attribution | Meter tokens and tool costs per run, tenant, and agent. Enforce hard caps and alert on anomalies. |
| Model selection and routing | Use cheaper models for simple steps and stronger ones for planning or hard reasoning. Route by task type, with fallback on failure. |
| Caching and reuse | Cache prompt prefixes, deterministic tool results, and retrieval results, with correct keys and invalidation. Never cache user-specific or sensitive data across tenants. |
| Concurrency and rate limiting | Limit concurrent runs per tenant and calls per tool and per model provider. Queue with fairness and handle provider `429`s with backoff. |

---

## 4. Model Training

**Core model:** A scheduler allocates GPUs (gang-scheduled, topology-aware) to jobs. Workers load sharded data, run parallel training with collective communication, and periodically checkpoint so failures cost minutes, not days.

### Data Pipeline

| Topic | Details |
|---|---|
| Distributed data loading | Parallel readers with prefetching and shuffling across epochs. Keep loading off the critical path. |
| Sharding and sampling | Deterministic shards per rank, stable shuffles, and resumable sampler state so restarts don't repeat or skip data. |
| Preprocessing bottlenecks | Tokenization, decoding, and augmentation can starve GPUs. Pre-process offline, cache results, use more loader workers, and offload to dedicated CPU pools. |
| Storage throughput and caching | Use local NVMe caches in front of object storage, sequential-friendly formats, and avoid many small files. |

### Scheduling and Cluster Management

| Topic | Details |
|---|---|
| Gang scheduling | All workers of a job start together or not at all, to avoid deadlocks and wasted partial allocations. |
| GPU fragmentation and topology | Place jobs to keep GPUs on the same node/NVLink domain and nearby on the network. Bin-pack to reduce fragmentation. |
| Fairness and priority | Quotas per team, priority tiers, preemption of low-priority work, and backfill of small jobs into gaps. |
| Multi-tenant isolation | Namespace and quota isolation, network and storage isolation, and per-tenant accounting. |
| Elastic training | Scale the worker count up or down during a run (rendezvous, re-sharding, learning-rate and batch-size adjustment). Helps use spare capacity and survive node loss. |
| Training/inference contention | Share GPUs only with care. Prefer separate pools, or preemptible training on spare inference capacity with fast eviction. |

### Parallelism and Communication

| Topic | Details |
|---|---|
| Data parallelism and FSDP | DP replicates the model and all-reduces gradients. FSDP/ZeRO shards parameters, gradients, and optimizer state, trading extra communication (all-gather, reduce-scatter) for memory. |
| Tensor and pipeline parallelism | Tensor: split matrices within layers (high bandwidth needed, keep within a node). Pipeline: split layers into stages (micro-batching to reduce bubbles). Large models combine DP + TP + PP. |
| AllReduce and NCCL | Ring and tree all-reduce algorithms. NCCL handles GPU collectives, topology detection, and transport selection. |
| Communication/computation overlap | Overlap gradient communication with backward computation and prefetch parameters (FSDP) to hide network time. |
| Gradient accumulation and checkpointing | Accumulation simulates larger batches with less memory. Activation (gradient) checkpointing recomputes activations to save memory at ~30% extra compute. |
| Mixed precision | BF16/FP16/FP8 with FP32 master weights, plus loss scaling for FP16. Faster and lighter, but watch numerical stability. |
| RDMA and InfiniBand | Name-drop: low-latency, high-bandwidth, kernel-bypass networking (GPUDirect RDMA) that makes large-scale collectives efficient. |

### Checkpointing and Fault Tolerance

| Topic | Details |
|---|---|
| Distributed checkpoint coordination | Each rank saves its shard. Use a coordinated barrier and an atomic "commit" marker so partial checkpoints are never loaded. |
| Async vs. sync checkpointing | Sync blocks training but is simple. Async copies state to host memory and uploads in the background, minimizing stall at the cost of complexity and memory. |
| Frequency, RPO, storage | Checkpoint interval = trade-off between overhead and lost work (recovery-point objective). Use tiered storage (local, then remote), retention policies, and integrity checks. |
| Partial worker failures | Detect via heartbeats and NCCL timeouts. Restart the affected job, or replace workers and restore from the latest checkpoint. Elastic setups can continue with fewer workers. |
| Preemption and resumption | Handle signals with a quick final checkpoint. Resume exactly: model, optimizer, LR schedule, RNG, and data-loader position. |

### Monitoring

| Topic | Details |
|---|---|
| Utilization | GPU utilization, MFU (model FLOPs utilization), memory use, and data-loader wait time. |
| Communication overhead | All-reduce time, network bandwidth, and exposed (non-overlapped) communication. |
| Straggler identification | Compare per-rank step times. Causes: slow GPU, thermal throttling, bad NIC, noisy storage. Replace or cordon bad nodes. |
| Throughput and time-to-train | Tokens or samples per second, scaling efficiency, and end-to-end time to target quality. |

---

## 5. Feature Store

**Core model:** A registry defines features. An offline store (warehouse/lake) holds history for training. An online store (low-latency key-value) serves current values for inference. Pipelines keep them consistent.

### Definitions and Governance

| Topic | Details |
|---|---|
| Definitions and metadata | Entity, feature name, type, transformation logic, source, owner, freshness SLA, and description. |
| Registry, versioning, ownership, discovery | Central catalog with search, lineage, access control, and owners. Version features so changes don't silently break models. |
| Schema evolution | Additive changes are safe. Breaking changes need a new version and migration. Validate compatibility with consuming models. |

### Architecture and Consistency

| Topic | Details |
|---|---|
| Online vs. offline stores | Offline: columnar, large scans, historical data. Online: key-value (Redis, DynamoDB, Cassandra-style), millisecond reads, latest values only. |
| Train/serve consistency | Define the transformation **once** and run it in both paths (shared code or a unified engine) to avoid skew. |
| Batch vs. streaming computation | Batch: simpler, cheaper, higher staleness. Streaming: fresh but needs state, ordering, and failure handling. Hybrid is common. |
| Online/offline synchronization | Materialize offline-computed features to online on a schedule, and write stream outputs to both stores. Monitor divergence. |

### Streaming Semantics

| Topic | Details |
|---|---|
| Event time vs. processing time | Use event time for correctness (when it happened), processing time for simplicity. Watermarks decide when a window is complete. |
| Windowed aggregations | Tumbling, sliding, and session windows. Manage state size and emit policies (early, on-time, late). |
| Late events and corrections | Allowed lateness, retractions or updates, and reprocessing. Decide whether the online store accepts corrections. |
| Point-in-time joins | For training, join each label to feature values **as of** its timestamp, never future data. Prevents leakage. Needs versioned or timestamped feature history. |

### Serving and Reliability

| Topic | Details |
|---|---|
| Low-latency and batch retrieval | Online: batched multi-get across entities, parallel fetches, and tight timeouts. Offline: bulk historical retrieval for training sets. |
| Caching and eviction | Local and distributed caches in front of the store, with TTL aligned to freshness requirements. Avoid serving stale data past its SLA. |
| Hot-key mitigation | Replicate popular entities, add local caches, and use key salting or request coalescing. |
| Missing or stale features | Defaults, last-known value, or imputed values, with an explicit "stale/missing" signal to the model. Choose fail-open or fail-closed per feature. |
| Skew detection and prevention | Log served features and compare distributions with training data. Alert on drift, null spikes, and schema mismatches. |
| Freshness SLAs and monitoring | Measure end-to-end lag from event to online availability. Alert on breaches. |
| Data quality validation | Range, null, type, and distribution checks at ingestion. Quarantine bad data. |
| Backfills | Idempotent and versioned, with consistent logic and no overwriting of live values unintentionally. Test against point-in-time correctness. |

### Scale and Cost

| Topic | Details |
|---|---|
| High-throughput ingestion | Partitioned streams, batched writes, and backpressure handling. Keep write amplification in check. |
| Partitioning and replication | Partition by entity key for even distribution. Replicate for availability and read scaling, and weigh consistency vs. latency. |
| Multi-tenant isolation | Namespaces, quotas, and access control per team. Protect shared stores from noisy tenants. |
| Storage cost optimization | Tier hot and cold data, TTL for online features, compact and compress offline data, and drop unused features. |

---

## 6. Chatbot & RAG & Knowledge Base

**Core model:** An **ingestion pipeline** turns documents into searchable chunks. A **query path** retrieves relevant chunks, builds a prompt within a token budget, calls the LLM, and returns an answer with citations.

### Ingestion

| Topic | Details |
|---|---|
| Parsing and cleaning | Extract text from PDFs, HTML, and office files. Preserve structure (headings, tables). Handle OCR and junk. |
| Chunking | Fixed-size with overlap, or structure-aware (by heading or paragraph). Chunk size trades precision against context. Store metadata (source, section, ACLs, timestamps). |
| Embedding | Batch embedding jobs, queue-based with retries. Version the embedding model. Changing it means **re-embedding everything**, so plan for dual indexes during migration. |
| Indexing | Vector index plus a keyword index (BM25). Write path should be idempotent. |
| Freshness | Incremental updates by change detection (hash or modified time), deletions via tombstones, and reindex on schedule or event. |

### Retrieval and Generation

| Topic | Details |
|---|---|
| Vector indexes | HNSW (high recall, memory-heavy), IVF-PQ (compressed, less accurate, scales cheaply). Tune recall vs. latency. |
| Hybrid search | Combine vector and keyword results (for example reciprocal rank fusion) to cover exact terms and semantics. |
| Reranking | A cross-encoder reranks the top 50-100 candidates down to a handful. Better quality, extra latency. |
| Query processing | Query rewriting, expansion, and decomposition for multi-part questions. Conversation history for follow-ups. |
| Access control | Enforce per-user document permissions at retrieval time. **Pre-filter** by ACL metadata is safest. Post-filtering can leak existence and wastes recall. Never rely on the prompt to hide data. |
| Context assembly | Fit chunks into the token budget, order by relevance, dedupe near-duplicates, include citations and source IDs. |
| Generation | Instruct the model to answer only from context and say when it doesn't know. Stream responses. |
| Caching | Cache embeddings, retrieval results for frequent queries, and prompt prefixes. Respect ACLs in cache keys. |

### Quality, Safety, and Scale

| Topic | Details |
|---|---|
| Evaluation | Retrieval: recall@k, MRR. Generation: faithfulness (grounded in context), answer relevance, citation accuracy. Build a labeled dataset from real queries. Run on every change. |
| Failure modes | Stale or conflicting documents, missed retrievals, over-long context, hallucinated citations, ambiguous queries. Add "no answer" behavior and fallbacks. |
| Prompt injection | Documents are untrusted. Treat retrieved text as data, not instructions. Restrict tool use and sensitive actions after retrieval. |
| Multi-tenancy | Per-tenant indexes (strong isolation, more overhead) or a shared index with tenant filters (cheaper, riskier). Per-tenant quotas. |
| Feedback loop | Collect thumbs up/down and unanswered queries to improve content and ranking. |
| Latency and cost | Budget per stage (embed, search, rerank, generate). Generation dominates. Use smaller models for rewriting and reranking. |

---

## 7. Cross-Cutting Themes

- **Separate control plane from data plane** (serving, training scheduler, feature registry) so management failures don't take down live traffic.
- **Backpressure, admission control, and load shedding** protect every shared resource (serving queues, tool calls, feature stores).
- **Batching trades latency for throughput** (dynamic batching, continuous batching, async checkpointing, batched feature reads).
- **Memory and bandwidth, not just compute,** are usually the real bottleneck (KV cache, FSDP, data loaders, online stores).
- **Tail latency and stragglers** matter more than averages (P99 serving, slow training ranks, slow tool calls).
- **Idempotency, durable state, and checkpoints** make retries and recovery safe (agents, training, backfills).
- **Version everything** (models, prompts, features, workflows) and use canary, shadow, and rollback.
- **Multi-tenant fairness and isolation** need quotas, priorities, and noisy-neighbor controls throughout.
- **Training/serving consistency** (features, tokenizers, preprocessing) prevents silent quality bugs.
- **Measure the right things:** SLO metrics, cost attribution, quality evals, and drift detection.