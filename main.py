from ClusterManager import ClusterManager
from DataProcessingTask import DataProcessingTask
from EmailNotificationTask import EmailNotificationTask
from ResourceCapacityException import ResourceCapacityException
from WorkerNode import WorkerNode

if __name__ == "__main__":
    # 1. Creating a manager and a server with space for 2 tasks
    manager = ClusterManager()
    node = WorkerNode(node_id="Node-1", max_capacity=2)
    manager.register_node(node)

    # 2. Creating a task and sending it to a cluster
    task = DataProcessingTask(task_id=1, priority=5, payload_size_mb=100)
    manager.dispatch(task)

    # 3. Running the tasks and printing the result
    results = manager.run_cluster()
    print(results)