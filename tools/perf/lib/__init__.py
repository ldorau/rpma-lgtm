#!/usr/bin/env python3
#
# SPDX-License-Identifier: BSD-3-Clause
# Copyright 2021, Intel Corporation
#

#
# __init__.py -- required for python imports
#

"""A set of entities dedicated to run benchmarks and process the results

On the input, you have to provide:

- a system configuration (for details about the required and optional parameters
  please see https://github.com/pmem/rpma/blob/master/tools/perf/CONFIG.JSON.md;
  `lib.bench.Bench.config`)
  and
- one or more parts of the report you want to generate. You can think of a part
  as a few pages from a document containing one or more figures and some textual
  content. These things are provided by two means, where:
    - figures are provided as JSON files e.g.:
      https://github.com/pmem/rpma/tree/master/tools/perf/figures
    - the textual content is provided via pair of a JSON and a Markdown files
      both stored in the `templates/` directory:
      https://github.com/pmem/rpma/tree/master/tools/perf/templates.
        - The JSON file provides the contents as key-value pairs.
        - The Markdown file contains a `jinja2` template referencing contents
          from both the JSON file and figures.
- a report configuration file providing some data required to fill up common
  parts of the report (for details please see
  https://github.com/pmem/rpma/blob/master/tools/perf/report.json.example).

On the output, you will get a set of files which compiles results from all
the benchmarks you have ordered:

- each figure from all the parts will be compiled into a single `*.png` file
- data collected for groups of figures will be stored into a common JSON file
  `<name_of_the_group>.json` where each figure's data will occupy a separate
  key.
- all the request parts will be combined into an HTML report file referencing
  all the figure files and combining all the collected data into easily
  consumable form.

**Note**: All three files of a single part shares the same name. The
`report_bench`'s `--figures` argument accepts just part's figures JSON file(s).
The files under the `templates/` directory are matched based on the name e.g.

- `figures/write.json` (part's figures JSON file),
- `templates/part_write.json` and
- `templates/part_write.md`

A single figure (`lib.figure.base.Figure`) consists of one or more series of
data points, where each of them is a single benchmark run
(`lib.benchmark.base.Benchmark`). A series has to describe requirements it
imposes on the benchmarking environment (`lib.Requirement.Requirement`) e.g.

```json
"requirements": {
    "direct_write_to_pmem": false
}
```

**Note**: `templates/part_*.*` files are optional. Especially when you decide to
prepare a custom part's figures file. But in this case you cannot use
`report_create` to generate a report including your custom part. It will end up
with an error. Instead you can directly use `*.png` files generated by
`report_figures`. Anyways, executing a part(s), either predefined or custom,
starts from `report_bench`.
"""
