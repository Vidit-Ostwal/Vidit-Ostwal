# Recent GitHub Activity for Vidit-Ostwal

## 💬 Recent Comments
- [Commented](https://github.com/crewAIInc/crewAI/issues/2131#issuecomment-2660681309) in [crewAIInc/crewAI] on 2025-02-15.
  > *AI Summary: @Vidit-Ostwal has suggested that the entire code be shared once. This will allow reviewers to have a comprehensive understanding of the code's structure and functionality, enabling them to provide more informed feedback and identify potential areas for improvement. By sharing the complete code in one instance, it ensures that all*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2102#issuecomment-2659922689) in [crewAIInc/crewAI] on 2025-02-14.
  > *AI Summary: @Vidit-Ostwal has suggested trying to update the package as the session ends perfectly fine for them.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2105#issuecomment-2659884693) in [crewAIInc/crewAI] on 2025-02-14.
  > *AI Summary: @Vidit-Ostwal has suggested that you re-examine the goals and description you have provided for the task. Additionally, they recommend trying to obtain the output in a different format, such as JSON, to see if that resolves the issue.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2123#issuecomment-2659864458) in [crewAIInc/crewAI] on 2025-02-14.
  > *AI Summary: @Vidit-Ostwal has suggested confirming whether the file path in which your crew is running is the same as the path in the terminal where you are executing the `crewai reset-memories -a` command.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2105#issuecomment-2653744764) in [crewAIInc/crewAI] on 2025-02-12.
  > *AI Summary: @Vidit-Ostwal has suggested that it should be checked if the comment gets appended to the Python output.*
- [Commented](https://github.com/crewAIInc/crewAI/pull/2071#issuecomment-2653722469) in [crewAIInc/crewAI] on 2025-02-12.
  > *AI Summary: @Vidit-Ostwal has suggested merging the current pull request.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2097#issuecomment-2651667767) in [crewAIInc/crewAI] on 2025-02-11.
  > *AI Summary: @Vidit-Ostwal has suggested incorporating a crew within a tool, and introducing parent agents. The tool will have the ability to initiate a crew, which will be managed by a parent crew. This approach allows for a hierarchical structure, providing better control and coordination within the system.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2095#issuecomment-2651664099) in [crewAIInc/crewAI] on 2025-02-11.
  > *AI Summary: @Vidit-Ostwal suggests that instead of using pre-computed or generalized managers, it's better to maintain control over the process. This allows for greater flexibility and customization, ensuring that specific requirements are met effectively.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2092#issuecomment-2651660502) in [crewAIInc/crewAI] on 2025-02-11.
  > *AI Summary: @Vidit-Ostwal has suggested clarifying the usage of `human_input`. The function is invoked after task execution and prompts for feedback on the generated response, rather than during execution to incorporate additional context. Instead, he recommends providing all necessary input during `crew.kickoff()`.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2095#issuecomment-2650913664) in [crewAIInc/crewAI] on 2025-02-11.
  > *AI Summary: @Vidit-Ostwal has suggested including context and information about the tools and agents used by the manager LLM. However, they express concern that adding a "manager_note" specifically for the manager LLM may not be appropriate since it is treated internally as an agent only. Instead, they propose allowing users to request*

## 🐛 Issues Raised
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/2111) in [crewAIInc/crewAI]: [BUG] LiteLLM call fails, when `human_input` set to True (2025-02-12).
  > *AI Summary: @Vidit-Ostwal has suggested that when running a crew with `human_input`, set to True, the lite llm is not given the user role in the messages, causing it to fail for any user input. To address this, feedback has been added in the user role. However, providing a more detailed solution*
- Raised an [issue](https://github.com/BerriAI/litellm/issues/8467) in [BerriAI/litellm]: [Bug]: Support to Google AI Studio (2025-02-11).
  > *AI Summary: @Vidit-Ostwal has suggested that an error is encountered while calling litellm with Google Studio API. The error message indicates that the 'contents' field is not specified in the GenerateContentRequest. @Vidit-Ostwal has provided code that throws the error: ```python response = completion( model="gemini/gemini-1.5-pro", messages=[{'role': 'system', 'content': '...'}], api_key='' ) ``` To*
- Raised an [issue](https://github.com/langfuse/langfuse/issues/5432) in [langfuse/langfuse]: bug: Running Langfuse Locally Dcoker (2025-02-08).
  > *AI Summary: @Vidit-Ostwal has suggested that there is a bug in the Langfuse software when setting it up using docker. The problem is that both ClickHouse and MinIO use port 9000, which can already be occupied by another system process. Changing this port doesn't help as it seems to be used internally*
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/2030) in [crewAIInc/crewAI]: Documentation Error in memory docs (2025-02-04).
  > *AI Summary: @Vidit-Ostwal has suggested that the input parameter for the embedder should be changed from `model_name` to `model` in the example code provided in the docs. This change is suggested for all the example code mentioned in the docs page, including those for Azure OpenAI Embeddings, Google AI Embeddings, Vertex AI*
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/1984) in [crewAIInc/crewAI]: output_log_file should also suppport JSON format. (2025-01-27).
  > *AI Summary: @Vidit-Ostwal has suggested adding a JSON logging format to the output_log_file. They believe this would improve the parsability and usefulness of the logs for analysis. They also mention that this would partially address issue #1970. @Vidit-Ostwal is willing to contribute a pull request to implement this change.*

## 🚀 Pull Requests
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2155) in [crewAIInc/crewAI]: Fixed the issue 2123 around memory command with CLI (2025-02-17).
  > *AI Summary: @Vidit-Ostwal has suggested resolving the issue #2123 by patching the `get_crew()` function to retrieve the correct object.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2112) in [crewAIInc/crewAI]: Added user message before calling litellm (2025-02-12).
  > *AI Summary: @Vidit-Ostwal has suggested a fix for the issue reported in #2111 by incorporating a formatted user message using the `feedback` function. This modification enhances the user experience by providing a more informative and structured message.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2071) in [crewAIInc/crewAI]: Added functionality to have any llm run test functionality (2025-02-09).
  > *AI Summary: @Vidit-Ostwal has suggested a fix for the issues mentioned in #2067.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2047) in [crewAIInc/crewAI]: Added reset memories function inside crew class (2025-02-06).
  > *AI Summary: @Vidit-Ostwal has suggested fixing the reset memories issue mentioned in #2023. Additionally, they propose removing the CLI command for resetting memories and making documentation changes. However, they are seeking confirmation that this solution aligns before implementing these additional changes.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2031) in [crewAIInc/crewAI]: Fixed the memory documentation (2025-02-04).
  > *AI Summary: @Vidit-Ostwal has addressed the documentation problem identified in issue #2030. This effectively solves the previously reported issue.*

## ⭐ Starred Repositories
- Starred [bespokelabsai/curator](https://github.com/bespokelabsai/curator) on 2025-02-13.
- Starred [dipanjanS/training-fine-tuning-large-language-models-workshop-dhs2024](https://github.com/dipanjanS/training-fine-tuning-large-language-models-workshop-dhs2024) on 2025-02-12.
- Starred [sentient-engineering/sentient](https://github.com/sentient-engineering/sentient) on 2025-02-08.
- Starred [langflow-ai/langflow](https://github.com/langflow-ai/langflow) on 2025-02-07.
- Starred [langfuse/langfuse](https://github.com/langfuse/langfuse) on 2025-02-04.

## 🍴 Forked Repositories
- Forked [crewAIInc/crewAI](https://github.com/Vidit-Ostwal/crewAI) on 2025-01-27.
- Forked [explodinggradients/ragas](https://github.com/Vidit-Ostwal/ragas) on 2025-01-24.
