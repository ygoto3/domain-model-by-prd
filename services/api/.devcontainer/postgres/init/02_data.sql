\c db

INSERT INTO prd (title, body) VALUES ('Sample PRD', '# What is this?' || CHR(10) || CHR(10) || 'This is a sample PRD.');
INSERT INTO domain_model (prd_id, mermaid) VALUES (1, 'classDiagram' || CHR(10) || '    class Animal' || CHR(10) || '    Vehicle <|-- Car');
