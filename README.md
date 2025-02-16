# Recent GitHub Activity for Vidit-Ostwal

## 💬 Recent Comments
- [Commented](https://github.com/crewAIInc/crewAI/issues/2131#issuecomment-2660681309) in [crewAIInc/crewAI] on 2025-02-15.
  > *AI Summary: @Vidit-Ostwal has suggested that it would be helpful if the entire code for this project could be shared in one place for easier reference.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2102#issuecomment-2659922689) in [crewAIInc/crewAI] on 2025-02-14.
  > *AI Summary: @Vidit-Ostwal has suggested that @ashishpatel26 try updating the package as the sessions are ending perfectly fine for them.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2105#issuecomment-2659884693) in [crewAIInc/crewAI] on 2025-02-14.
  > *AI Summary: @Vidit-Ostwal has suggested that the issue may be specific to the user's case. They recommend checking the goals and description provided, and trying to get the output in a different format, such as JSON.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2123#issuecomment-2659864458) in [crewAIInc/crewAI] on 2025-02-14.
  > *AI Summary: @Vidit-Ostwal has suggested that you verify if the file path where your crew is running and the path in the terminal where you execute `crewai reset-memories -a` are identical. Ensuring this will help resolve any issues related to memory reset.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2105#issuecomment-2653744764) in [crewAIInc/crewAI] on 2025-02-12.
  > *AI Summary: @Vidit-Ostwal has suggested that the observation made by @ninad-opsverse should be investigated to determine if it also gets appended to the Python output. This suggestion is made in response to the comment from @ninad-opsverse, but @Vidit-Ostwal does not provide any specific details or examples to support their suggestion.*
- [Commented](https://github.com/crewAIInc/crewAI/pull/2071#issuecomment-2653722469) in [crewAIInc/crewAI] on 2025-02-12.
  > *AI Summary: @Vidit-Ostwal has suggested that this pull request should be merged. This request should be given priority as it has been thoroughly reviewed and addresses a critical issue. The code included in this pull request is optimized to enhance the overall performance and stability of the application.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2097#issuecomment-2651667767) in [crewAIInc/crewAI] on 2025-02-11.
  > *AI Summary: @Vidit-Ostwal has suggested incorporating a crew within a tool, along with parent agents. This tool would be capable of initiating a crew and managing it under the supervision of a parent crew. This hierarchical structure would enhance organization and efficiency in managing crews and agents within the system.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2095#issuecomment-2651664099) in [crewAIInc/crewAI] on 2025-02-11.
  > *AI Summary: @Vidit-Ostwal has suggested that while pre-computed or generalized managers may be feasible, it is preferable to maintain direct control over the management process. This allows for greater customization and flexibility in decision-making.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2092#issuecomment-2651660502) in [crewAIInc/crewAI] on 2025-02-11.
  > *AI Summary: @Vidit-Ostwal has suggested that `human_input` is called after a task to ask the user if the generated response is good. Incorporating additional context while the agent is asking for input may not be ideal. Instead, it's recommended to provide all necessary input during the `crew.kickoff()` function. This approach clarifies the*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2095#issuecomment-2650913664) in [crewAIInc/crewAI] on 2025-02-11.
  > *AI Summary: @Vidit-Ostwal has suggested that including context about agents and tools used by the manager LLM is a good idea. However, they have also expressed concern that adding a unique "manager_note" for one agent may not be optimal. Instead, they propose allowing users to request that an agent generate descriptions, goals,*

## 🐛 Issues Raised
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/2111) in [crewAIInc/crewAI]: [BUG] LiteLLM call fails, when `human_input` set to True (2025-02-12).
  > *AI Summary: @Vidit-Ostwal has suggested that the code fails to run because the lite llm when called isn't given the user role in the messages. They have attached a screenshot of the error, and provided a code snippet to reproduce the issue. The error occurs when the code attempts to run a*
- Raised an [issue](https://github.com/BerriAI/litellm/issues/8467) in [BerriAI/litellm]: [Bug]: Support to Google AI Studio (2025-02-11).
  > *AI Summary: @Vidit-Ostwal has suggested including contents in the GenerateContentRequest when calling the litellm completion function to resolve a BadRequestError. The error was due to unspecified contents in the request. The relevant log output and ML Ops Team status are not provided in the comment. The LiteLLM version used is 1.60.2. No*
- Raised an [issue](https://github.com/langfuse/langfuse/issues/5432) in [langfuse/langfuse]: bug: Running Langfuse Locally Dcoker (2025-02-08).
  > *AI Summary: @Vidit-Ostwal has suggested investigating a port conflict issue encountered while setting up Langfuse via Docker Compose. The default port 9000, used by both ClickHouse and Minio, is already in use by an external system process that cannot be terminated. Additionally, it's believed that the port is also referenced internally, resulting*
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/2030) in [crewAIInc/crewAI]: Documentation Error in memory docs (2025-02-04).
  > *AI Summary: @Vidit-Ostwal has suggested that the input argument for the embedder in the code examples should be `model_name` instead of `model`. This correction applies to all the given examples in the documentation. The issue has been observed across different platforms including Azure OpenAI Embeddings, Google AI Embeddings, Vertex AI Embeddings, and*
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/1984) in [crewAIInc/crewAI]: output_log_file should also suppport JSON format. (2025-01-27).
  > *AI Summary: @Vidit-Ostwal has suggested a feature enhancement for the core functionality, whereby the output_log_file should support JSON format in addition to the current .txt format. This JSON format will enable further analysis and partially addresses the issue raised in #1970. They are willing to contribute by submitting a pull request for*

## 🚀 Pull Requests
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2112) in [crewAIInc/crewAI]: Added user message before calling litellm (2025-02-12).
  > *AI Summary: @Vidit-Ostwal has suggested fixing issue #2111 by adding user message formatted by `feedback`. This change addresses the reported issue and improves the user experience by providing a more informative and user-friendly message.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2071) in [crewAIInc/crewAI]: Added functionality to have any llm run test functionality (2025-02-09).
  > *AI Summary: @Vidit-Ostwal has suggested that this commit fixes the issue mentioned in #2067.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2047) in [crewAIInc/crewAI]: Added reset memories function inside crew class (2025-02-06).
  > *AI Summary: @Vidit-Ostwal has suggested fixing the reset memories issue reported in #2023. Their solution includes:

