# Airport Codes

Get airport information from Wikipedia.

## Preset Data

If you would like to get preset data, See [/preset-data](/preset-data).

Please note it may not be up to date.

## Get Data on Your Own

### Requirements

* Python 3

### Install

```
pip install -r requirements.txt
```

### Usage

```
python3 main.py [-o/--optput <Output File>] [-l/--language <Wikipedia language>] [-v/--variant <Variant>] [--http-proxy <HTTP Proxy URL>]
```

#### Example

```
python3 main.py -o results/chinese.json -l zh -v zh-hk --http-proxy http://user:pass@10.11.22.33:3128
```

### Supported Languages

> Please note that data from the non-English Wikipedia may missing some information. (e.g. ICAO Codes)

## License

MIT
