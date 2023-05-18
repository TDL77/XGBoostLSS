from setuptools import setup, find_packages

setup(
    name="xgboostlss",
    version="0.2.0",
    description="XGBoostLSS - An extension of XGBoost to probabilistic forecasting",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Alexander März",
    author_email="alex.maerz@gmx.net",
    url="https://github.com/StatMixedML/XGBoostLSS",
    license="Apache License 2.0",
    packages=find_packages(exclude=["tests"]),
    include_package_data=True,
    package_data={'': ['datasets/*.csv']},
    zip_safe=True,
    python_requires=">=3.9",
    install_requires=[
        "xgboost~=1.7.5",
        "torch~=2.0.1",
        "optuna~=3.1.1",
        "properscoring~=0.1",
        "scikit-learn~=1.2.2",
        "git+https://github.com/dsgibbons/shap.git",
        "numpy~=1.24.3",
        "pandas~=2.0.1",
        "plotnine~=0.12.1",
        "scipy",
        "tqdm",
        "matplotlib",
    ],
    test_suite="tests",
    tests_require=["flake8", "pytest"],
)