- Removing the CLI command for resetting memories
- Making necessary documentation changes

They are willing to implement these changes if the proposed solution aligns with the team's vision.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2031) in [crewAIInc/crewAI]: Fixed the memory documentation (2025-02-04).
  > *AI Summary: @Vidit-Ostwal has suggested that this commit addresses a documentation-related issue identified in issue #2030. No further details were provided in the comment.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/1985) in [crewAIInc/crewAI]: Added functionality to have json format as well for the logs (2025-01-27).
  > *AI Summary: @Vidit-Ostwal has suggested adding support to save logs as a JSON file. When initializing the crew, users can now set "output_log_file" to a file name (e.g., "log.json") and enable "save_as_json" to save logs as an array of JSON events in the specified file. This JSON file can be easily parsed*

## ⭐ Starred Repositories
- Starred [bespokelabsai/curator](https://github.com/bespokelabsai/curator) on 2025-02-13.
- Starred [dipanjanS/training-fine-tuning-large-language-models-workshop-dhs2024](https://github.com/dipanjanS/training-fine-tuning-large-language-models-workshop-dhs2024) on 2025-02-12.
- Starred [sentient-engineering/sentient](https://github.com/sentient-engineering/sentient) on 2025-02-08.
- Starred [langflow-ai/langflow](https://github.com/langflow-ai/langflow) on 2025-02-07.
- Starred [langfuse/langfuse](https://github.com/langfuse/langfuse) on 2025-02-04.

## 🍴 Forked Repositories
- Forked [crewAIInc/crewAI](https://github.com/Vidit-Ostwal/crewAI) on 2025-01-27.
- Forked [explodinggradients/ragas](https://github.com/Vidit-Ostwal/ragas) on 2025-01-24.
