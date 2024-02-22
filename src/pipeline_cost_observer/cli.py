import argparse
from pipeline_cost_observer.core import build_snapshot


def main() -> None:
    parser = argparse.ArgumentParser(description="Observer utilities for runtime, storage, and cost estimates across pipeline stages.")
    parser.add_argument("--summary", action="store_true")
    args = parser.parse_args()
    if args.summary:
        print(build_snapshot())


if __name__ == "__main__":
    main()
