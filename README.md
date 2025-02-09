# Recent GitHub Activity for Vidit-Ostwal

## 💬 Recent Comments
- [Commented](https://github.com/crewAIInc/crewAI/issues/2014#issuecomment-2646308001) in [crewAIInc/crewAI] on 2025-02-09.
  > *AI Summary: @Vidit-Ostwal has suggested to set the environment variable `CREWAI_STORAGE_DIR` to specify the directory where Crew AI instances and memories will be stored. This ensures that all crew-related data is organized and accessible in the designated directory.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2046#issuecomment-2646302061) in [crewAIInc/crewAI] on 2025-02-09.
  > *AI Summary: @Vidit-Ostwal has suggested that there might be an error in how the argument is being passed to the tool. To troubleshoot this, they have requested to provide the entire code for context.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2054#issuecomment-2646300138) in [crewAIInc/crewAI] on 2025-02-09.
  > *AI Summary: @Vidit-Ostwal has suggested that a complete code for the project should be shared. This will provide a better understanding of the project's functionality and implementation details. By including the complete code, users can explore the project more thoroughly and contribute to its development with a comprehensive understanding of its structure*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2065#issuecomment-2646298829) in [crewAIInc/crewAI] on 2025-02-09.
  > *AI Summary: @Vidit-Ostwal has suggested exploring alternatives to Serper.dev for fetching search engine results. The alternatives can provide additional features, better pricing, or improved accuracy. Examples include Searchlight, SearchAPI, and Serpstack. Before making a decision, it is advisable to thoroughly research and evaluate the capabilities of each alternative.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2023#issuecomment-2644717512) in [crewAIInc/crewAI] on 2025-02-08.
  > *AI Summary: @Vidit-Ostwal has suggested that the issue should be resolved by the provided PR. They recommend closing the issue if the PR successfully addresses the problem.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2025#issuecomment-2644714108) in [crewAIInc/crewAI] on 2025-02-08.
  > *AI Summary: @Vidit-Ostwal suggests that when attempting to yield a particular value in a generator object, the value needs to be iterated over to use it effectively. To illustrate this concept, an example code snippet is provided. This code involves using the langchain_google_genai and crewai libraries to generate a random city and*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2055#issuecomment-2643704539) in [crewAIInc/crewAI] on 2025-02-07.
  > *AI Summary: @Vidit-Ostwal has suggested an update to the crew version to potentially resolve the issue mentioned. The suggestion is based on the assumption that the problem may have been previously resolved, and hence recommends checking out pull request #2055 for further details.*
- [Commented](https://github.com/crewAIInc/crewAI/pull/2047#issuecomment-2643616523) in [crewAIInc/crewAI] on 2025-02-07.
  > *AI Summary: @Vidit-Ostwal suggests exploring the inclusion of built-in evaluations for CrewAI to assess tool outputs, agent performance, and task results based on predefined criteria such as factual accuracy. They draw inspiration from the structured evaluations provided by the RAGAS framework for retrieval-augmented generation and express curiosity about how a similar approach*
- [Commented](https://github.com/crewAIInc/crewAI/pull/2047#issuecomment-2641883649) in [crewAIInc/crewAI] on 2025-02-07.
  > *AI Summary: @Vidit-Ostwal has suggested expanding the summarization to support `get_crew` functionality. This would allow CLI commands to directly link with the current crew instance, which was not previously considered. This addition would enhance the capabilities of the summarization feature.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2023#issuecomment-2640720257) in [crewAIInc/crewAI] on 2025-02-06.
  > *AI Summary: @Vidit-Ostwal has suggested that the issue might be due to discrepancies in how `reset_memory_command` initializes `short_term_memory` and `entity_memory` from the CLI compared to within `crew.py`. While the CLI command works for `long_term_memory` and `knowledge_memory`, which don't need initialization arguments, it may not work for custom initialization of other memory types.*

## 🐛 Issues Raised
- Raised an [issue](https://github.com/langfuse/langfuse/issues/5432) in [langfuse/langfuse]: bug: Running Langfuse Locally Dcoker (2025-02-08).
  > *AI Summary: @Vidit-Ostwal has suggested investigating a bug where the system is unable to set up langfuse via docker docker compose up because the port 9000 used by both clickhouse and minio is already in use by a different system process. Changing the port on the web interface does not fully resolve*
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/2030) in [crewAIInc/crewAI]: Documentation Error in memory docs (2025-02-04).
  > *AI Summary: @Vidit-Ostwal has suggested that the sample code examples in the documentation at [this link](https://docs.crewai.com/concepts/memory) incorrectly use the parameter `model` instead of `model_name` in the embedder input. They recommend replacing `model` with `model_name` in all instances. This would enhance the accuracy and consistency of the code examples.*
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/1984) in [crewAIInc/crewAI]: output_log_file should also suppport JSON format. (2025-01-27).
  > *AI Summary: @Vidit-Ostwal has suggested enhancing the output_log_file logging feature. Currently, the file is in a non-parsable .txt format, but they propose adding a JSON format option to facilitate further analysis. This improvement partially addresses issue #1970. @Vidit-Ostwal expresses willingness to contribute and submit a pull request to implement the JSON format*
- Raised an [issue](https://github.com/browser-use/browser-use/issues/407) in [browser-use/browser-use]: Use of use_vision while defining agent (2025-01-26).
  > *AI Summary: @Vidit-Ostwal has suggested that the purpose of `use_vision set = True` in defining an agent using Gemini 1.5 Pro is unclear. It is not apparent whether the screenshot is sent to the multimodal LLM for parsing or if the entire image is still processed through traditional scraping and decision-making methods.*

## 🚀 Pull Requests
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2047) in [crewAIInc/crewAI]: Added reset memories function inside crew class (2025-02-06).
  > *AI Summary: @Vidit-Ostwal has suggested a fix for the reset memory issue reported in #2023. The solution involves removing the CLI command for resetting memories and making necessary documentation updates. @Vidit-Ostwal is willing to implement these changes if the proposed solution is approved.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2031) in [crewAIInc/crewAI]: Fixed the memory documentation (2025-02-04).
  > *AI Summary: @Vidit-Ostwal has suggested a fix for the documentation issue raised in issue #2030. The suggested fix is now in the documentation and should resolve the problem.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/1985) in [crewAIInc/crewAI]: Added functionality to have json format as well for the logs (2025-01-27).
  > *AI Summary: @Vidit-Ostwal has suggested adding support to save logs as a JSON file. When initializing the crew, users can set `output_log_file` to `True` or provide a file name. They can also enable `save_as_json` by setting it to `True`. This will create a JSON file containing an array of JSON events, facilitating*
- Opened a [PR](https://github.com/explodinggradients/ragas/pull/1880) in [explodinggradients/ragas]: Changed the parse_run_traces to include last 4 letters of run_id (2025-01-25).
  > *AI Summary: @Vidit-Ostwal has suggested a modification to the function parse_run_traces in the issue #1871. The change involves altering the function to incorporate the last four characters of the run_id of the trace, thereby guaranteeing a distinct key for each call. This modification aims to enhance the function's efficacy.*
- Opened a [PR](https://github.com/explodinggradients/ragas/pull/1879) in [explodinggradients/ragas]: Change the validate_samples functionality (2025-01-24).
  > *AI Summary: @Vidit-Ostwal has suggested modifying the validate_samples functionality to pinpoint the specific indexed sample responsible for causing any issues. This enhancement will provide more granular information about any errors, enabling more targeted troubleshooting and resolution.*

## ⭐ Starred Repositories
- Starred [sentient-engineering/sentient](https://github.com/sentient-engineering/sentient) on 2025-02-08.
- Starred [langflow-ai/langflow](https://github.com/langflow-ai/langflow) on 2025-02-07.
- Starred [langfuse/langfuse](https://github.com/langfuse/langfuse) on 2025-02-04.
- Starred [microsoft/autogen](https://github.com/microsoft/autogen) on 2025-01-31.
- Starred [browser-use/browser-use](https://github.com/browser-use/browser-use) on 2025-01-26.

## 🍴 Forked Repositories
- Forked [crewAIInc/crewAI](https://github.com/Vidit-Ostwal/crewAI) on 2025-01-27.
- Forked [explodinggradients/ragas](https://github.com/Vidit-Ostwal/ragas) on 2025-01-24.
