from setuptools import setup

setup(
    name="reda-2024-pipeline-cost-observer",
    version="0.1.0",
    description="Observer utilities for runtime, storage, and cost estimates across pipeline stages.",
    author="Red@",
    packages=["pipeline_cost_observer"],
    package_dir={"": "src"},
)
