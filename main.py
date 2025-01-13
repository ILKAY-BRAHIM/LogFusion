from executor import Executor


if __name__ == "__main__":
    commands = [
        "curl -s https://raw.githubusercontent.com/k3d-io/k3d/main/install.sh | bash",
        "k3d cluster create streamguard-cluster --servers 1 --agents 2 --kubeconfig-update-default --wait",
        "k3d cluster delete streamguard-cluster",
    ]

    executor = Executor()
    executor.start(commands)