# Recent GitHub Activity for Vidit-Ostwal

## 💬 Recent Comments
- [Commented](https://github.com/crewAIInc/crewAI/issues/2131#issuecomment-2660681309) in [crewAIInc/crewAI] on 2025-02-15.
  > *AI Summary: @Vidit-Ostwal has suggested sharing the entire code in one place for easier reference. This would eliminate the need to refer to multiple places to gather all the relevant code snippets, making it more convenient to work with.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2102#issuecomment-2659922689) in [crewAIInc/crewAI] on 2025-02-14.
  > *AI Summary: @Vidit-Ostwal has suggested that the issue of sessions ending abruptly may be resolved by updating the package. @ashishpatel26, it is recommended to try updating the package to see if it rectifies the problem.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2105#issuecomment-2659884693) in [crewAIInc/crewAI] on 2025-02-14.
  > *AI Summary: @Vidit-Ostwal has suggested that you try the following steps to resolve the issue:

1. Verify the goals and description provided.
2. Attempt to obtain the output in a different format, such as JSON.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2123#issuecomment-2659864458) in [crewAIInc/crewAI] on 2025-02-14.
  > *AI Summary: @Vidit-Ostwal has suggested confirming whether the file path where the crew is running matches the path where the command `crewai reset-memories -a` is executed in the terminal. This is crucial to ensure proper execution and avoid potential errors.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2105#issuecomment-2653744764) in [crewAIInc/crewAI] on 2025-02-12.
  > *AI Summary: @Vidit-Ostwal has suggested that @ninad-opsverse's observation on whether the information gets appended to the Python output should be considered.*
- [Commented](https://github.com/crewAIInc/crewAI/pull/2071#issuecomment-2653722469) in [crewAIInc/crewAI] on 2025-02-12.
  > *AI Summary: @Vidit-Ostwal has suggested merging this pull request.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2097#issuecomment-2651667767) in [crewAIInc/crewAI] on 2025-02-11.
  > *AI Summary: @Vidit-Ostwal has suggested incorporating a crew within a tool and introducing parent agents. The tool should be able to initiate a crew under the management of a parent crew. This structure allows for a hierarchical organization of crews within tools.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2095#issuecomment-2651664099) in [crewAIInc/crewAI] on 2025-02-11.
  > *AI Summary: @Vidit-Ostwal has suggested that it is preferable to have control over pre-computed or generalized managers rather than relying on them entirely. This provides greater flexibility and customization options.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2092#issuecomment-2651660502) in [crewAIInc/crewAI] on 2025-02-11.
  > *AI Summary: @Vidit-Ostwal has suggested that `human_input` is called after a task is performed, prompting the user to evaluate the generated response. They recommend providing all necessary input during `crew.kickoff()` rather than adding additional context during execution. This approach ensures that the agent has all the required information to complete the task*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2095#issuecomment-2650913664) in [crewAIInc/crewAI] on 2025-02-11.
  > *AI Summary: @Vidit-Ostwal suggests improving the context provided to the manager LLM by including information about agents and tools it can use. However, they caution against adding a dedicated `manager_note` field specifically for the manager LLM, as it may not be appropriate since the manager LLM is essentially an agent itself. Instead,*

## 🐛 Issues Raised
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/2111) in [crewAIInc/crewAI]: [BUG] LiteLLM call fails, when `human_input` set to True (2025-02-12).
  > *AI Summary: @Vidit-Ostwal has suggested that the provided code doesn't work because the lite llm doesn't receive the user role. They have added feedback as a user to guide the lite llm and have provided an image to illustrate the issue. The code snippet provided runs a crew with human input set*
- Raised an [issue](https://github.com/BerriAI/litellm/issues/8467) in [BerriAI/litellm]: [Bug]: Support to Google AI Studio (2025-02-11).
  > *AI Summary: @Vidit-Ostwal has suggested that a call to the litellm API with a Gemini model returns an error indicating that the contents are not specified. The error occurs when attempting to determine user satisfaction based on provided feedback.*
- Raised an [issue](https://github.com/langfuse/langfuse/issues/5432) in [langfuse/langfuse]: bug: Running Langfuse Locally Dcoker (2025-02-08).
  > *AI Summary: @Vidit-Ostwal has suggested that the local setup for langfuse is failing due to port 9000 already being used by another process. The error seems to be coming from the clickhouse database. @Vidit-Ostwal is interested in contributing a fix for this bug and would appreciate guidance on where to make the*
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/2030) in [crewAIInc/crewAI]: Documentation Error in memory docs (2025-02-04).
  > *AI Summary: @Vidit-Ostwal has suggested that the CrewAI documentation for embeddings, specifically in the Azure OpenAI, Google AI, Vertex AI, and Cohere embeddings sections, contains a mistake. The `model` parameter should be replaced with `model_name` for consistency with the input that the embedder expects.*
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/1984) in [crewAIInc/crewAI]: output_log_file should also suppport JSON format. (2025-01-27).
  > *AI Summary: @Vidit-Ostwal has suggested adding a JSON format to the output_log_file which currently has a .txt format. This will make the log file parsable for further analysis. The JSON format will partially address issue #1970. @Vidit-Ostwal is willing to submit a pull request for this change.*

## 🚀 Pull Requests
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2112) in [crewAIInc/crewAI]: Added user message before calling litellm (2025-02-12).
  > *AI Summary: @Vidit-Ostwal has suggested that the issue #2111 has been fixed. Additionally, a user message has been included, which is formatted by the feedback framework.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2071) in [crewAIInc/crewAI]: Added functionality to have any llm run test functionality (2025-02-09).
  > *AI Summary: @Vidit-Ostwal has suggested a fix for the issue reported in #2067. The proposed change addresses the underlying cause of the problem, ensuring that the issue no longer occurs. This resolution will enhance the stability and overall performance of the software.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2047) in [crewAIInc/crewAI]: Added reset memories function inside crew class (2025-02-06).
  > *AI Summary: @Vidit-Ostwal has suggested fixes for the reset memories issue mentioned in #2023. They have also identified additional changes that need to be made, including: 1. Removing the CLI command to reset memories 2. Making documentation changes @Vidit-Ostwal has indicated they can implement these additional changes if their proposed solution is*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2031) in [crewAIInc/crewAI]: Fixed the memory documentation (2025-02-04).
  > *AI Summary: @Vidit-Ostwal has suggested a fix for the documentation issue mentioned in #2030. This commit addresses the issue raised and provides a detailed explanation of the changes made to resolve it. The documentation has been updated accordingly, ensuring its accuracy and clarity for users.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/1985) in [crewAIInc/crewAI]: Added functionality to have json format as well for the logs (2025-01-27).
  > *AI Summary: @Vidit-Ostwal has suggested adding support for saving logs as a JSON file in the crew initialization. Users can now set the output_log_file parameter to True or provide a file name, and enable save_as_json to True. This generates a .json file containing an array of JSON events, simplifying parsing and working*

## ⭐ Starred Repositories
- Starred [bespokelabsai/curator](https://github.com/bespokelabsai/curator) on 2025-02-13.
- Starred [dipanjanS/training-fine-tuning-large-language-models-workshop-dhs2024](https://github.com/dipanjanS/training-fine-tuning-large-language-models-workshop-dhs2024) on 2025-02-12.
- Starred [sentient-engineering/sentient](https://github.com/sentient-engineering/sentient) on 2025-02-08.
- Starred [langflow-ai/langflow](https://github.com/langflow-ai/langflow) on 2025-02-07.
- Starred [langfuse/langfuse](https://github.com/langfuse/langfuse) on 2025-02-04.

## 🍴 Forked Repositories
- Forked [crewAIInc/crewAI](https://github.com/Vidit-Ostwal/crewAI) on 2025-01-27.
- Forked [explodinggradients/ragas](https://github.com/Vidit-Ostwal/ragas) on 2025-01-24.
