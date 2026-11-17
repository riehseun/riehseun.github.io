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

Randomly pick a question out of Leet 250 if Array & Hashmap, Two Pointers, Sliding Window.
Randomly pick a question out of Leet 150 if everything else.

| Topic | Problems |
|---|---:|
| Arrays & Hashing (Prefix Sum, String) | Neet 250 |
| Two Pointers | Neet 250 |
| Stack | Neet 150 |
| Binary Search | Neet 150 |
| Sliding Window | Neet 250 |
| Linked List | Neet 150 |
| Tree (DFS, BFS) | Neet 150 |
| Heap | Neet 150 |
| Graph (DFS, BFS, Topological Sort, Union Find) | Neet 150 |
| 1D DP | Neet 150 |
| Interval | Neet 150 |
| Greedy | Neet 150 |
| Advanced Graph (Dijkstra, Bellman-Ford, Prim, Hierholzer) | Neet 150 |
| 2D DP | Neet 150 |
| Trie | Neet 150 |
| Backtracking | Neet 150 |
| Math & Geometry | Out of Scope |
| Bit Manipulation | Out of Scope |

| Topic | Problems |
|---|---:|
| Rate limiter | 359, 362, 933, 346, 1797 |
| LRU cache with TTL, thread-safe | 146, 460, 1797, 2622 |
| Micro-batching collector | 1188, 622, 1834, 2636 |
| DAG task executor | 207, 210, 1136, 2050, 2115, 269 |
| Worker pool / bounded queue | 1188, 1114, 1115, 1116, 1195, 1226, 1242 |
| KV store with transactions | 588, 1166, 2043, 380, 1146 |
| Time-versioned KV store | 981, 1146, 2034 |
| Retry, backoff, circuit breaker |  |
| Request router / load balancer | 1882, 1606, 528, 2402 |
| Log / metrics aggregator | 347, 692, 295, 480, 239, 1396, 636, 635 |
| Job scheduler with priorities and resources | 621, 1834, 253, 355, 1235, 2365, 2502, 3408 |
| Debug a broken codebase | |


# SOFTWARE ENGINEERING (25%)

| Week | Plan |
|---|---|
| W1 | practice 1 behavioral story per day |
| W2 | practice 1 behavioral story per day |
| W3 | practice 1 behavioral story per day |
| W4 | practice 1 behavioral story per day |
| W5 | practice 1 behavioral story per day |
| W6 | practice 1 behavioral story per day |
| W7 | practice 1 behavioral story per day |
| W8 | practice 1 behavioral story per day |
| W9 | practice 1 behavioral story per day |
| W0 | practice 1 behavioral story per day |


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

| Topic | Detail |
|---|---:|
| Distributed Job Scheduler | job API, DAG dependencies, queueing, worker leasing, retries, priorities, multi-tenant fairness, exactly-once vs. at-least-once, duplicate execution, stuck leases, thundering herd on cron boundaries, backfills |
| Distributed Rate Limiter | token bucket vs. sliding window, central vs. local counters, per-tenant and per-key limits, fail-open vs. fail-closed, clock skew, hot keys, Redis failover, burst handling |
| Distributed Message Queue | partitioning, ordering, consumer groups, offsets, replication, retention, DLQ, backpressure, rebalancing, ordering vs. throughput, replay, poison messages |
| Distributed Cache | consistent hashing, replication, quorum, eviction, TTL, cache invalidation, hot-key mitigation, leader election, split brain, stampedes, consistency model choice |
| Metrics, Logging, Monitoring platform | push vs. pull models; agent-based collection; batching and buffering; backpressure and ingestion throttling |
| TinyURL | Out of Scope |
| Amazon | Out of Scope |
| Instagram | Out of Scope |
| Parking Reservation | Out of Scope |
| Hotel Reservation | Out of Scope |


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

