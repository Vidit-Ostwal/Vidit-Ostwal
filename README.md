# Recent GitHub Activity for Vidit-Ostwal

## 💬 Recent Comments
- [Commented](https://github.com/langfuse/langfuse/issues/5432#issuecomment-2648098489) in [langfuse/langfuse] on 2025-02-10.
  > *AI Summary: @Vidit-Ostwal has suggested trying the logs again. Here are the logs for reference: - 1:C 10 Feb 2025 13:51:24.643 * oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo - 1:C 10 Feb 2025 13:51:24.643 * Redis version=7.4.2, bits=64, commit=00000000, modified=0, pid=1, just started - 1:C 10 Feb 2025 13:51:24.643 * Configuration loaded -*
- [Commented](https://github.com/langfuse/langfuse/issues/5432#issuecomment-2648019685) in [langfuse/langfuse] on 2025-02-10.
  > *AI Summary: @Vidit-Ostwal has suggested an update to the `docker-compose.yml` file to resolve an issue where changing ports for ClickHouse and Minio did not resolve the problem. They have updated the ports for ClickHouse migration URL and ClickHouse URL, as well as the ClickHouse external port and MinIO external port. They have*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2067#issuecomment-2646579129) in [crewAIInc/crewAI] on 2025-02-09.
  > *AI Summary: @Vidit-Ostwal has suggested adding a PR to resolve the issue. The PR allows passing an instance of an `LLM` class to run the evals. This change enables the evaluation of different LLM models within the framework.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2046#issuecomment-2646469809) in [crewAIInc/crewAI] on 2025-02-09.
  > *AI Summary: @Vidit-Ostwal has suggested that the issue in the code might be due to using `\n` to separate text. They recommend replacing the `\n` with a comma `,` or using triple double quotes `"""` instead of single double quotes `""` to enclose the text. This should resolve the problem.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2014#issuecomment-2646308001) in [crewAIInc/crewAI] on 2025-02-09.
  > *AI Summary: @Vidit-Ostwal has suggested that @paarttipaabhalaji's original intent is unclear. To resolve this, @Vidit-Ostwal has set the CREWAI_STORAGE_DIR environment variable, directing the crew instance and memory storage to a specified directory as configured in the .env file.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2046#issuecomment-2646302061) in [crewAIInc/crewAI] on 2025-02-09.
  > *AI Summary: @Vidit-Ostwal has suggested that there might be an error with how the argument is being passed to the tool. To assist in troubleshooting, they have requested that the entire code be shared for review.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2054#issuecomment-2646300138) in [crewAIInc/crewAI] on 2025-02-09.
  > *AI Summary: @Vidit-Ostwal has suggested providing the complete code for better context and analysis. This would eliminate the need for users to refer to external sources, ensuring a more cohesive and streamlined discussion. By having all the relevant information readily available, participants can engage in more informed and efficient exchanges.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2065#issuecomment-2646298829) in [crewAIInc/crewAI] on 2025-02-09.
  > *AI Summary: @Vidit-Ostwal has suggested exploring alternative platforms to Serper.dev. They believe that there may be better options available for scraping and parsing search engine results. They encourage users to research and consider other platforms that align with their specific needs and requirements.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2023#issuecomment-2644717512) in [crewAIInc/crewAI] on 2025-02-08.
  > *AI Summary: @Vidit-Ostwal has suggested that the issue reported in this thread should be resolved with the PR that he linked. He has requested the issue creator, @heckfy88, to close the issue if the PR resolves the problem.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2025#issuecomment-2644714108) in [crewAIInc/crewAI] on 2025-02-08.
  > *AI Summary: @Vidit-Ostwal suggests a code modification to yield a particular value during flow execution. If the yielded value is a generator object, its first yielded value is obtained. This modification enables the use of the actual value in subsequent flow steps. Additionally, @Vidit-Ostwal inquires about potential use cases where using yield*

## 🐛 Issues Raised
- Raised an [issue](https://github.com/langfuse/langfuse/issues/5432) in [langfuse/langfuse]: bug: Running Langfuse Locally Dcoker (2025-02-08).
  > *AI Summary: @Vidit-Ostwal has suggested that the bug in setting up LangFuse via Docker Compose is due to port 9000, used by ClickHouse and Minio, being occupied by another process. Changing this port elsewhere in the system is necessary. Despite attempts to modify the port, @Vidit-Ostwal believes there may be additional internal*
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/2030) in [crewAIInc/crewAI]: Documentation Error in memory docs (2025-02-04).
  > *AI Summary: @Vidit-Ostwal has suggested that the CrewAI documentation for memory mentions the embedder taking the input of `model` instead of `model_name`, which is incorrect. The documentation should be corrected to use `model_name` instead of `model`. The issue affects the following documentation pages:

- https://docs.crewai.com/concepts/memory#using-azure-openai-embeddings
- https://docs.crewai.com/concepts/memory#using-google-ai-embeddings
- https://docs.crewai.com/concepts/memory#using-vertex-ai-embeddings
- https://docs.crewai.com/concepts/memory#using-cohere-embeddings*
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/1984) in [crewAIInc/crewAI]: output_log_file should also suppport JSON format. (2025-01-27).
  > *AI Summary: @Vidit-Ostwal has suggested to improve the logging by adding JSON format in the output_log_file. Currently, the file is in .txt format and since it's not parsable, adding JSON will enable further analysis and partially address issue #1970. @Vidit-Ostwal is willing to contribute by submitting a pull request.*
- Raised an [issue](https://github.com/browser-use/browser-use/issues/407) in [browser-use/browser-use]: Use of use_vision while defining agent (2025-01-26).
  > *AI Summary: @Vidit-Ostwal has suggested an exploration of the `use_vision` parameter when defining an agent. They question its functionality in terms of whether it triggers multimodal processing of images. @Vidit-Ostwal has not observed any significant output differences with or without `use_vision = True`, except for the saving of a .gif file. They*

## 🚀 Pull Requests
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2071) in [crewAIInc/crewAI]: Added functionality to have any llm run test functionality (2025-02-09).
  > *AI Summary: @Vidit-Ostwal has suggested a fix for the issue reported in #2067. The details of the fix have not been provided in this comment, and further investigation is required to understand the specific solution implemented.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2047) in [crewAIInc/crewAI]: Added reset memories function inside crew class (2025-02-06).
  > *AI Summary: @Vidit-Ostwal has suggested enhancements to address the reset memories issue raised in #2023. Beyond the fix, they propose removing the CLI command for memory reset and updating documentation. However, implementation of these changes is contingent upon the alignment of the proposed solution with the overall project goals.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2031) in [crewAIInc/crewAI]: Fixed the memory documentation (2025-02-04).
  > *AI Summary: @Vidit-Ostwal has suggested a fix for the documentation issue raised in #2030. The solution addresses the specific problem mentioned in the issue and ensures that the documentation is accurate and up-to-date. By implementing this fix, users will have access to improved documentation, which will enhance their understanding and usage of*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/1985) in [crewAIInc/crewAI]: Added functionality to have json format as well for the logs (2025-01-27).
  > *AI Summary: @Vidit-Ostwal has suggested adding a feature to save logs as a JSON file. Users can now set "output_log_file" to "True" or a desired file name, and set "save_as_json" to "True" while initializing "Crew." This will create a .json file containing an array of JSON events, facilitating easy parsing and manipulation*
- Opened a [PR](https://github.com/explodinggradients/ragas/pull/1880) in [explodinggradients/ragas]: Changed the parse_run_traces to include last 4 letters of run_id (2025-01-25).
  > *AI Summary: @Vidit-Ostwal has suggested modifying the `parse_run_traces` function to incorporate the last four characters of the run ID in each trace. This modification ensures that each call now has a distinct key, thereby eliminating duplicates. The updated function utilizes a combination of the run ID and trace ID to create unique*

## ⭐ Starred Repositories
- Starred [sentient-engineering/sentient](https://github.com/sentient-engineering/sentient) on 2025-02-08.
- Starred [langflow-ai/langflow](https://github.com/langflow-ai/langflow) on 2025-02-07.
- Starred [langfuse/langfuse](https://github.com/langfuse/langfuse) on 2025-02-04.
- Starred [microsoft/autogen](https://github.com/microsoft/autogen) on 2025-01-31.
- Starred [browser-use/browser-use](https://github.com/browser-use/browser-use) on 2025-01-26.

## 🍴 Forked Repositories
- Forked [crewAIInc/crewAI](https://github.com/Vidit-Ostwal/crewAI) on 2025-01-27.
- Forked [explodinggradients/ragas](https://github.com/Vidit-Ostwal/ragas) on 2025-01-24.
