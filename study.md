# DATA STRUCTURE AND ALGORITHM (25%)

| Week | Plan |
|---|---|
| W1 | 3 medium/hard mandatory problems per day |
| W2 | 3 medium/hard mandatory problems per day |
| W3 | 3 medium/hard mandatory problems per day |
| W4 | 3 medium/hard mandatory problems per day |
| W5 | 3 medium/hard mandatory problems per day |
| W6 | 3 medium/hard mandatory problems per day |
| W7 | 3 medium/hard mandatory problems per day |
| W8 | 3 medium/hard mandatory problems per day |
| W9 | 3 medium/hard mandatory problems per day |
| W0 | 3 medium/hard mandatory problems per day |

## Mandatory

Design problems are most important; randomly pick 150 out of 250.

| Topic | Problems |
|---|---:|
| Array / Prefix Sum / Hash Map / String | 8/9/22 |
| Two Pointers | 3/5/13 |
| Stack | 1/6/14 |
| Binary Search | 2/7/14 |
| Sliding Window | 4/6/9 |
| Linked List | 6/11/14 |
| Tree DFS / BFS | 11/15/23 |
| Heap | 1/7/12 |
| Graph DFS / BFS / Topo Sort / Union Find | 6/13/21 |
| 1D DP | 10/12/17 |
| Interval | 5/6/7 |
| Greedy | 2/8/14 |
| Advanced Graph | 1/6/10 |
| 2D DP | 2/11/16 |
| Trie | 3/3/4 |
| Backtracking | 2/10/17 |

## Optional

- Math / Geometry (3/8/13)
- Bit Manipulation (5/7/10)

## Reference

- NeetCode
- LeetCode


# SOFTWARE ENGINEERING (25%)

| Week | Plan |
|---|---|
| W1 | practice 1 mandatory problem per day + practice 1 behavioral story per day |
| W2 | practice 1 mandatory problem per day + practice 1 behavioral story per day |
| W3 | practice 1 mandatory problem per day + practice 1 behavioral story per day |
| W4 | practice 1 mandatory problem per day + practice 1 behavioral story per day |
| W5 | practice 1 mandatory problem per day + practice 1 behavioral story per day |
| W6 | practice 1 mandatory problem per day + practice 1 behavioral story per day |
| W7 | practice 1 mandatory problem per day + practice 1 behavioral story per day |
| W8 | practice 1 mandatory problem per day + practice 1 behavioral story per day |
| W9 | practice 1 mandatory problem per day + practice 1 behavioral story per day |
| W0 | practice 1 mandatory problem per day + practice 1 behavioral story per day |

## Mandatory

### Tier 1

