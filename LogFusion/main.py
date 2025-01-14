import argparse
from LogFusion import LogFusion

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="LogFusion: A tool to run commands with animated output.")
    parser.add_argument(
        "commands",
        metavar="CMD",
        type=str,
        nargs="+",
        help="Shell commands to execute. Provide them as space-separated strings.",
    )
    args = parser.parse_args()

    # Initialize LogFusion
    log_fusion = LogFusion()

    # Start the execution of commands
    log_fusion.start(args.commands)

if __name__ == "__main__":
    main()
