PAYLOAD_SCHEMA_YAML=		eu_hcert_v1_schema.yaml
PAYLOAD_SCHEMA_JSON=		eu_hcert_v1_schema.json
PAYLOAD_SCHEMA_JSON_DRAFT_07=	eu_hcert_v1_schema_draft_07.json

GENERATED=	$(PAYLOAD_SCHEMA_JSON) $(PAYLOAD_SCHEMA_JSON_DRAFT_07)


all: $(GENERATED)

test: $(PAYLOAD_SCHEMA_YAML)
	python3 schemacheck.py $<
	
$(PAYLOAD_SCHEMA_JSON): $(PAYLOAD_SCHEMA_YAML)
	python3 schemacheck.py --json $< >$@

$(PAYLOAD_SCHEMA_JSON_DRAFT_07): $(PAYLOAD_SCHEMA_YAML)
	python3 schemacheck.py --json --version draft-07 $< >$@

clean:
	rm -f $(GENERATED)