- **Rate limiter:** allow(user_id) with token bucket and per-user limits; thread-safe without a global lock (per-key locks or sharding); sliding window log vs counter on memory and accuracy; Redis distribution (Lua atomicity, clock skew, Redis failure behavior); evict idle users; burst vs sustained rates and per-tier limits.
- **Worker pool:** fixed workers, bounded queue, submit(task); backpressure policy (block, reject, caller-runs); cancel queued and running tasks; graceful vs immediate shutdown; futures for results and exceptions; priorities; worker crash mid-task.
- **KV store with transactions:** get/set/delete with begin/commit/rollback; nested transactions; isolation for concurrent transactions (read committed vs snapshot); optimistic versioning for conflicts; undo log vs write buffer; durability with a WAL.
- **Dynamic request batcher:** flush when full or on max wait; per-request futures with error isolation; variable-length inputs (bucketing, padding); queue cap and backpressure; adaptive wait time; flush on shutdown.
- **Request coalescing:** collapse identical in-flight calls; one caller’s cancel must not cancel the others; share errors and negative caching; TTL and stale-while-revalidate; key normalization; cross-process coalescing (lease or lock); stuck leader timeout.
- **Tool-calling agent loop:** mocked LLM reason-and-call cycles; malformed tool calls (repair, retry, feed error back); parallel calls with ordered results; step limits, timeouts, loop detection; context growth; streaming and cancellation.
- **DAG executor:** dependency order under a parallelism limit; fail-fast vs continue independent branches; rerun from the failed node; step caching by content hash; cycle detection; resource-aware limits; cancellation.
- **Job scheduler (simplified):** priority plus dependencies; retry with backoff; preemption; fair share and team quotas; priority aging; cycle detection; persist state and recover after a crash.
- **Retry wrapper:** exponential backoff with jitter; retryable vs non-retryable errors; retry budget and overall deadline; idempotency requirement; preventing retry storms across layers.
- **Circuit breaker:** closed, open, half-open; error rate vs consecutive failures; limit concurrent probes in half-open; sliding window; per-dependency state; thread safety.
- **Pub/sub with DLQ:** delivery to subscribers; at-least-once vs at-most-once; per-key ordering and consumer groups; retry policy before dead-lettering; slow consumer backpressure; DLQ replay.
- **Consistent hashing:** key-to-node mapping with virtual nodes; add/remove nodes and measure keys moved; replicate to N successors; weighted nodes and hot keys; bounded-load hashing.
- **Tool registry:** typed schemas; validate and coerce arguments; versioning and deprecation; permission scoping per agent or tenant; structured validation errors an LLM can act on.
- **Token budget tracker:** per-tenant metering; streaming responses; hard vs soft quotas and reset windows; reserve up front then reconcile with actuals; concurrent requests racing past the limit; distributed counters.

### Tier 2

- **Continuous batching scheduler:** token-step scheduling within a token budget; admit against KV memory; preempt or evict when memory runs out; prefill vs decode (chunked prefill); starvation and priorities; cancel mid-batch.
- **Point-in-time join:** latest feature value as of each event’s timestamp; late data and backfills; tie-breaking on equal timestamps; feature TTL and staleness limits; out-of-core scale (sorted merge, partitioning, key skew); multiple feature tables; batch vs streaming.
- **Model router:** load-aware routing across replicas; least-loaded vs power-of-two-choices; health checks and ejection; session stickiness for KV cache reuse; retries and hedging; heterogeneous replicas.
- **Heartbeat monitor:** detect dead workers; reduce false positives (phi-accrual, grace periods); reschedule without duplicating work; network partition detection; zombie workers returning.
- **Log parser:** parse lines into records with p50/p99; tolerate malformed lines; streaming mergeable percentiles (t-digest, histograms); out-of-order timestamps.
- **Config merge/diff:** deep merge with override rules; list merge semantics; path-level diff; secret redaction; schema validation.

### Tier 3

- **KV/prefix cache (radix):** reuse computed prompt prefixes; split and merge radix nodes; ref-count in-use prefixes; LRU leaf eviction under a memory budget; concurrent readers and writers; block-level memory accounting.
- **Streaming aggregator:** rolling windowed aggregates; late events with watermarks and allowed lateness; tumbling, sliding, session windows; exactly-once via idempotent sinks or checkpointed offsets; bounded state.
- **Agent state/memory store:** per-session state; truncate vs summarize over context limit; pin critical messages; concurrent writes to one session; persist and expire sessions; accurate token counting.
- **Eval harness:** parallel prompts and aggregated scores; respect rate limits; retry flaky failures without double-counting; partial results on interruption; confidence intervals; LLM-as-judge.
- **Distributed lock with fencing:** expiring leases; fencing tokens rejected by the resource when stale; lease renewal, GC pauses, clock skew; leader election on top; Redis single-instance lock vs consensus.
- **Count-min/HLL:** approximate frequency and cardinality; error bounds and sketch sizing; merging across nodes; heavy hitters; why deletes are hard.

## Behavioral

- Ownership
- Conflict
- Leadership
- Mentorship
- Ambiguity
- Challenge
- Impact
- Failure
- Risk
- Influence without authority
- Technical strategy
- Disagree and commit.

## Reference

- Software Engineer’s Guidebook


# SYSTEM DESIGN (25%)

