# Recent GitHub Activity for Vidit-Ostwal

## 💬 Recent Comments
- [Commented](https://github.com/crewAIInc/crewAI/issues/2131#issuecomment-2660681309) in [crewAIInc/crewAI] on 2025-02-15.
  > *AI Summary: @Vidit-Ostwal has suggested that the entire code should be shared in one place for easy reference. This will help others to quickly understand the context and implementation details without having to search through multiple sources. By centralizing the code, it also becomes easier to maintain and update in the future,*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2102#issuecomment-2659922689) in [crewAIInc/crewAI] on 2025-02-14.
  > *AI Summary: @Vidit-Ostwal has suggested trying to update the package to fix the issue where sessions end abruptly. They mentioned that the issue does not occur on their end, and that the package may require an update.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2105#issuecomment-2659884693) in [crewAIInc/crewAI] on 2025-02-14.
  > *AI Summary: @Vidit-Ostwal suggested checking the goals and description provided and trying to get the output in a different format, such as JSON. They were unable to reproduce the issue again today and believe it may be specific to the user's case.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2123#issuecomment-2659864458) in [crewAIInc/crewAI] on 2025-02-14.
  > *AI Summary: @Vidit-Ostwal has suggested confirming if the file path where your crew is running is the same as the path in the terminal where you are executing the `crewai reset-memories -a` command. This is a crucial step to ensure successful execution of the command.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2105#issuecomment-2653744764) in [crewAIInc/crewAI] on 2025-02-12.
  > *AI Summary: @Vidit-Ostwal has suggested that we check if the observed behavior, where a string gets appended to the Python output, occurs consistently. They have requested confirmation on this matter.*
- [Commented](https://github.com/crewAIInc/crewAI/pull/2071#issuecomment-2653722469) in [crewAIInc/crewAI] on 2025-02-12.
  > *AI Summary: @Vidit-Ostwal has suggested merging this request.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2097#issuecomment-2651667767) in [crewAIInc/crewAI] on 2025-02-11.
  > *AI Summary: @Vidit-Ostwal has suggested incorporating a crew inside a tool, along with parent agents. The tool should be capable of initiating a crew managed by a parent crew. By doing so, the crew within the tool can be managed and controlled by the parent crew, providing a hierarchical structure and centralized*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2095#issuecomment-2651664099) in [crewAIInc/crewAI] on 2025-02-11.
  > *AI Summary: @Vidit-Ostwal has suggested that while pre-computed or generalized managers may be sufficient, it's preferable to have greater control over the process. This allows for more flexibility and customization, ensuring that the specific requirements of the project or task are met.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2092#issuecomment-2651660502) in [crewAIInc/crewAI] on 2025-02-11.
  > *AI Summary: @Vidit-Ostwal suggests that `human_input` is called after a task is performed to get feedback on the generated response. Incorporating additional context while the agent asks for input may not be optimal. Instead, it is recommended to provide all necessary input during `crew.kickoff()`.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2095#issuecomment-2650913664) in [crewAIInc/crewAI] on 2025-02-11.
  > *AI Summary: @Vidit-Ostwal suggests including context and agent tools in the manager LLM. However, they acknowledge that the manager LLM is essentially an agent itself, making it potentially inconsistent to add a "manager_note" specifically for one agent. Instead, they propose allowing users to request that an agent generate descriptions, goals, and context*

## 🐛 Issues Raised
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/2111) in [crewAIInc/crewAI]: [BUG] LiteLLM call fails, when `human_input` set to True (2025-02-12).
  > *AI Summary: @Vidit-Ostwal has suggested that the issue with running a crew with `human_input` set to True is that the lite llm doesn't have the user role in the messages when called. This causes the crew to fail for any input provided by the user. To resolve this, feedback should be added*
- Raised an [issue](https://github.com/BerriAI/litellm/issues/8467) in [BerriAI/litellm]: [Bug]: Support to Google AI Studio (2025-02-11).
  > *AI Summary: @Vidit-Ostwal has suggested looking into a BadRequestError encountered while attempting to call litellm with the Google Studio API. The error indicates missing contents in the GenerateContentRequest. The code sample provided includes the litellm.completion function call with the "gemini/gemini-1.5-pro" model, a message with a role of 'system' and content for satisfaction*
- Raised an [issue](https://github.com/langfuse/langfuse/issues/5432) in [langfuse/langfuse]: bug: Running Langfuse Locally Dcoker (2025-02-08).
  > *AI Summary: @Vidit-Ostwal has suggested that the port 9000 is being used by another system process that cannot be terminated. They have tried changing the port, but believe that port 9000 is also being used internally. The suggested reproduction steps are to setup langfuse via docker docker compose up as stated in*
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/2030) in [crewAIInc/crewAI]: Documentation Error in memory docs (2025-02-04).
  > *AI Summary: @Vidit-Ostwal has suggested aligning the input parameters of `embedder` with the documentation. Specifically, the `model_name` parameter in the sample code examples should be replaced with `model`. This change should be made in the following documentation pages:
- https://docs.crewai.com/concepts/memory#using-azure-openai-embeddings
- https://docs.crewai.com/concepts/memory#using-google-ai-embeddings
- https://docs.crewai.com/concepts/memory#using-vertex-ai-embeddings
- https://docs.crewai.com/concepts/memory#using-cohere-embeddings*
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/1984) in [crewAIInc/crewAI]: output_log_file should also suppport JSON format. (2025-01-27).
  > *AI Summary: @Vidit-Ostwal has suggested that the output log file should support JSON format in addition to the current .txt format. They believe this would make the log file more parsable and useful for further analysis. They also suggest that this would partially address issue #1970. @Vidit-Ostwal is willing to contribute a*

## 🚀 Pull Requests
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2112) in [crewAIInc/crewAI]: Added user message before calling litellm (2025-02-12).
  > *AI Summary: @Vidit-Ostwal has suggested fixing issue #2111 by adding a user message formatted by `feedback`. This change may enhance the user experience by providing more relevant and helpful feedback.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2071) in [crewAIInc/crewAI]: Added functionality to have any llm run test functionality (2025-02-09).
  > *AI Summary: @Vidit-Ostwal has suggested a fix for the issue mentioned in issue number 2067. Unfortunately, the comment does not provide any further details regarding the specific nature of the fix or the changes that were made to resolve the issue.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2047) in [crewAIInc/crewAI]: Added reset memories function inside crew class (2025-02-06).
  > *AI Summary: @Vidit-Ostwal has suggested fixing the reset memories issue mentioned in #2023. Additionally, they recommend removing the CLI command to reset memories and making necessary documentation changes. They are available to implement these changes if the solution aligns with the team's requirements.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2031) in [crewAIInc/crewAI]: Fixed the memory documentation (2025-02-04).
  > *AI Summary: @Vidit-Ostwal has suggested the documentation issue mentioned in #2030 has been fixed in the latest commit. Unfortunately, the exact issue being resolved is not specified in this comment.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/1985) in [crewAIInc/crewAI]: Added functionality to have json format as well for the logs (2025-01-27).
  > *AI Summary: @Vidit-Ostwal has suggested adding a feature to save logs as a JSON file. By setting the output_log_file parameter to a file name (e.g., "log.json") and setting save_as_json to True, the generated JSON file will contain an array of JSON events, allowing for easy parsing and analysis.*

## ⭐ Starred Repositories
- Starred [bespokelabsai/curator](https://github.com/bespokelabsai/curator) on 2025-02-13.
- Starred [dipanjanS/training-fine-tuning-large-language-models-workshop-dhs2024](https://github.com/dipanjanS/training-fine-tuning-large-language-models-workshop-dhs2024) on 2025-02-12.
- Starred [sentient-engineering/sentient](https://github.com/sentient-engineering/sentient) on 2025-02-08.
- Starred [langflow-ai/langflow](https://github.com/langflow-ai/langflow) on 2025-02-07.
- Starred [langfuse/langfuse](https://github.com/langfuse/langfuse) on 2025-02-04.

## 🍴 Forked Repositories
- Forked [crewAIInc/crewAI](https://github.com/Vidit-Ostwal/crewAI) on 2025-01-27.
- Forked [explodinggradients/ragas](https://github.com/Vidit-Ostwal/ragas) on 2025-01-24.
