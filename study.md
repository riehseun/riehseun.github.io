# DATA STRUCTURE AND ALGORITHM (25%)

| Week | Plan |
|---|---|
| W1 | 3 medium/hard mandatory problems per day |
| W2 | 3 medium/hard mandatory problems per day |
| W3 | 3 medium/hard mandatory problems per day |
| W4 | 3 medium/hard mandatory problems per day |
| W5 | break |
| W6 | 3 medium/hard mandatory problems per day |
| W7 | 3 medium/hard mandatory problems per day |
| W8 | 3 medium/hard mandatory problems per day |
| W9 | 3 medium/hard mandatory problems per day |
| W0 | break |

## Mandatory

Randomly pick a question out of Leet 250 if Array & Hashmap, Two Pointers, Sliding Window
Randomly pick a question out of Leet 150 if everything else

| Topic | Problems |
|---|---:|
| Arrays & Hashing (Prefix Sum, String) | 8/9/22 |
| Two Pointers | 3/5/13 |
| Stack | 1/6/14 |
| Binary Search | 2/7/14 |
| Sliding Window | 4/6/9 |
| Linked List | 6/11/14 |
| Tree (DFS, BFS) | 11/15/23 |
| Heap | 1/7/12 |
| Graph (DFS, BFS, Topological Sort, Union Find) | 6/13/21 |
| 1D DP | 10/12/17 |
| Interval | 5/6/7 |
| Greedy | 2/8/14 |
| Advanced Graph (Dijkstra, Bellman-Ford, Prim, Hierholzer) | 1/6/10 |
| 2D DP | 2/11/16 |
| Trie | 3/3/4 |
| Backtracking | 2/10/17 |

## Optional

- Math & Geometry (3/8/13)
- Bit Manipulation (5/7/10)


# SOFTWARE ENGINEERING (25%)

| Week | Plan |
|---|---|
| W1 | break |
| W2 | break |
| W3 | break |
| W4 | break |
| W5 | practice 1 mandatory problem per day + practice 1 behavioral story per day |
| W6 | break |
| W7 | break |
| W8 | break |
| W9 | break |
| W0 | practice 1 mandatory problem per day + practice 1 behavioral story per day |

## Mandatory

Thread-safe token bucket rate limiter: allow or reject requests per key under concurrent callers, with burst and sustained limits.
LRU cache with TTL: O(1) get/put with eviction, thread safety, expiry, and single-flight loading.
Bounded blocking queue: producer/consumer queue with blocking put/take, backpressure, and graceful shutdown.
Async worker pool: run tasks on N workers with timeouts, cancellation, priorities, and result futures.
KV store with transactions: get/set/delete plus begin/commit/rollback, including nested transactions.
SQS-like queue with visibility timeout: enqueue, receive, and ack, redeliver on timeout, and route to a DLQ after max receives.
Log aggregator with sliding window: count errors per service per minute, then rolling p95 or top-K, handling late events.
API client with pagination and retries: paginate results, retry on 429/5xx with backoff, and support a resumable cursor.
Dynamic request batcher: group requests by max size or max wait time, with per-request futures and error isolation.
DAG task executor: run tasks in topological order with a parallelism limit, cycle detection, and failure propagation.

## Optional

GPU job scheduler (coding version): place jobs by resource fit, then priorities, bin-packing, preemption, and gang scheduling.
Agent tool-execution loop: call tools and feed results back, with timeouts, retries, parallel calls, state persistence, and a max-step guard.
Read/write lock or semaphore: build a lock from basic primitives with fairness and starvation avoidance.
Pub/sub event bus: subscribe and publish with subscriber isolation, ordering, DLQ, and replay.
Time-versioned KV store: return the value at timestamp T, with deletes, range queries, and compaction.
In-memory file system: mkdir, ls, read/write, move, and delete, then permissions and quotas.
Bank / ledger: accounts and transfers with history, idempotency, scheduled payments, and merges.
In-memory SQL-like table: insert, filter, sort, and project rows, then add a secondary index and simple joins.
Reservation / booking system: book and cancel with overlap conflict detection, then waitlists and concurrency.
Sessionization of an event stream: group events into gap-based sessions, handling out-of-order events with bounded memory.
Event deduplicator: drop duplicate events by ID, with TTL on seen IDs and restart safety.
CSV/JSON transformer with validation: parse and map records with schema checks and bad-row handling, streaming large files.
Idempotent webhook handler: verify signatures and dedupe by event ID, handling out-of-order delivery and replays.
Debug failing tests / race condition: reproduce a bug in an unfamiliar repo, find the root cause, and fix it with a regression test.
Retry with backoff plus circuit breaker: add jittered backoff and per-error policies, then half-open state and retry budgets.

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
- Disagree and commit


