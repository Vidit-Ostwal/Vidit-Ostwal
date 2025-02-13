# Recent GitHub Activity for Vidit-Ostwal

## 💬 Recent Comments
- [Commented](https://github.com/crewAIInc/crewAI/issues/2105#issuecomment-2653744764) in [crewAIInc/crewAI] on 2025-02-12.
  > *AI Summary: @Vidit-Ostwal has suggested that you verify if the strings being appended to the Python output are similar to the ones being printed in the terminal, as observed by @ninad-opsverse.*
- [Commented](https://github.com/crewAIInc/crewAI/pull/2071#issuecomment-2653722469) in [crewAIInc/crewAI] on 2025-02-12.
  > *AI Summary: @Vidit-Ostwal has suggested merging this pull request.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2097#issuecomment-2651667767) in [crewAIInc/crewAI] on 2025-02-11.
  > *AI Summary: @Vidit-Ostwal has suggested incorporating crews within a tool, managed by parent crews. These parent crews would be capable of initiating the crews within the tool, offering a hierarchical structure for managing crew operations. This design allows for more granular control over the tool's operation, enabling tailored crew configurations for specific*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2095#issuecomment-2651664099) in [crewAIInc/crewAI] on 2025-02-11.
  > *AI Summary: @Vidit-Ostwal has suggested that pre-computed or generalized managers are available, but believes it is better to maintain direct control over them. They advocate for having the ability to customize and manage the managers according to specific needs and preferences. This level of control allows for greater flexibility and adaptability in*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2092#issuecomment-2651660502) in [crewAIInc/crewAI] on 2025-02-11.
  > *AI Summary: @Vidit-Ostwal has suggested that `human_input` is called after a task is performed and asks users whether the response is good or not. They believe that incorporating additional context while the agent is asking for user input may not be the best idea. Instead, they recommend providing all necessary input while*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2095#issuecomment-2650913664) in [crewAIInc/crewAI] on 2025-02-11.
  > *AI Summary: @Vidit-Ostwal has suggested including context, as well as information about the agents and tools that the manager LLM can use, in the manager LLM guidelines. However, they have raised a concern that since the manager LLM is internally just another agent, adding a special `manager_note` just for it may not*
- [Commented](https://github.com/langfuse/langfuse/issues/5432#issuecomment-2648935567) in [langfuse/langfuse] on 2025-02-10.
  > *AI Summary: @Vidit-Ostwal has suggested that the issue was resolved by modifying the Docker port and the ClickHouse port from 9000 to 9005. They acknowledged that the fix was a simple adjustment and expressed gratitude for the assistance provided by @Steffen911.*
- [Commented](https://github.com/langfuse/langfuse/issues/5432#issuecomment-2648363009) in [langfuse/langfuse] on 2025-02-10.
  > *AI Summary: @Vidit-Ostwal has suggested that the issue lies with port 9000 being occupied by a security process that cannot be terminated. This prevents the desired application from running on that port.*
- [Commented](https://github.com/langfuse/langfuse/issues/5432#issuecomment-2648098489) in [langfuse/langfuse] on 2025-02-10.
  > *AI Summary: @Vidit-Ostwal has suggested the following: I just tried that again, here are the logs for your reference. The logs show the Redis server starting, PostgreSQL listening on ports 5432, and ClickHouse starting. However, applying ClickHouse migrations failed due to the database being unavailable. The logs also show MinIO, LangFuse, and*
- [Commented](https://github.com/langfuse/langfuse/issues/5432#issuecomment-2648019685) in [langfuse/langfuse] on 2025-02-10.
  > *AI Summary: @Vidit-Ostwal has updated the `docker-compose.yml` and suggested using updated ports for Clickhouse and Minio services: - Clickhouse external port is now 9009. - Clickhouse migration URL in the worker environment is now `http://clickhouse:9009`. - Minio external port is now 9010. - Minio S3 event upload endpoint in the worker environment*

## 🐛 Issues Raised
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/2111) in [crewAIInc/crewAI]: [BUG] LiteLLM call fails, when `human_input` set to True (2025-02-12).
  > *AI Summary: @Vidit-Ostwal has suggested that the failure of the code when the `human_input` is set to `True` is because the lite llm doesn't receive the user role in the messages when called. They have provided an image that demonstrates this issue. To resolve this, they recommend adding feedback in the user*
- Raised an [issue](https://github.com/BerriAI/litellm/issues/8467) in [BerriAI/litellm]: [Bug]: Support to Google AI Studio (2025-02-11).
  > *AI Summary: @Vidit-Ostwal has suggested that they are encountering an error when calling the `litellm` API to generate text. The error they are receiving indicates that no content was specified in the request. They have provided a code snippet that demonstrates the issue. @Vidit-Ostwal is using `litellm` version 1.60.2 and is not*
- Raised an [issue](https://github.com/langfuse/langfuse/issues/5432) in [langfuse/langfuse]: bug: Running Langfuse Locally Dcoker (2025-02-08).
  > *AI Summary: @Vidit-Ostwal has suggested addressing a bug in setting up Langfuse via Docker compose up. The issue arises due to port 9000 being occupied by another system process. The current fix involves changing the port 9000 used by both Clickhouse and Minio, but it seems that the port is also being*
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/2030) in [crewAIInc/crewAI]: Documentation Error in memory docs (2025-02-04).
  > *AI Summary: @Vidit-Ostwal has suggested that the embedder takes the input of `model` instead of `model_name` in the sample code examples given in the CrewAI docs. This is inconsistent with the `model_name` parameter specified in the docs. The affected pages are: - [Using Azure OpenAI Embeddings](https://docs.crewai.com/concepts/memory#using-azure-openai-embeddings) - [Using Google AI Embeddings](https://docs.crewai.com/concepts/memory#using-google-ai-embeddings) -*
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/1984) in [crewAIInc/crewAI]: output_log_file should also suppport JSON format. (2025-01-27).
  > *AI Summary: @Vidit-Ostwal has suggested adding a JSON format option to the output_log_file for further analysis, which also partially addresses issue #1970. The current .txt format is not parsable, so the JSON format would be a valuable addition.*

## 🚀 Pull Requests
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2112) in [crewAIInc/crewAI]: Added user message before calling litellm (2025-02-12).
  > *AI Summary: @Vidit-Ostwal has suggested a fix for issue #2111 by adding a user message formatted by `feedback`. This change addresses the specific issue mentioned in the bug report, providing a more user-friendly and informative experience for users encountering the issue. The implementation details, including specific code examples, are not mentioned in*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2071) in [crewAIInc/crewAI]: Added functionality to have any llm run test functionality (2025-02-09).
  > *AI Summary: @Vidit-Ostwal has suggested a fix for the issue raised in #2067. The suggested fix resolves the reported problem.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2047) in [crewAIInc/crewAI]: Added reset memories function inside crew class (2025-02-06).
  > *AI Summary: @Vidit-Ostwal suggests addressing the reset memories issue raised in issue #2023 by fixing the code. However, they also propose further changes: eliminating the CLI command for resetting memories and updating the documentation. They express their willingness to implement these changes if the solution is deemed suitable.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2031) in [crewAIInc/crewAI]: Fixed the memory documentation (2025-02-04).
  > *AI Summary: @Vidit-Ostwal has suggested resolving the documentation issue brought up in Issue #2030. This improvement ensures the accuracy and clarity of the documentation, making it more useful for users.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/1985) in [crewAIInc/crewAI]: Added functionality to have json format as well for the logs (2025-01-27).
  > *AI Summary: @Vidit-Ostwal has suggested adding a feature to save logs as a JSON file when initializing the crew object. Users can specify a file name or set output_log_file to True. By setting save_as_json to True, the generated JSON file will contain an array of JSON events, enabling easy parsing and manipulation.*

## ⭐ Starred Repositories
- Starred [dipanjanS/training-fine-tuning-large-language-models-workshop-dhs2024](https://github.com/dipanjanS/training-fine-tuning-large-language-models-workshop-dhs2024) on 2025-02-12.
- Starred [sentient-engineering/sentient](https://github.com/sentient-engineering/sentient) on 2025-02-08.
- Starred [langflow-ai/langflow](https://github.com/langflow-ai/langflow) on 2025-02-07.
- Starred [langfuse/langfuse](https://github.com/langfuse/langfuse) on 2025-02-04.
- Starred [microsoft/autogen](https://github.com/microsoft/autogen) on 2025-01-31.

## 🍴 Forked Repositories
- Forked [crewAIInc/crewAI](https://github.com/Vidit-Ostwal/crewAI) on 2025-01-27.
- Forked [explodinggradients/ragas](https://github.com/Vidit-Ostwal/ragas) on 2025-01-24.
