# Recent GitHub Activity for Vidit-Ostwal

## 💬 Recent Comments
- [Commented](https://github.com/crewAIInc/crewAI/issues/2102#issuecomment-2659922689) in [crewAIInc/crewAI] on 2025-02-14.
  > *AI Summary: @Vidit-Ostwal suggests trying to update the package to resolve the issue with sessions ending unexpectedly. They mentioned that sessions are ending perfectly fine on their end, indicating that the issue may be specific to the requester's setup or environment.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2105#issuecomment-2659884693) in [crewAIInc/crewAI] on 2025-02-14.
  > *AI Summary: @Vidit-Ostwal has suggested that the issue may be specific to the user's case. They recommend checking the goals and description provided, or trying to get the output in a different format, possibly JSON. @Vidit-Ostwal made these suggestions after attempting to reproduce the issue again today but being unable to do*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2123#issuecomment-2659864458) in [crewAIInc/crewAI] on 2025-02-14.
  > *AI Summary: @Vidit-Ostwal has suggested verifying that the file path where the crew is running matches the path in the terminal where `crewai reset-memories -a` is being executed. This check is essential to ensure that the memories are being reset for the correct crew.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2105#issuecomment-2653744764) in [crewAIInc/crewAI] on 2025-02-12.
  > *AI Summary: @Vidit-Ostwal has suggested that it should be clarified whether the information is also appended to the Python output.*
- [Commented](https://github.com/crewAIInc/crewAI/pull/2071#issuecomment-2653722469) in [crewAIInc/crewAI] on 2025-02-12.
  > *AI Summary: @Vidit-Ostwal has suggested merging this pull request.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2097#issuecomment-2651667767) in [crewAIInc/crewAI] on 2025-02-11.
  > *AI Summary: @Vidit-Ostwal has suggested incorporating a crew within a tool. Each tool should be capable of initiating a crew managed by a parent crew. This hierarchical structure of crews and parent agents within tools allows for more efficient crew management and tool functionality. The parent crew can provide oversight and coordination,*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2095#issuecomment-2651664099) in [crewAIInc/crewAI] on 2025-02-11.
  > *AI Summary: @Vidit-Ostwal has suggested that while pre-computed or generalized managers are available, it is preferable to retain control over the computation process.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2092#issuecomment-2651660502) in [crewAIInc/crewAI] on 2025-02-11.
  > *AI Summary: @Vidit-Ostwal has suggested clarifying the usage of `human_input`. It is called after the task is performed to assess the response's quality. Adding context during agent input is discouraged. Instead, all necessary input should be provided during `crew.kickoff()`.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2095#issuecomment-2650913664) in [crewAIInc/crewAI] on 2025-02-11.
  > *AI Summary: @Vidit-Ostwal suggests that the `manager_note` feature may not be suitable for the manager LLM as it is internally just an agent. Instead, they propose allowing users to request the LLM to generate descriptions, goals, and context for the manager agent. This would leverage the LLM's ability to access and utilize*
- [Commented](https://github.com/langfuse/langfuse/issues/5432#issuecomment-2648935567) in [langfuse/langfuse] on 2025-02-10.
  > *AI Summary: @Vidit-Ostwal has suggested a solution to the issue. They modified the Docker port and changed the ClickHouse port from 9000 to 9005, which resolved the problem. They expressed gratitude for the assistance provided by @Steffen911.*

## 🐛 Issues Raised
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/2111) in [crewAIInc/crewAI]: [BUG] LiteLLM call fails, when `human_input` set to True (2025-02-12).
  > *AI Summary: @Vidit-Ostwal has suggested a possible solution to an issue where a crew with `human_input` set to True fails for any user input. The issue arises because the lite llm used in the crew is not given the user role in the messages. To resolve this, they recommend adding feedback in*
- Raised an [issue](https://github.com/BerriAI/litellm/issues/8467) in [BerriAI/litellm]: [Bug]: Support to Google AI Studio (2025-02-11).
  > *AI Summary: @Vidit-Ostwal has suggested that while attempting to call litellm using the Google Studio API, they encountered a BadRequestError with the message "* GenerateContentRequest.contents: contents is not specified." They have included the code snippet and relevant error log but have not specified the ML Ops team status or LiteLLM version being*
- Raised an [issue](https://github.com/langfuse/langfuse/issues/5432) in [langfuse/langfuse]: bug: Running Langfuse Locally Dcoker (2025-02-08).
  > *AI Summary: @Vidit-Ostwal has suggested that the langfuse setup via Docker Compose fails because port 9000, used by both ClickHouse and MinIO, is occupied by another process. They believe that changing this port may not resolve the issue as it may be used internally elsewhere. The comment includes an error message indicating*
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/2030) in [crewAIInc/crewAI]: Documentation Error in memory docs (2025-02-04).
  > *AI Summary: @Vidit-Ostwal has suggested that the code examples in the documentation for the "Concepts: Memory" section should use "model_name" as the input parameter for the embedder instead of "model". This inconsistency is present in the examples for Azure OpenAI Embeddings, Google AI Embeddings, Vertex AI Embeddings, and Cohere Embeddings.*
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/1984) in [crewAIInc/crewAI]: output_log_file should also suppport JSON format. (2025-01-27).
  > *AI Summary: @Vidit-Ostwal has suggested adding JSON format as an option for the output_log_file. Currently, the output_log_file is in .txt format, which is not easily parsable. JSON would provide a more useful format for analysis. This suggestion partially addresses issue #1970. @Vidit-Ostwal is willing to contribute a pull request to implement this*

## 🚀 Pull Requests
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2112) in [crewAIInc/crewAI]: Added user message before calling litellm (2025-02-12).
  > *AI Summary: @Vidit-Ostwal has suggested that the changes in this pull request resolve issue #2111. Additionally, they have included a user message formatted by "feedback."*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2071) in [crewAIInc/crewAI]: Added functionality to have any llm run test functionality (2025-02-09).
  > *AI Summary: @Vidit-Ostwal has suggested a fix for the issue raised in #2067.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2047) in [crewAIInc/crewAI]: Added reset memories function inside crew class (2025-02-06).
  > *AI Summary: @Vidit-Ostwal has suggested fixes for the reset memories issue raised in #2023. Additionally, they recommend removing the CLI command for resetting memories and updating the documentation. However, they request confirmation on the alignment of their proposed solution.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2031) in [crewAIInc/crewAI]: Fixed the memory documentation (2025-02-04).
  > *AI Summary: @Vidit-Ostwal has suggested resolving the documentation issue raised in the issue #2030. They have not provided any additional details or context regarding the specific documentation issue or the proposed resolution.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/1985) in [crewAIInc/crewAI]: Added functionality to have json format as well for the logs (2025-01-27).
  > *AI Summary: @Vidit-Ostwal has suggested implementing the ability to save logs as a JSON file. By setting `output_log_file` to `True` or specifying a file name (e.g., `"log.json"`) and setting `save_as_json` to `True`, the generated JSON file will contain an array of events, facilitating parsing and analysis.*

## ⭐ Starred Repositories
- Starred [bespokelabsai/curator](https://github.com/bespokelabsai/curator) on 2025-02-13.
- Starred [dipanjanS/training-fine-tuning-large-language-models-workshop-dhs2024](https://github.com/dipanjanS/training-fine-tuning-large-language-models-workshop-dhs2024) on 2025-02-12.
- Starred [sentient-engineering/sentient](https://github.com/sentient-engineering/sentient) on 2025-02-08.
- Starred [langflow-ai/langflow](https://github.com/langflow-ai/langflow) on 2025-02-07.
- Starred [langfuse/langfuse](https://github.com/langfuse/langfuse) on 2025-02-04.

## 🍴 Forked Repositories
- Forked [crewAIInc/crewAI](https://github.com/Vidit-Ostwal/crewAI) on 2025-01-27.
- Forked [explodinggradients/ragas](https://github.com/Vidit-Ostwal/ragas) on 2025-01-24.
