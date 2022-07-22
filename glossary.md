
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

<table prefix="rdfs: http://www.w3.org/2000/01/rdf-schema# ncit: http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl# dc: http://purl.org/dc/elements/1.1/">
  <tr> <!-- the header -->
    <td><b>Term</b></td>
    <td><b>Abbreviation</b></td>
    <td><b>Definition</b></td>
  </tr>

  <tr>
    <td property="rdfs:label">3 Rs Principle</td>
    <td property="ncit:C42610">3Rs</td>
    <td property="dc:description">Replacement, Reduction, Refinement.</td>
  </tr>

  <tr>
    <td property="rdfs:label">Bench mark dose</td>
    <td property="ncit:C42610">BMD</td>
    <td property="dc:description"></td>
  </tr>

  <tr>
    <td property="rdfs:label">Developmental and Reproductive Toxicology</td>
    <td property="ncit:C42610">DART</td>
    <td property="dc:description"></td>
  </tr>

  <tr>
    <td property="rdfs:label">Developmental Neurotoxicity</td>
    <td property="ncit:C42610">DNT</td>
    <td property="dc:description"></td>
  </tr>

  <tr>
    <td property="rdfs:label">Embryonic Stem Cell</td>
    <td property="ncit:C42610">EST</td>
    <td property="dc:description">Typically combined like: hESTc (human, cardiac).</td>
  </tr>

  <tr>
    <td property="rdfs:label">Lowest Observed Adverse Effect Level</td>
    <td property="ncit:C42610">LOAEL</td>
    <td property="dc:description"></td>
  </tr>

  <tr>
    <td property="rdfs:label">New Approach Methodology</td>
    <td property="ncit:C42610">NAM</td>
    <td property="dc:description"></td>
  </tr>
  <tr>
    <td property="rdfs:label">High Throughput Screening</td>
    <td property="ncit:C42610">HTS</td>
    <td property="dc:description"></td>
  </tr>
  <tr>
    <td property="rdfs:label">No Observed Adverse Effect Level</td>
    <td property="ncit:C42610">NOAEL</td>
    <td property="dc:description"></td>
  </tr>

  <tr>
    <td property="rdfs:label">Teratology</td>
    <td property="ncit:C42610"></td>
    <td property="dc:description">Scientific field that studies the causes, mechanisms, and classes of congenital malformations in animals and plants.<sup><a href="https://www.britannica.com/science/teratology">ref</a></sup></td>
  </tr>

  <tr>
    <td property="rdfs:label"></td>
    <td property="ncit:C42610">NOEL</td>
    <td property="dc:description"></td>
  </tr>

</table>


## Adverse Outcome Pathway-related terms

