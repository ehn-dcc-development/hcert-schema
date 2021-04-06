PAYLOAD_SCHEMA_YAML=	eu_hcert_v1_schema.yaml
PAYLOAD_SCHEMA_JSON=	eu_hcert_v1_schema.json


all: $(PAYLOAD_SCHEMA_JSON)
	
$(PAYLOAD_SCHEMA_JSON): $(PAYLOAD_SCHEMA_YAML)
	python3 schemacheck.py --json $< >$@
