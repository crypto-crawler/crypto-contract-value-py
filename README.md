# crypto-contract-value

Python bindings for the [crypto-contract-value](https://github.com/soulmachine/crypto-crawler-rs/tree/main/crypto-contract-value) library.

## Quickstart

Install,

```bash
pip3 install crypto-contract-value
```

```python
from crypto_contract_value import MarketType, get_contract_value


assert get_contract_value("binance", MarketType['inverse_swap'], 'BTCUSD')== 100.0
assert get_contract_value("binance", MarketType['inverse_swap'], 'ETHUSD')== 10.0
```

## How to build

On Mac OS X,

```bash
conda install --file requirements-dev.txt

rm -rf build crypto-contract-value-ffi/target
python3 setup.py bdist_wheel

# Need to create a ~/.pypirc file first
twine upload --repository testpypi dist/*
python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps crypto-contract-value

twine upload dist/*
```

For Linux,

```bash
docker run -it --rm -v $(pwd):/project soulmachine/rust:manylinux2014 bash

/opt/python/cp36-cp36m/bin/pip3 install -r requirements-dev.txt
rm -rf build crypto-contract-value-ffi/target
/opt/python/cp36-cp36m/bin/python3 setup.py bdist_wheel
auditwheel repair dist/*linux*.whl --plat manylinux2014_x86_64
/opt/python/cp36-cp36m/bin/twine upload --repository testpypi wheelhouse/*
```

## Test

```bash
python3 setup.py develop
pytest -s
```
