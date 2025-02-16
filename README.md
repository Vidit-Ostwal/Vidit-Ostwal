# Recent GitHub Activity for Vidit-Ostwal

## 💬 Recent Comments
- [Commented](https://github.com/crewAIInc/crewAI/issues/2131#issuecomment-2660681309) in [crewAIInc/crewAI] on 2025-02-15.
  > *AI Summary: @Vidit-Ostwal has suggested sharing the entire code in a single place. This will make it easier for everyone to access and review the code, facilitating better collaboration and understanding.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2102#issuecomment-2659922689) in [crewAIInc/crewAI] on 2025-02-14.
  > *AI Summary: @Vidit-Ostwal has suggested that @ashishpatel26 try updating the package they are using, as they have not experienced any issues with sessions ending prematurely.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2105#issuecomment-2659884693) in [crewAIInc/crewAI] on 2025-02-14.
  > *AI Summary: @Vidit-Ostwal has suggested that the issue might be specific to the user's case. They recommend checking the goals and description provided, or trying to get the output in a different format, such as JSON.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2123#issuecomment-2659864458) in [crewAIInc/crewAI] on 2025-02-14.
  > *AI Summary: @Vidit-Ostwal has suggested confirming if the file path where the crew is running matches the path in the terminal where the `crewai reset-memories -a` command is executed. This will help ensure that the command is targeting the correct file.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2105#issuecomment-2653744764) in [crewAIInc/crewAI] on 2025-02-12.
  > *AI Summary: @Vidit-Ostwal has suggested that it would be helpful to verify whether the changes made to the build apply to the Python output as well. They have requested confirmation on whether these changes are reflected in both the Ruby and Python outputs.*
- [Commented](https://github.com/crewAIInc/crewAI/pull/2071#issuecomment-2653722469) in [crewAIInc/crewAI] on 2025-02-12.
  > *AI Summary: @Vidit-Ostwal has suggested merging the current pull request.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2097#issuecomment-2651667767) in [crewAIInc/crewAI] on 2025-02-11.
  > *AI Summary: @Vidit-Ostwal has suggested incorporating a crew within a tool, along with parent agents. The tool should possess the ability to initiate a crew, which would be managed by a parent crew. This approach aims to establish a hierarchical structure within the system.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2095#issuecomment-2651664099) in [crewAIInc/crewAI] on 2025-02-11.
  > *AI Summary: @Vidit-Ostwal has suggested that although pre-computed or generalized managers can be used, it is beneficial to have direct control over the manager. This allows for customization and tailoring to specific requirements, ensuring optimal performance and meeting specific needs.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2092#issuecomment-2651660502) in [crewAIInc/crewAI] on 2025-02-11.
  > *AI Summary: @Vidit-Ostwal has suggested that the human input should be requested after the task is performed and it should be used to determine the quality of the generated response. Adding additional input context during crew execution is not recommended. Instead, all necessary input should be provided during `crew.kickoff()`.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2095#issuecomment-2650913664) in [crewAIInc/crewAI] on 2025-02-11.
  > *AI Summary: @Vidit-Ostwal suggests providing context on available agents and tools for the manager LLM. They believe that the current approach creates an unnecessary distinction between the manager LLM and other agents. Instead, they propose that users could instruct the LLM to generate context for the manager LLM, utilizing information from other*

## 🐛 Issues Raised
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/2111) in [crewAIInc/crewAI]: [BUG] LiteLLM call fails, when `human_input` set to True (2025-02-12).
  > *AI Summary: @Vidit-Ostwal has suggested resolving an issue where a crew fails to run properly with `human_input` set to `True`. The problem arises because the lite language model (LLM) used in the crew is not assigned the user role. As a solution, @Vidit-Ostwal proposed adding feedback in the user role. The issue*
- Raised an [issue](https://github.com/BerriAI/litellm/issues/8467) in [BerriAI/litellm]: [Bug]: Support to Google AI Studio (2025-02-11).
  > *AI Summary: @Vidit-Ostwal has suggested exploring a BadRequestError when attempting to call litellm with Google Studio API. The error stems from an unspecified contents parameter in the GenerateContentRequest. To resolve this issue, ensure that the contents parameter is specified before invoking the API.*
- Raised an [issue](https://github.com/langfuse/langfuse/issues/5432) in [langfuse/langfuse]: bug: Running Langfuse Locally Dcoker (2025-02-08).
  > *AI Summary: @Vidit-Ostwal has suggested that the error "failed to open database" while setting up Langfuse via Docker Compose is due to port 9000 being used by another process. They have attempted to change the port, but believe that the port is being used internally elsewhere. They request assistance in identifying where*
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/2030) in [crewAIInc/crewAI]: Documentation Error in memory docs (2025-02-04).
  > *AI Summary: @Vidit-Ostwal has suggested updating the documentation to address the discrepancy between the provided code examples and the actual parameters required by the embedder. In the code examples, the embedder takes the input of `model` instead of `model_name`. This issue is present across multiple examples, including those using Azure OpenAI Embeddings,*
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/1984) in [crewAIInc/crewAI]: output_log_file should also suppport JSON format. (2025-01-27).
  > *AI Summary: @Vidit-Ostwal has suggested adding JSON formatting to the `output_log_file` for enhanced parsability and analysis. This feature is partially related to issue #1970. @Vidit-Ostwal is willing to contribute a pull request for this implementation.*

## 🚀 Pull Requests
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2112) in [crewAIInc/crewAI]: Added user message before calling litellm (2025-02-12).
  > *AI Summary: @Vidit-Ostwal has suggested a fix for issue #2111 by adding a user message that is formatted by `feedback`. This change ensures that user messages are presented in a consistent and clear manner, enhancing the user experience and simplifying the message-formatting process.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2071) in [crewAIInc/crewAI]: Added functionality to have any llm run test functionality (2025-02-09).
  > *AI Summary: @Vidit-Ostwal has suggested a fix for the issue raised in #2067. Unfortunately, the comment does not provide any detailed description of the fix or its implementation.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2047) in [crewAIInc/crewAI]: Added reset memories function inside crew class (2025-02-06).
  > *AI Summary: @Vidit-Ostwal has suggested addressing the memory reset issue raised in #2023. They propose additional changes including removing the CLI command for memory reset and making documentation updates. However, they emphasize that these changes should only be implemented if the proposed solution is deemed suitable.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2031) in [crewAIInc/crewAI]: Fixed the memory documentation (2025-02-04).
  > *AI Summary: @Vidit-Ostwal has suggested fixing the documentation issue mentioned in issue #2030.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/1985) in [crewAIInc/crewAI]: Added functionality to have json format as well for the logs (2025-01-27).
  > *AI Summary: @Vidit-Ostwal has suggested adding the ability to save logs as a JSON file when initializing the crew. This can be done by setting `output_log_file` to a file name (e.g., "log.json") and enabling `save_as_json` by setting it to True. The generated JSON file will contain an array of JSON events, making*

## ⭐ Starred Repositories
- Starred [bespokelabsai/curator](https://github.com/bespokelabsai/curator) on 2025-02-13.
- Starred [dipanjanS/training-fine-tuning-large-language-models-workshop-dhs2024](https://github.com/dipanjanS/training-fine-tuning-large-language-models-workshop-dhs2024) on 2025-02-12.
- Starred [sentient-engineering/sentient](https://github.com/sentient-engineering/sentient) on 2025-02-08.
- Starred [langflow-ai/langflow](https://github.com/langflow-ai/langflow) on 2025-02-07.
- Starred [langfuse/langfuse](https://github.com/langfuse/langfuse) on 2025-02-04.

## 🍴 Forked Repositories
- Forked [crewAIInc/crewAI](https://github.com/Vidit-Ostwal/crewAI) on 2025-01-27.
- Forked [explodinggradients/ragas](https://github.com/Vidit-Ostwal/ragas) on 2025-01-24.
