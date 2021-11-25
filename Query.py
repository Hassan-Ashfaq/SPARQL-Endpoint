Mapper  = [
    ["List all Nobel Prize categories?", 0],
    ["List the names of all persons who won the Nobel Prize in Chemistry?", 1],
    ["Who won the Nobel Prize in Chemistry in 1911?", 2],
    ["List the names of all persons who won the Nobel Prize in Chemistry, ordered by the year of the award.", 3],
    ["Who won the Nobel Prize in Physics in 1930?", 4],
    ["List all Nobel Prize laureates from Sweden or Finland?", 5]
]

All_Queries = [
"""PREFIX : <http://data.nobelprize.org/resource>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX nobel: <http://data.nobelprize.org/terms/>

SELECT * WHERE{
?Categories rdf:type nobel:Category.
}""", 
"""PREFIX : <http://data.nobelprize.org/resource>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX nobel: <http://data.nobelprize.org/terms/>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX category: <http://data.nobelprize.org/resource/category/>

SELECT ?name ?NobelPrize WHERE{
?people rdf:type nobel:Laureate;
foaf:name ?name;
nobel:nobelPrize ?NobelPrize.
?NobelPrize nobel:category category:Chemistry.
}""", 
"""PREFIX : <http://data.nobelprize.org/resource>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX nobel: <http://data.nobelprize.org/terms/>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX category: <http://data.nobelprize.org/resource/category/>

SELECT ?name ?NobelPrize WHERE{
?people rdf:type nobel:Laureate;
foaf:name ?name;
nobel:nobelPrize ?NobelPrize.
?NobelPrize nobel:category category:Chemistry;
nobel:year 1911.
}""",
"""PREFIX : <http://data.nobelprize.org/resource>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX nobel: <http://data.nobelprize.org/terms/>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX category: <http://data.nobelprize.org/resource/category/>

SELECT ?name ?year WHERE{
?people rdf:type nobel:Laureate;
foaf:name ?name;
nobel:nobelPrize ?NobelPrize.
?NobelPrize nobel:category category:Chemistry;
nobel:year ?year.
} order by ASC (?year)""",
"""PREFIX : <http://data.nobelprize.org/resource>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX nobel: <http://data.nobelprize.org/terms/>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX category: <http://data.nobelprize.org/resource/category/>

SELECT ?name ?NobelPrize WHERE{
?people rdf:type nobel:Laureate;
foaf:name ?name;
nobel:nobelPrize ?NobelPrize.
?NobelPrize nobel:category category:Physics;
nobel:year 1930.
}""",
"""PREFIX : <http://data.nobelprize.org/resource>
PREFIX nobel: <http://data.nobelprize.org/terms/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX country: <http://data.nobelprize.org/resource/country/>
PREFIX db: <http://dbpedia.org/ontology/>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>

SELECT ?name WHERE{
   {?people rdf:type nobel:Laureate;
           	foaf:name ?name;
        	db:birthPlace country:Sweden.}
   UNION 
   {?people rdf:type nobel:Laureate;
            foaf:name ?name;
        	db:birthPlace country:Finland.}
}"""]