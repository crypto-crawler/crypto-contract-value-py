from setuptools import find_packages, setup


def build_native(spec):
    build = spec.add_external_build(
        cmd=['cargo', 'build', '--release'],
        path='./crypto-contract-value-ffi'
    )
    spec.add_cffi_module(
        module_path='crypto_contract_value._lowlevel',
        dylib=lambda: build.find_dylib(
            'crypto_contract_value_ffi', in_path='target/release'),
        header_filename=lambda: build.find_header(
            'crypto_contract_value.h', in_path='include'),
        rtld_flags=['NOW', 'NODELETE']
    )


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='crypto_contract_value',
    version="0.0.2",
    author="soulmachine",
    description="Get the unit value of a crypto contract",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/soulmachine/crypto-contract-value-py",
    packages=find_packages(),
    include_package_data=True,
    setup_requires=['milksnake'],
    install_requires=['milksnake'],
    milksnake_tasks=[build_native],
    python_requires='>=3.6',
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: Apache Software License",
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords=['blockchain', 'cryptocurrency', 'trading'],
)