| Topic | Detail |
|---|---:|
| Model Serving | model artifact distribution and deployment across serving nodes; cold starts, model warm-up, and readiness management; control plane vs. data plane, admission control and request prioritization; queue management, backpressure, overload protection, and load shedding; request deadlines, timeouts, and cancellation, P50/P95/P99 latency and tail-latency optimization; throughput vs. latency trade-offs; dynamic batching; GPU/CPU utilization and memory bottlenecks; model autoscaling and scale-to-zero trade-offs, health checks and readiness probes; circuit breakers and fallback models; model versioning and compatibility; canary analysis, automated rollback, and traffic shifting; shadow deployments and A/B testing, resource quotas, tenant isolation, fair scheduling, and noisy-neighbor mitigation |
| LLM Serving | GPU compute vs. memory bandwidth bottlenecks; GPU memory hierarchy; KV cache memory estimation; KV cache allocation, paging, eviction, and fragmentation (PagedAttention), continuous batching; prefix caching; chunked prefill; prefill/decode disaggregation; FlashAttention fundamentals; quantization (INT8, INT4, FP8); speculative decoding; multi-GPU inference (tensor and pipeline parallelism); CUDA graphs and expert parallelism for MoE (name-drop), LLM request scheduling, admission control, prioritization, and preemption; context-length limits and token budgeting; multi-LoRA / adapter serving; model routing and fallback, TTFT vs. TPOT vs. end-to-end latency; tokens per second, throughput, GPU and KV cache utilization; latency-throughput trade-offs under different workloads |
| Agentic Platform | DAG and state-machine execution; sequential and parallel tool execution; durable execution, checkpointing, recovery, and workflow versioning (see SD W4); agent loop and execution lifecycle; stateful vs. stateless agent execution; multi-agent communication and coordination, tool authentication, authorization, permissions, and access control; sandboxing, execution isolation, and resource limits; tool timeouts, cancellation, idempotency, and retry handling; prompt injection, tool output validation, and trust boundaries, context-window management; short-term vs. long-term memory; conversation state persistence; retrieval and context compression, offline and online evaluation, regression testing, and evaluation datasets; agent trajectory evaluation (end-to-end task success, tool-call success rate, tool-selection errors, hallucination); failure detection and recovery; human approval and escalation, token budgets and cost attribution; model selection and routing; caching and reuse; concurrency limits and rate limiting |
| Model Training | distributed data loading; data sharding and sampling; data preprocessing bottlenecks; storage throughput and caching, gang scheduling; GPU fragmentation, allocation, and topology; scheduling fairness and priority; multi-tenant workload isolation; elastic training and worker scaling; training/inference workload contention, data parallelism and FSDP; tensor and pipeline parallelism; AllReduce and NCCL; communication/computation overlap; gradient accumulation and gradient checkpointing; mixed precision training; RDMA and InfiniBand (name-drop), distributed checkpoint coordination; asynchronous vs. synchronous checkpointing; checkpoint frequency, recovery-point objectives, and checkpoint storage; recovery from partial worker failures; training job preemption and resumption, GPU and memory utilization; data-loader wait time; communication overhead and network bandwidth; straggler identification; training throughput and time-to-train |
| Feature Store | feature definitions and metadata; feature registry, versioning, ownership, and discovery; feature schema evolution; online vs. offline store architecture; feature transformation consistency between training and inference, batch vs. streaming feature computation; stream processing and event-time vs. processing-time semantics; windowed aggregations; late-arriving events and corrections; point-in-time joins and historical feature retrieval, low-latency and batch feature retrieval; cache strategies and eviction; hot-key mitigation; fallback behavior for missing or stale features, training-serving skew detection and prevention; feature freshness SLAs and monitoring; data quality validation; backfill consistency and recovery; online/offline synchronization, high-throughput feature ingestion; partitioning and replication; multi-tenant isolation; storage cost optimization |
| Recommendation System | Out of Scope |
| Search Ranking | Out of Scope |
| Real-time Detection | Out of Scope |
| Fraud Detection (Layer6 AI) | Out of Scope |
| Real-time Auction (Index Exchange) | Out of Scope |


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