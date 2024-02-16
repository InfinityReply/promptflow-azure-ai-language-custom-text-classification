from setuptools import find_packages, setup

PACKAGE_NAME = "promptflow-azure-ai-language-custom-text-classification"

setup(
    name=PACKAGE_NAME,
    version="0.1.0",
    description="Use Azure AI Language to generate abstractive summaries of documents.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    entry_points={
        "package_tools": ["custom_text_classification = custom_text_classification_tool.tools.utils:list_package_tools"],
    },
    include_package_data=True,   # This line tells setuptools to include files from MANIFEST.in
)