from backend.database import query

query("""
MERGE (d:DrugCandidate {id: $drug_id}) SET d.name = $drug
MERGE (x:Disease {id: $disease_id}) SET x.name = $disease
MERGE (s:ResearchSession {id: $session_id})
MERGE (a:Assessment {id: $assessment_id})
  SET a.status = $status, a.rationale = $rationale, a.created_at = $created_at
MERGE (d)-[:EVALUATED_FOR]->(x)
MERGE (a)-[:ABOUT_DRUG]->(d)
MERGE (a)-[:ABOUT_DISEASE]->(x)
MERGE (a)-[:RECORDED_IN]->(s)
""", {
    "drug_id": "drug_demo_1", "drug": "ExampleDrug",
    "disease_id": "disease_demo_1", "disease": "Parkinson disease",
    "session_id": "session_1", "assessment_id": "assessment_1",
    "status": "needs_review",
    "rationale": "Initial evidence requires further evaluation.",
    "created_at": "2026-10-16T20:00:00+05:30",
})
print("Seeded.")