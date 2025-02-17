# Recent GitHub Activity for Vidit-Ostwal

## 💬 Recent Comments
- [Commented](https://github.com/crewAIInc/crewAI/issues/2131#issuecomment-2660681309) in [crewAIInc/crewAI] on 2025-02-15.
  > *AI Summary: @Vidit-Ostwal has suggested sharing the entire code for reference. They believe that providing the complete code would make it easier for others to understand the context and functionality of the proposed changes.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2102#issuecomment-2659922689) in [crewAIInc/crewAI] on 2025-02-14.
  > *AI Summary: @Vidit-Ostwal has suggested that @ashishpatel26 try updating the package because the sessions are ending perfectly fine for them.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2105#issuecomment-2659884693) in [crewAIInc/crewAI] on 2025-02-14.
  > *AI Summary: @Vidit-Ostwal has suggested that the issue being experienced might be specific to the user's case. They recommend checking the provided goals and description or trying to obtain the output in a different format, possibly JSON. @Vidit-Ostwal was unable to reproduce the issue when they attempted it again.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2123#issuecomment-2659864458) in [crewAIInc/crewAI] on 2025-02-14.
  > *AI Summary: @Vidit-Ostwal has suggested to confirm whether the file path where the crew is running and the path in the terminal where `crewai reset-memories -a` is executed are the same.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2105#issuecomment-2653744764) in [crewAIInc/crewAI] on 2025-02-12.
  > *AI Summary: @Vidit-Ostwal has suggested considering whether the count information from the GraphQL query also gets appended to the Python output.*
- [Commented](https://github.com/crewAIInc/crewAI/pull/2071#issuecomment-2653722469) in [crewAIInc/crewAI] on 2025-02-12.
  > *AI Summary: @Vidit-Ostwal has suggested merging the current pull request. They have not provided any specific reasons or context for their request, requesting the maintainer to review the changes and merge the pull request if appropriate.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2097#issuecomment-2651667767) in [crewAIInc/crewAI] on 2025-02-11.
  > *AI Summary: @Vidit-Ostwal has suggested incorporating a crew within a tool, where parent agents can manage the crew. The tool should be designed to initiate and manage crews efficiently, allowing for a hierarchical structure where crews operate under the supervision of parent crews. This approach enables effective crew management with clear roles*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2095#issuecomment-2651664099) in [crewAIInc/crewAI] on 2025-02-11.
  > *AI Summary: @Vidit-Ostwal has suggested that it is better to have control over pre-computed or generalized managers. This would allow for greater flexibility and customization in managing the system.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2092#issuecomment-2651660502) in [crewAIInc/crewAI] on 2025-02-11.
  > *AI Summary: @Vidit-Ostwal has suggested clarifying the usage of `human_input`. He explains that `human_input` is called after a task is performed to gather feedback on the generated response. He recommends providing all necessary input during the `crew.kickoff()` stage rather than adding it during the crew execution, to avoid confusion and ensure the*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2095#issuecomment-2650913664) in [crewAIInc/crewAI] on 2025-02-11.
  > *AI Summary: @Vidit-Ostwal has suggested that it is a good idea to include context about the agents or tools that the manager LLM can use. However, they have also expressed concern that adding a `manager_note` just for one agent may not be the best approach since the manager LLM is essentially an*

## 🐛 Issues Raised
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/2111) in [crewAIInc/crewAI]: [BUG] LiteLLM call fails, when `human_input` set to True (2025-02-12).
  > *AI Summary: @Vidit-Ostwal has suggested improving the handling of user input in a specific crew where agents are required to have the "user role." The issue arises when using the `lite llm` without providing the user role, resulting in validation failures. The proposed solution involves adding feedback to the user role to*
- Raised an [issue](https://github.com/BerriAI/litellm/issues/8467) in [BerriAI/litellm]: [Bug]: Support to Google AI Studio (2025-02-11).
  > *AI Summary: @Vidit-Ostwal has suggested that a "BadRequestError" is encountered while trying to call "litellm" with the Google Studio API. The specific error message indicates that the "contents" field in "GenerateContentRequest" is not specified. This error is occurring with litellm version 1.60.2.*
- Raised an [issue](https://github.com/langfuse/langfuse/issues/5432) in [langfuse/langfuse]: bug: Running Langfuse Locally Dcoker (2025-02-08).
  > *AI Summary: @Vidit-Ostwal has suggested that when attempting to set up langfuse via Docker Compose, port 9000, used by ClickHouse and Minio, is already occupied by another system process. They believe that port 9000 is also used internally, but changing it externally is insufficient. @Vidit-Ostwal seeks assistance in identifying all locations where*
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/2030) in [crewAIInc/crewAI]: Documentation Error in memory docs (2025-02-04).
  > *AI Summary: @Vidit-Ostwal has suggested that the sample code examples in the CrewAI documentation for Azure OpenAI Embeddings, Google AI Embeddings, Vertex AI Embeddings, and Cohere Embeddings incorrectly use "model" as the input parameter for the embedder instead of "model_name". They recommend replacing the "model" parameter with "model_name" in the documentation.*
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/1984) in [crewAIInc/crewAI]: output_log_file should also suppport JSON format. (2025-01-27).
  > *AI Summary: @Vidit-Ostwal has suggested adding a JSON format option to the output_log_file, as the current .txt format is not parsable. This would allow for easier analysis of the logging data and partially address issue #1970. @Vidit-Ostwal is willing to contribute a pull request for this feature.*

## 🚀 Pull Requests
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2112) in [crewAIInc/crewAI]: Added user message before calling litellm (2025-02-12).
  > *AI Summary: @Vidit-Ostwal has suggested a fix for issue #2111 by incorporating a user message formatted by the "feedback" function. This enhancement aligns with the guidelines for summarization, which require the following: brevity, comprehensiveness, adherence to the user's perspective, exclusion of external links, and code details.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2071) in [crewAIInc/crewAI]: Added functionality to have any llm run test functionality (2025-02-09).
  > *AI Summary: @Vidit-Ostwal has suggested that this commit fixes the issue mentioned in #2067. No additional details or context were provided in the comment.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2047) in [crewAIInc/crewAI]: Added reset memories function inside crew class (2025-02-06).
  > *AI Summary: @Vidit-Ostwal has suggested fixing the reset memories issue reported in #2023. Additionally, they recommend removing the CLI command for resetting memories and updating the documentation to reflect these changes. They are willing to implement these modifications if the proposed solution aligns with the project's goals.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2031) in [crewAIInc/crewAI]: Fixed the memory documentation (2025-02-04).
  > *AI Summary: @Vidit-Ostwal has suggested a fix for the documentation issue reported in issue #2030. They have made the necessary changes to resolve the issue and ensured that the documentation accurately reflects the current behavior and functionality of the system. This update aims to provide clearer and more precise information to users,*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/1985) in [crewAIInc/crewAI]: Added functionality to have json format as well for the logs (2025-01-27).
  > *AI Summary: @Vidit-Ostwal has suggested adding support to save logs as a JSON file in the crew initialization process. Users can set output_log_file to True or provide a file name and enable save_as_json to True. This generates a JSON file with an array of JSON events, simplifying parsing and working with the*

## ⭐ Starred Repositories
- Starred [bespokelabsai/curator](https://github.com/bespokelabsai/curator) on 2025-02-13.
- Starred [dipanjanS/training-fine-tuning-large-language-models-workshop-dhs2024](https://github.com/dipanjanS/training-fine-tuning-large-language-models-workshop-dhs2024) on 2025-02-12.
- Starred [sentient-engineering/sentient](https://github.com/sentient-engineering/sentient) on 2025-02-08.
- Starred [langflow-ai/langflow](https://github.com/langflow-ai/langflow) on 2025-02-07.
- Starred [langfuse/langfuse](https://github.com/langfuse/langfuse) on 2025-02-04.

## 🍴 Forked Repositories
- Forked [crewAIInc/crewAI](https://github.com/Vidit-Ostwal/crewAI) on 2025-01-27.
- Forked [explodinggradients/ragas](https://github.com/Vidit-Ostwal/ragas) on 2025-01-24.
