# Recent GitHub Activity for Vidit-Ostwal

## 💬 Recent Comments
- [Commented](https://github.com/crewAIInc/crewAI/issues/2131#issuecomment-2660681309) in [crewAIInc/crewAI] on 2025-02-15.
  > *AI Summary: @Vidit-Ostwal has suggested sharing the complete code in one place for easier reference. This would provide a comprehensive view of the code and its functionality, making it more accessible and convenient for reviewers to understand the overall solution.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2102#issuecomment-2659922689) in [crewAIInc/crewAI] on 2025-02-14.
  > *AI Summary: @Vidit-Ostwal has suggested updating the package since the sessions end properly for them.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2105#issuecomment-2659884693) in [crewAIInc/crewAI] on 2025-02-14.
  > *AI Summary: @Vidit-Ostwal has suggested that the issue may be specific to the user's case. They recommend checking the goals and description provided, or trying to get the output in a different format, such as JSON. @Vidit-Ostwal also mentioned that they were unable to reproduce the issue.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2123#issuecomment-2659864458) in [crewAIInc/crewAI] on 2025-02-14.
  > *AI Summary: @Vidit-Ostwal has suggested that the team confirms whether the file path in which their crew is running matches the path in the terminal where they are executing the `crewai reset-memories -a` command. This confirmation will help to ensure that the `reset-memories` command is being executed correctly.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2105#issuecomment-2653744764) in [crewAIInc/crewAI] on 2025-02-12.
  > *AI Summary: @Vidit-Ostwal has suggested that @ninad-opsverse's observation is on point and asks if the observation also gets appended to the Python output.*
- [Commented](https://github.com/crewAIInc/crewAI/pull/2071#issuecomment-2653722469) in [crewAIInc/crewAI] on 2025-02-12.
  > *AI Summary: @Vidit-Ostwal has suggested that the provided merge request should be merged.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2097#issuecomment-2651667767) in [crewAIInc/crewAI] on 2025-02-11.
  > *AI Summary: @Vidit-Ostwal has suggested incorporating a crew within a tool, with parent agents managing the tool. The tool should be capable of initiating a crew, which would then be managed by a parent crew. This multi-layered approach allows for efficient management of crews and their associated tasks.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2095#issuecomment-2651664099) in [crewAIInc/crewAI] on 2025-02-11.
  > *AI Summary: @Vidit-Ostwal has suggested considering pre-computed or generalized managers as an alternative. However, @Vidit-Ostwal emphasizes the importance of retaining control over such management, implying that custom solutions may be more suitable in certain scenarios.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2092#issuecomment-2651660502) in [crewAIInc/crewAI] on 2025-02-11.
  > *AI Summary: @Vidit-Ostwal has suggested that the `human_input` function is used after a task is performed to gather feedback on the generated response. He advises against incorporating additional context during crew execution and instead recommends providing all necessary input during the `crew.kickoff()` call to avoid misunderstandings.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2095#issuecomment-2650913664) in [crewAIInc/crewAI] on 2025-02-11.
  > *AI Summary: @Vidit-Ostwal suggests providing context about agents and tools that the manager LLM can utilize. However, they express concern that adding a "manager_note" specifically for the manager LLM may not be ideal since it is essentially an agent itself. They also recommend allowing users to request that an agent create descriptions,*

## 🐛 Issues Raised
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/2111) in [crewAIInc/crewAI]: [BUG] LiteLLM call fails, when `human_input` set to True (2025-02-12).
  > *AI Summary: @Vidit-Ostwal has suggested that the issue with running a crew with `human_input` set to True may be due to the fact that the lite llm is not given the user role in the messages when called. To solve this, they have added feedback in the user role. They have also*
- Raised an [issue](https://github.com/BerriAI/litellm/issues/8467) in [BerriAI/litellm]: [Bug]: Support to Google AI Studio (2025-02-11).
  > *AI Summary: @Vidit-Ostwal has suggested that there seems to be an issue with the Python code used to call LiteLLM. The code snippet provided in the comment results in a "BadRequestError" with the message "contents is not specified". @Vidit-Ostwal is not on an ML Ops Team and is using LiteLLM version 1.60.2.*
- Raised an [issue](https://github.com/langfuse/langfuse/issues/5432) in [langfuse/langfuse]: bug: Running Langfuse Locally Dcoker (2025-02-08).
  > *AI Summary: @Vidit-Ostwal has suggested the following: Langfuse is failing to setup using docker-compose due to port 9000 conflict with an existing system process. They have tried to change the port but believe it's also referenced elsewhere internally. They are seeking guidance on where to change the port to resolve this issue*
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/2030) in [crewAIInc/crewAI]: Documentation Error in memory docs (2025-02-04).
  > *AI Summary: @Vidit-Ostwal has suggested that the code examples provided in the documentation for the Memory concept are incorrect. The parameter `model` should be replaced with `model_name` in the examples. This affects code examples for Azure OpenAI Embeddings, Google AI Embeddings, Vertex AI Embeddings, and Cohere Embeddings.*
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/1984) in [crewAIInc/crewAI]: output_log_file should also suppport JSON format. (2025-01-27).
  > *AI Summary: @Vidit-Ostwal has suggested a feature addition to improve the parsability of the output_log_file. Currently, the file is in .txt format, which makes it difficult for further analysis. The suggestion is to add a JSON format option to the output_log_file, which would address the issue raised in #1970. @Vidit-Ostwal has expressed*

## 🚀 Pull Requests
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2112) in [crewAIInc/crewAI]: Added user message before calling litellm (2025-02-12).
  > *AI Summary: @Vidit-Ostwal has suggested fixing issue #2111 by adding a user message formatted by `feedback`. This solution enhances the user experience by providing clear and tailored feedback to the user. By implementing this suggestion, the application can effectively communicate important information and guide users through the system.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2071) in [crewAIInc/crewAI]: Added functionality to have any llm run test functionality (2025-02-09).
  > *AI Summary: @Vidit-Ostwal has suggested a fix for the issue raised in #2067. Unfortunately, I cannot provide more detailed information about the fix without access to the specific code changes associated with the issue.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2047) in [crewAIInc/crewAI]: Added reset memories function inside crew class (2025-02-06).
  > *AI Summary: @Vidit-Ostwal has suggested a fix for the reset memories issue reported in #2023. They also recommend additional changes, including removing the CLI command for resetting memories and making documentation updates. They are willing to implement these changes if the proposed solution aligns with the overall approach.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2031) in [crewAIInc/crewAI]: Fixed the memory documentation (2025-02-04).
  > *AI Summary: @Vidit-Ostwal has suggested an update to address documentation issues raised in #2030. The changes aim to improve clarity and accuracy in the documentation, ensuring users have a better understanding of the platform's features and functionality. This update will enhance the user experience and simplify the onboarding process for new users.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/1985) in [crewAIInc/crewAI]: Added functionality to have json format as well for the logs (2025-01-27).
  > *AI Summary: @Vidit-Ostwal has suggested adding support to save logs as a JSON file in the crew initialization. This enables users to specify an output log file name (e.g., "log.json") or set the output_log_file to True. Additionally, the save_as_json flag should be set to True to enable saving logs in JSON format.*

## ⭐ Starred Repositories
- Starred [bespokelabsai/curator](https://github.com/bespokelabsai/curator) on 2025-02-13.
- Starred [dipanjanS/training-fine-tuning-large-language-models-workshop-dhs2024](https://github.com/dipanjanS/training-fine-tuning-large-language-models-workshop-dhs2024) on 2025-02-12.
- Starred [sentient-engineering/sentient](https://github.com/sentient-engineering/sentient) on 2025-02-08.
- Starred [langflow-ai/langflow](https://github.com/langflow-ai/langflow) on 2025-02-07.
- Starred [langfuse/langfuse](https://github.com/langfuse/langfuse) on 2025-02-04.

## 🍴 Forked Repositories
- Forked [crewAIInc/crewAI](https://github.com/Vidit-Ostwal/crewAI) on 2025-01-27.
- Forked [explodinggradients/ragas](https://github.com/Vidit-Ostwal/ragas) on 2025-01-24.
