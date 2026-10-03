import json,pytest
from test_harness import load
@pytest.fixture
def e(): return load('translation_parity.py','TranslationParity','pairs')
def test_review_receipt(e):
 _,c,q,b,U=e;c.register_pair('POL-1','https://policy.example/en','https://policy.fr/es','en','fr')
 a='The permit lasts twelve months and may be renewed.'; z='Le permis dure douze mois et peut etre renouvele.'; out='{"status":"PARITY","summary":"Obligations and duration agree.","missing_concepts":[],"material_differences":[],"confidence":96}'
 b.extend([a,z,a,z]); q.extend([out,out]); c.review_pair('pol-1'); r=json.loads(c.get_pair('0xowner','POL-1')); assert r['state']=='REVIEWED' and r['status']=='PARITY' and len(r['digests'])==2
def test_guards(e):
 _,c,q,b,U=e
 with pytest.raises(U): c.register_pair('BAD','http://policy.example/en','https://policy.fr/es','en','fr')
 with pytest.raises(U): c.register_pair('BAD','https://policy.example/en','https://policy.example/fr','en','fr')
 c.register_pair('POL-1','https://policy.example/en','https://policy.fr/es','en','fr')
 with pytest.raises(U): c.register_pair(' pol-1 ','https://a.example/en','https://b.example/fr','en','fr')
def test_forged_validator_rejected(e):
 _,c,q,b,U=e;c.register_pair('POL-2','https://policy.example/en','https://policy.fr/es','en','fr');b.extend(['A legal deadline is 30 days.','Le delai legal est de 60 jours.','A legal deadline is 30 days.','Le delai legal est de 60 jours.']);q.extend(['{"status":"PARITY","summary":"forged","missing_concepts":[],"material_differences":[],"confidence":99}','{"status":"DRIFT","summary":"deadline differs","missing_concepts":[],"material_differences":["deadline"],"confidence":98}'])
 with pytest.raises(U): c.review_pair('POL-2')
