# Output from the Common Language Task Force

This webpage includes the glossary  of the terms that are relevant to the [VHP4Safety](https://vhp4safety.nl/) Project.

The (current **development version** of) the glossary can be found [here](index.md). The [OWL version](glossary.owl)
is also available.

## Metadata

This work is licensed under the [CC-BY 4.0 International](https://github.com/VHP4Safety/glossary/blob/main/LICENCE.md). 

## New content?

To make new entry queries, please create an issue [here](https://github.com/VHP4Safety/glossary/issues/new/choose) using the [issue template]([https://github.com/VHP4Safety/glossary/blob/main/.github/ISSUE_TEMPLATE/ontology-term-request.md](https://github.com/VHP4Safety/glossary/issues/new?assignees=&labels=categorization&projects=&template=ontology-term-request.yml&title=%5BTERM+REQUEST%5D+Please+add+this+glossary+term)). Experienced GitHub users
are encouraged to submit pull requests.

For other issues, suggestions, or problems, please create an issue [here](https://github.com/VHP4Safety/glossary/issues). 

## Data format

The Glossary is mainly presented under https://glossary.vhp4safety.nl/ in the HTML rendering of a [Markdown](https://en.wikipedia.org/wiki/Markdown) file with
[HTML](https://en.wikipedia.org/wiki/HTML) bits and [RDFa](https://rdfa.info/docs) annotation.

New terms are added under the adequate template in [/templates](/templates), and the Markdown gets updated automatically via a GitHub action.

The Glossary terms are listed in a set of HTML tables, where each row describes a single term.
Here, we take advantage of the HTML+RDFa standard, and embed the OWL data. Because OWL is
just RDF, we effectively specify RDF triples:

```html
<tr about="https://vhp4safety.github.io/glossary#VHP0000086" typeof="owl:Class">
  <td property="rdfs:label">Task Force</td>
  <td property="ncit:C42610">TF</td>
  <td property="dc:description">Cross work package effort to reach some goal.</td>
</tr>
```

RDFa uses the HTML attribute `about` to specify of the *subject* and the `property`
attribute to specify the *predicate*. The `object` can be specified in different ways,
and the above example shows how the `Literal` is given.

## Extract OWL triples

With the `extractOWL.groovy` tool this can
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
