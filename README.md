# Recent GitHub Activity for Vidit-Ostwal

## 💬 Recent Comments
- [Commented](https://github.com/crewAIInc/crewAI/issues/2131#issuecomment-2660681309) in [crewAIInc/crewAI] on 2025-02-15.
  > *AI Summary: @Vidit-Ostwal has requested if the entire code for the project can be shared. It would be helpful to have the complete codebase available to better understand the project implementation and its functionality.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2102#issuecomment-2659922689) in [crewAIInc/crewAI] on 2025-02-14.
  > *AI Summary: @Vidit-Ostwal has suggested that since the session ends well on their system, @ashishpatel26 should try updating the package that is causing issues. It is possible that the issue is due to an outdated package.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2105#issuecomment-2659884693) in [crewAIInc/crewAI] on 2025-02-14.
  > *AI Summary: @Vidit-Ostwal has suggested that the issue may be specific to your case, as they were unable to reproduce it. They recommend checking the goals and description provided to ensure accuracy or trying to get the output in a different format, such as JSON.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2123#issuecomment-2659864458) in [crewAIInc/crewAI] on 2025-02-14.
  > *AI Summary: @Vidit-Ostwal suggests verifying if the file path where the crew is running matches the path in the terminal where the `crewai reset-memories -a` command is being executed. He highlights that this is crucial for a successful reset of crew memories.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2105#issuecomment-2653744764) in [crewAIInc/crewAI] on 2025-02-12.
  > *AI Summary: @Vidit-Ostwal has suggested that we should determine if a string gets appended to the Python output. This is in response to @ninad-opsverse's observation.*
- [Commented](https://github.com/crewAIInc/crewAI/pull/2071#issuecomment-2653722469) in [crewAIInc/crewAI] on 2025-02-12.
  > *AI Summary: @Vidit-Ostwal has suggested merging this pull request.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2097#issuecomment-2651667767) in [crewAIInc/crewAI] on 2025-02-11.
  > *AI Summary: @Vidit-Ostwal has suggested incorporating a crew within a tool, along with parent agents. The tool should be capable of initiating a crew and being managed by a parent crew. This would allow for more granular control and flexibility in managing crews and agents, enabling users to tailor the setup to*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2095#issuecomment-2651664099) in [crewAIInc/crewAI] on 2025-02-11.
  > *AI Summary: @Vidit-Ostwal has suggested using a pre-computed or generalized manager. However, they believe it would be better to maintain control over the management process.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2092#issuecomment-2651660502) in [crewAIInc/crewAI] on 2025-02-11.
  > *AI Summary: @Vidit-Ostwal has suggested that the `human_input` function is called after a task is performed to ask for feedback on the generated response. Instead of incorporating additional context while the agent is requesting input, he recommends providing all necessary input during the `crew.kickoff()` function. This is believed to be a better*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2095#issuecomment-2650913664) in [crewAIInc/crewAI] on 2025-02-11.
  > *AI Summary: @Vidit-Ostwal suggests including context, agents, and tools for Manager LLM. However, they note that Manager LLM is an agent itself, so it may not be logical to add `manager_note` for a single agent. Instead, they propose requesting descriptions, goals, and context from any agent, including the Manager LLM, to leverage*

## 🐛 Issues Raised
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/2111) in [crewAIInc/crewAI]: [BUG] LiteLLM call fails, when `human_input` set to True (2025-02-12).
  > *AI Summary: @Vidit-Ostwal has suggested that when the lite llm is called in a crew with `human_input` set to True, it should be given the user role in the messages to avoid issues where the crew fails for any user-provided input. This is because the lite llm does not have the user*
- Raised an [issue](https://github.com/BerriAI/litellm/issues/8467) in [BerriAI/litellm]: [Bug]: Support to Google AI Studio (2025-02-11).
  > *AI Summary: @Vidit-Ostwal has suggested a summary of the issue they encountered while attempting to call the litellm API using Google Studio API. They encountered a BadRequestError due to unspecified contents in the GenerateContentRequest. To resolve the issue, they suggest specifying the contents for the request.*
- Raised an [issue](https://github.com/langfuse/langfuse/issues/5432) in [langfuse/langfuse]: bug: Running Langfuse Locally Dcoker (2025-02-08).
  > *AI Summary: @Vidit-Ostwal has suggested that when attempting to set up langfuse via Docker compose up as per the guidelines on https://langfuse.com/self-hosting/local, issues arise due to port 9000 being used by another system process. As a result, the database connection fails. @Vidit-Ostwal is interested in contributing a fix and requests assistance in*
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/2030) in [crewAIInc/crewAI]: Documentation Error in memory docs (2025-02-04).
  > *AI Summary: @Vidit-Ostwal has suggested that the example code in the documentation for using Azure OpenAI, Google AI, Vertex AI, and Cohere embeddings incorrectly uses the parameter `model` instead of `model_name`. They recommend updating the documentation to use `model_name` instead.*
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/1984) in [crewAIInc/crewAI]: output_log_file should also suppport JSON format. (2025-01-27).
  > *AI Summary: @Vidit-Ostwal has suggested adding a JSON format option to the output_log_file, which currently has a .txt format that is not parsable. This enhancement would address issue #1970 and facilitate further analysis by providing a structured format for log data. @Vidit-Ostwal has expressed willingness to contribute a pull request implementing this*

## 🚀 Pull Requests
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2112) in [crewAIInc/crewAI]: Added user message before calling litellm (2025-02-12).
  > *AI Summary: @Vidit-Ostwal has suggested a fix for issue #2111 by implementing a user message formatted by `feedback`. This addresses the issue that was causing problems with the formatting of this message.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2071) in [crewAIInc/crewAI]: Added functionality to have any llm run test functionality (2025-02-09).
  > *AI Summary: @Vidit-Ostwal has suggested a fix for the issue mentioned in issue #2067. The suggested fix addresses the problem described in the aforementioned issue, ensuring that the issue is resolved. This change will improve the overall functionality and reliability of the system.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2047) in [crewAIInc/crewAI]: Added reset memories function inside crew class (2025-02-06).
  > *AI Summary: @Vidit-Ostwal has suggested changes to resolve the memory reset issue raised in #2023. Their proposed modifications include:

