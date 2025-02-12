# Recent GitHub Activity for Vidit-Ostwal

## 💬 Recent Comments
- [Commented](https://github.com/crewAIInc/crewAI/issues/2095#issuecomment-2650913664) in [crewAIInc/crewAI] on 2025-02-11.
  > *AI Summary: @Vidit-Ostwal suggests that while including context about agents and tools used by the manager LLM is beneficial, creating a unique `manager_note` specifically for the manager LLM may not be ideal since it's essentially an agent itself. Instead, @Vidit-Ostwal proposes allowing agents to generate descriptions, goals, and context for the manager*
- [Commented](https://github.com/langfuse/langfuse/issues/5432#issuecomment-2648935567) in [langfuse/langfuse] on 2025-02-10.
  > *AI Summary: @Vidit-Ostwal has suggested that changing the docker port resolved the issue. The issue was related to the clickhouse port being set to 9000 instead of 9005. After modifying the clickhouse port to 9005, the issue was resolved.*
- [Commented](https://github.com/langfuse/langfuse/issues/5432#issuecomment-2648363009) in [langfuse/langfuse] on 2025-02-10.
  > *AI Summary: @Vidit-Ostwal has suggested that there is an issue with setting up the program on port 9000 due to a security process running on the same port. The process cannot be terminated, hence preventing the program from running on port 9000.*
- [Commented](https://github.com/langfuse/langfuse/issues/5432#issuecomment-2648098489) in [langfuse/langfuse] on 2025-02-10.
  > *AI Summary: @Vidit-Ostwal has suggested that I provide the logs for reference. Here are the logs: - Redis is starting and is running in standalone mode on port 6379. - PostgreSQL is listening on IPv4 and IPv6 addresses on port 5432 and is ready to accept connections. - ClickHouse is running and*
- [Commented](https://github.com/langfuse/langfuse/issues/5432#issuecomment-2648019685) in [langfuse/langfuse] on 2025-02-10.
  > *AI Summary: @Vidit-Ostwal has suggested updating the `docker-compose.yml` file. The ports for `clickhouse` and `minio` have been changed to `9009` and `9010` respectively. Additionally, the `CLICKHOUSE_MIGRATION_URL` and `LANGFUSE_S3_EVENT_UPLOAD_ENDPOINT` environment variables have been updated to reflect these port changes. The user has also mentioned that they are still facing the same issue and*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2067#issuecomment-2646579129) in [crewAIInc/crewAI] on 2025-02-09.
  > *AI Summary: @Vidit-Ostwal has suggested adding a PR to resolve an issue. With this PR, users can now pass an instance of a `LLM` class to run the evaluations.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2046#issuecomment-2646469809) in [crewAIInc/crewAI] on 2025-02-09.
  > *AI Summary: @Vidit-Ostwal has suggested considering that the problem may be due to the use of `\n`. They recommend replacing it with a `,` or using triple `""` instead of single `""` for the values in the string. They believe this should resolve the issue.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2014#issuecomment-2646308001) in [crewAIInc/crewAI] on 2025-02-09.
  > *AI Summary: @Vidit-Ostwal has suggested a fix to the issue. They were unable to understand the initial intention, but they set the `CREWAI_STORAGE_DIR` environment variable and configured the crew instance and memories to be stored in the directory specified in the `.env` file. This setup worked for them, and they believe it*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2046#issuecomment-2646302061) in [crewAIInc/crewAI] on 2025-02-09.
  > *AI Summary: @Vidit-Ostwal has suggested that there might be an error in the way arguments are being passed to the tool. To troubleshoot, they have requested the entire code to be shared.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2054#issuecomment-2646300138) in [crewAIInc/crewAI] on 2025-02-09.
  > *AI Summary: @Vidit-Ostwal has suggested sharing the complete code for better understanding and clarity. They have requested the code to be included in the discussion for easy reference and comprehensive analysis.*

## 🐛 Issues Raised
- Raised an [issue](https://github.com/langfuse/langfuse/issues/5432) in [langfuse/langfuse]: bug: Running Langfuse Locally Dcoker (2025-02-08).
  > *AI Summary: @Vidit-Ostwal has suggested investigating the port issue encountered during LangFuse setup via Docker Compose. Port 9000, used by ClickHouse and MinIO, is already in use, preventing successful setup. They suspect that the port is used internally elsewhere, leading to the error "failed to open database." @Vidit-Ostwal has expressed interest in*
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/2030) in [crewAIInc/crewAI]: Documentation Error in memory docs (2025-02-04).
  > *AI Summary: @Vidit-Ostwal has suggested that the sample code examples in the documentation for the following links:

- https://docs.crewai.com/concepts/memory#using-azure-openai-embeddings
- https://docs.crewai.com/concepts/memory#using-google-ai-embeddings
- https://docs.crewai.com/concepts/memory#using-vertex-ai-embeddings
- https://docs.crewai.com/concepts/memory#using-cohere-embeddings

need to be updated to replace the `model` parameter with `model_name` in the `embedder` function to match the expected behavior.*
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/1984) in [crewAIInc/crewAI]: output_log_file should also suppport JSON format. (2025-01-27).
  > *AI Summary: @Vidit-Ostwal has suggested a new feature that would add JSON format support to the output_log_file. Currently, the log file is in .txt format, which is not easily parsable. JSON format would enable further analysis and partially address issue #1970. @Vidit-Ostwal is willing to contribute a pull request to implement this*
- Raised an [issue](https://github.com/browser-use/browser-use/issues/407) in [browser-use/browser-use]: Use of use_vision while defining agent (2025-01-26).
  > *AI Summary: @Vidit-Ostwal has suggested reviewing the usage of `use_vision = True` when defining an agent. They inquire about the purpose of this flag and whether it enables multimodal processing of images by the LLM or if it still relies on scraping elements and decision-making based on that. The commenter also expresses*

## 🚀 Pull Requests
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2071) in [crewAIInc/crewAI]: Added functionality to have any llm run test functionality (2025-02-09).
  > *AI Summary: @Vidit-Ostwal has suggested a fix for the issue mentioned in #2067.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2047) in [crewAIInc/crewAI]: Added reset memories function inside crew class (2025-02-06).
  > *AI Summary: @Vidit-Ostwal has suggested resolving an issue (#2023) regarding memory reset. The fix involves the following:

- Removing the CLI command for memory reset
- Updating documentation 

They are willing to implement these changes if the proposed solution aligns with the team's approach.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2031) in [crewAIInc/crewAI]: Fixed the memory documentation (2025-02-04).
  > *AI Summary: @Vidit-Ostwal has suggested a fix for the documentation issue raised in #2030. The documentation has been updated to resolve the reported issue, ensuring that the documentation is accurate and comprehensive for users.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/1985) in [crewAIInc/crewAI]: Added functionality to have json format as well for the logs (2025-01-27).
  > *AI Summary: @Vidit-Ostwal has suggested adding support to save logs as a JSON file. When initializing the Crew class, users can specify output_log_file as True or a file name, and set save_as_json to True. The resulting JSON file contains an array of JSON events, simplifying parsing and manipulation.*
- Opened a [PR](https://github.com/explodinggradients/ragas/pull/1880) in [explodinggradients/ragas]: Changed the parse_run_traces to include last 4 letters of run_id (2025-01-25).
  > *AI Summary: @Vidit-Ostwal has suggested changing the parse_run_traces function to include the last 4 letters of the run_id of the trace. This modification ensures that each call has a unique key, making it easier to identify and track individual calls.*

## ⭐ Starred Repositories
- Starred [sentient-engineering/sentient](https://github.com/sentient-engineering/sentient) on 2025-02-08.
- Starred [langflow-ai/langflow](https://github.com/langflow-ai/langflow) on 2025-02-07.
- Starred [langfuse/langfuse](https://github.com/langfuse/langfuse) on 2025-02-04.
- Starred [microsoft/autogen](https://github.com/microsoft/autogen) on 2025-01-31.
- Starred [browser-use/browser-use](https://github.com/browser-use/browser-use) on 2025-01-26.

## 🍴 Forked Repositories
- Forked [crewAIInc/crewAI](https://github.com/Vidit-Ostwal/crewAI) on 2025-01-27.
- Forked [explodinggradients/ragas](https://github.com/Vidit-Ostwal/ragas) on 2025-01-24.
