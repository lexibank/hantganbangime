from setuptools import setup, find_packages
import json


with open("metadata.json", encoding="utf-8") as fp:
    metadata = json.load(fp)


setup(
    name="lexibank_hantganbangime",
    version="1.2.0",
    description=metadata["title"],
    license=metadata.get("license", ""),
    url=metadata.get("url", ""),
    py_modules=["lexibank_hantganbangime"],
    packages=find_packages(where="src"),
    include_package_data=True,
    zip_safe=False,
    entry_points={"lexibank.dataset": ["hantganbangime=lexibank_hantganbangime:Dataset"]},
    install_requires=["pylexibank>=3.0"],
)
