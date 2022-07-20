
# VHP4Safety Glossary

This work is licensed under the [CC-BY 4.0 International](https://github.com/VHP4Safety/glossary/blob/main/LICENCE.md). 

<div about="https://vhp4safety.github.io/cloud/glossary#" typeof="owl:Ontology">
<p>
  This <span property="dc:title">VHP4Safety Glossary</span> ontology is collected by (in alphabetical order)
  <span property="dc:contributor">Ozan Çınar</span>, <span property="dc:contributor">Marvin Martens</span>,
  <span property="dc:contributor">Egon Willighagen</span>, and others from the VHP4Safety project.
</p>
</div>

## DEVELOPMENT VERSION

This glossary is under development.

To make new entry queries, please create an issue [here](https://github.com/VHP4Safety/glossary/issues/new/choose)
using the [issue template](https://github.com/VHP4Safety/glossary/blob/main/.github/ISSUE_TEMPLATE/ontology-term-request.md).
For other issues, suggestions, or problems, please create an issue [here](https://github.com/VHP4Safety/glossary/issues). 
Experienced GitHub users are encouraged to submit pull requests.

## Toxicology in General

| **Term** 									| **Abbreviation** 	| **Definition** 										| 
|-------------------------------------------|-------------------|-------------------------------------------------------|
| 3 Rs Principle                            | 3Rs 				| Replacement, Reduction, Refinement 					|
| Bench mark dose 							| BMD 				| 														|
| Developmental and Reproductive Toxicology | DART 				| 														|
| Developmental Neurotoxicity               | DNT				| 														|
| Embryonic Stem Cell 						| EST 				| Typically combined like: hESTc (human, cardiac) 		|
| Lowest Observed Adverse Effect Level 		| LOAEL 			| 														|
| New Approach Methodology 					| NAM 				| 														|		
| No Observed Adverse Effect Levek 			| NOAEL 			| 														|
| Teratology             					|                   | Study of bith defects (literally study of monsters) 	|
| The legislation of ‘Registration, Evaluation, Authorisation and Restriction of Chemicals’ | REACH | 					|


## Adverse Outcome Pathway-related terms

| **Term** 									| **Abbreviation** 	| **Definition** 										| 
|-------------------------------------------|-------------------|-------------------------------------------------------|
| Adverse Outcome 							| AO				| 														|
| Adverse Outcome Pathway					| AOP 				| 														|		
| European Centre for the Validation of Alternative Methods | ECVAM | 													|		
| European Chemical Agency 					| ECHA 				| Legislator 											|
| European Food Safety Authority 			| EFSA 				| Legislator 											|
| Key Event 								| KE 				| 														|
| Key Event Relationship 					| KER 				| 														|
| Molecular Adverse Outcome Pathways 		| mAOP 				| Metapathway connected events as e.g. WikiPathways pathways |
| Molecular Initiating Event 				| MIE 				| 														|
| Quantitative Adverse Outcome Pathway 		| qAOP 				| Reserved for "Leiden" approach on coexpression changes|
| Stressor 									| 					| 														|


## Server-related terms

| **Term** 									| **Abbreviation** 	| **Definition** 										| 
|-------------------------------------------|-------------------|-------------------------------------------------------|
| Docker image  							| 					| 														|
| Secure Shell 								| ssh 				| 														|		
| Strato 									| 					| 														|
| VHP server 1 								| 					| 														|
| VHP server 2 								| 					| 														|


## Risk assessment-related terms

<table prefix="rdfs: http://www.w3.org/2000/01/rdf-schema#">
  <tr> <!-- the header -->
    <td><b>Term</b></td>
    <td><b>Abbreviation</b></td>
    <td><b>Definition</b></td>
  </tr>
  <tr about="https://vhp4safety.github.io/cloud/glossary#VHP0000001" typeof="owl:Class">
    <td property="rdfs:label">Apical Endpoint</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>High Throughput Screening</td>
    <td>HTS</td>
    <td></td>
  </tr>
  <tr>
    <td>Integrated Approaches to Testing and Assessment</td>
    <td>IATA</td>
    <td></td>
  </tr>
  <tr>
    <td>Mode of Action</td>
    <td>MoA</td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td>NOEL</td>
    <td></td>
  </tr>
</table>

## Tool/service-related terms

| **Term** 									| **Abbreviation** 	| **Definition** 										| 
|-------------------------------------------|-------------------|-------------------------------------------------------|
| Accessible								| 					| 														|
| Application Programming Interface			| API				| 														|
| Data stewardship							|					|														|
| FAIR	 									| 					| 														|
| Findable 									| 					| 														|
| Identifier								|					|														|
| Interoperable								| 					| 														|
| Metadata									|					|														|
| Model										|					|														|
| Ontology 									| 					| 														|
| Open Data									| 					|														|
| Physiologically Based (Pharma) Kinetic Modelling | PBPK 		|														|
| Quantitative Structure Activity Relationships	| QSAR 			| 														|
| Resource Description Framework			| RDF				| 														|
| Reusable									| 					| 														|
| Sysrev									| 					| Ortec's literature reviewe support and  curation documentationn storage system. |
| 											| DMP 				| 														|
| 											| IVIVE 			| 														|

## Project-related terms

| **Term** 									| **Abbreviation** 	| **Definition** 										| 
|-------------------------------------------|-------------------|-------------------------------------------------------|
| Research Line 1 							| RL1				| Building the Virtual Human Platform					|
| Research Line 2 							| RL2				| Feeding the Virtual Human Platform														|
| Research Line 3 							| RL3				| Implementing the Virtual Human Platform														|
| Work Package 1.1							| WP1.1				| Building the ICT infrastructure for the VHP: objectives to develop the technical infrastructure, setting up a predictive platform, developing analysis workflows, making services and data available and interoperable									|
| Work Package 1.2							| WP1.2				| In silico toxicokinetics: objectives to define parameters required for PBPK modelling, developing PBK models and providing guidance for in vitro to in vivo extrapolations 									|
| Work Package 1.3							| WP1.3				| Computational toxicodynamics: objectives to develop QSAR and MIE prediction models, develop qAOPs, testing the platform and generating safety estimates									|
| Work Package 2.1							| WP2.1				| In vitro models to provide toxicokinetics & toxicodynamics parameters: objectives to verify in vitro models for ADME and local toxicity, obtaining parameters for PBK modelling, test chemicals on iPSC models 									|
| Work Package 2.2							| WP2.2				| Disease state - Case study chronic kidney disease: objectives to identify critical physiological pathways, develop AOP networks, test toxicity of selected drugs, and assess the safety of selected drugs								|
| Work Package 2.3							| WP2.3				| Life course exposure - Case study neurodegenerative disease and life course exposure to chemicals: objectives to identify critical physiological pathways, model life time exposure, develop AOP networks, test toxicity and assess the safety of selected chemicals									|
| Work Package 2.4							| WP2.4				| Age and gender specific safety - Case study Thyroid mediated developmental neurotoxicity: objectives to collect mechanistic physiological data, determine critical pathways, establish quantitative AOP network, identify gender-specific sentitivities and compounds that discriminate, and assess the safety of compound exposure							|
| Work Package 3.1							| WP3.1				| Technology Assessment of VHP: objectives to perform technology assessment, study and analyse the initiation, development and implementation of VHP, and specify performance criteria 									|
| Work Package 3.2							| WP3.2				| Acceptance of VHP for safety assessment: objectives to position the VHP in the transition to animal-free safety assessment, raise awareness, investigate uncertainties and acceptance of safety assessments									|
| Work Package 3.3							| WP3.3				| Training and Education: objectives to promote collaboration, facilitate transferability of methods and models, implementing new teaching modules, promote capacity building and awareness of stakeholders, improve skills regarding risk communication									|
| Work Package 4							| WP4				| Project Coordination, Impact and Data Management: objectives to ensure that project objectives are achieved, deliverables are completed, manage overall knowledge utilisation, and provide effective and sustainable data management							|


### Funding

VHP4Safety – the Virtual Human Platform for safety assessment project
[NWA 1292.19.272](https://www.nwo.nl/projecten/nwa129219272) is part of the NWA
research program ‘Research along Routes by Consortia (ORC)’, which is funded by the Netherlands Organization
for Scientific Research (NWO). The project started on June 1, 2021 with a budget of over 10 million Euros
and will last for the duration of 5 years. 
