# Recent GitHub Activity for Vidit-Ostwal

## 💬 Recent Comments
- [Commented](https://github.com/crewAIInc/crewAI/issues/2105#issuecomment-2653744764) in [crewAIInc/crewAI] on 2025-02-12.
  > *AI Summary: @Vidit-Ostwal has suggested that if the specified !include 'myconfig' gets appended to the python output, this could solve the problem.*
- [Commented](https://github.com/crewAIInc/crewAI/pull/2071#issuecomment-2653722469) in [crewAIInc/crewAI] on 2025-02-12.
  > *AI Summary: @Vidit-Ostwal has suggested merging this commit into the main branch. They have explicitly called out @joaomdmoura, but do not provide any additional context or detailed information regarding the commit or its purpose in their comment.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2097#issuecomment-2651667767) in [crewAIInc/crewAI] on 2025-02-11.
  > *AI Summary: @Vidit-Ostwal has suggested incorporating a crew inside a tool. Additionally, they recommend adding parent agents with the ability for the tool to kick off a crew, which would be managed by a parent crew. These suggestions aim to improve the organization and management of crews within the tool.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2095#issuecomment-2651664099) in [crewAIInc/crewAI] on 2025-02-11.
  > *AI Summary: @Vidit-Ostwal suggests that while pre-computed or generalized managers exist, it would be more beneficial to maintain granular control over the process.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2092#issuecomment-2651660502) in [crewAIInc/crewAI] on 2025-02-11.
  > *AI Summary: @Vidit-Ostwal has suggested clarifying the usage of `human_input`. It should be called after the task is performed to get feedback on the generated response, not to provide additional context during the task execution. Instead, necessary input should be provided during `crew.kickoff()`.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2095#issuecomment-2650913664) in [crewAIInc/crewAI] on 2025-02-11.
  > *AI Summary: @Vidit-Ostwal has suggested that while including context and information about available tools in the manager LLM is a good idea, it might not be optimal to introduce a `manager_note` specifically for this agent, as internally, the manager LLM operates solely as an agent. Alternatively, it has been proposed to consider*
- [Commented](https://github.com/langfuse/langfuse/issues/5432#issuecomment-2648935567) in [langfuse/langfuse] on 2025-02-10.
  > *AI Summary: @Vidit-Ostwal has suggested that changing the Docker port resolved their issue. Specifically, they changed the ClickHouse port from 9000 to 9005, which fixed the problem. They acknowledged the assistance provided by @Steffen911 and expressed gratitude for the support.*
- [Commented](https://github.com/langfuse/langfuse/issues/5432#issuecomment-2648363009) in [langfuse/langfuse] on 2025-02-10.
  > *AI Summary: @Vidit-Ostwal has suggested that the issue arises due to a security process running on port 9000. This security process cannot be terminated, thus preventing the desired operation on that port.*
- [Commented](https://github.com/langfuse/langfuse/issues/5432#issuecomment-2648098489) in [langfuse/langfuse] on 2025-02-10.
  > *AI Summary: @Vidit-Ostwal has suggested providing the logs for reference. These logs show the startup and configuration of various services in a Kubernetes cluster, including Redis, PostgreSQL, Clickhouse, MinIO, and langfuse-web and langfuse-worker containers. The logs also show errors encountered during the migration of data to Clickhouse.*
- [Commented](https://github.com/langfuse/langfuse/issues/5432#issuecomment-2648019685) in [langfuse/langfuse] on 2025-02-10.
  > *AI Summary: @Vidit-Ostwal suggests updating `docker-compose.yml` to resolve a recurring issue. Ports for both ClickHouse and Minio have been modified, with ClickHouse's external port set to 9009 and Minio's external port set to 9010. The updated code has been provided, but the issue persists, leading to a suspicion that the problem may*

## 🐛 Issues Raised
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/2111) in [crewAIInc/crewAI]: [BUG] LiteLLM call fails, when `human_input` set to True (2025-02-12).
  > *AI Summary: @Vidit-Ostwal has suggested a solution to an issue where a crew fails to run properly when `human_input` is set to True. The problem is that the lite llm used by the Pokemon Color Specialist agent does not have the user role assigned to it in messages. This causes the agent*
- Raised an [issue](https://github.com/BerriAI/litellm/issues/8467) in [BerriAI/litellm]: [Bug]: Support to Google AI Studio (2025-02-11).
  > *AI Summary: @Vidit-Ostwal has suggested addressing this issue of aBadRequestError when calling the litellm API in Google Studio. The error is related to unspecified content in the GenerateContentRequest. The suggestion includes double-checking the content specified in the request and ensuring it's non-empty. Additionally, they recommend debugging the issue by calling litellm._turn_on_debug() and*
- Raised an [issue](https://github.com/langfuse/langfuse/issues/5432) in [langfuse/langfuse]: bug: Running Langfuse Locally Dcoker (2025-02-08).
  > *AI Summary: @Vidit-Ostwal has suggested that there is a bug in the langfuse docker setup. When trying to set up langfuse via docker-compose, the port 9000, which is used by both clickhouse and minio, is already in use by another system process. Changing the port in the docker-compose file does not resolve*
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/2030) in [crewAIInc/crewAI]: Documentation Error in memory docs (2025-02-04).
  > *AI Summary: @Vidit-Ostwal has suggested that the sample code examples in the documentation for the embedder incorrectly reference "model" when they should be referencing "model_name". This issue affects multiple pages in the documentation, including those covering Azure OpenAI Embeddings, Google AI Embeddings, Vertex AI Embeddings, and Cohere Embeddings.*
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/1984) in [crewAIInc/crewAI]: output_log_file should also suppport JSON format. (2025-01-27).
  > *AI Summary: @Vidit-Ostwal has suggested implementing a JSON format along with the existing .txt format for the output_log_file. This is because the .txt format is not parseable, making further analysis difficult. Adding JSON support would partially address issue #1970. @Vidit-Ostwal is willing to contribute a pull request for this change.*

## 🚀 Pull Requests
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2112) in [crewAIInc/crewAI]: Added user message before calling litellm (2025-02-12).
  > *AI Summary: @Vidit-Ostwal has suggested fixing issue #2111 by adding a user message formatted by `feedback`. No further information is provided in the comment.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2071) in [crewAIInc/crewAI]: Added functionality to have any llm run test functionality (2025-02-09).
  > *AI Summary: @Vidit-Ostwal has suggested a fix for the issue raised in #2067. The provided fix resolves the underlying problem, ensuring the optimal functioning of the feature. This addresses the concerns raised in the earlier issue and enhances the overall performance and reliability of the system.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2047) in [crewAIInc/crewAI]: Added reset memories function inside crew class (2025-02-06).
  > *AI Summary: @Vidit-Ostwal suggests fixing the reset memories issue raised in #2023. Further changes are required:

1. Removing the CLI command for resetting memories
2. Updating documentation

They are willing to implement these changes if the solution aligns with the overall project goals.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2031) in [crewAIInc/crewAI]: Fixed the memory documentation (2025-02-04).
  > *AI Summary: @Vidit-Ostwal has suggested a fix for the documentation issue mentioned in issue #2030. This change addresses the reported problem and improves the clarity of the documentation. By implementing this change, the documentation will be more accurate and easier to follow for users, enhancing their understanding of the system's functionality.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/1985) in [crewAIInc/crewAI]: Added functionality to have json format as well for the logs (2025-01-27).
  > *AI Summary: @Vidit-Ostwal has suggested adding support to save logs as a JSON file. When initializing the crew, users can set "output_log_file" to True or a file name like "log.json." By enabling "save_as_json," a JSON file will be created containing an array of JSON events. This simplifies parsing and working with logs.*

## ⭐ Starred Repositories
- Starred [bespokelabsai/curator](https://github.com/bespokelabsai/curator) on 2025-02-13.
- Starred [dipanjanS/training-fine-tuning-large-language-models-workshop-dhs2024](https://github.com/dipanjanS/training-fine-tuning-large-language-models-workshop-dhs2024) on 2025-02-12.
- Starred [sentient-engineering/sentient](https://github.com/sentient-engineering/sentient) on 2025-02-08.
- Starred [langflow-ai/langflow](https://github.com/langflow-ai/langflow) on 2025-02-07.
- Starred [langfuse/langfuse](https://github.com/langfuse/langfuse) on 2025-02-04.

## 🍴 Forked Repositories
- Forked [crewAIInc/crewAI](https://github.com/Vidit-Ostwal/crewAI) on 2025-01-27.
- Forked [explodinggradients/ragas](https://github.com/Vidit-Ostwal/ragas) on 2025-01-24.
