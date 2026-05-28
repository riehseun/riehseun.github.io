# Debug system-level performance issues in a large-scale GPU-backed model training setup

Track metrics
- MFU (Model FLOPs utilization): how much of GPU capabilties are used in computation
- Step Time Breakdown: track where time is spent during model training
- GPU utilization: low usually means starvation 
- SM (Streaming Multiprocessor) occupancy: high occupancy means high throughput

Identity bottleneck - Use NSight (assuming NVIDIA GPUs)
- GPU compute : if GPUs are at 95%+ capacity but low MFU
- GPU memory: high occupancy but low throughput
- Communication - GPUs sit idle, all-reduce takes long time (step time increases during all-reduce)
- Input: GPUs are waiting for data (periodic drop in GPU utilization)

Remediate
- GPU compute : combine operations (for example, attention computation) into single GPU kernal
- GPU memory: recompute activation instead of storing it to relieve memory footprint (small increase in compute cost)
- Communication: perform all-reduce in async, compress gradients, use larger batch size
- Input: prefetch batches into GPU memory, increase number of workers to perform data loading