- Eliminating the CLI command for memory reset
- Updating the documentation to reflect these changes

However, @Vidit-Ostwal seeks confirmation on whether their proposed solution aligns with the project's objectives before implementing them.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2031) in [crewAIInc/crewAI]: Fixed the memory documentation (2025-02-04).
  > *AI Summary: @Vidit-Ostwal has suggested a change that addresses the documentation issue brought up in #2030.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/1985) in [crewAIInc/crewAI]: Added functionality to have json format as well for the logs (2025-01-27).
  > *AI Summary: @Vidit-Ostwal has suggested adding support to save logs as a JSON file when initializing the crew. By setting output_log_file to True or providing a file name and setting save_as_json to True, users can generate a JSON file containing an array of JSON events. This feature simplifies parsing and working with*

## ⭐ Starred Repositories
- Starred [bespokelabsai/curator](https://github.com/bespokelabsai/curator) on 2025-02-13.
- Starred [dipanjanS/training-fine-tuning-large-language-models-workshop-dhs2024](https://github.com/dipanjanS/training-fine-tuning-large-language-models-workshop-dhs2024) on 2025-02-12.
- Starred [sentient-engineering/sentient](https://github.com/sentient-engineering/sentient) on 2025-02-08.
- Starred [langflow-ai/langflow](https://github.com/langflow-ai/langflow) on 2025-02-07.
- Starred [langfuse/langfuse](https://github.com/langfuse/langfuse) on 2025-02-04.

## 🍴 Forked Repositories
- Forked [crewAIInc/crewAI](https://github.com/Vidit-Ostwal/crewAI) on 2025-01-27.
- Forked [explodinggradients/ragas](https://github.com/Vidit-Ostwal/ragas) on 2025-01-24.
