# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['fal',
 'fal.feature_store',
 'faldbt',
 'faldbt.cp',
 'faldbt.cp.contracts',
 'faldbt.cp.contracts.graph',
 'faldbt.cp.parser',
 'faldbt.cp.task',
 'faldbt.utils']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=6.0,<7.0',
 'agate-sql>=0.5.8,<0.6.0',
 'arrow>=1.2.0,<2.0.0',
 'firebase-admin>=5.1.0,<6.0.0',
 'google-cloud-bigquery-storage>=2.9.1,<3.0.0',
 'google-cloud-bigquery>=2.28.1,<3.0.0',
 'pandas>=1.3.4,<2.0.0',
 'pyarrow>=5.0.0,<6.0.0',
 'pydantic>=1.8.2,<2.0.0',
 'sqlalchemy-bigquery>=1.2.2,<2.0.0']

entry_points = \
{'console_scripts': ['fal = fal.cli:cli']}

setup_kwargs = {
    'name': 'fal',
    'version': '0.2.0',
    'description': 'fal allows you to run python scripts directly from your dbt project.',
    'long_description': '# fal: do more with dbt\nfal allows you to run python scripts directly from your [dbt](https://www.getdbt.com/) project.\n\n[February Roadmap](https://www.notion.so/featuresandlabels/February-Roadmap-e6521e39514a4ed598745aa71167de6b)\n\n<p align="center">\n  <a href="https://pepy.tech/project/fal">\n    <img src="https://static.pepy.tech/personalized-badge/fal?period=total&units=international_system&left_color=grey&right_color=blue&left_text=Downloads" alt="Total downloads" />\n  </a>&nbsp;\n  <a href="https://pypi.org/project/fal/">\n    <img src="https://badge.fury.io/py/fal.svg" alt="Angular on npm" />\n  </a>&nbsp;\n  <a href="https://discord.com/invite/Fyc9PwrccF">\n    <img src="https://badgen.net/badge/icon/Join%20Us%20On%20Discord/red?icon=discord&label" alt="Discord conversation" />\n  </a>\n</p>\n\nWith fal, you can:\n- Send Slack notifications upon dbt model success or failure.\n- Download dbt models into a Python context with a familiar syntax: `ref(\'my_dbt_model\')`\n- Use python libraries such as [`sklearn`](https://scikit-learn.org/) or [`prophet`](https://facebook.github.io/prophet/) to build more complex pipelines downstream of `dbt` models.\n\nand more...\n\nCheck out our [Getting Started](#getting-started) guide to get a quickstart, head to our [documentation site](https://docs.fal.ai/) for a deeper dive or play with [in-depth examples](#examples) to see how fal can help you get more done with dbt.\n\n[<img src="https://cdn.loom.com/sessions/thumbnails/bb49fffaa6f74e90b91d26c77f35ecdc-1637262660876-with-play.gif">](https://www.loom.com/share/bb49fffaa6f74e90b91d26c77f35ecdc)\n\n\n# Getting Started\n\n## 1. Install fal\n```bash\n$ pip install fal\n```\n\n## 2. Go to your dbt directory\n```bash\n$ cd ~/src/my_dbt_project\n```\n\n## 3. Create a python script: `send_slack_message.py`\n```python\nimport os\nfrom slack_sdk import WebClient\nfrom slack_sdk.errors import SlackApiError\n\nCHANNEL_ID = os.getenv("SLACK_BOT_CHANNEL")\nSLACK_TOKEN = os.getenv("SLACK_BOT_TOKEN")\n\nclient = WebClient(token=SLACK_TOKEN)\nmessage_text = f"Model: {context.current_model.name}. Status: {context.current_model.status}."\n\ntry:\n    response = client.chat_postMessage(\n        channel=CHANNEL_ID,\n        text=message_text\n    )\nexcept SlackApiError as e:\n    assert e.response["error"]\n```\n\n## 4. Add a `meta` section in your `schema.yml`\n```yaml\nmodels:\n  - name: historical_ozone_levels\n    description: Ozone levels\n    config:\n      materialized: table\n    columns:\n      - name: ozone_level\n        description: Ozone level\n      - name: ds\n        description: Date\n    meta:\n      fal:\n        scripts:\n          - send_slack_message.py\n```\n\n## 5. Run `dbt` and `fal` consecutively\n```bash\n$ dbt run\n# Your dbt models are ran\n\n$ fal run\n# Your python scripts are ran\n```\n\n# Examples\nTo explore what is possible with fal, take a look at the in-depth examples below. We will be adding more examples here over time:\n- [Example 1: Send Slack notifications](examples/slack-example.md)\n- [Example 2: Metric forecasting](examples/metric-forecast.md)\n- [Example 3: Sentiment analysis on support tickets](examples/sentiment-analysis.md)\n- [Example 4: Send event to Datadog](examples/datadog_event.md)\n- [Example 5: Incorporate fal in CI/CD workflow](examples/ci_example.md)\n- [Example 6: Send data to Firestore](examples/write_to_firestore.md)\n- [Example 7: Write dbt artifacts to GCS](examples/write_to_gcs.md)\n- [Example 8: Write dbt artifacts to AWS S3](examples/write_to_aws.md)\n- [Example 9: Use dbt from a Jupyter Notebook](examples/write_jupyter_notebook.md)\n- [Example 10: Read and parse dbt metadata](examples/read_dbt_metadata.md)\n- [Example 11: Anomaly Detection](examples/anomaly-detection.md)\n\n# How it works?\n`fal` is a command line tool that can read the state of your `dbt` project and help you run Python scripts after your `dbt run`s by leveraging the [`meta` config](https://docs.getdbt.com/reference/resource-configs/meta).\n\n```yaml\nmodels:\n  - name: historical_ozone_levels\n    ...\n    meta:\n      fal:\n        scripts:\n          - send_slack_message.py\n          - another_python_script.py # will be ran after the first script\n```\n\n## Model scripts selection\n\nBy default, the `fal run` command runs the Python scripts as a post-hook, **only** on the models that were ran on the last `dbt run`; that means that if you are using model selectors, `fal` will only run on the models `dbt` ran. To achieve this, fal needs the dbt-generated file `run_results.json` available.\n\nIf you are running `fal` in a clean environment (no `run_results.json` available) or just want to specify which models you want to run the scripts for, `fal` handles [dbt\'s selection flags](https://docs.getdbt.com/reference/node-selection/syntax) for `dbt run` as well as offering an extra flag for just running _all_ models:\n\n```\n--all                    Run scripts for all models.\n-s, --select TEXT        Specify the nodes to include.\n-m, --models TEXT        Specify the nodes to include. (Deprecated)\n--exclude TEXT           Specify the models to exclude.\n--selector TEXT          The selector name to use, as defined in selectors.yml\n```\n\nFor passing more than one selection or exlusion, you must specify the flag multiple times:\n\n```bash\n$ fal run -s model_alpha -s model_beta\n... | Starting fal run for following models and scripts:\nmodel_alpha: script.py\nmodel_beta: script.py, other.py\n```\n\n`fal` also provides useful helpers within the Python context to seamlessly interact with dbt models: `ref("my_dbt_model_name")` will pull a dbt model into your Python script as a [`pandas.DataFrame`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html).\n\n# Concepts\n## profile.yml and Credentials\n`fal` integrates with `dbt`\'s `profile.yml` file to access and read data from the data warehouse. Once you setup credentials in your `profile.yml` file for your existing `dbt` workflows anytime you use `ref` or `source` to create a dataframe `fal` authenticates using the credentials specified in the `profile.yml` file.\n\n## `meta` Syntax\n```yaml\nmodels:\n  - name: historical_ozone_levels\n    ...\n    meta:\n      owner: "@me"\n      fal:\n        scripts:\n          - send_slack_message.py\n          - another_python_script.py # will be run sequentially\n```\nUse the `fal` and `scripts` keys underneath the `meta` config to let `fal` CLI know where to look for the Python scripts. You can pass a list of scripts as shown above to run one or more scripts as a post-hook operation after a `dbt run`.\n\n## Variables and functions\nInside a Python script, you get access to some useful variables and functions\n\n### Variables\n\nA `context` object with information relevant to the model through which the script was run. For the [`meta` Syntax](#meta-syntax) example, we would get the following:\n```python\ncontext.current_model.name\n#= historical_ozone_levels\n\ncontext.current_model.meta\n#= {\'owner\': \'@me\'}\n\ncontext.current_model.meta.get("owner")\n#= \'@me\'\n\ncontext.current_model.status\n# Could be one of\n#= \'success\'\n#= \'error\'\n#= \'skipped\'\n```\n\n`context` object also has access to test information related to the current model. If the previous dbt command was either `test` or `build`, the `context.current_model.test` property is populated with a list of tests:\n```python\ncontext.current_model.tests\n#= [CurrentTest(name=\'not_null\', modelname=\'historical_ozone_levels, column=\'ds\', status=\'Pass\')]\n```\n\n### `ref` and `source` functions\nThere are also available some familiar functions from `dbt`\n```python\n# Refer to dbt models or sources by name and returns it as `pandas.DataFrame`\nref(\'model_name\')\nsource(\'source_name\', \'table_name\')\n\n# You can use it to get the running model data\nref(context.current_model.name)\n```\n\n### `write_to_source` function\nIt is also possible to send data back to your datawarehouse. This makes it easy to get the data, process it and upload it back into dbt territory.\n\nAll you have to do is define the target source in your schema and use it in fal. \nThis operation appends to the existing source by default and should only be used targetting tables, not views.\n```python\n# Upload a `pandas.DataFrame` back to the datawarehouse\nwrite_to_source(df, \'source_name\', \'table_name2\')\n```\n\n## Lifecycle and State Management\nBy default, the `fal run` command runs the Python scripts as a post-hook, **only** on the models that were ran on the last `dbt run` (So if you are using model selectors, `fal` will only run on the selected models).\n\nIf you want to run all Python scripts regardless, you can do so by using the `--all` flag with the `fal` CLI:\n\n```bash\n$ fal run --all\n```\n\n## Importing `fal` as a Python package\nYou may be interested in accessing dbt models and sources easily from a Jupyter Notebook or another Python script.\nFor that, just import the `fal` package and intantiate a FalDbt project:\n\n```py\nfrom fal import FalDbt\nfaldbt = FalDbt(profiles_dir="~/.dbt", project_dir="../my_project")\n\nfaldbt.list_sources()\n# [[\'results\', \'ticket_data_sentiment_analysis\']]\n\nfaldbt.list_models()\n# {\n#   \'zendesk_ticket_metrics\': <RunStatus.Success: \'success\'>,\n#   \'stg_o3values\': <RunStatus.Success: \'success\'>,\n#   \'stg_zendesk_ticket_data\': <RunStatus.Success: \'success\'>,\n#   \'stg_counties\': <RunStatus.Success: \'success\'>\n# }\n\nsentiments = faldbt.source(\'results\', \'ticket_data_sentiment_analysis\')\n# pandas.DataFrame\ntickets = faldbt.ref(\'stg_zendesk_ticket_data\')\n# pandas.DataFrame\n```\n\n# Supported `dbt` versions\n\nAny extra configuration to work with different `dbt` versions is not needed, latest `fal` version currently supports:\n\n- 0.20.*\n- 0.21.*\n- 1.0.*\n\nIf you need another version, [open an issue](https://github.com/fal-ai/fal/issues/new) and we will take a look!\n\n# Contributing / Development\n\nWe use Poetry for dependency management and easy development testing.\n\nUse Poetry shell to trying your changes right away:\n\n```sh\n~ $ cd fal\n\n~/fal $ poetry install\n\n~/fal $ poetry shell\nSpawning shell within [...]/fal-eFX98vrn-py3.8\n\n~/fal fal-eFX98vrn-py3.8 $ cd ../dbt_project\n\n~/dbt_project fal-eFX98vrn-py3.8 $ fal run\n19:27:30  Found 5 models, 0 tests, 0 snapshots, 0 analyses, 165 macros, 0 operations, 0 seed files, 1 source, 0 exposures, 0 metrics\n19:27:30 | Starting fal run for following models and scripts:\n[...]\n```\n\n## Running tests\n\nTests rely on a Postgres database to be present, this can be achieved with docker-compose:\n\n```sh\n~/fal $ docker-compose -f tests/docker-compose.yml up -d\nCreating network "tests_default" with the default driver\nCreating fal_db ... done\n\n# Necessary for the import test\n~/fal $ dbt run --profiles-dir tests/mock/mockProfile --project-dir tests/mock\nRunning with dbt=1.0.1\n[...]\nCompleted successfully\nDone. PASS=5 WARN=0 ERROR=0 SKIP=0 TOTAL=5\n\n~/fal $ pytest -s\n```\n\n# Why are we building this?\nWe think `dbt` is great because it empowers data people to get more done with the tools that they are already familiar with.\n\n`dbt`\'s SQL only design is powerful, but if you ever want to get out of SQL-land and connect to external services or get into Python-land for any reason, you will have a hard time. We built `fal` to enable Python workloads (sending alerts to Slack, building predictive models, pushing data to non-data warehose destinations and more) **right within `dbt`**.\n\nThis library will form the basis of our attempt to more comprehensively enable **data science workloads** downstream of dbt. And because having reliable data pipelines is the most important ingredient in building predictive analytics, we are building a library that integrates well with dbt.\n\n\n# Have feedback or need help?\n[Join us in #fal on Discord](https://discord.com/invite/Fyc9PwrccF)\n',
    'author': 'Meder Kamalov',
    'author_email': 'meder@fal.ai',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/fal-ai/fal',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7.1,<3.10',
}


setup(**setup_kwargs)