<table prefix="rdfs: http://www.w3.org/2000/01/rdf-schema# ncit: http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl# dc: http://purl.org/dc/elements/1.1/">
  <tr> <!-- the header -->
    <td><b>Term</b></td>
    <td><b>Abbreviation</b></td>
    <td><b>Definition</b></td>
  </tr>

  <tr>
    <td property="rdfs:label">Adverse Outcome Pathway</td>
    <td property="ncit:C42610">AOP</td>
    <td property="dc:description">An AOP describes a sequence of events commencing with initial interaction(s) of a stressor with a biomolecule within an organism that causes a perturbation in its biology (i.e., molecular initiating event, MIE), which can progress through a dependent series of intermediate key events (KEs) and culminate in an adverse outcome (AO) considered relevant to risk assessment or regulatory decision-making. <sup><a href="https://doi.org/10.1787/5jlv1m9d1g32-en">ref</a></sup>  </td>
  </tr>
  <tr>
    <td property="rdfs:label">Molecular Initiating Event</td>
    <td property="ncit:C42610">MIE</td>
    <td property="dc:description">A specialised type of key event that represents the initial point of chemical/stressor interaction at the molecular level within the organism that results in a perturbation that starts the AOP.<sup><a href="https://doi.org/10.1787/5jlv1m9d1g32-en">ref</a></sup></td>
  </tr>
  
  <tr>
    <td property="rdfs:label">Adverse Outcome</td>
    <td property="ncit:C42610">AO</td>
    <td property="dc:description">A specialised type of key event that is generally accepted as being of regulatory significance on the basis of correspondence to an established protection goal or equivalence to an apical endpoint in an accepted regulatory guideline toxicity test.<sup><a href="https://doi.org/10.1787/5jlv1m9d1g32-en">ref</a></sup></td>
  </tr>
  <tr>
    <td property="rdfs:label">Key Event</td>
    <td property="ncit:C42610">KE</td>
    <td property="dc:description">A change in biological or physiological state that is both measurable and essential to the progression of a defined biological perturbation leading to a specific adverse outcome.<sup><a href="https://doi.org/10.1787/5jlv1m9d1g32-en">ref</a></sup></td>
  </tr>

  <tr>
    <td property="rdfs:label">Key Event Relationship</td>
    <td property="ncit:C42610">KER</td>
    <td property="dc:description">A scientifically-based relationship that connects one key event to another, defines a causal and predictive relationship between the upstream and downstream event, and thereby facilitates inference or extrapolation of the state of the downstream key event from the known, measured, or predicted state of the upstream key event.<sup><a href="https://doi.org/10.1787/5jlv1m9d1g32-en">ref</a></sup></td>
  </tr>
  <tr>
    <td property="rdfs:label">Stressor</td>
    <td property="ncit:C42610"></td>
    <td property="dc:description"></td>
  </tr>
  <tr>
    <td property="rdfs:label">Molecular Adverse Outcome Pathways</td>
    <td property="ncit:C42610">mAOP</td>
    <td property="dc:description">Metapathway, similar to conventional AOPs, but connected events as e.g. WikiPathways pathways. Their function is to expand KEs with molecular pathways and allow analyses of omics data.</td>
  </tr>

  <tr>
    <td property="rdfs:label">Quantitative Adverse Outcome Pathway</td>
    <td property="ncit:C42610">qAOP</td>
    <td property="dc:description">Reserved for "Leiden" approach on coexpression changes.</td>
  </tr>



</table>


## Server-related terms

<table prefix="rdfs: http://www.w3.org/2000/01/rdf-schema# ncit: http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl# dc: http://purl.org/dc/elements/1.1/">
  <tr> <!-- the header -->
    <td><b>Term</b></td>
    <td><b>Abbreviation</b></td>
    <td><b>Definition</b></td>
  </tr>

  <tr>
    <td property="rdfs:label">Docker image</td>
    <td property="ncit:C42610"></td>
    <td property="dc:description"></td>
  </tr>

  <tr>
    <td property="rdfs:label">Secure Shell</td>
    <td property="ncit:C42610">ssh</td>
    <td property="dc:description"></td>
  </tr>

  <tr>
    <td property="rdfs:label">Strato</td>
    <td property="ncit:C42610"></td>
    <td property="dc:description"></td>
  </tr>

  <tr>
    <td property="rdfs:label">VHP server 1</td>
    <td property="ncit:C42610"></td>
    <td property="dc:description"></td>
  </tr>

  <tr>
    <td property="rdfs:label">VHP server 2</td>
    <td property="ncit:C42610"></td>
    <td property="dc:description"></td>
  </tr>

</table>


## Risk assessment-related terms

