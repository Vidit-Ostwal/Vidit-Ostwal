# Recent GitHub Activity for Vidit-Ostwal

## 💬 Recent Comments
- [Commented](https://github.com/crewAIInc/crewAI/issues/2105#issuecomment-2653744764) in [crewAIInc/crewAI] on 2025-02-12.
  > *AI Summary: @Vidit-Ostwal has suggested that the commenter verify if the specified observation also gets appended to the Python output. No further information was provided.*
- [Commented](https://github.com/crewAIInc/crewAI/pull/2071#issuecomment-2653722469) in [crewAIInc/crewAI] on 2025-02-12.
  > *AI Summary: @Vidit-Ostwal has suggested to merge the pull request.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2097#issuecomment-2651667767) in [crewAIInc/crewAI] on 2025-02-11.
  > *AI Summary: @Vidit-Ostwal has suggested incorporating a crew within a tool and adding parent agents. The tool should have the ability to initiate a crew, which would then be managed by a parent crew. This approach would allow for more flexibility and control in managing crews and tools.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2095#issuecomment-2651664099) in [crewAIInc/crewAI] on 2025-02-11.
  > *AI Summary: @Vidit-Ostwal suggests that while pre-computed or generalized managers may be options, it's preferable to maintain direct control over the management process. This allows for greater customization and flexibility in managing the system.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2092#issuecomment-2651660502) in [crewAIInc/crewAI] on 2025-02-11.
  > *AI Summary: @Vidit-Ostwal suggested clarifying the usage of `human_input`. The function is called after task execution to gather feedback on the generated response. Adding additional context during crew execution is not recommended. Instead, all necessary input should be provided during `crew.kickoff()`. This approach ensures a more streamlined and efficient workflow.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2095#issuecomment-2650913664) in [crewAIInc/crewAI] on 2025-02-11.
  > *AI Summary: @Vidit-Ostwal has suggested that it's a good idea to provide context and information about the agents and tools that the manager LLM can utilize. However, they have raised a concern that internally, the manager LLM is essentially an agent itself, so adding a "manager_note" specifically for this agent may not*
- [Commented](https://github.com/langfuse/langfuse/issues/5432#issuecomment-2648935567) in [langfuse/langfuse] on 2025-02-10.
  > *AI Summary: @Vidit-Ostwal has suggested that changing the Docker port resolved the issue. The ClickHouse port was modified from 9000 to 9005, resulting in a successful resolution of the problem.*
- [Commented](https://github.com/langfuse/langfuse/issues/5432#issuecomment-2648363009) in [langfuse/langfuse] on 2025-02-10.
  > *AI Summary: @Vidit-Ostwal has suggested that the issue may stem from a security process running on port 9000. This process is preventing the desired application from starting on that port. Due to its nature, it cannot be terminated.*
- [Commented](https://github.com/langfuse/langfuse/issues/5432#issuecomment-2648098489) in [langfuse/langfuse] on 2025-02-10.
  > *AI Summary: @Vidit-Ostwal has suggested that the user just tried again, providing logs for reference. The provided logs contain a mix of log entries from various microservices and databases, including Redis, PostgreSQL, ClickHouse, MinIO, and Langfuse components. These logs generally indicate that the services started successfully, but there were issues with applying*
- [Commented](https://github.com/langfuse/langfuse/issues/5432#issuecomment-2648019685) in [langfuse/langfuse] on 2025-02-10.
  > *AI Summary: @Vidit-Ostwal has suggested updating the ports for Clickhouse and Minio in the `docker-compose.yml` configuration to resolve the issue being faced. Specifically, the Clickhouse external port is updated to 9009, and the Minio external port is updated to 9010. They believe that this change may address the problem, but further investigation*

## 🐛 Issues Raised
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/2111) in [crewAIInc/crewAI]: [BUG] LiteLLM call fails, when `human_input` set to True (2025-02-12).
  > *AI Summary: @Vidit-Ostwal has suggested adding feedback in the user role to resolve the issue where the code fails to run with `human_input` set to True due to the lite LLM not being given the user role in the messages. The attached screenshot showcases the error, and @Vidit-Ostwal has provided a Python*
- Raised an [issue](https://github.com/BerriAI/litellm/issues/8467) in [BerriAI/litellm]: [Bug]: Support to Google AI Studio (2025-02-11).
  > *AI Summary: @Vidit-Ostwal has suggested providing a fix for an error encountered while calling litellm with the Google Studio API. The error "contents is not specified" indicates that the GenerateContentRequest.contents field is missing. To resolve this, ensure that the contents parameter is provided when calling the completion() function.*
- Raised an [issue](https://github.com/langfuse/langfuse/issues/5432) in [langfuse/langfuse]: bug: Running Langfuse Locally Dcoker (2025-02-08).
  > *AI Summary: @Vidit-Ostwal has suggested that port 9000, which is used by both ClickHouse and MinIO containers, is already occupied by another process that cannot be terminated. They have attempted to change the port but believe that port 9000 is used elsewhere internally. As a result, migrations to the database fail, causing*
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/2030) in [crewAIInc/crewAI]: Documentation Error in memory docs (2025-02-04).
  > *AI Summary: @Vidit-Ostwal has suggested that the `model` parameter in the sample code examples given in the docs page should be replaced with `model_name`. The affected examples are:

- https://docs.crewai.com/concepts/memory#using-azure-openai-embeddings
- https://docs.crewai.com/concepts/memory#using-google-ai-embeddings
- https://docs.crewai.com/concepts/memory#using-vertex-ai-embeddings
- https://docs.crewai.com/concepts/memory#using-cohere-embeddings*
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/1984) in [crewAIInc/crewAI]: output_log_file should also suppport JSON format. (2025-01-27).
  > *AI Summary: @Vidit-Ostwal has suggested adding JSON support to the output_log_file to enable better parsability and enhance analytical capabilities. This proposed enhancement could partially address issue #1970. They are willing to contribute to the implementation through a pull request.*

## 🚀 Pull Requests
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2112) in [crewAIInc/crewAI]: Added user message before calling litellm (2025-02-12).
  > *AI Summary: @Vidit-Ostwal has suggested to include user messages that are formatted by 'feedback' as a solution to addressing issue #2111.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2071) in [crewAIInc/crewAI]: Added functionality to have any llm run test functionality (2025-02-09).
  > *AI Summary: @Vidit-Ostwal has suggested a fix for the issue reported in #2067. This comment provides a brief update, indicating that the issue has been addressed and resolved. However, the specific details of the fix and the underlying cause of the issue are not provided within this comment.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2047) in [crewAIInc/crewAI]: Added reset memories function inside crew class (2025-02-06).
  > *AI Summary: @Vidit-Ostwal has suggested the following changes to fix the reset memories issue reported in #2023:

- Remove the CLI command to reset memories
- Make necessary documentation changes

@Vidit-Ostwal has requested confirmation that these changes align with the desired solution before implementing them.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2031) in [crewAIInc/crewAI]: Fixed the memory documentation (2025-02-04).
  > *AI Summary: @Vidit-Ostwal has suggested a change to fix the documentation issue mentioned in issue #2030. They have not provided any further details or code examples in this comment.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/1985) in [crewAIInc/crewAI]: Added functionality to have json format as well for the logs (2025-01-27).
  > *AI Summary: @Vidit-Ostwal has suggested a feature that allows saving logs as a JSON file. With this addition, users can set "output_log_file" to a filename (e.g., "log.json") and enable "save_as_json" to True, to save the logs as a JSON file. This saved file contains an array of JSON events, enabling easier parsing*

## ⭐ Starred Repositories
- Starred [dipanjanS/training-fine-tuning-large-language-models-workshop-dhs2024](https://github.com/dipanjanS/training-fine-tuning-large-language-models-workshop-dhs2024) on 2025-02-12.
- Starred [sentient-engineering/sentient](https://github.com/sentient-engineering/sentient) on 2025-02-08.
- Starred [langflow-ai/langflow](https://github.com/langflow-ai/langflow) on 2025-02-07.
- Starred [langfuse/langfuse](https://github.com/langfuse/langfuse) on 2025-02-04.
- Starred [microsoft/autogen](https://github.com/microsoft/autogen) on 2025-01-31.

## 🍴 Forked Repositories
- Forked [crewAIInc/crewAI](https://github.com/Vidit-Ostwal/crewAI) on 2025-01-27.
- Forked [explodinggradients/ragas](https://github.com/Vidit-Ostwal/ragas) on 2025-01-24.
