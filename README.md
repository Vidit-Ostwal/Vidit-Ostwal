# Recent GitHub Activity for Vidit-Ostwal

## 💬 Recent Comments
- [Commented](https://github.com/crewAIInc/crewAI/issues/2105#issuecomment-2653744764) in [crewAIInc/crewAI] on 2025-02-12.
  > *AI Summary: @Vidit-Ostwal has suggested exploring if the specified output gets appended to the Python output as well, based on @ninad-opsverse's observation.*
- [Commented](https://github.com/crewAIInc/crewAI/pull/2071#issuecomment-2653722469) in [crewAIInc/crewAI] on 2025-02-12.
  > *AI Summary: @Vidit-Ostwal has suggested that you merge the current pull request. They did not provide any specific justification or context for their request.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2097#issuecomment-2651667767) in [crewAIInc/crewAI] on 2025-02-11.
  > *AI Summary: @Vidit-Ostwal has suggested adding a crew within a tool and incorporating parent agents. The tool should be able to initiate a crew managed by a parent crew. This would establish a hierarchical structure with multiple levels of crews and parent agents, enhancing management and flexibility within the system.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2095#issuecomment-2651664099) in [crewAIInc/crewAI] on 2025-02-11.
  > *AI Summary: @Vidit-Ostwal suggests giving the user more control over pre-computed or generalized managers. While these are valuable options, they believe it is beneficial for the user to have the ability to customize and manage these functions themselves.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2092#issuecomment-2651660502) in [crewAIInc/crewAI] on 2025-02-11.
  > *AI Summary: @Vidit-Ostwal has suggested that `human_input` is called after the task has been performed to collect feedback on the response. He recommends providing all necessary input during the `crew.kickoff()` to avoid interrupting the crew execution flow. He further advises against incorporating additional input context during crew execution.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2095#issuecomment-2650913664) in [crewAIInc/crewAI] on 2025-02-11.
  > *AI Summary: @Vidit-Ostwal suggested including information about agents or tools that the manager LLM can use. However, they think adding a `manager_note` specifically for the manager LLM might not be ideal since it's internally considered just another agent. Instead, they propose allowing users to request descriptions, goals, and context for the manager*
- [Commented](https://github.com/langfuse/langfuse/issues/5432#issuecomment-2648935567) in [langfuse/langfuse] on 2025-02-10.
  > *AI Summary: @Vidit-Ostwal has suggested that changing the port number of the ClickHouse container from 9000 to 9005 resolved an issue. They also acknowledged that the adjustment was relatively minor and expressed gratitude for the guidance provided by @Steffen911.*
- [Commented](https://github.com/langfuse/langfuse/issues/5432#issuecomment-2648363009) in [langfuse/langfuse] on 2025-02-10.
  > *AI Summary: @Vidit-Ostwal has suggested that the underlying cause of this issue could be a security process running on port 9000. This security process is preventing the user from using port 9000, and it cannot be terminated. As a result, the user is unable to complete the task at hand because it*
- [Commented](https://github.com/langfuse/langfuse/issues/5432#issuecomment-2648098489) in [langfuse/langfuse] on 2025-02-10.
  > *AI Summary: @Vidit-Ostwal has suggested that the logs provided could be used to verify that the container is running as expected. To summarize the logs: - Redis is running and connected to a database. - PostgreSQL is running and listening on ports 5432 and 9001. - ClickHouse is running and is processing*
- [Commented](https://github.com/langfuse/langfuse/issues/5432#issuecomment-2648019685) in [langfuse/langfuse] on 2025-02-10.
  > *AI Summary: @Vidit-Ostwal has suggested that they have modified the ports for `clickhouse` and `minio` components within the `docker-compose.yml` configuration, but continue to experience the same issue. They have provided an updated code snippet. Additionally, they have mentioned that they suspect the problem might lie within another internal file.*

## 🐛 Issues Raised
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/2111) in [crewAIInc/crewAI]: [BUG] LiteLLM call fails, when `human_input` set to True (2025-02-12).
  > *AI Summary: @Vidit-Ostwal has suggested giving the user role in the messages when calling lite llm to resolve the issue where crew fails for any user input when human_input is set to True. This is because the problem arises due to the absence of the user role in the messages when lite*
- Raised an [issue](https://github.com/BerriAI/litellm/issues/8467) in [BerriAI/litellm]: [Bug]: Support to Google AI Studio (2025-02-11).
  > *AI Summary: @Vidit-Ostwal has suggested that while calling the litellm API via Google Studio, a BadRequestError was encountered. The error message indicates that the contents field in the GenerateContentRequest is not specified. They have provided a code snippet that triggers this error and are not on an ML Ops Team. They are*
- Raised an [issue](https://github.com/langfuse/langfuse/issues/5432) in [langfuse/langfuse]: bug: Running Langfuse Locally Dcoker (2025-02-08).
  > *AI Summary: @Vidit-Ostwal has suggested that port 9000 used by ClickHouse and Minio is already occupied by another process, causing the setup of LangFuse via Docker to fail. Changing the port in the configuration does not resolve the issue due to internal references to port 9000 elsewhere in the code. Assistance is*
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/2030) in [crewAIInc/crewAI]: Documentation Error in memory docs (2025-02-04).
  > *AI Summary: @Vidit-Ostwal has suggested that the provided code examples in the documentation contain a discrepancy. The examples show the embedder taking the input of `model` instead of `model_name`, as is mentioned in the documentation text. This inconsistency affects the usage of Azure OpenAI, Google AI, Vertex AI, and Cohere embeddings.*
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/1984) in [crewAIInc/crewAI]: output_log_file should also suppport JSON format. (2025-01-27).
  > *AI Summary: @Vidit-Ostwal has suggested expanding the output_log_file's current .txt format to include a parsable JSON format. This would address the need for further analysis and partially resolve issue #1970. They are willing to contribute a pull request for this implementation.*

## 🚀 Pull Requests
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2112) in [crewAIInc/crewAI]: Added user message before calling litellm (2025-02-12).
  > *AI Summary: @Vidit-Ostwal has fixed the issue reported in #2111.

The fix involves adding user message formatting by `feedback`. No further details regarding the implementation of the fix are provided in the comment.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2071) in [crewAIInc/crewAI]: Added functionality to have any llm run test functionality (2025-02-09).
  > *AI Summary: @Vidit-Ostwal has suggested a fix for the issue reported in #2067. Unfortunately, the specific details of the fix are not provided in this comment.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2047) in [crewAIInc/crewAI]: Added reset memories function inside crew class (2025-02-06).
  > *AI Summary: @Vidit-Ostwal has suggested fixing the memory reset issue reported in #2023. They also recommend removing the CLI command for memory reset and updating the documentation accordingly. However, they seek confirmation that these changes align with the project's direction before implementing them.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2031) in [crewAIInc/crewAI]: Fixed the memory documentation (2025-02-04).
  > *AI Summary: @Vidit-Ostwal has suggested that this change addresses the documentation issue reported in Issue #2030. By incorporating this fix, the documentation will be updated to provide more accurate and comprehensive information. This enhancement aims to improve the user experience by making it easier for individuals to access and understand the necessary*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/1985) in [crewAIInc/crewAI]: Added functionality to have json format as well for the logs (2025-01-27).
  > *AI Summary: @Vidit-Ostwal has suggested adding a feature to save logs as JSON files when initializing a crew. By setting `output_log_file` to a filename and `save_as_json` to `True`, the generated JSON file will contain an array of JSON events, simplifying parsing and working with the logs.*

## ⭐ Starred Repositories
- Starred [bespokelabsai/curator](https://github.com/bespokelabsai/curator) on 2025-02-13.
- Starred [dipanjanS/training-fine-tuning-large-language-models-workshop-dhs2024](https://github.com/dipanjanS/training-fine-tuning-large-language-models-workshop-dhs2024) on 2025-02-12.
- Starred [sentient-engineering/sentient](https://github.com/sentient-engineering/sentient) on 2025-02-08.
- Starred [langflow-ai/langflow](https://github.com/langflow-ai/langflow) on 2025-02-07.
- Starred [langfuse/langfuse](https://github.com/langfuse/langfuse) on 2025-02-04.

## 🍴 Forked Repositories
- Forked [crewAIInc/crewAI](https://github.com/Vidit-Ostwal/crewAI) on 2025-01-27.
- Forked [explodinggradients/ragas](https://github.com/Vidit-Ostwal/ragas) on 2025-01-24.