<table prefix="rdfs: http://www.w3.org/2000/01/rdf-schema# ncit: http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl# dc: http://purl.org/dc/elements/1.1/">
  <tr> <!-- the header -->
    <td><b>Term</b></td>
    <td><b>Abbreviation</b></td>
    <td><b>Definition</b></td>
  </tr>

  <tr about="https://vhp4safety.github.io/cloud/glossary#VHP0000001" typeof="owl:Class">
    <td property="rdfs:label">Apical Endpoint</td>
    <td property="ncit:C42610"></td>
    <td property="dc:description"></td>
  </tr>



  <tr>
    <td property="rdfs:label">Integrated Approaches to Testing and Assessment</td>
    <td property="ncit:C42610">IATA</td>
    <td property="dc:description"></td>
  </tr>

  <tr>
    <td property="rdfs:label">Mode of Action</td>
    <td property="ncit:C42610">MoA</td>
    <td property="dc:description"></td>
  </tr>


  <tr>
    <td property="rdfs:label">European Centre for the Validation of Alternative Methods</td>
    <td property="ncit:C42610">ECVAM</td>
    <td property="dc:description"></td>
  </tr>

  <tr>
    <td property="rdfs:label">European Chemical Agency</td>
    <td property="ncit:C42610">ECHA</td>
    <td property="dc:description">Legislator</td>
  </tr>

  <tr>
    <td property="rdfs:label">European Food Safety Authority</td>
    <td property="ncit:C42610">EFSA</td>
    <td property="dc:description">Legislator</td>
  </tr>
    <tr>
    <td property="rdfs:label">The legislation of ‘Registration, Evaluation, Authorisation and Restriction of Chemicals’</td>
    <td property="ncit:C42610">REACH</td>
    <td property="dc:description">Regulation (EC) No 1907/2006 of the European Parliament and of the Council concerning the Registration, Evaluation, Authorisation and Restriction of Chemicals (REACH)<sup><a href="http://data.europa.eu/eli/reg/2006/1907/2022-05-01">ref</a></sup></td>
  </tr>
</table>


## Tool/service-related terms