# SYSTEM DESIGN (25%)

| Week | Plan |
|---|---|
| W1 | practice 1 mandatory problem per day |
| W2 | break |
| W3 | practice 1 mandatory problem per day |
| W4 | break |
| W5 | practice 1 mandatory problem per day |
| W6 | break |
| W7 | practice 1 mandatory problem per day |
| W8 | break |
| W9 | practice 1 mandatory problem per day |
| W0 | break |

## Mandatory

### Distributed Job Scheduler

- Job API, DAG dependencies, queueing, worker leasing, retries, priorities, multi-tenant fairness, exactly-once vs. at-least-once
- Duplicate execution, stuck leases, thundering herd on cron boundaries, backfills

### Distributed Rate Limiter

- Token bucket vs. sliding window, central vs. local counters, per-tenant and per-key limits, fail-open vs. fail-closed
- Clock skew, hot keys, Redis failover, burst handling

### Distributed Message Queue

- Partitioning, ordering, consumer groups, offsets, replication, retention, DLQ, backpressure
- Rebalancing, ordering vs. throughput, replay, poison messages

### Distributed Cache

- Consistent hashing, replication, quorum, eviction, TTL, cache invalidation, hot-key mitigation
- Leader election, split brain, stampedes, consistency model choice

### Metrics, Logging, Monitoring platform

- **Data Collection and Ingestion:** push vs. pull models; agent-based collection; batching and buffering; backpressure and ingestion throttling.
- **Data Modeling and Storage:** time-series data modeling; indexing, partitioning, and compression; retention and downsampling; high-cardinality labels, cardinality management, and label limits.
- **Distributed Processing:** stream processing, aggregation, and sampling; windowing (tumbling, sliding, session); late-arriving and out-of-order events; deduplication and exactly-once vs. at-least-once ingestion.
- **Query and Observability:** query execution, indexing, and distributed fan-out; aggregation and filtering; metrics, logs, and distributed traces; trace context propagation and correlation IDs; alerting and anomaly detection.
- **Reliability and Scaling:** replication and fault tolerance; data loss prevention; multi-tenancy and noisy-neighbor isolation; cost optimization.

## Optional

### TinyURL

### Amazon

### Instagram

### Parking Reservation

### Hotel Reservation


# MACHINE LEARNING SYSTEM DESIGN (25%)

| Week | Plan |
|---|---|
| W1 | break |
| W2 | practice 1 mandatory problem per day |
| W3 | break |
| W4 | practice 1 mandatory problem per day |
| W5 | break |
| W6 | practice 1 mandatory problem per day |
| W7 | break |
| W8 | practice 1 mandatory problem per day |
| W9 | break |
| W0 | practice 1 mandatory problem per day |

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


# MACHINE LEARNING

| Week | Plan |
|---|---|
| W1 | CS336, CS329Z, CME295, CME296, CS224N, CS230 |
| W2 | CS336, CS329Z, CME295, CME296, CS224N, CS230 |
| W3 | CS336, CS329Z, CME295, CME296, CS224N, CS230 |
| W4 | CS336, CS329Z, CME295, CME296, CS224N, CS230 |
| W5 | CS336, CS329Z, CME295, CME296, CS224N, CS230 |
| W6 | CS336, CS329Z, CME295, CME296, CS224N, CS230 |
| W7 | CS336, CS329Z, CME295, CME296, CS224N, CS230 |
| W8 | CS336, CS329Z, CME295, CME296, CS224N, CS230 |
| W9 | CS336, CS329Z, CME295, CME296, CS224N, CS230 |
| W0 | CS336, CS329Z, CME295, CME296, CS224N, CS230 |


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