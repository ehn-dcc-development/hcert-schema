# Electronic Health Certificate Schemata

This repository contains schemata for Electronic Health Certificates:

- [EU Digital Green Certificate v1](eu_hcert_v1_schema.yaml) -- `eu_dgc_v1`, claim key 1


## Implementation Notes

### CBOR Encoding

Concise Binary Object Representation (CBOR), specified in [RFC7049](https://tools.ietf.org/html/rfc7049), defined a number of major data types. The following types are RECOMMENDED to be used by parties creating electronic health certificates payloads:

- Integers are encoded as CBOR major type 0, an unsigned integer.
- Strings are encoded as CBOR major type 3. a text string.
- Arrays are encoded as CBOR major type 4, an array of data items.
- Objects are encoded as CBOR major type 5, a map of pairs of data items.

Parties validating payloads are strongly advised to follow the robustness principle and be liberal in what you accept from others.
