# Recent GitHub Activity for Vidit-Ostwal

## 💬 Recent Comments
- [Commented](https://github.com/crewAIInc/crewAI/issues/2105#issuecomment-2653744764) in [crewAIInc/crewAI] on 2025-02-12.
  > *AI Summary: @Vidit-Ostwal has suggested checking if the observed behavior also occurs in the Python output. By doing this, we can assess whether the problem is specific to the TypeScript output or affects the overall code functionality.*
- [Commented](https://github.com/crewAIInc/crewAI/pull/2071#issuecomment-2653722469) in [crewAIInc/crewAI] on 2025-02-12.
  > *AI Summary: @Vidit-Ostwal has suggested merging the pull request.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2097#issuecomment-2651667767) in [crewAIInc/crewAI] on 2025-02-11.
  > *AI Summary: @Vidit-Ostwal has suggested incorporating a crew within a tool and introducing parent agents. The tool should have the capability to initiate a crew and be managed by a parent crew. This approach provides a hierarchical structure with nested crews and parent agents, allowing for flexible and efficient crew management. It*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2095#issuecomment-2651664099) in [crewAIInc/crewAI] on 2025-02-11.
  > *AI Summary: @Vidit-Ostwal has suggested that pre-computed or generalized managers can be used, but having finer control is more advantageous.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2092#issuecomment-2651660502) in [crewAIInc/crewAI] on 2025-02-11.
  > *AI Summary: @Vidit-Ostwal has suggested clarifying the usage of `human_input`. It is intended to be invoked after task execution to evaluate the generated response. Incorporating additional context during agent input is not recommended. Instead, all necessary input should be provided during `crew.kickoff()`.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2095#issuecomment-2650913664) in [crewAIInc/crewAI] on 2025-02-11.
  > *AI Summary: @Vidit-Ostwal suggests that providing context in the manager LLM would be valuable but raises the concern that singling it out with a `manager_note` might not be ideal since it's essentially an agent. They propose an alternative approach where the user could instruct other agents to create descriptions, goals, and context*
- [Commented](https://github.com/langfuse/langfuse/issues/5432#issuecomment-2648935567) in [langfuse/langfuse] on 2025-02-10.
  > *AI Summary: @Vidit-Ostwal has suggested changing the docker port and clickhouse port to resolve the issue. The error was resolved by changing the clickhouse port from 9000 to 9005.*
- [Commented](https://github.com/langfuse/langfuse/issues/5432#issuecomment-2648363009) in [langfuse/langfuse] on 2025-02-10.
  > *AI Summary: @Vidit-Ostwal has suggested that the issue might be caused by a security process running on port 9000, which prevents the process from initiating on that port. This security process cannot be terminated.*
- [Commented](https://github.com/langfuse/langfuse/issues/5432#issuecomment-2648098489) in [langfuse/langfuse] on 2025-02-10.
  > *AI Summary: @Vidit-Ostwal has suggested analyzing the logs provided in the comment to troubleshoot the issue with applying Clickhouse migrations. By examining the logs, it is possible to gain insights into the challenges encountered during the migration process and take appropriate action to resolve them. This approach can help in identifying and*
- [Commented](https://github.com/langfuse/langfuse/issues/5432#issuecomment-2648019685) in [langfuse/langfuse] on 2025-02-10.
  > *AI Summary: @Vidit-Ostwal suggests updating the `docker-compose.yml` file to resolve an issue with ports for Clickhouse and Minio. The Clickhouse migration port is now set to 9009, and the Clickhouse and Minio service ports are updated to 8123 and 9010, respectively. These changes aim to address the issue @Vidit-Ostwal encountered when changing*

## 🐛 Issues Raised
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/2111) in [crewAIInc/crewAI]: [BUG] LiteLLM call fails, when `human_input` set to True (2025-02-12).
  > *AI Summary: @Vidit-Ostwal has suggested a solution for the issue where the crew fails when run with human input set to True. The problem arises because the Lite LLM doesn't receive the user role in the messages when called. To resolve this, they have proposed adding feedback in the user role. Additionally,*
- Raised an [issue](https://github.com/BerriAI/litellm/issues/8467) in [BerriAI/litellm]: [Bug]: Support to Google AI Studio (2025-02-11).
  > *AI Summary: @Vidit-Ostwal has suggested that when calling litellm with the google studio api, an error is encountered. The error indicates that the contents parameter in the GenerateContentRequest is not specified. The code provided is missing the text that should be passed as the contents parameter. The issue can be resolved by*
- Raised an [issue](https://github.com/langfuse/langfuse/issues/5432) in [langfuse/langfuse]: bug: Running Langfuse Locally Dcoker (2025-02-08).
  > *AI Summary: @Vidit-Ostwal has suggested improvements for resolving a port conflict issue during Langfuse setup via Docker Compose. Specifically, the issue arises when port 9000, used by both ClickHouse and Minio, is already in use by an external system process. To resolve this, @Vidit-Ostwal suggests identifying all instances where port 9000 is*
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/2030) in [crewAIInc/crewAI]: Documentation Error in memory docs (2025-02-04).
  > *AI Summary: @Vidit-Ostwal has suggested that the documentation on embeddings at https://docs.crewai.com/concepts/memory needs to be updated to replace the `model_name` parameter with `model` in the code examples. This affects the sections on Azure OpenAI, Google AI, Vertex AI, and Cohere embeddings.*
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/1984) in [crewAIInc/crewAI]: output_log_file should also suppport JSON format. (2025-01-27).
  > *AI Summary: @Vidit-Ostwal has suggested the addition of a JSON format option for the output_log_file to support further analysis. This JSON format would address the issue raised in #1970. @Vidit-Ostwal is willing to contribute a pull request to implement this feature.*

## 🚀 Pull Requests
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2112) in [crewAIInc/crewAI]: Added user message before calling litellm (2025-02-12).
  > *AI Summary: @Vidit-Ostwal has suggested resolving the #2111 issue by incorporating a user message formatted by "feedback." The provided solution involves resolving the issue and implementing the suggested formatting using the "feedback" functionality. This modification aims to enhance the user experience and provide a more consistent and informative messaging format.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2071) in [crewAIInc/crewAI]: Added functionality to have any llm run test functionality (2025-02-09).
  > *AI Summary: @Vidit-Ostwal has suggested a fix for the issue raised in #2067. This resolves the problem reported in that issue. However, the exact details of the resolution are not provided in this comment.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2047) in [crewAIInc/crewAI]: Added reset memories function inside crew class (2025-02-06).
  > *AI Summary: @Vidit-Ostwal has suggested fixes for the memory reset issue reported in #2023. The proposed solution involves:

1. Elimination of the CLI command for memory reset
2. Updates to the documentation

@Vidit-Ostwal has indicated a willingness to implement these changes upon confirmation of alignment with the existing solution.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2031) in [crewAIInc/crewAI]: Fixed the memory documentation (2025-02-04).
  > *AI Summary: @Vidit-Ostwal has suggested a fix for the documentation issue that was mentioned in #2030. The specifics of the documentation fix are not provided in this comment.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/1985) in [crewAIInc/crewAI]: Added functionality to have json format as well for the logs (2025-01-27).
  > *AI Summary: @Vidit-Ostwal has suggested adding support to save logs as a JSON file. Now, users can initialize the crew by setting output_log_file to True or providing a file name. By setting save_as_json to True, the generated JSON file will include an array of JSON events, simplifying parsing and analysis.*

## ⭐ Starred Repositories
- Starred [dipanjanS/training-fine-tuning-large-language-models-workshop-dhs2024](https://github.com/dipanjanS/training-fine-tuning-large-language-models-workshop-dhs2024) on 2025-02-12.
- Starred [sentient-engineering/sentient](https://github.com/sentient-engineering/sentient) on 2025-02-08.
- Starred [langflow-ai/langflow](https://github.com/langflow-ai/langflow) on 2025-02-07.
- Starred [langfuse/langfuse](https://github.com/langfuse/langfuse) on 2025-02-04.
- Starred [microsoft/autogen](https://github.com/microsoft/autogen) on 2025-01-31.

## 🍴 Forked Repositories
- Forked [crewAIInc/crewAI](https://github.com/Vidit-Ostwal/crewAI) on 2025-01-27.
- Forked [explodinggradients/ragas](https://github.com/Vidit-Ostwal/ragas) on 2025-01-24.