| Week | Plan |
|---|---|
| W1 | review 1 mandatory problem per day |
| W2 | break |
| W3 | practice 1 mandatory problem per day |
| W4 | break |
| W5 | review 1 mandatory problem per day |
| W6 | break |
| W7 | practice 1 mandatory problem per day |
| W8 | break |
| W9 | review 1 optional problem per day |
| W0 | break |

## Mandatory

### Distributed Job Scheduler and Message Queue

- **Job Scheduling:** delayed and recurring jobs; priority scheduling and fairness; resource-aware scheduling; scheduling across multiple workers.
- **Message Queue Architecture:** queue vs. pub/sub; partitioning and consumer groups; ordering guarantees; consumer rebalancing and partition reassignment.
- **Delivery and Processing Guarantees:** at-most-once, at-least-once, exactly-once semantics; acknowledgments and visibility timeouts; deduplication and idempotency; dead-letter queues and poison messages.
- **Distributed Coordination:** leader election; distributed locks, leases, and lease renewal/expiration; worker registration, heartbeats, and failure detection; fencing tokens and stale worker protection.
- **Reliability and Scalability:** backpressure and load shedding; retry policies; queue recovery and replay; horizontal scaling and autoscaling; consumer lag monitoring and mitigation.

### Distributed Cache and Key-Value Store

- **Data Partitioning and Distribution:** consistent hashing and virtual nodes; partition rebalancing and data migration; hot partitions and hot keys.
- **Caching Strategies and Eviction:** cache-aside, write-through, write-back; LRU, LFU, TTL-based eviction; cache stampede, penetration, and avalanche, plus prevention (request coalescing, locking, probabilistic early expiration).
- **Consistency and Replication:** strong vs. eventual consistency; quorum reads/writes; leader-follower vs. leaderless replication; conflict resolution and versioning; split-brain scenarios (fencing tokens: see W3); read repair and hinted handoff (name-drop).
- **Reliability and Performance:** failover and replica recovery; cache invalidation; latency, throughput, and availability trade-offs; multi-region replication (name-drop).

### Distributed Workflow Engine

- **Workflow Definition and Execution:** DAG-based vs. state-machine-based workflows; dependency resolution and parallel execution; dynamic workflow generation.
- **Durable Execution:** event sourcing, execution history, and event replay semantics; persisted state and deterministic replay; workflow versioning and schema evolution.
- **Failure Handling:** retry policies and exponential backoff; idempotency and deduplication; compensation and saga patterns; cancellation and timeout propagation.
- **Distributed Execution:** worker assignment, task leasing, heartbeats, and failure detection (see SD W3); task queues and scheduling (see SD W3).
- **Scalability and Operations:** workflow throughput and execution latency; long-running workflow management; multi-tenancy and resource isolation; workflow observability and debugging.

### Metrics, Logging, Monitoring platform

- **Data Collection and Ingestion:** push vs. pull models; agent-based collection; batching and buffering; backpressure and ingestion throttling.
- **Data Modeling and Storage:** time-series data modeling; indexing, partitioning, and compression; retention and downsampling; high-cardinality labels, cardinality management, and label limits.
- **Distributed Processing:** stream processing, aggregation, and sampling; windowing (tumbling, sliding, session); late-arriving and out-of-order events; deduplication and exactly-once vs. at-least-once ingestion.
- **Query and Observability:** query execution, indexing, and distributed fan-out; aggregation and filtering; metrics, logs, and distributed traces; trace context propagation and correlation IDs; alerting and anomaly detection.
- **Reliability and Scaling:** replication and fault tolerance; data loss prevention; multi-tenancy and noisy-neighbor isolation; cost optimization.

### Distributed Object Storage