<table prefix="rdfs: http://www.w3.org/2000/01/rdf-schema# ncit: http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl# dc: http://purl.org/dc/elements/1.1/">
  <tr> <!-- the header -->
    <td><b>Term</b></td>
    <td><b>Abbreviation</b></td>
    <td><b>Definition</b></td>
  </tr>



  <tr>
    <td property="rdfs:label">Application Programming Interface</td>
    <td property="ncit:C42610">API</td>
    <td property="dc:description"></td>
  </tr>

  <tr>
    <td property="rdfs:label">Data stewardship</td>
    <td property="ncit:C42610"></td>
    <td property="dc:description"></td>
  </tr>
 <tr>
    <td property="rdfs:label">Identifier</td>
    <td property="ncit:C42610"></td>
    <td property="dc:description"></td>
  </tr>
  <tr>
    <td property="rdfs:label">Findable, Accessible, Interoperable, Reusable</td>
    <td property="ncit:C42610">FAIR</td>
    <td property="dc:description">The FAIR principles emphasise machine-actionability (i.e., the capacity of computational systems to find, access, interoperate, and reuse data with none or minimal human intervention) because humans increasingly rely on computational support to deal with data as a result of the increase in volume, complexity, and creation speed of data.<sup><a href="https://www.go-fair.org/fair-principles/">ref</a></sup></td>
  </tr>

  <tr>
    <td property="rdfs:label">Findable</td>
    <td property="ncit:C42610"></td>
    <td property="dc:description">Metadata and data should be easy to find for both humans and computers. Machine-readable metadata are essential for automatic discovery of datasets and services.<sup><a href="https://www.go-fair.org/fair-principles/">ref</a></sup></td>
  </tr>
  <tr>
    <td property="rdfs:label">Accessible</td>
    <td property="ncit:C42610"></td>
    <td property="dc:description">One needs to know how data can be accessed, possibly including authentication and authorisation.<sup><a href="https://www.go-fair.org/fair-principles/">ref</a></sup></td>
  </tr>
  <tr>
    <td property="rdfs:label">Interoperable</td>
    <td property="ncit:C42610"></td>
    <td property="dc:description">To speed up discovery and uncover new insights, research data should be easily combined with other datasets, applications and workflows by humans as well as computer systems.<sup><a href="https://www.go-fair.org/fair-principles/">ref</a></sup></td>
  </tr>
  <tr>
    <td property="rdfs:label">Reusable</td>
    <td property="ncit:C42610"></td>
    <td property="dc:description">Research data should be ready for future research and future processing, making it self-evident that findings can be replicated and that new research effectively builds on already acquired, previous results.<sup><a href="https://www.go-fair.org/fair-principles/">ref</a></sup></td>
  </tr>
  <tr>
    <td property="rdfs:label">Metadata</td>
    <td property="ncit:C42610"></td>
    <td property="dc:description"></td>
  </tr>

  <tr>
    <td property="rdfs:label">Open Data</td>
    <td property="ncit:C42610"></td>
    <td property="dc:description"></td>
  </tr>


  <tr>
    <td property="rdfs:label">Resource Description Framework</td>
    <td property="ncit:C42610">RDF</td>
    <td property="dc:description">A globally-accepted framework for data and knowledge representation that is intended to be read and interpreted by machines.<sup><a href="https://doi.org/10.1038/sdata.2016.18">ref</a></sup></td>
  </tr>

  <tr>
    <td property="rdfs:label">Ontology</td>
    <td property="ncit:C42610"></td>
    <td property="dc:description"></td>
  </tr>

  <tr>
    <td property="rdfs:label">Sysrev</td>
    <td property="ncit:C42610"></td>
    <td property="dc:description">Ortec's literature reviewer support and curation documentationn storage system.</td>
  </tr>

  <tr>
    <td property="rdfs:label"></td>
    <td property="ncit:C42610">DMP</td>
    <td property="dc:description"></td>
  </tr>
  
  <tr>
    <td property="rdfs:label">Model</td>
    <td property="ncit:C42610"></td>
    <td property="dc:description">A simplified (generally mathematical) representation of a real system (e.g. of system: an organism, an organ, a cell…)</td>
  </tr>
  <tr>
    <td property="rdfs:label"></td>
    <td property="ncit:C42610">ADME</td>
    <td property="dc:description">Absorption, distribution, metabolism, and elimination of a substance (toxic or not) in a living organism, following exposure to this substance</td>
  </tr>
  <tr>
    <td property="rdfs:label">Pharmacokinetics</td>
    <td property="ncit:C42610">PK</td>
    <td property="dc:description"></td>
  </tr>
  <tr>
    <td property="rdfs:label">Toxicokinetics</td>
    <td property="ncit:C42610">TK</td>
    <td property="dc:description"></td>
  </tr>
  <tr>
    <td property="rdfs:label">Physiologically based pharmacokinetic model</td>
    <td property="ncit:C42610">PBPK</td>
    <td property="dc:description">Mechanistic representation of ADME processes for a chemical in a living organism, based on physiological and chemical properties</td>
  </tr>
    <tr>
    <td property="rdfs:label">Physiologically based toxicokinetic model</td>
    <td property="ncit:C42610">PBTK</td>
    <td property="dc:description"></td>
  </tr>
    <tr>
    <td property="rdfs:label">Physiologically based biokinetic model</td>
    <td property="ncit:C42610">PBBK</td>
    <td property="dc:description"></td>
  </tr>
    <tr>
    <td property="rdfs:label">Physiologically based kinetic model</td>
    <td property="ncit:C42610">PBK model</td>
    <td property="dc:description"></td>
  </tr>
  <tr>
    <td property="rdfs:label">In-vitro-in-vivo extrapolation</td>
    <td property="ncit:C42610">IVIVE</td>
    <td property="dc:description"></td>
  </tr>
  
  <tr>
    <td property="rdfs:label">Quantitative Structure Activity Relationships</td>
    <td property="ncit:C42610">QSAR</td>
    <td property="dc:description"></td>
  </tr>

</table>


## Project-related terms

