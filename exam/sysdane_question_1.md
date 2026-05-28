# Debug system-level performance issues in a large-scale GPU-backed model training setup

Identity bottleneck
- Use NSight (assuming NVIDIA GPUs)

CPU compute - if GPUs are at 95%+ capacity
Communication - GPUs sit idle, all-reduce takes long time
Input - 
Memory - 