- **Storage Architecture:** object metadata vs. object data; metadata service architecture; control plane vs. data plane; storage abstraction and object naming.
- **Data Partitioning and Durability:** replication vs. erasure coding; data placement and rebalancing; checksums and data integrity; failure domains and availability zones.
- **Upload and Download:** multipart and resumable uploads, including cleanup of incomplete uploads; range requests and large-object streaming; pre-signed URLs and delegated access.
- **Consistency and Reliability:** strong vs. eventual and read-after-write consistency; metadata consistency; repair and recovery; object versioning and deletion semantics.
- **Performance, Cost, and Security (name-drop):** hot/cold tiers, lifecycle policies, CDN, compression/deduplication; authentication/authorization, encryption, tenant isolation, audit logging.

## Optional

### TinyURL

### Amazon

### Instagram

### Parking Reservation

### Hotel Reservation

## Reference

- System Design I
- System Design II
- Designing Data-Intensive Applications


# MACHINE LEARNING SYSTEM DESIGN (25%)

| Week | Plan |
|---|---|
| W1 | break |
| W2 | review 1 mandatory problem per day |
| W3 | break |
| W4 | practice 1 mandatory problem per day |
| W5 | break |
| W6 | review 1 mandatory problem per day |
| W7 | break |
| W8 | practice 1 mandatory problem per day |
| W9 | break |
| W0 | review 1 optional problem per day |

## Mandatory

### Model Serving

- **Model Lifecycle and Deployment:** model artifact distribution and deployment across serving nodes; cold starts, model warm-up, and readiness management; control plane vs. data plane.
- **Request Management:** admission control and request prioritization; queue management, backpressure, overload protection, and load shedding; request deadlines, timeouts, and cancellation.
- **Performance and Scalability:** P50/P95/P99 latency and tail-latency optimization; throughput vs. latency trade-offs; dynamic batching; GPU/CPU utilization and memory bottlenecks; model autoscaling and scale-to-zero trade-offs.
- **Reliability:** health checks and readiness probes; circuit breakers and fallback models; model versioning and compatibility; canary analysis, automated rollback, and traffic shifting; shadow deployments and A/B testing.
- **Multi-tenancy:** resource quotas, tenant isolation, fair scheduling, and noisy-neighbor mitigation.

### LLM Serving

- **GPU Architecture and Memory:** GPU compute vs. memory bandwidth bottlenecks; GPU memory hierarchy; KV cache memory estimation; KV cache allocation, paging, eviction, and fragmentation (PagedAttention).
- **Inference Optimization:** continuous batching; prefix caching; chunked prefill; prefill/decode disaggregation; FlashAttention fundamentals; quantization (INT8, INT4, FP8); speculative decoding; multi-GPU inference (tensor and pipeline parallelism); CUDA graphs and expert parallelism for MoE (name-drop).
- **Serving Architecture:** LLM request scheduling, admission control, prioritization, and preemption; context-length limits and token budgeting; multi-LoRA / adapter serving; model routing and fallback.
- **Performance Evaluation:** TTFT vs. TPOT vs. end-to-end latency; tokens per second, throughput, GPU and KV cache utilization; latency-throughput trade-offs under different workloads.

### Agentic Platform

- **Workflow Orchestration:** DAG and state-machine execution; sequential and parallel tool execution; durable execution, checkpointing, recovery, and workflow versioning (see SD W4); agent loop and execution lifecycle; stateful vs. stateless agent execution; multi-agent communication and coordination.
- **Tool Execution and Security:** tool authentication, authorization, permissions, and access control; sandboxing, execution isolation, and resource limits; tool timeouts, cancellation, idempotency, and retry handling; prompt injection, tool output validation, and trust boundaries.
- **Context and Memory:** context-window management; short-term vs. long-term memory; conversation state persistence; retrieval and context compression.
- **Evaluation and Reliability:** offline and online evaluation, regression testing, and evaluation datasets; agent trajectory evaluation (end-to-end task success, tool-call success rate, tool-selection errors, hallucination); failure detection and recovery; human approval and escalation.
- **Cost and Performance:** token budgets and cost attribution; model selection and routing; caching and reuse; concurrency limits and rate limiting.

### Model Training

