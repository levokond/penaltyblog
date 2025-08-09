Roadmap
====================

This roadmap outlines planned features, ideas under exploration, and long-term goals for ``penaltyblog``.

It’s not a guarantee, but a guide - contributions, feedback, and suggestions are welcome!

🔜 Planned
-------------------------

MatchFlow
""""""""""""

**Usability + Helper Expansion**

- ☐ General speed optimisations + cythonization to make faster
- ☐ More ``where_`` and ``get_`` helpers
- ☐ ``Flow.describe()`` improvements
- ☐ Docs: Writing custom helpers tutorial
- ☐ Docs: More ``Flow`` recipes
- ☐ Add plugin interface to make it easy to add in other data providers
- ☑ Progress bars
- ☑ Custom query DSL for natural quering - ``flow.query("player.name == 'Kevin de Bruyne'")``
- ☑ Optimization of internal DAG plan

**Joins & I/O Enhancements**

- ☐ Join-on-multiple-fields support
- ☐ Benchmarks page in docs
- ☐ Parallel loading of files

**Rolling & Windowed Aggregates**

- ☑ ``.rolling(...)`` and ``.expanding(...)`` on grouped flows
- ☐ Support for **rolling summary** fields like moving average xG

Plotting
""""""""

- ☑ Publish penaltyblog **plotting** library
- ☑ Native support for **plotting Flow pipelines**

Models
"""""""""

- ☐ Bring the **Bayesian models** back to the party
- ☐ Add new models based on **time-series approaches**
- ☐ Pre-trained models, e.g. **xT**
- ☐ Updated **player ratings** model

Scrapers
"""""""""

- ☐ Give scraper module an overhaul to make it **more efficient and easier to use**
- ☐ Add support for **new data sources** such as Sofa Score
- ☐ Add automatic **throttling** to avoid overloading servers
- ☐ Hook up scrapers to **MatchFlow**
- ☐ Caching of scraped data sources

General
""""""""

- ☐ Refresh / expand rest of documentation

--------

🧪 Under Exploration
---------------------

These are bigger ideas I'm researching - feedback welcome!

MatchFlow
""""""""""

- **FlowZ**: A custom binary format for fast I/O on nested JSON
- **Partitioning** of large datasets for faster processing
- Built-in **indexing or predicate pushdown**
- **Streaming joins** for large datasets
- A lightweight **visual data explorer** (maybe based on my upcoming plotting library)
- Declarative **YAML/JSON** pipeline definitions.
- **Pluggable transforms** (e.g. xT, formation_detection, pressing_zones)

Models
""""""""""

- Custom **Bayesian** library focussed on building sports models without depenency hassles

--------

Contributing
------------

If you're interested in helping with anything here, feel free to open an issue, submit a PR, or just reach out.
