# Recent GitHub Activity for Vidit-Ostwal

## 💬 Recent Comments
- [Commented](https://github.com/crewAIInc/crewAI/issues/2095#issuecomment-2650913664) in [crewAIInc/crewAI] on 2025-02-11.
  > *AI Summary: @Vidit-Ostwal suggests adding context to the manager LLM, including information about the agents and tools it can use. However, they express concern that adding a "manager_note" specifically for the manager LLM may not be ideal since it is internally treated as just another agent. They propose an alternative solution, where*
- [Commented](https://github.com/langfuse/langfuse/issues/5432#issuecomment-2648935567) in [langfuse/langfuse] on 2025-02-10.
  > *AI Summary: @Vidit-Ostwal has suggested that he had to change the port of his Docker image. He changed the ClickHouse port from 9000 to 9005, and this change fixed the issue he was facing.*
- [Commented](https://github.com/langfuse/langfuse/issues/5432#issuecomment-2648363009) in [langfuse/langfuse] on 2025-02-10.
  > *AI Summary: @Vidit-Ostwal has suggested that the issue stems from port 9000 being occupied by a security process that cannot be terminated. This prevents the user from running their program on port 9000.*
- [Commented](https://github.com/langfuse/langfuse/issues/5432#issuecomment-2648098489) in [langfuse/langfuse] on 2025-02-10.
  > *AI Summary: @Vidit-Ostwal has suggested providing the attached logs for further investigation into the issue of applying ClickHouse migrations.*
- [Commented](https://github.com/langfuse/langfuse/issues/5432#issuecomment-2648019685) in [langfuse/langfuse] on 2025-02-10.
  > *AI Summary: @Vidit-Ostwal has suggested updating the `docker-compose.yml` configuration to use different ports for ClickHouse (now 9009) and Minio (now 9010). They have confirmed making these changes in their local setup but continue to experience the same issue. They have provided an updated version of their `docker-compose.yml` file for review, suggesting that*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2067#issuecomment-2646579129) in [crewAIInc/crewAI] on 2025-02-09.
  > *AI Summary: @Vidit-Ostwal has suggested a change where a `LLM` class instance can now be passed to run the evaluations. This has been addressed in a pull request.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2046#issuecomment-2646469809) in [crewAIInc/crewAI] on 2025-02-09.
  > *AI Summary: @Vidit-Ostwal has suggested that the problem may be due to `\n` being passed. They recommend replacing it with a comma or using triple `"""` instead of single `""` for the string. They have advised trying out this suggestion to resolve the issue.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2014#issuecomment-2646308001) in [crewAIInc/crewAI] on 2025-02-09.
  > *AI Summary: @Vidit-Ostwal has suggested revisiting the comment as they were initially unable to grasp the intent. However, they resolved the issue by setting the `CREWAI_STORAGE_DIR` environment variable. This resulted in the successful creation of the crew instance and memories within the specified directory, as defined in the `.env` file.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2046#issuecomment-2646302061) in [crewAIInc/crewAI] on 2025-02-09.
  > *AI Summary: @Vidit-Ostwal has suggested that there might be an error in how the argument is being passed to the tool. They have requested to share the complete code to investigate the issue further.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2054#issuecomment-2646300138) in [crewAIInc/crewAI] on 2025-02-09.
  > *AI Summary: @Vidit-Ostwal has suggested that the complete code be shared in the current location to provide context and facilitate easier comprehension for other readers.*

## 🐛 Issues Raised
- Raised an [issue](https://github.com/langfuse/langfuse/issues/5432) in [langfuse/langfuse]: bug: Running Langfuse Locally Dcoker (2025-02-08).
  > *AI Summary: @Vidit-Ostwal has suggested investigating a bug encountered while setting up Langfuse via Docker, where port 9000 is already in use by another process. @Vidit-Ostwal believes that port 9000 is referenced internally elsewhere, beyond the code provided in the comment. They request assistance in identifying all necessary port changes to resolve*
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/2030) in [crewAIInc/crewAI]: Documentation Error in memory docs (2025-02-04).
  > *AI Summary: @Vidit-Ostwal has suggested that in the provided sample code examples, the embedder takes the input of `model` instead of `model_name`. This discrepancy should be corrected across the related documentation pages. The expected behavior is for the `model_name` parameter to be used instead of `model`.*
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/1984) in [crewAIInc/crewAI]: output_log_file should also suppport JSON format. (2025-01-27).
  > *AI Summary: @Vidit-Ostwal has suggested changing the file format of `output_log_file` to JSON. They believe it will enhance parsability and support further analysis. This feature request also partially addresses issue #1970. @Vidit-Ostwal is willing to contribute a pull request to implement this change.*
- Raised an [issue](https://github.com/browser-use/browser-use/issues/407) in [browser-use/browser-use]: Use of use_vision while defining agent (2025-01-26).
  > *AI Summary: @Vidit-Ostwal has suggested reviewing the use of `use_vision set = True` when defining an agent. They inquire about the role of the multimodal LLM in processing screenshots when using this setting. Specifically, they ask if the entire screenshot is still parsed through the LLM or if some elements are scraped*

## 🚀 Pull Requests
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2071) in [crewAIInc/crewAI]: Added functionality to have any llm run test functionality (2025-02-09).
  > *AI Summary: @Vidit-Ostwal has suggested a fix for the issue highlighted in #2067. The suggested fix addresses the reported problem effectively, resolving the issue.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2047) in [crewAIInc/crewAI]: Added reset memories function inside crew class (2025-02-06).
  > *AI Summary: @Vidit-Ostwal has suggested resolving the reset memories issue mentioned in #2023. They also propose removing the CLI command for memory reset and updating the relevant documentation. The suggested solution depends on whether it aligns with the project's goals. @Vidit-Ostwal can implement these changes if the solution receives approval.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2031) in [crewAIInc/crewAI]: Fixed the memory documentation (2025-02-04).
  > *AI Summary: @Vidit-Ostwal has suggested that this commit fixes the documentation issue identified in issue #2030. Unfortunately, the details of the documentation issue or the specific changes made to address it are not provided in this comment.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/1985) in [crewAIInc/crewAI]: Added functionality to have json format as well for the logs (2025-01-27).
  > *AI Summary: @Vidit-Ostwal has suggested adding support to save logs as a JSON file. Users can now set output_log_file to True or provide a file name and enable save_as_json by setting it to True. The generated .json file will contain an array of JSON events, allowing users to easily parse and work*
- Opened a [PR](https://github.com/explodinggradients/ragas/pull/1880) in [explodinggradients/ragas]: Changed the parse_run_traces to include last 4 letters of run_id (2025-01-25).
  > *AI Summary: @Vidit-Ostwal has suggested changing the `parse_run_traces` function to include the last 4 letters of the `run_id` of the trace. This modification creates a unique key for every call, ensuring that each call has a distinct identifier.*

## ⭐ Starred Repositories
- Starred [sentient-engineering/sentient](https://github.com/sentient-engineering/sentient) on 2025-02-08.
- Starred [langflow-ai/langflow](https://github.com/langflow-ai/langflow) on 2025-02-07.
- Starred [langfuse/langfuse](https://github.com/langfuse/langfuse) on 2025-02-04.
- Starred [microsoft/autogen](https://github.com/microsoft/autogen) on 2025-01-31.
- Starred [browser-use/browser-use](https://github.com/browser-use/browser-use) on 2025-01-26.

## 🍴 Forked Repositories
- Forked [crewAIInc/crewAI](https://github.com/Vidit-Ostwal/crewAI) on 2025-01-27.
- Forked [explodinggradients/ragas](https://github.com/Vidit-Ostwal/ragas) on 2025-01-24.