<table prefix="rdfs: http://www.w3.org/2000/01/rdf-schema# ncit: http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl# dc: http://purl.org/dc/elements/1.1/">
  <tr> <!-- the header -->
    <td><b>Term</b></td>
    <td><b>Abbreviation</b></td>
    <td><b>Definition</b></td>
  </tr>

  <tr>
    <td property="rdfs:label">Research Line 1</td>
    <td property="ncit:C42610">RL1</td>
    <td property="dc:description">Building the Virtual Human Platform.</td>
  </tr>

  <tr>
    <td property="rdfs:label">Research Line 2</td>
    <td property="ncit:C42610">RL2</td>
    <td property="dc:description">Feeding the Virtual Human Platform.</td>
  </tr>

  <tr>
    <td property="rdfs:label">Research Line 3</td>
    <td property="ncit:C42610">RL3</td>
    <td property="dc:description">Implementing the Virtual Human Platform.</td>
  </tr>

  <tr>
    <td property="rdfs:label">Work Package 1.1</td>
    <td property="ncit:C42610">WP1.1</td>
    <td property="dc:description">Building the ICT infrastructure for the VHP: objectives to develop the technical infrastructure, setting up a predictive platform, developing analysis workflows, making services and data available and interoperable.</td>
  </tr>

  <tr>
    <td property="rdfs:label">Work Package 1.2</td>
    <td property="ncit:C42610">WP1.2</td>
    <td property="dc:description">In silico toxicokinetics: objectives to define parameters required for PBPK modelling, developing PBK models and providing guidance for in vitro to in vivo extrapolations.</td>
  </tr>

  <tr>
    <td property="rdfs:label">Work Package 1.3</td>
    <td property="ncit:C42610">WP1.3</td>
    <td property="dc:description">Computational toxicodynamics: objectives to develop QSAR and MIE prediction models, develop qAOPs, testing the platform and generating safety estimates.</td>
  </tr>

  <tr>
    <td property="rdfs:label">Work Package 2.1</td>
    <td property="ncit:C42610">WP2.1</td>
    <td property="dc:description">In vitro models to provide toxicokinetics & toxicodynamics parameters: objectives to verify in vitro models for ADME and local toxicity, obtaining parameters for PBK modelling, test chemicals on iPSC models.</td>
  </tr>

  <tr>
    <td property="rdfs:label">Work Package 2.2</td>
    <td property="ncit:C42610">WP2.2</td>
    <td property="dc:description">Disease state - Case study chronic kidney disease: objectives to identify critical physiological pathways, develop AOP networks, test toxicity of selected drugs, and assess the safety of selected drugs.</td>
  </tr>

  <tr>
    <td property="rdfs:label">Work Package 2.3</td>
    <td property="ncit:C42610">WP2.3</td>
    <td property="dc:description">Life course exposure - Case study neurodegenerative disease and life course exposure to chemicals: objectives to identify critical physiological pathways, model life time exposure, develop AOP networks, test toxicity and assess the safety of selected chemicals.</td>
  </tr>

  <tr>
    <td property="rdfs:label">Work Package 2.4</td>
    <td property="ncit:C42610">WP2.4</td>
    <td property="dc:description">Age and gender specific safety - Case study Thyroid mediated developmental neurotoxicity: objectives to collect mechanistic physiological data, determine critical pathways, establish quantitative AOP network, identify gender-specific sentitivities and compounds that discriminate, and assess the safety of compound exposure.</td>
  </tr>

  <tr>
    <td property="rdfs:label">Work Package 3.1</td>
    <td property="ncit:C42610">WP3.1</td>
    <td property="dc:description">Technology Assessment of VHP: objectives to perform technology assessment, study and analyse the initiation, development and implementation of VHP, and specify performance criteria.</td>
  </tr>

  <tr>
    <td property="rdfs:label">Work Package 3.2</td>
    <td property="ncit:C42610">WP3.2</td>
    <td property="dc:description">Acceptance of VHP for safety assessment: objectives to position the VHP in the transition to animal-free safety assessment, raise awareness, investigate uncertainties and acceptance of safety assessments.</td>
  </tr>

  <tr>
    <td property="rdfs:label">Work Package 3.3</td>
    <td property="ncit:C42610">WP3.3</td>
    <td property="dc:description">Training and Education: objectives to promote collaboration, facilitate transferability of methods and models, implementing new teaching modules, promote capacity building and awareness of stakeholders, improve skills regarding risk communication.</td>
  </tr>

  <tr>
    <td property="rdfs:label">Work Package 4</td>
    <td property="ncit:C42610">WP4</td>
    <td property="dc:description">Project Coordination, Impact and Data Management: objectives to ensure that project objectives are achieved, deliverables are completed, manage overall knowledge utilisation, and provide effective and sustainable data management.</td>
  </tr>

</table>


### Funding

VHP4Safety – the Virtual Human Platform for safety assessment project
[NWA 1292.19.272](https://www.nwo.nl/projecten/nwa129219272) is part of the NWA
research program ‘Research along Routes by Consortia (ORC)’, which is funded by the Netherlands Organization
for Scientific Research (NWO). The project started on June 1, 2021 with a budget of over 10 million Euros
and will last for the duration of 5 years. 