- **Training Data Pipeline:** distributed data loading; data sharding and sampling; data preprocessing bottlenecks; storage throughput and caching.
- **GPU Scheduling and Resource Management:** gang scheduling; GPU fragmentation, allocation, and topology; scheduling fairness and priority; multi-tenant workload isolation; elastic training and worker scaling; training/inference workload contention.
- **Distributed Training Optimization:** data parallelism and FSDP; tensor and pipeline parallelism; AllReduce and NCCL; communication/computation overlap; gradient accumulation and gradient checkpointing; mixed precision training; RDMA and InfiniBand (name-drop).
- **Fault Tolerance:** distributed checkpoint coordination; asynchronous vs. synchronous checkpointing; checkpoint frequency, recovery-point objectives, and checkpoint storage; recovery from partial worker failures; training job preemption and resumption.
- **Performance Monitoring:** GPU and memory utilization; data-loader wait time; communication overhead and network bandwidth; straggler identification; training throughput and time-to-train.

### Feature Store

- **Feature Management:** feature definitions and metadata; feature registry, versioning, ownership, and discovery; feature schema evolution; online vs. offline store architecture; feature transformation consistency between training and inference.
- **Feature Computation:** batch vs. streaming feature computation; stream processing and event-time vs. processing-time semantics; windowed aggregations; late-arriving events and corrections; point-in-time joins and historical feature retrieval.
- **Online Serving:** low-latency and batch feature retrieval; cache strategies and eviction; hot-key mitigation; fallback behavior for missing or stale features.
- **Correctness and Reliability:** training-serving skew detection and prevention; feature freshness SLAs and monitoring; data quality validation; backfill consistency and recovery; online/offline synchronization.
- **Scalability:** high-throughput feature ingestion; partitioning and replication; multi-tenant isolation; storage cost optimization.

## Optional

### Recommendation System

### Search Ranking

### Real-time Detection

### Fraud Detection (Layer6 AI)

### Real-time Auction (Index Exchange)

## Reference

- Designing Machine Learning Systems
- Machine Learning Design Patterns
- Machine Learning System Design
- Generative AI System Design


# MACHINE LEARNING

| Week | Plan |
|---|---|
| W1 | CS336, CME295, CME296, CS224N   |
| W2 | CS336, CME295, CME296, CS224N   |
| W3 | CS336, CME295, CME296, CS224N   |
| W4 | CS336, CME295, CME296, CS224N   |
| W5 | CS336, CME295, CME296, CS224N   |
| W6 | CS336, CME295, CME296, CS224N   |
| W7 | CS336, CME295, CME296, CS224N   |
| W8 | CS336, CME295, CME296, CS224N   |
| W9 | CS336, CME295, CME296, CS224N   |
| W0 | CS336, CME295, CME296, CS224N |


# ORGANIZE

| Week | Plan |
|---|---|
| W1 | Data (Password, Sketch, Kakaotalk, SD Card, Portable Disk, Google Drive, ICloud) |
| W2 | Data (Password, Sketch, Kakaotalk, SD Card, Portable Disk, Google Drive, ICloud) |
| W3 | Data (Password, Sketch, Kakaotalk, SD Card, Portable Disk, Google Drive, ICloud) |
| W4 | Data (Password, Sketch, Kakaotalk, SD Card, Portable Disk, Google Drive, ICloud) |
| W5 | Data (Password, Sketch, Kakaotalk, SD Card, Portable Disk, Google Drive, ICloud) |
| W6 | Documents (Paper, Electronic) |
| W7 | SMS Pictures (LinkedIn, Instagram, Turo, Airbnb, Facebook, Meet Up) |
| W8 | Address (Job, Banks - TD / CIBC / SIM / EQ / TG / WS / US, Service Ontario - Driver / Health / Car Ownership, CRA, Family Doctor, Car Insurance - N/A, Amazon) |
| W9 | ID (Passport 2036-04-14, Driver 2030-04-06, Health 2030-04-06, Nexus 2030-04-06) |
| W0 | Computer (Format big one, sell old one) |
