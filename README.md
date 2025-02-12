# Recent GitHub Activity for Vidit-Ostwal

## 💬 Recent Comments
- [Commented](https://github.com/crewAIInc/crewAI/issues/2105#issuecomment-2653744764) in [crewAIInc/crewAI] on 2025-02-12.
  > *AI Summary: @Vidit-Ostwal has suggested that it should be clarified whether the change mentioned in the PR also gets appended to the Python output.*
- [Commented](https://github.com/crewAIInc/crewAI/pull/2071#issuecomment-2653722469) in [crewAIInc/crewAI] on 2025-02-12.
  > *AI Summary: @Vidit-Ostwal has suggested merging the current pull request. No specific reasoning or additional information was provided in the comment.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2097#issuecomment-2651667767) in [crewAIInc/crewAI] on 2025-02-11.
  > *AI Summary: @Vidit-Ostwal has suggested incorporating a crew within a tool, along with parent agents. The tool would be able to initiate a crew and be managed by a parent crew. This would allow for a more hierarchical and organized approach to managing crews and their tasks within the tool.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2095#issuecomment-2651664099) in [crewAIInc/crewAI] on 2025-02-11.
  > *AI Summary: @Vidit-Ostwal has suggested that while using pre-computed or generalized managers might be efficient, it would be better to have manual control over the computation process to ensure accuracy and customization.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2092#issuecomment-2651660502) in [crewAIInc/crewAI] on 2025-02-11.
  > *AI Summary: @Vidit-Ostwal suggests that `human_input` is invoked after the task is done to request feedback on the generated response. They recommend providing all necessary inputs during the `crew.kickoff()` stage. Adding additional input context while the crew is executing may not be ideal.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2095#issuecomment-2650913664) in [crewAIInc/crewAI] on 2025-02-11.
  > *AI Summary: @Vidit-Ostwal has suggested including context regarding agents and tools used by the manager LLM. However, they express concern that adding a "manager_note" specifically for the manager LLM may not be suitable, given that it functions similarly to other agents. Instead, they propose the option of instructing an agent to generate*
- [Commented](https://github.com/langfuse/langfuse/issues/5432#issuecomment-2648935567) in [langfuse/langfuse] on 2025-02-10.
  > *AI Summary: @Vidit-Ostwal has suggested that they were able to resolve the issue by changing the Docker port and ClickHouse port from 9000 to 9005. This modification allowed them to successfully run the application. They have expressed gratitude for the assistance provided by @Steffen911 in resolving this issue.*
- [Commented](https://github.com/langfuse/langfuse/issues/5432#issuecomment-2648363009) in [langfuse/langfuse] on 2025-02-10.
  > *AI Summary: @Vidit-Ostwal has suggested that the issue stems from port 9000 being occupied by a security process that cannot be terminated. This is hindering the ability to run the application on the desired port.*
- [Commented](https://github.com/langfuse/langfuse/issues/5432#issuecomment-2648098489) in [langfuse/langfuse] on 2025-02-10.
  > *AI Summary: @Vidit-Ostwal has suggested that they just tried the Redis setup again, and provided the logs for reference.*
- [Commented](https://github.com/langfuse/langfuse/issues/5432#issuecomment-2648019685) in [langfuse/langfuse] on 2025-02-10.
  > *AI Summary: @Vidit-Ostwal has noticed and updated the `docker-compose.yml` file, changing the ports for both the Clickhouse and Minio services. However, the issue persists. The updated code provided has been analyzed, but no immediate cause for the problem could be identified. It is recommended to review other internal files to determine if*

## 🐛 Issues Raised
- Raised an [issue](https://github.com/BerriAI/litellm/issues/8467) in [BerriAI/litellm]: [Bug]: Support to Google AI Studio (2025-02-11).
  > *AI Summary: @Vidit-Ostwal has suggested checking the `GenerateContentRequest.contents` as the error message indicates that it is not specified. They have also mentioned that they are not on the ML Ops Team and are using LiteLLM version 1.60.2.*
- Raised an [issue](https://github.com/langfuse/langfuse/issues/5432) in [langfuse/langfuse]: bug: Running Langfuse Locally Dcoker (2025-02-08).
  > *AI Summary: @Vidit-Ostwal has suggested that there is an issue when trying to set up langfuse via Docker due to port 9000 being used by another system process. They have tried to change the port, but believe it is also being used internally. They have provided a log error message and are*
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/2030) in [crewAIInc/crewAI]: Documentation Error in memory docs (2025-02-04).
  > *AI Summary: @Vidit-Ostwal has suggested that in the CrewAI documentation for memory concepts, the sample code examples use `model` as the input parameter for the embedder instead of `model_name`. This is incorrect, and the parameter should be `model_name`. The issue affects several examples in the documentation, including those for Azure OpenAI Embeddings,*
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/1984) in [crewAIInc/crewAI]: output_log_file should also suppport JSON format. (2025-01-27).
  > *AI Summary: @Vidit-Ostwal has suggested a feature to enhance the output_log_file by adding support for JSON formatting. This will make the log file more parsable and suitable for further analysis. It partially addresses issue #1970. @Vidit-Ostwal has expressed willingness to contribute by submitting a pull request.*
- Raised an [issue](https://github.com/browser-use/browser-use/issues/407) in [browser-use/browser-use]: Use of use_vision while defining agent (2025-01-26).
  > *AI Summary: @Vidit-Ostwal has suggested that the `use_vision set = True` option in agent definition should be clarified. It is unclear whether this option directs screenshots to the multimodal LLM for parsing or if the system still relies on web scraping and element analysis. They have also observed that the primary visible*

## 🚀 Pull Requests
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2071) in [crewAIInc/crewAI]: Added functionality to have any llm run test functionality (2025-02-09).
  > *AI Summary: @Vidit-Ostwal has suggested a fix for an issue mentioned in #2067.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2047) in [crewAIInc/crewAI]: Added reset memories function inside crew class (2025-02-06).
  > *AI Summary: @Vidit-Ostwal has suggested several changes to address the reset memories issue raised in #2023:

- Removal of the CLI command for resetting memories
- Updates to documentation

@Vidit-Ostwal has expressed a willingness to implement these changes upon confirmation that they align with the project's solution.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2031) in [crewAIInc/crewAI]: Fixed the memory documentation (2025-02-04).
  > *AI Summary: @Vidit-Ostwal has suggested that this commit resolves the documentation issue that was reported in issue #2030. The exact details of the resolution are not provided in this commit message.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/1985) in [crewAIInc/crewAI]: Added functionality to have json format as well for the logs (2025-01-27).
  > *AI Summary: @Vidit-Ostwal has suggested adding support to save logs as a JSON file. This can be enabled by setting the output_log_file parameter to True or providing a file name and setting save_as_json to True. The generated JSON file will contain an array of JSON events, simplifying parsing and further analysis.*
- Opened a [PR](https://github.com/explodinggradients/ragas/pull/1880) in [explodinggradients/ragas]: Changed the parse_run_traces to include last 4 letters of run_id (2025-01-25).
  > *AI Summary: @Vidit-Ostwal has suggested modifying the `parse_run_traces` function to include the last four letters of the `run_id` of the trace, creating a unique key for each call.*

## ⭐ Starred Repositories
- Starred [sentient-engineering/sentient](https://github.com/sentient-engineering/sentient) on 2025-02-08.
- Starred [langflow-ai/langflow](https://github.com/langflow-ai/langflow) on 2025-02-07.
- Starred [langfuse/langfuse](https://github.com/langfuse/langfuse) on 2025-02-04.
- Starred [microsoft/autogen](https://github.com/microsoft/autogen) on 2025-01-31.
- Starred [browser-use/browser-use](https://github.com/browser-use/browser-use) on 2025-01-26.

## 🍴 Forked Repositories
- Forked [crewAIInc/crewAI](https://github.com/Vidit-Ostwal/crewAI) on 2025-01-27.
- Forked [explodinggradients/ragas](https://github.com/Vidit-Ostwal/ragas) on 2025-01-24.
