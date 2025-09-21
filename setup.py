from setuptools import setup, find_packages
from pip._internal.req import parse_requirements  
setup(
    name="Document_Intelligence_Platform",
    author="Harikrishna Nariyanpilly",
    version="0.1",
    description="RAG-powered LLMOps pipeline for enterprise document Q&A.",
    packages=find_packages(),
    include_package_data=True,
    extras_require={
        "dev": ["pytest", "pylint", "ipykernel"]
    },
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.10",
)
