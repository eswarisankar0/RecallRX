from backend.database import query


def get_candidate_history(drug_id):
    return query("""
    MATCH (a:Assessment)-[:ABOUT_DRUG]->(d:DrugCandidate {id: $drug_id})
    MATCH (a)-[:ABOUT_DISEASE]->(x:Disease)
    MATCH (a)-[:RECORDED_IN]->(s:ResearchSession)
    RETURN a.id, a.status, a.rationale, a.created_at, d.name, x.name, s.id
    ORDER BY a.created_at
    """, {"drug_id": drug_id})


if __name__ == "__main__":
    for row in get_candidate_history("drug_demo_1"):
        print(row)