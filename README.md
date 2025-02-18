# Recent GitHub Activity for Vidit-Ostwal

## 💬 Recent Comments
- [Commented](https://github.com/crewAIInc/crewAI/issues/2131#issuecomment-2660681309) in [crewAIInc/crewAI] on 2025-02-15.
  > *AI Summary: @Vidit-Ostwal has suggested sharing the entire code once, for better understanding and ease of implementation. They believe that providing the complete code snippet upfront will eliminate the need for users to piece together information from multiple sources. This approach simplifies the implementation process, allowing users to quickly grasp the functionality*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2102#issuecomment-2659922689) in [crewAIInc/crewAI] on 2025-02-14.
  > *AI Summary: @Vidit-Ostwal has suggested that the package should be updated. This suggestion is based on the observation that the session ends without issue for them.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2105#issuecomment-2659884693) in [crewAIInc/crewAI] on 2025-02-14.
  > *AI Summary: @Vidit-Ostwal has suggested that the issue faced by @ninad-opsverse might be specific to their case and could not be reproduced. They recommend checking the provided goals and description, or trying to obtain the output in a different format, such as JSON, to troubleshoot the issue.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2123#issuecomment-2659864458) in [crewAIInc/crewAI] on 2025-02-14.
  > *AI Summary: @Vidit-Ostwal has suggested that the user confirm if the file path where the crew is running is the same as the path in the terminal where `crewai reset-memories -a` is being executed. This verification is crucial to ensure the success of the `reset-memories` command.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2105#issuecomment-2653744764) in [crewAIInc/crewAI] on 2025-02-12.
  > *AI Summary: @Vidit-Ostwal has suggested checking if the observed behavior is also appended to the Python output.*
- [Commented](https://github.com/crewAIInc/crewAI/pull/2071#issuecomment-2653722469) in [crewAIInc/crewAI] on 2025-02-12.
  > *AI Summary: @Vidit-Ostwal has suggested merging the current pull request.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2097#issuecomment-2651667767) in [crewAIInc/crewAI] on 2025-02-11.
  > *AI Summary: @Vidit-Ostwal has suggested incorporating a crew within a tool and some parent agents, with the tool having the capability to initiate a crew managed by a parent crew. This approach would involve nesting crews and agents in a hierarchical structure, allowing for more complex and structured agent-based simulations.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2095#issuecomment-2651664099) in [crewAIInc/crewAI] on 2025-02-11.
  > *AI Summary: @Vidit-Ostwal has suggested that instead of using a pre-computed or generalized manager, it would be more beneficial to have direct control over the manager. This would allow for more flexibility and customization in managing the system.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2092#issuecomment-2651660502) in [crewAIInc/crewAI] on 2025-02-11.
  > *AI Summary: @Vidit-Ostwal has suggested that there may be a misunderstanding regarding the function of `human_input`. `human_input` is designed to prompt the user for feedback on the generated response after the task has been completed, asking the user to evaluate the response's quality. Incorporating additional context during the agent's request for input*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2095#issuecomment-2650913664) in [crewAIInc/crewAI] on 2025-02-11.
  > *AI Summary: @Vidit-Ostwal suggests including context about agents and tools available to the manager LLM. However, they note the concern that adding a `manager_note` specifically for the manager LLM may not be ideal since it's an agent like any other internally. Additionally, @Vidit-Ostwal proposes exploring the possibility of having agents generate descriptions,*

## 🐛 Issues Raised
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/2111) in [crewAIInc/crewAI]: [BUG] LiteLLM call fails, when `human_input` set to True (2025-02-12).
  > *AI Summary: @Vidit-Ostwal has suggested that the code snippet fails to work when running a crew with `human_input` set to True because the lite llm is not given the user role in the messages. They have suggested adding feedback in the user role to resolve the issue. The code snippet attempts to*
- Raised an [issue](https://github.com/BerriAI/litellm/issues/8467) in [BerriAI/litellm]: [Bug]: Support to Google AI Studio (2025-02-11).
  > *AI Summary: @Vidit-Ostwal has suggested that an error is occurring when calling the `litellm` library with Google Studio API. The error indicates that the `contents` parameter in the `GenerateContentRequest` is not specified. The code provided uses the `completion` function from the `litellm` library, but does not include any content for the AI*
- Raised an [issue](https://github.com/langfuse/langfuse/issues/5432) in [langfuse/langfuse]: bug: Running Langfuse Locally Dcoker (2025-02-08).
  > *AI Summary: @Vidit-Ostwal has suggested the following changes to address the issue with port 9000 being used by a different process: - Investigate if port 9000 is used internally by langfuse within clickhouse migrations or other areas. - Provide guidance on all necessary port changes to resolve the conflict and enable langfuse*
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/2030) in [crewAIInc/crewAI]: Documentation Error in memory docs (2025-02-04).
  > *AI Summary: @Vidit-Ostwal has suggested that in the sample code examples provided in the documentation, the embedder takes the input of `model` instead of `model_name`. This issue affects all the examples mentioned in the documentation: - https://docs.crewai.com/concepts/memory#using-azure-openai-embeddings - https://docs.crewai.com/concepts/memory#using-google-ai-embeddings - https://docs.crewai.com/concepts/memory#using-vertex-ai-embeddings - https://docs.crewai.com/concepts/memory#using-cohere-embeddings @Vidit-Ostwal has not provided any steps to reproduce, expected*
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/1984) in [crewAIInc/crewAI]: output_log_file should also suppport JSON format. (2025-01-27).
  > *AI Summary: @Vidit-Ostwal has suggested enhancing the output log file by adding a JSON format option. This is because the current .txt format is not easily parsable for analysis. By supporting JSON, it will facilitate further analysis of the log data. This proposed change also partially addresses issue #1970. Additionally, @Vidit-Ostwal expresses*

## 🚀 Pull Requests
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2112) in [crewAIInc/crewAI]: Added user message before calling litellm (2025-02-12).
  > *AI Summary: @Vidit-Ostwal has suggested that this change addresses issue #2111, and adds user messages that are formatted using the "feedback" function. This change resolves the problem previously identified in the issue, ensuring that user messages are correctly formatted and displayed.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2071) in [crewAIInc/crewAI]: Added functionality to have any llm run test functionality (2025-02-09).
  > *AI Summary: @Vidit-Ostwal has suggested a fix for the issue brought up in #2067. This fix addresses the reported problem, ensuring that the affected functionality now operates correctly.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2047) in [crewAIInc/crewAI]: Added reset memories function inside crew class (2025-02-06).
  > *AI Summary: @Vidit-Ostwal has suggested fixes for the reset memories issue reported in #2023. To implement this, they propose:

