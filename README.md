# Output from the Common Language Task Force

This webpage includes the glossary  of the terms that are relevant to the [VHP4Safety](https://vhp4safety.nl/) Project.

The (current **development version** of) the glossary can be found [here](glossary.md). The [OWL version](glossary.owl)
is also available.

## Metadata

This work is licensed under the [CC-BY 4.0 International](https://github.com/VHP4Safety/glossary/blob/main/LICENCE.md). 

## New content?

To make new entry queries, please create an issue [here](https://github.com/VHP4Safety/glossary/issues/new/choose) using the [issue template](https://github.com/VHP4Safety/glossary/blob/main/.github/ISSUE_TEMPLATE/ontology-term-request.md). Experienced GitHub users
are encouraged to submit pull requests.

For other issues, suggestions, or problems, please create an issue [here](https://github.com/VHP4Safety/glossary/issues). 

## Extract OWL triples

The OWL ontology is encoded in the Markdown file as HTML+RDFa. With the `extractOWL.groovy` tool this can
be extracted into a stand-alone OWL files (in Notation3) with:

```shell
groovy extractOWL.groovy > glossary.owl
```

This is done by [a GitHub Action](https://github.com/VHP4Safety/glossary/blob/main/.github/workflows/extract.yml).

### Funding

VHP4Safety – the Virtual Human Platform for safety assessment project
[NWA 1292.19.272](https://www.nwo.nl/projecten/nwa129219272) is part of the NWA
research program ‘Research along Routes by Consortia (ORC)’, which is funded by the Netherlands Organization
for Scientific Research (NWO). The project started on June 1, 2021 with a budget of over 10 million Euros
and will last for the duration of 5 years. 
