from WorkerNode import WorkerNode
from BaseTask import BaseTask

class ClusterManager:
    def __init__(self, nodes=None, completed_archive=None):
        self.nodes = {n.node_id: n for n in nodes} if nodes else {}
        self.completed_archive = list(completed_archive) if completed_archive else []

    def register_node(self, node: WorkerNode):
        if node.node_id in self.nodes:
            raise ValueError(f"Worker node with ID '{node.node_id}' already exists.")
        self.nodes[node.node_id] = node

    @property
    def total_capacity_available(self):
        return sum(node.max_capacity - len(node) for node in self.nodes)


    def dispatch(self, task: BaseTask):
        available_nodes = [node for node in self.nodes.values() if len(node) < node.max_capacity]
        if not available_nodes:
            raise ResourceCapacityException("All cluster nodes are currently saturated.")
        best_node = min(available_nodes, key=lambda node: len(node) / node.max_capacity)

        best_node.assign_task(task)
        return best_node

    def run_cluster(self) -> list[dict]:
        summaries = []
        for node in self.nodes.values():
            summary = node.process_all()
            summaries.append(summary)
        return summaries