1. Eliminating the CLI command for resetting memories.
2. Modifying the documentation to reflect these changes.

@Vidit-Ostwal is open to making these alterations, contingent upon their solution's alignment with the project's objectives.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2031) in [crewAIInc/crewAI]: Fixed the memory documentation (2025-02-04).
  > *AI Summary: @Vidit-Ostwal has suggested resolving the documentation issue reported in issue #2030. The details of this documentation issue have not been provided in this comment, so please refer to the linked issue for more context.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/1985) in [crewAIInc/crewAI]: Added functionality to have json format as well for the logs (2025-01-27).
  > *AI Summary: @Vidit-Ostwal has suggested adding support to save logs as a JSON file. When initializing the crew, one can set output_log_file to True or provide a file name (e.g., "log.json") and enable save_as_json by setting it to True. The generated JSON file will contain an array of JSON events, facilitating easy*

## ⭐ Starred Repositories
- Starred [bespokelabsai/curator](https://github.com/bespokelabsai/curator) on 2025-02-13.
- Starred [dipanjanS/training-fine-tuning-large-language-models-workshop-dhs2024](https://github.com/dipanjanS/training-fine-tuning-large-language-models-workshop-dhs2024) on 2025-02-12.
- Starred [sentient-engineering/sentient](https://github.com/sentient-engineering/sentient) on 2025-02-08.
- Starred [langflow-ai/langflow](https://github.com/langflow-ai/langflow) on 2025-02-07.
- Starred [langfuse/langfuse](https://github.com/langfuse/langfuse) on 2025-02-04.

## 🍴 Forked Repositories
- Forked [crewAIInc/crewAI](https://github.com/Vidit-Ostwal/crewAI) on 2025-01-27.
- Forked [explodinggradients/ragas](https://github.com/Vidit-Ostwal/ragas) on 2025-01-24.
